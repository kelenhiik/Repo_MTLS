import random
list1 = [line.upper().rstrip() for line in (open('../data/train_test_sets/dssp_8_state.3line.txt', 'r')) if len(line.strip()) != 0]

dict1 = dict(zip(list1[::3], zip(list1[1::3], list1[2::3])))
randomized_keys = list(dict1.keys())

new_set = randomized_keys[:int(0.3 * len(dict1))]
#print (len(new_set))
output=open("../data/train_test_sets/randomized109_proteins.3line.txt",'w')
for identification in new_set:
    #variable = dict1[identification][0]
    output.write(identification + '\n' + dict1[identification][0] + '\n' + dict1[identification][1] + '\n')
    print (identification + '\n' + dict1[identification][0] + '\n' + dict1[identification][1] + '\n')
output.close()

