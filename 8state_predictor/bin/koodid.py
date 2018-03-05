def fasta_parser_onlyseq(filename):
    emptylist=[]
    values=[]
    filename1= open(filename, 'r')
    for line in filename1:
        #print (line)
        if line.startswith("["):
            pass
            
        else: 
            emptylist.append(line)

    for element in emptylist:
        #print (element [8:14])
        #values.append(element[8:16]) #range for random forest
        values.append(element[4:11]) #range for decisiontree
        
    sorting=sorted(values)
    print (sorting)           
    #sorted_keys = sorted(emptylist[])
    #print (sorted_keys)
    
if __name__ == "__main__": 
    print(fasta_parser_onlyseq("decisiontree_result.txt"))    

