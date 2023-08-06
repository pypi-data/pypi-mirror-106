from gffutils.iterators import DataIterator
import argparse
import pandas as pd
import gzip
import os
from riboloco.shared_riboloco_functions import order_features

def find_transcript_pos(feature_pos, exon_d, strand):
    """
    This function takes a genomic coordinate, feature_pos, and finds its relative position within the transcript
    """
    if strand == "-":
        m = -1
    else:
        m = 1

    cumulative_distance = 0
    rel_pos = "unsure"

    for d in exon_d.values():
        if d['start'] <= feature_pos <= d['end']:
            if strand == "+":
                rel_pos = cumulative_distance + feature_pos - d['start'] + 1  # 1 based correction
            else:
                rel_pos = cumulative_distance + d["end"] - feature_pos + 1  # 1 based correction
            break
        else:
            cumulative_distance += d['length']

    return rel_pos


def find_features(tx_d, cds_d, exon_d, gene_ids, stop_correction):
    cds_starts = []
    cds_ends = []
    cds_lengths = []
    tx_lengths = []
    tx_ids = []
    genes = []
    gene_id_list = []
    strands = []

    genomic_starts_stops = {}  # record ALL annotated cds starts and stops for given gene

    counter = 0
    for gene, tx_list in tx_d.items():

        if gene not in genomic_starts_stops.keys():
            genomic_starts_stops[gene] = {'starts': [], 'stops': []}

        for tx in tx_list:
            counter += 1
            if counter % 10_000 == 0:
                print("Analysed " + str(counter) + " transcripts")
            if tx in cds_d.keys() and tx in exon_d.keys():
                cds_list = cds_d[tx]
                exon_list = exon_d[tx]
                strand = cds_list[0]["strand"]

                ordered_cds = order_features(cds_list, strand)
                ordered_exons = order_features(exon_list, strand)

                cds_start, cds_end, cds_length, tx_length, g_cds_s, g_cds_e = find_metadata(ordered_cds=ordered_cds,
                                                                                            ordered_exons=ordered_exons,
                                                                                            strand=strand,
                                                                                            stop_correction=stop_correction)

                if 'unsure' not in [cds_start, cds_end]:
                    cds_starts.append(cds_start)
                    cds_ends.append(cds_end)
                    cds_lengths.append(cds_length)
                    tx_lengths.append(tx_length)
                    tx_ids.append(tx)
                    genes.append(gene)
                    gene_id_list.append(gene_ids[gene])
                    strands.append(strand)

                    genomic_starts_stops[gene]['starts'].append(str(g_cds_s))  # already corrected for strand
                    genomic_starts_stops[gene]['stops'].append(str(g_cds_e))  # # already corrected for strand

    df = pd.DataFrame.from_dict({'transcript_id': tx_ids,
                                 'gene_name': genes, 'gene_id': gene_id_list,
                                 'cds_start': cds_starts, 'cds_end': cds_ends, 'cds_length': cds_lengths,
                                 'transcript_length': tx_lengths, 'strand': strands
                                 })

    return df, genomic_starts_stops


def find_metadata(ordered_cds, ordered_exons, strand, stop_correction):
    """
    This function finds cds start, cds end, cds length, transcript length
    """
    if strand == '+':
        genomic_cds_start = min([a['start'] for a in ordered_cds.values()])
        genomic_cds_end = max([a['end'] for a in ordered_cds.values()])

    else:
        genomic_cds_start = max([a['end'] for a in ordered_cds.values()])
        genomic_cds_end = min([a['start'] for a in ordered_cds.values()])

    cds_start = find_transcript_pos(genomic_cds_start, ordered_exons, strand)
    cds_end = find_transcript_pos(genomic_cds_end, ordered_exons, strand)
    if not cds_end == "unsure":
        cds_end += stop_correction

    cds_length = max([a["cumulative_length"] for a in ordered_cds.values()])
    if not cds_length == "unsure":
        cds_length += stop_correction
    tx_length = max([a["cumulative_length"] for a in ordered_exons.values()])

    return cds_start, cds_end, cds_length, tx_length, genomic_cds_start, genomic_cds_end


def parse_features(args):
    tx_d = {}
    cds_d = {}
    exon_d = {}
    gene_ids = {}

    types = set()
    tx_attributes = set()
    exon_attributes = set()
    cds_attributes = set()

    print("Checking that expected features are present in GTF...")
    for c, feature in enumerate(DataIterator(args.input_gtf)):
        featuretype = feature.featuretype

        # find feature types
        types.add(featuretype)

        if featuretype == args.cds_word:
            for a in feature.attributes:
                cds_attributes.add(a)

        if featuretype == args.exon_word:
            for a in feature.attributes:
                exon_attributes.add(a)

        # find all transcript attributes
        if featuretype in [args.transcript_word]:
            for a in feature.attributes:
                tx_attributes.add(a)

        if c > 5_000:
            break

    # ensure we have expected features
    for a in [args.transcript_word, args.cds_word, args.exon_word]:
        allowed_types = ', '.join([a for a in types]) + '.'
        error_message = ' '.join([a, 'is not a recognised feature type.',
                                  'Allowed types are:', allowed_types, '(See above for full details.)'])
        assert a in types, error_message

    # ensure we have expected attributes in tx
    if args.bypass_tx_type_filter:
        attribute_list = [args.gene_id_word, args.gene_name_word, args.transcript_id_word]
    else:
        attribute_list = [args.feature_type_word, args.gene_id_word, args.gene_name_word,
                          args.transcript_id_word]

    for a in attribute_list:
        allowed_attributes = ', '.join([a for a in tx_attributes]) + '.'
        error_message = ' '.join([a, 'is not a recognised attribute.',
                                  'Allowed types are:', allowed_attributes, '(See above for full details.)',
                                  "To bypass filtering by transcript type, run --bypass_tx_type_filter"])
        assert a in tx_attributes, error_message

    # and cds
    allowed_attributes = ', '.join([a for a in cds_attributes]) + '.'
    error_message = ' '.join([a, 'is not a recognised attribute.',
                              'Allowed types are:', allowed_attributes, '(See above for full details.)',
                              "To bypass filtering by transcript type, run --bypass_tx_type_filter"])
    assert args.transcript_id_word in cds_attributes, error_message

    allowed_attributes = ', '.join([a for a in exon_attributes]) + '.'
    error_message = ' '.join([a, 'is not a recognised attribute.',
                              'Allowed types are:', allowed_attributes, '(See above for full details.)',
                              "To bypass filtering by transcript type, run --bypass_tx_type_filter"])
    assert args.transcript_id_word in exon_attributes, error_message

    # Start parsing for real
    txn = 0
    for c, feature in enumerate(DataIterator(args.input_gtf)):
        if c % 100_000 == 0 and c > 0:
            print(str(c) + " records parsed")

        if c > args.early_stop > -1:
            break

        chrom = strip_rubbish(feature.seqid)
        strand = feature.strand
        featuretype = feature.featuretype

        # check if it's a transcript, and if it's protein coding (or whatever)
        if featuretype == args.transcript_word:
            txn += 1
            if not args.bypass_tx_type_filter:  # ie we are filtering
                feature_type = feature.attributes[args.feature_type_word]
                # check for more specific filtering
                if args.filter_for != "all":
                    if args.filter_for not in feature_type:
                        continue

            # find the gene name and gene id associated with this transcript
            # if args.gene_name_word in feature.attributes and args.gene_id_word in feature.attributes:
            gene_name = feature.attributes[args.gene_name_word][0]
            gene_ids[gene_name] = feature.attributes[args.gene_id_word][0]
            transcript_name = feature.attributes[args.transcript_id_word][0]

            if gene_name not in tx_d.keys():
                tx_d[gene_name] = [transcript_name]
            else:
                tx_d[gene_name].append(transcript_name)

        # check if this feature is a CDS
        if featuretype == args.cds_word:
            # parent_tx = feature[args.transcript_id_word]
            parent_tx = feature.attributes[args.transcript_id_word]
            this_d = {'chrom': chrom, 'strand': strand, 'start': feature.start, 'end': feature.end}

            for tx in parent_tx:
                if tx not in cds_d.keys():
                    cds_d[tx] = [this_d]
                else:
                    cds_d[tx].append(this_d)

        if featuretype == args.exon_word:
            # parent_tx = feature[args.transcript_id_word]
            parent_tx = feature.attributes[args.transcript_id_word]
            this_d = {'chrom': chrom, 'strand': strand, 'start': feature.start, 'end': feature.end}

            for tx in parent_tx:
                if tx not in exon_d.keys():
                    exon_d[tx] = [this_d]
                else:
                    exon_d[tx].append(this_d)

    if args.assume_cds_same:
        cds_d = exon_d

    print("Analysing features...")

    df, genomic_starts_stops = find_features(tx_d=tx_d, cds_d=cds_d, exon_d=exon_d, gene_ids=gene_ids,
                                             stop_correction=args.stop_correction)
    return df, exon_d, genomic_starts_stops


def generate_fasta(df, exon_d, genome_fasta, output_fasta, stop_correction):
    # Filter exon_d for transcripts in df (i.e. transcripts we have successfully processed)
    filtered_exon_d = {}
    key_set = set(list(df["transcript_id"]))
    for key, value in exon_d.items():
        if key in key_set:
            filtered_exon_d[key] = value

    tx_n = 0
    with gzip.open(genome_fasta, 'rb') as file:
        for compressed_line in file:
            line = compressed_line.decode().rstrip()
            if line[0:1] == ">":  # if it's a header
                new_chrom = line.replace(">", "")

                if tx_n > 0:
                    print("Saving transcript fasta for " + this_chrom.split(" ")[0])
                    gen_txs(this_chrom, sequence, filtered_exon_d, output_fasta, df, stop_correction)

                # now reset
                sequence = ""
                print("Reading " + new_chrom)

            else:
                this_chrom = new_chrom
                tx_n += 1
                sequence += line

        print("Saving transcript fasta for " + this_chrom)
        gen_txs(this_chrom, sequence, filtered_exon_d, output_fasta, df, stop_correction)


def strip_rubbish(name):
    """
    this function removes stuff that stops them matching
    """
    # remove trailing characters
    name = name.split(" ")[0].split("_")[0]
    # if just a number then it adds chr in front
    if name.isdigit():
        name = "chr" + name
    else:
        name = name.lower()
    return name


def gen_txs(this_chrom, sequence, filtered_exon_d, output_fasta, df, stop_correction):
    """
    This function generates transcript sequences from the genomic fasta provided
    """

    this_chrom = strip_rubbish(this_chrom)  # an attempt to stop problems due to differences in labelling

    end_with_stop = {"yes": 0, "no": 0, 'minus3': 0, 'plus3': 0}

    for tx, tx_exon_ds in filtered_exon_d.items():
        if tx_exon_ds[0]['chrom'] == this_chrom:
            strand = tx_exon_ds[0]["strand"]
            seqs = {}
            for d in tx_exon_ds:
                seqs[d['start']] = sequence[d['start'] - 1:d['end']]

            seqs = dict(sorted(seqs.items()))
            tx_seq = ""
            for seq in seqs.values():
                tx_seq += seq

            tx_seq = tx_seq.upper()

            if strand == "-":
                tx_seq = rev_c(tx_seq)

            cds_stop = int(df[df["transcript_id"] == tx].cds_end)
            #cds_start = int(df[df["transcript_id"] == tx].cds_start)
            stop_seq = tx_seq[cds_stop - 3:cds_stop]

            if stop_seq not in ["TAG", "TGA", "TAA"]:
                if tx_seq[cds_stop - 3 - 3:cds_stop - 3] in ["TAG", "TGA", "TAA"]:
                    end_with_stop['minus3'] += 1
                if tx_seq[cds_stop - 3 + 3:cds_stop + 3] in ["TAG", "TGA", "TAA"]:
                    end_with_stop['plus3'] += 1
                end_with_stop["no"] += 1
            else:
                end_with_stop["yes"] += 1

            with open(output_fasta, "a+") as file:
                file.write(">" + tx + "\n")
                file.write(tx_seq + "\n")

    if sum(end_with_stop.values()) > 0:
        fraction_didnt_end_stop = end_with_stop["no"]/(end_with_stop['yes'] + end_with_stop['no'])
        if fraction_didnt_end_stop > 0.30:  # if more than 30% issue warning
            print(' '.join([str(round(100*fraction_didnt_end_stop, 2)), "% didn't end with a stop!"]))
        if end_with_stop["plus3"]/(end_with_stop['yes'] + end_with_stop['no']) > 20*(1-fraction_didnt_end_stop):
            print("Perhaps change --stop_correction parameter to " + str(stop_correction + 3))
        if end_with_stop["minus3"]/(end_with_stop['yes'] + end_with_stop['no']) > 20*(1-fraction_didnt_end_stop):
            print("Perhaps change --stop_correction parameter to " + str(stop_correction - 3))


def rev_c(seq):
    """
    simple function that reverse complements a given sequence
    """
    tab = str.maketrans("ACTGN", "TGACN")
    # first reverse the sequence
    seq = seq[::-1]
    # and then complement
    seq = seq.translate(tab)
    return seq


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-gtf", "--input_gtf", type=str, required=True,
                        help="A gtf file with your genome annotation. Can be .gz compressed.")
    parser.add_argument("-o", "--output_filename", type=str, required=True,
                        help="The outfile filename")
    parser.add_argument("-ffl", "--filter_for_longest", action='store_true', default=False,
                        help="Only use the longest protein coding transcript associated with each gene.")
    parser.add_argument("-nf", "--no_fasta", action="store_true", default=False,
                        help="Don't generate a fasta of transcripts")
    parser.add_argument("--stop_correction", type=int, default=3, help="Add 3 nt for stop codon. Can be changed "
                                                                       "to 0 depending on whether the annotation "
                                                                       "includes the stop codon within the annotated"
                                                                       " CDSs.")
    parser.add_argument("-f", "--genome_fasta", type=str, default="None", required=True)
    parser.add_argument("--transcript_word", default="transcript")
    parser.add_argument("--feature_type_word", default="gene_type")
    parser.add_argument("--filter_for", default="protein_coding", help="Which transcript types to filter for. Set "
                                                                       "to 'all' to disable. Default=protein_coding")
    parser.add_argument("--gene_name_word", default="gene_name")
    parser.add_argument("--cds_word", default="CDS")
    parser.add_argument("--gene_id_word", default="gene_id")
    parser.add_argument("--transcript_id_word", default="transcript_id")
    parser.add_argument("--exon_word", default="exon", help="The key word that signifies exons. Default=exon")
    parser.add_argument("--early_stop", type=int, default=-1, help="Stop after n reads parsed. -1 to disable (default)")
    parser.add_argument("-pf", "--print_features", default=False, action="store_true")
    parser.add_argument("--bypass_tx_type_filter", default=False, action="store_true")
    parser.add_argument("--assume_cds_same", default=False, action="store_true",
                        help="Sets CDS to same as transcript. Useful for writing out eg snoRNAs")
    args = parser.parse_args()

    if not args.no_fasta:  # ie if fasta
        assert args.genome_fasta != "None", "Need to provide a genomic fasta unless --no_fasta is used"

    df, exon_d, genomic_starts_stops = parse_features(args)

    if not args.print_features:
        if args.filter_for_longest:
            # filter for longest cds, then longest transcript of those with the same cds length
            maxes = df.groupby("gene_id").cds_length.transform(max)
            df = df[df["cds_length"] == maxes].reset_index()
            maxes = df.groupby("gene_id").transcript_length.transform(max)
            df = df[df["transcript_length"] == maxes].reset_index()

            # and finally remove any duplicates left over
            df = df.drop_duplicates(subset=["gene_id"], keep="first")
            df = df[
                ["transcript_id", "gene_name", "gene_id", "cds_start", "cds_end", "cds_length", "transcript_length"]]

        # add genomic start stops data
        g_starts = []
        g_stops = []
        for gene in df["gene_name"]:
            g_starts.append(":".join(genomic_starts_stops[gene]["starts"]))
            g_stops.append(":".join(genomic_starts_stops[gene]["stops"]))
        df["genomic_cds_starts"] = g_starts
        df["genomic_cds_stops"] = g_stops

        print("Writing info file to " + args.output_filename)
        df.to_csv(args.output_filename, index=False, sep="\t")
        print("done!")

        if not args.no_fasta:
            args.output_fasta = args.output_filename + '.fasta'
            if os.path.exists(args.output_fasta):
                os.remove(args.output_fasta)
            print("Generating transcript fasta")
            generate_fasta(df, exon_d, args.genome_fasta, args.output_fasta, args.stop_correction)


if __name__ == "__main__":
    main()
