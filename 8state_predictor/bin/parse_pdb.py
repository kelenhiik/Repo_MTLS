import numpy as np
#convert = lambda x: str(x.strip()'C') 

NAMES = ('1A62', '1AH7', '1AHO', '1ATG', '1B0B', '1BGF', '1BKR', '1BRT', '1BX7', '1BYI', '1C0P',  '1C1K', '1C7K', '1CC8', '1CY5', '1D4O', '1D5T', '1DK8', '1DP7', '1DS1', '1DYP', '1E58', '1E5K', '1E6U', '1EAZ', '1EB6', '1EJ8', '1ES5', '1ES9', '1EUW', '1EW4', '1F1E', '1FCY', '1FG7', '1FP2', '1FS7', '1FT5', '1G12', '1G2R', '1G5A', '1G66', '1G6X', '1G8A', '1GCI', '1GKM', '1GMX', '1GP0', '1GS5', '1GVP', '1GWE', '1GWM', '1GXU', '1H12', '1H16')

OUTPUT = open('./PDB/dataset_of_50.txt','w')
for names in NAMES:
    lower=names.lower()
    INPUT = ('./PDB/pdb' + str(lower) + '.ent.txt')
    pdb_ss_list = []
    pdb_seq_list = []
    format_pdb = (np.genfromtxt(INPUT,
                                 skip_header=27,
                                 dtype = str,
                                 usecols=range(3, 5)))

    for lines in format_pdb:
        pdb_seq_list.append(lines[0])
        if lines[1] not in 'GIHEBTSC':
            pdb_ss_list.append('C')
        else:
            pdb_ss_list.append(lines[1])
    pdb_ss_list = "".join(pdb_ss_list)
    pdb_seq_list = "".join(pdb_seq_list)
    OUTPUT.write('>' + str(lower) + '\n' + pdb_seq_list + '\n' + pdb_ss_list  + '\n')
OUTPUT.close()


"""
if aminoacid not in "ACDEFGHIKLMNPQRSTVWY"

def fun(x):
    if x == 'G', 'I', 'H', 'E', 'B', 'T', 'S', 'C':
        pass
    else:
        x = 'C'
"""
