import numpy as np

def parse_with_all_codes(filename, sliding_window):
    all_training_set = []
    all_topologies = []
    dictionary=fasta_parser(filename)
    
    for ID in dictionary:
                   
        training_set = encode_protein((dictionary[ID][0]), sliding_window)
        all_training_set.extend(training_set)
        topology_set=topology_in_numbers((dictionary[ID])[1])
        all_topologies.extend(topology_set)
        
    all_topologies = np.array(all_topologies)
    all_training_set = np.array(all_training_set)
    return all_training_set, all_topologies

#the method list.index(obj) returns the lowest index in list that obj appears.
def fasta_parser(filename):
    list1=[line.upper().rstrip() for line in (open (filename, 'r')) if len (line.strip()) != 0]
    
    dict1=dict(zip(list1[::3], zip (list1[1::3], list1[2::3])))
    return (dict1)




### Manually made dictionary for the topologies in numerical form###
topology_dict={'G':1, 'I':2, 'H':3, 'E':4, 'B':5, 'T':6, 'S':7, 'C':8}

### Create a binary dictionary for the amino acid residues###
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




##### Go through a sequence and do all full sliding windows###
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

###########################
# Fix topologies #
#######################    

def topology_in_numbers(my_topo):
    topologies=[]
    for topology in my_topo:

        topologies.append(topology_dict[topology])
    
    return topologies
if __name__ == "__main__":
    print(parse_with_all_codes("shortseq.txt", 3))

