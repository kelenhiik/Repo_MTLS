""" Parses PSSM profiles for machine learning """
import re

def pssm_parsing(filename):
    """ Sliding windows for PSSM profile """
    profile = open(filename, 'r')
    profile2=profile.readlines()
    for position in (profile2[2]):
        if position == ' ':
            pass
        else:
            print(position)
        
    
    #print (profile)
    #re.compile[" + \d + [A-Z]"] #Used to indicate a set of characters, separated by "-"
    profile.close()



if __name__ == "__main__":
    print(pssm_parsing(">D1A04.fasta.pssm"))
    
