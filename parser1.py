def fasta_parser(filename):
    
    heading_list=[]
    seqtop_list=[]
    #seq_list=[]
    #top_list=[]
    for sitt1, sitt2 in enumerate (open(filename)):
    
        sitt2=sitt2.strip() #if the lines have spaces in the beginning or end
        #print (sitt1)
        if sitt2.startswith(">"):
            heading=sitt2.split(">")
            #print (heading)
            
            heading_list.append(heading[1])
        else:
            if len(sitt2.strip()) != 0 : #to take out the last empty line fo the file
                seqtop_list.append(sitt2)
                
    #seq_list.append(seqtop_list[::2])
    #top_list.append(seqtop_list[1::2])
    dict1=dict(zip(heading_list, zip(seqtop_list[::2], seqtop_list[1::2])))        
                
                #print(read)
    print (dict1)

       
                
            

            
            #fasta_dict[keys] = 
    #filehandle.close()
    #return fasta_dict

if __name__ == "__main__": 
    print(fasta_parser("8_state_smallerset.3line.txt"))
