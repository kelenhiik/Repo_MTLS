import Bio
from Bio.PDB import PDBList, PDBParser, PPBuilder, DSSP


output_list = PDBList()
PDBlist_names=['1A62', '1AH7', '1AHO', '1AMT', '1ATG', '1B0B', '1B5E', '1BGF', '1BKR', '1BRT', '1BTE', '1BTK', '1BX7', '1BYI', '1C0P', '1C1D', '1C1K', '1C4Q', '1C5E', '1C7K', '1CC8', '1CCW', '1CXQ', '1CY5', '1D2S', '1D4O', '1D5T', '1D8W', '1DBW', '1DCS', '1DD9', '1DFM', '1DG6', '1DJ0', '1DK8', '1DLF', '1DP7', '1DS1', '1DYP', '1DZK', '1E2W', '1E30', '1E58', '1E5K', '1E6U', '1E7L', '1EAJ', '1EAQ', '1EAZ', '1EB6', '1EGW', '1EJ8', '1EKQ', '1ELK', '1ELU', '1ES5', '1ES9', '1ET1', '1EU1', '1EUV', '1EUW', '1EVL', '1EW4', '1EZG', '1F0L', '1F1E', '1F2T', '1F46', '1F86', '1F8E', '1F9V', '1FCQ', '1FCY', '1FG7', '1FIU', '1FM0', '1FO8', '1FP2', '1FS7', '1FSG', '1FT5', '1FYE', '1G12', '1G2R', '1G2Y', '1G3P', '1G5A', '1G61', '1G66', '1G6G', '1G6X', '1G8A', '1GA6', '1GCI', '1GHE', '1GJ7', '1GK9', '1GKM', '1GMU', '1GMX', '1GNL', '1GP0', '1GPP', '1GQI', '1GS5', '1GU2', '1GUT', '1GV9', '1GVE', '1GVF', '1GVP', '1GWE', '1GWM', '1GXM', '1GXU', '1GY7', '1GYX', '1H12', '1H16']
for i in PDBlist_names:
    output_list.retrieve_pdb_file(i,pdir='PDB')
"""

p = PDBParser()
structure = p.get_structure('X', './PDB/pdb1a62.ent')

model = structure[0]
dssp = DSSP(model, './PDB/pdb1a623.ent')

ppb = PPBuilder()
pps = ppb.build_peptides(structure)
seq =  []
for peptides in pps:
    seqs = peptides.get_sequence()
    seq.append(seqs)
print(seq)

"""
