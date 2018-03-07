""" Parses PSSM profiles for machine learning """
import re

def pssm_parsing(filename):
    """ Sliding windows for PSSM profile """
    profile = open(filename, 'r')
    for line in profile:
        print(line)
    #re.compile[" + \d + [A-Z]"]



if __name__ == "__main__":
    print(pssm_parsing(">D1A04.fasta.pssm"))
    
