def fasta_parser(filename):
    
    #heading_list=[]
    #seqtop_list=[]
    #seq_list=[]
    #top_list=[]
    #for sitt1, sitt2 in enumerate (open(filename)):
    list1=[]
    #for line in (open(filename,'r')):
        #if len(line.strip()) != 0:
            #list1.append(line.rstrip())
            
    #dict1=dict(zip(list1[::3],  zip(list1[1::3],list1[2::3])))
            
        
    list1=[line.rstrip() for line in (open(filename,'r')) if len(line.strip()) != 0]
    dict1=dict(zip(list1[::3],  zip(list1[1::3],list1[2::3])))
    
    seq, topol = dict1['>d1ccd']
    assert len(seq) == len(topol)
    
    #print (dict1)
        #sitt2=sitt2.strip()
        #print (sitt1)
        #if sitt2.startswith(">"):
            #heading=sitt2.split(">")
            #print (heading)
            
            #heading_list.append(heading[1])
        #else:
            #if len(sitt2.strip()) != 0 :
                #seqtop_list.append(sitt2)
                
    #seq_list.append(seqtop_list[::2])
    #top_list.append(seqtop_list[1::2])
    #dict1=dict(zip(heading_list, zip(seqtop_list[::2], seqtop_list[1::2])))        
                
                #print(read)
    #print (dict1)

       
                
            

            
            #fasta_dict[keys] = 
    #filehandle.close()
    #return fasta_dict

if __name__ == "__main__": 
    print(fasta_parser("8_state_smallerset.3line.txt"))
