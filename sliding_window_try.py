import numpy as np

def fasta_parser(filename):
    list1=[line.rstrip() for line in (open (filename, 'r')) if len (line.strip()) != 0]
    dict1=dict(zip(list1[::3], zip (list1[1::3], list1[2::3])))
    return (dict1)

def slidw1(seq,sw):
    #sw1-sliding window positions after element in view
    #sw2-sliding window positions before element in view
    #sw1=(sw//2)
    #sw2=-sw1
    #print (sw2)
    #sw=int(sw)
    window=[]
    all_windows=[]
    aa_list=[]
    aa_=[]
   # print (seq)
    #prints dictionary
   # print ("-----")
    for ID in seq:
       # print (ID)
        #prints the dictionary keys aka ID
       # print("llllllll")
        aa_list.append((seq[ID])[0])
    print(aa_list)    
    #prints the dictionary's first values, so ID value in position 0 
   # for aa_element in aa_list:
           # print (aa_value)
           # aa_list.append(aa_value)
   
    pos_in_window=list(range(0,len(aa_list)))
    #print(pos_in_window)#---[0, 1,] position of sequences in list
    #seqkeys= seq.values[1]   
    for element in aa_list:
        #for positions in
        print (element) #this just prints the sequences, because I guess it takes the element as the thing that fills the positions 0 and 1 that i have.... 
       # window.append(element)
    #print(window) #['A', 'D', 'E', 'R', 'R', 'G']

    
    
    for number in pos_in_window: 
        #print (number)
                        #0 
                        #1
                        #2
                        #3
                        #4
                        #5

        if sw+number <= len(seq):
        # if sliding window size and the number from pos_window sum up to be less or equal to the length of the sequence, so it wouldn't continue going over the sequence creating lists smaller than the window size. 
        
            all_windows.extend (window[number:(number+sw)])
            #adds all the values in window list that correspond to the positions from and between number and sw+number (where it starts the value and goes one by one, so does the sliding window shift as much) into one continous list.
         
    
    print (all_windows) #----['A', 'D', 'E', 'D', 'E', 'R', 'E', 'R', 'R', 'R', 'R', 'G'] this maybe works, but might be too complicated and mby does not work for larger data??
        
        
        
def slidw2(seq,sw):
    window=[]
    pos_in_window=[]
    all_windows=[]
    for position, element in enumerate(seq):
        pos_in_window.append(position)
        print (position, element)
        #this might be quicker if i could figure out if there is a way to use this
        #for positions in
        #window.append(element)
    
    

    


        
def empty_vec(seq):

    #print (seq)

    for i in range (0,len(seq)):
        #print(i)
        vector=[0]*(len(seq))
        
        print (vector)
        #print(-(11//2))
        


if __name__ == "__main__":
    print (slidw1(fasta_parser("shortseq.txt"),3) )
