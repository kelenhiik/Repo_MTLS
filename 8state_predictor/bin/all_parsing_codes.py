import numpy as np

################################################################################
# This function takes a filename and a sliding window and returns all sequences in binary with appropriate sliding windows. The format for SVM predicting?
################################################################################


def parse_unknown_file(filename, sliding_window):
    all_unknown_topo_seq_set = []

    dictionary=fasta_parser_onlyseq(filename)

    for ID in dictionary:                  
        sliding_window_of_unknown_topo_seq = encode_protein((dictionary[ID][0]), sliding_window)
        all_unknown_topo_seq_set.extend(sliding_window_of_unknown_topo_seq)

        

    all_unknown_topo_seq_set = np.array(all_unknown_topo_seq_set)
    return all_unknown_topo_seq_set
    
    
################################################################################
# This function takes a filename and a sliding window and returns all sequences in binary with appropriate sliding windows. The format for SVM training.
################################################################################

def parse_with_all_codes(filename, sliding_window):
    all_training_set = []
    all_topologies = []
    dictionary=fasta_parser(filename)
    #get the keys in the same order, since if i wanna cross-validate, I'd have the same one's when checking dif parameters
    sorted_keys = sorted(dictionary.keys(), key=lambda x: x[3:])

    for ID in sorted_keys:                  
        training_set = encode_protein((dictionary[ID][0]), sliding_window)
        all_training_set.extend(training_set)
        topology_set=topology_in_numbers((dictionary[ID])[1])
        all_topologies.extend(topology_set)
        
    all_topologies = np.array(all_topologies)
    all_training_set = np.array(all_training_set)
    return all_training_set, all_topologies
 
################################################################################    
# This function takes a filename and a sliding window. Then it calls the parser function and makes a dictionary out of the filename. Afterwards it splits the dictionary keys so I could have a separate training and testing set. Complicated with a dictionary, bias is minimized by sorting the dictionary keys by the positions in the name of the key that have been assigned randomly in pdb. The out of this key list it takes 70% for training and results in 30% for testing sets that it encodes for proteins and topology using custom functions, returns results as numpy arrays.
################################################################################


def parse_with_train_test(filename, sliding_window):
    all_training_set = []
    train_topologies = []
    
    all_test_set = []
    test_topologies = []
    
    dictionary=fasta_parser(filename)

    # TODO: explain in a comment : 
    #sorts keys in my dictionary based on the values from 3:end and saves them in a variable sorted_keys so I can specify from that list the 70% i wanna use for testing. lambda is a small function, so insead of defining a function (x) you put lambda. 
      
    sorted_keys = sorted(dictionary.keys(), key=lambda x: x[3:])
    keys_train = sorted_keys[:int(0.7 * len(dictionary))]
    
    # Train set:
    for ID in keys_train:      
        training_set = encode_protein((dictionary[ID][0]), sliding_window)
        all_training_set.extend(training_set)
        topology_set=topology_in_numbers((dictionary[ID])[1])
        train_topologies.extend(topology_set)
    
    # Test set:
    for ID in set(dictionary) - set(keys_train):      
        test_set = encode_protein((dictionary[ID][0]), sliding_window)
        all_test_set.extend(test_set)
        topology_set=topology_in_numbers((dictionary[ID])[1])
        test_topologies.extend(topology_set)
    
    all_training_set = np.array(all_training_set)
    train_topologies = np.array(train_topologies)
    all_test_set = np.array(all_test_set)
    test_topologies = np.array(test_topologies)
    
    return all_training_set, train_topologies, all_test_set, test_topologies
    
    
################################################################################
# Takes a file with ID, seq, topology and assigns ID as key, seq and topology as values.
################################################################################


def fasta_parser(filename):
    list1=[line.upper().rstrip() for line in (open (filename, 'r')) if len (line.strip()) != 0]
    
    dict1=dict(zip(list1[::3], zip (list1[1::3], list1[2::3])))
    return (dict1)


def fasta_parser_onlyseq(filename):
    list1=[line.upper().rstrip() for line in (open (filename, 'r')) if len (line.strip()) != 0]
    
    dict2=dict(zip(list1[::2], list1[1::2]))
    return (dict2)


################################################################################
# Manually made dictionary for the topologies in numerical form
################################################################################


topology_dict={'G':1, 'I':2, 'H':3, 'E':4, 'B':5, 'T':6, 'S':7, 'C':8}


################################################################################
### Create a binary dictionary for the amino acid residues and specify what to do with uncommon residues 
################################################################################


amino_acid_dict={}
aminoacids='GALMFWKQESPVICYHRNDT'
for aa in aminoacids:
    temp_vector= [0]*20
    
    temp_vector[aminoacids.index(aa)]=1
    amino_acid_dict[aa]=temp_vector

amino_acid_dict['X'] = [1/20] * 20
temp_vector= [0]*20
temp_vector[aminoacids.index('Q')]=0.5
temp_vector[aminoacids.index('E')]=0.5
amino_acid_dict['Z'] = temp_vector
temp_vector= [0]*20
temp_vector[aminoacids.index('N')]=0.5
temp_vector[aminoacids.index('D')]=0.5
amino_acid_dict['B'] = temp_vector
temp_vector= [0]*20
temp_vector[aminoacids.index('I')]=0.5
temp_vector[aminoacids.index('L')]=0.5
amino_acid_dict['J'] = temp_vector

#FIXME decide what to do with these:
amino_acid_dict['O'] = amino_acid_dict['S']
amino_acid_dict['U'] = amino_acid_dict['S']


################################################################################
# Go through a sequence and do all full sliding windows#
################################################################################


def encode_protein(seq, windowlength):
    training_set = []
    pad=int(windowlength//2)
    for i in range(len(seq)): # All full windows
        if i < pad:
            
            number_of_pads = pad-i
            temp_encoded_window = [0]*(20*number_of_pads)
            for c in seq[:i+pad+1]:       # Go through each AA in sliding window
                temp_encoded_window.extend(amino_acid_dict[c])  # Extend (not append)
            training_set.append(temp_encoded_window) # Save to training set
        elif i > (len(seq)-pad-1):
            #print(i)
            number_of_pads = pad - (len(seq)- 1 - i)
            temp_encoded_window = [] #[0]*(20*number_of_pads)
            for c in seq[i-pad:]:       # Go through each AA in sliding window
                temp_encoded_window.extend(amino_acid_dict[c])  # Extend (not append)
            temp_encoded_window.extend([0]*(20*number_of_pads))
            training_set.append(temp_encoded_window) # Save to training set
        else:
            temp_window = seq[i-pad:i+pad+1] # Extract sliding window
            temp_encoded_window = []
            for c in temp_window:       # Go through each AA in sliding window
                temp_encoded_window.extend(amino_acid_dict[c])  # Extend (not append)
            # print(temp_encoded_window)
            training_set.append(temp_encoded_window) # Save to training set
    return training_set

################################################################################
# Fix topologies #
################################################################################
    

def topology_in_numbers(my_topo):
    topologies=[]
    for topology in my_topo:

        topologies.append(topology_dict[topology])
    
    return topologies
    
if __name__ == "__main__":
    #print(parse_with_all_codes("dssp_8_state.3line.txt", 3))
    print(fasta_parser_onlyseq('250_270_set.3line.txt'))

