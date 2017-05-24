from Bio import AlignIO
import Bio.SeqIO
import time
from timer import gettime

@gettime
def _read_file(filepath):
    reader = Bio.SeqIO.parse(filepath, 'fasta')
    for _ in reader:
        pass

if __name__ == "__main__":
    print "Bioinformatics 2017 project"

    print "Done in %f seconds" % _read_file('../data/msa-alignment/PF00290_full.txt_with_org.txt')[1]
    print "Done in %f seconds" % _read_file('../data/msa-alignment/PF00291_full.txt_with_org.txt')[1]
