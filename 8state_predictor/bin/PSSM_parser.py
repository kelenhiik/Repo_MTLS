""" Parses PSSM profiles for machine learning """
import re
import all_parsing_codes as alp
import numpy as np
def pssm_format(filename):
    """ Sliding windows for PSSM profile """
    info = (np.genfromtxt(filename, skip_header = 3, skip_footer = 5, autostrip = True, usecols = range(22,42)))/100

    return info


    """profile = open(filename, 'r')
    profile2=profile.readlines()
    for position in (profile2[2]):
        if position == ' ':
            pass
        else:
            print(position)


    #print (profile)
    #re.compile[" + \d + [A-Z]"] #Used to indicate a set of characters, separated by "-"
    profile.close()"""

def protein_w_pssm(filename, sliding_window):

    seq_profile_train = []
    topologies = []
    dictionary = alp.fasta_parser(filename)

    sorted_keys = sorted(dictionary.keys(), key=lambda x: x[3:])

    for identification in sorted_keys:
        #print (identification)
        pssm_array = pssm_format('../data/PSSM/' + identification + '.fasta.pssm')
        #print (pssm_array)
        sequence = dictionary[identification][0]

        pssm_set = []
        pad = int(sliding_window//2)
        for i in range (len(sequence)):
            #print (i)
                if i < pad:
                    number_of_pads = pad-i
                    temp_encoded_window = [0]*(20*number_of_pads)
                    for lists in pssm_array[:i+pad+1]:       # Go through each pssm list in sliding window
                        temp_encoded_window.extend(lists)  # Extend (not append)
                    pssm_set.append(temp_encoded_window) # Save to pssm training set
                    #print (pssm_set)

                elif i > (len(sequence)-pad-1):
                    #print(i)
                    number_of_pads = pad - (len(sequence)- 1 - i)
                    temp_encoded_window = []
                    for lists in pssm_array[i-pad:]:       # Go through each pssm list in sliding window
                        temp_encoded_window.extend(lists)  # Extend (not append)
                    temp_encoded_window.extend([0]*(20*number_of_pads))
                    pssm_set.append(temp_encoded_window) # Save to pssm training set
                else:
                    temp_window = pssm_array[i-pad:i+pad+1] # Extract sliding window
                    temp_encoded_window = []
                    for lists in temp_window:       # Go through each pssm list in sliding window
                        temp_encoded_window.extend(lists)  # Extend (not append)
                    # print(temp_encoded_window)
                    pssm_set.append(temp_encoded_window) # Save to training set
        return pssm_set



if __name__ == "__main__":
    print(protein_w_pssm("twoseq.txt", 3))
