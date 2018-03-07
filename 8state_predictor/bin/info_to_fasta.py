""" Parses lines in fasta format from .txt to a destination in .fasta - format """
import all_parsing_codes

################################################################################
# Takes a 3line.txt file, with fasta info and makes a fasta file with heading and
# second line (here it's the sequence). Saves these files to specified location.
################################################################################

# Enter 3line.txt file for parsing

FILE_FOR_PARSING = '../data/train_test_sets/dssp_8_state.3line.txt'
DICTIONARY_OF_ID_SEQ = all_parsing_codes.fasta_parsing_from_3lines(FILE_FOR_PARSING)

# Enter a directory for fasta file output

DIRECTORY_FOR_FASTAS = '../data/FASTA/'

for identification in DICTIONARY_OF_ID_SEQ:

    filename_to_be = str(identification)+'.fasta'
    sequence = DICTIONARY_OF_ID_SEQ[identification]
    file_writing = open(DIRECTORY_FOR_FASTAS + filename_to_be, 'w')
    file_writing.write(identification + '\n' + sequence)
    file_writing.close()
