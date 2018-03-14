import Bio
from Bio.PDB import PDBList, PDBParser, PPBuilder, DSSP

"""
output_list = PDBList()
PDBlist_names=['1A62', '1AH7', '1AHO', '1AMT', '1ATG', '1B0B', '1B5E', '1BGF', '1BKR', '1BRT', '1BTE', '1BTK', '1BX7', '1BYI', '1C0P', '1C1D', '1C1K', '1C4Q', '1C5E', '1C7K', '1CC8', '1CCW', '1CCW', '1CXQ', '1CY5', '1D2S', '1D4O', '1D5T', '1D8W', '1DBW', '1DCS', '1DD9', '1DFM', '1DG6', '1DJ0', '1DK8', '1DLF', '1DP7', '1DS1', '1DYP', '1DZK', '1E2W', '1E30', '1E58', '1E5K', '1E6U', '1E7L', '1EAJ', '1EAQ', '1EAZ', '1EB6', '1EGW']
for i in PDBlist_names:
    output_list.retrieve_pdb_file(i,pdir='PDB')
"""

p = PDBParser()
structure = p.get_structure('X', './PDB/pdb1a62.ent')

model = structure[0]
dssp = DSSP(model, './PDB/pdb1a623.ent')

"""
ppb = PPBuilder()
pps = ppb.build_peptides(structure)
seq =  []
for peptides in pps:
    seqs = peptides.get_sequence()
    seq.append(seqs)
print(seq)

"""
