""" Useful codes for looking at my prediction values and amount of proteins """


def scores2(filename):
    """ This works for the SVM file format. It takes a txt file from the
    crossvalidation output and gives the values in the printout.
    The last value is the highest. Not perfect, but gets the job done for me """

    emptylist = []
    values = []
    filename1 = open(filename, 'r')
    for line in filename1:
        #print (line)
        if line.startswith("["):
            pass
        else:
            pla = line.rstrip()
            pla = pla.split()
            emptylist.extend(pla)
    #for element in emptylist:
            #print (pla)
        #values.extend(element)
    values.extend(emptylist[4::5])
    values2 = sorted(values)
    print(values2)


def scores(filename):
    """ This works for random forest and decision tree, since it is hardcoded in the way I see the
    file. Does what the last function does. """
    emptylist = []
    values = []
    filename1 = open(filename, 'r')
    for line in filename1:
        #print (line)
        if line.startswith("["):
            pass

        else:
            emptylist.append(line)

    for element in emptylist:
        #print (element [8:14])
        values.append(element[8:16]) #range for random forest results
        #values.append(element[4:11]) #range for decisiontree results
        #print (element)


    sorting = sorted(values)
    print(sorting)
    #sorted_keys = sorted(emptylist[])
    #print (sorted_keys)

def protein_nr(filename):
    """ This takes a 3.line.txt and collects the ID's of the proteins so it gives the amount of proteins I have in a file. """

    emptylist = []
    values = []
    filename1 = open(filename, 'r')
    for line in filename1:
        #print (line)
        if line.startswith(">"):
            pla = line.rstrip()
            emptylist.append(pla)

        else:
            pass
    #for element in emptylist:
            #print (pla)
        #values.extend(element)

    print(len(emptylist))

def format_svm(filename):
    #OUTPUT = open("../data/testing_sets/protein_names.txt", 'w')
    viewing = open(filename, 'r')
    lists=[]
    for lines in viewing:
        headings = lines[:4]
        if headings not in lists:
            lists.append(headings)
    print(lists[1:120])
        #OUTPUT.write(headings + '\n')
    #OUTPUT.close()



if __name__ == "__main__":
    #print(scores("randomforest_second_set_of_ws.txt"))
    print(protein_nr("../data/testing_sets/dataset_of_50.txt"))
