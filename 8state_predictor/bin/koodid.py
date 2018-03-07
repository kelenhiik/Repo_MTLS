def scores2(filename):
    """ This works for the SVM file format """
    
    emptylist=[]
    values=[]
    filename1= open(filename, 'r')
    for line in filename1:
        #print (line)
        if line.startswith("["):
            pass
            
        else: 
            pla=line.rstrip()
            pla=pla.split()
            emptylist.extend(pla)
    #for element in emptylist:
            #print (pla)
        #values.extend(element)
    values.extend(emptylist[4::5])
    values2=sorted(values)
    print(values2)


def scores(filename):
    """ This works for random forest and decision tree, since it is hardcoded in the way I see the 
    file """
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
        #values.append(element[8:16]) #range for random forest results
        #values.append(element[4:11]) #range for decisiontree results
        print (element)

        
    #sorting=sorted(values)
    #print (sorting)           
    #sorted_keys = sorted(emptylist[])
    #print (sorted_keys)




if __name__ == "__main__": 
    #print(scores("decisiontree_result.txt"))
    print(scores2("SVM_result.txt"))

