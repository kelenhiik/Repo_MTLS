import pandas as pd 
import numpy as np


def fasta_parser(filename):
    
    list1=[line.rstrip() for line in (open(filename,'r')) if len(line.strip()) != 0]
    dict1=dict(zip(list1[::3],  zip(list1[1::3],list1[2::3])))
    
    #for key in dict1:
        #seq, topol = dict1[key]
        #assert len(seq) == len(topol) -----for testing if it's right, if the lengths are the same, the chances are it is right.
    
    return (dict1)

#files=open("testfile.csv","a")
frame=pd.DataFrame.from_dict(fasta_parser("8_state_smallerset.3line.txt"))
#pd.read_csv("testfile.csv").append(frame)
#frame.to_csv("testfile.csv")
#files.close()
#print (frame)

#if __name__ == "__main__": 
#    print(fasta_parser("8_state_smallerset.3line.txt"))
       
