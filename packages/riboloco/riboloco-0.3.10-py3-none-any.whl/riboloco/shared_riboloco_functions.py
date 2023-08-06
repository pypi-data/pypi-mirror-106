import pandas as pd


def read_info_file(filename):
    # Read in the info file
    info = pd.read_csv(filename, sep="\t")
    info["cds_start0"] = info["cds_start"] - 1
    return info


def read_fasta(filename):
    """
    This is a simple function written in base python that
    returns a dictionary made from a fasta file
    """
    # Read in the transcript fasta
    fasta = {}
    with open(filename, 'r') as file:
        for line in file:
            if line.rstrip()[0:1] == ">":
                this_tx_name = line.rstrip().replace(">", "")
            else:
                try:
                    fasta[this_tx_name] += line.rstrip()
                except KeyError:
                    fasta[this_tx_name] = line.rstrip()
    return fasta


def find_genomic_pos(feature_pos, exon_d, strand, debug=False):
    """
    This function takes a transcriptomic coordinate, and exon dictionary and strand, then finds
    the corresponding position in the genome.

    The exon dictionary is nested - for each exon (0 indexed) it contains the start, end, length and cumulative
    length. The exon d is ordered in transcript order - i.e. for - strand transcripts exon 0 start > exon 1 start
    However, exon 0 start < exon 0 end (starts are ALWAYS < ends for each exon, regardless of strand!)

    indexes:
    * genomic positions in the exon_d are 1 based because they're straight from the GTF
    * transcript positions are also 1 based for consistency
    """
    # First find the exon that it's within
    exon = min([a for a in exon_d.keys() if exon_d[a]["cumulative_length"] >= feature_pos])

    # Find the actual position
    assert strand == "+" or strand == "-", "Strand must be + or -"
    prev_cumul_length = exon_d[exon]['cumulative_length'] - exon_d[exon]['length']  # 1 based
    distance_into_exon = feature_pos - prev_cumul_length  # 1 based
    if strand == "+":
        pos = exon_d[exon]['start'] + distance_into_exon - 1  # 1 based correction
    else:
        pos = exon_d[exon]['end'] - distance_into_exon + 1  # 1 based correction

    if debug:
        print(exon)
        print(distance_into_exon)
        print(strand)

    return pos


def order_features(feature_list, strand):
    """
    Takes a list of dictionaries, each with start and end, and orders them into a new dictionary.
    It is strand aware (however note that feature starts are ALWAYS < feature ends)
    This function is useful for ordering exons or similar from genomic coordinates
    """
    d2 = {}
    out_d = {}  # dictionary with rank, start, end, length, cumulative length

    if strand == "-":
        m = -1
    else:
        m = 1

    for d in feature_list:
        d2[m * d["start"]] = m * d["end"]

    # order it
    d2 = dict(sorted(d2.items()))

    cumulative_length = 0
    i = -1

    # convert back to +ve values for those on negative strand
    for start, end in d2.items():
        i += 1
        length = m * end - m * start + 1  # +1 because GTF/GFF are 1 based
        cumulative_length += length

        out_d[i] = {'start': m * start,
                    'end': m * end,
                    'length': length,
                    'cumulative_length': cumulative_length}
    return out_d
