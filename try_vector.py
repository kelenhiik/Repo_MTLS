import numpy as np
#Tee aminohapete sonastik
#siis on variaabel minu järjestusest
#siis tee tyhi vektor, mille pikkus on 20?
#siis tee for-loop, kus on index minu järejstuses
#järgnev rida on midagimidagi, vektor? ja siis .index() ja kuskil [index]
#seq=
#win=
#for i in range (1, len(seq)):
#print seq[i-win//2, i+win//2+1]""
#if i < beginning
#add 20 zeros
#elif i > end
#else:.

#the method list.index(obj) returns the lowest index in list that obj appears.

aminoacids='GALMFWKQESPVICYHRNDT'
seq1=['GQAML']
ws=3
ws2=int(ws//2)

#vector2=np.zeros(20)
#print (vector1)
#print(vector2)
def vect(seq):
    global listAA
    listAA = []
    for residues in seq:
        vector1= [0]*20
        pla=aminoacids.index(residues)
        vector1[pla]=1
        listAA.append(vector1)
    #print (listAA)
    return listAA #nested list where first list is the 20 position sequence for a specific residue.

def slidingwindow(seq):
    vector2 = [[0]*20]*ws2
    seq_ws=vector2+listAA+vector2
    windows2=[]
    list_of_sws=[]
    
    for binary_code_list_position in range(0,len(seq_ws)):
        if binary_code_list_position + ws <= len(seq_ws):
            windows2.append(seq_ws[binary_code_list_position:binary_code_list_position + ws])
    print(windows2)
    
    #  HOW TO GET EACH SLIDING WINDOW IN A FLAT SEPARATE LIST???????
    
    #for lists_of_sliding_window_lists in windows2:
        #print (lists_of_sliding_window_lists)
        #list_of_sws.append(lists_of_sliding_window_lists[0])
        #for lists_inside in lists_of_sliding_window_lists:
            #list_of_sws.append(lists_inside)
            #print(lists_inside)
    #print(list_of_sws)
    
    #print (windows2)

            

       
        
    #print (seq_ws)
        
for i in seq1:
    vect(i)
    slidingwindow(i)
    
        
#vector2 = [[0]*20]*3 #emptyvector full of zeros size 20*length of sliding window

#print (vector2)
