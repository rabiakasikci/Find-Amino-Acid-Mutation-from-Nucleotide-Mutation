# Python program to
# demonstrate merging
# of two files

import sys

A=sys.argv[1]

B=sys.argv[2]

data = data2 = ""

# Reading data from file1
with open(A) as fp:
    data = fp.read()


with open(B) as file:
    mutation_list=file.readlines()

# Reading data from file2
for i in range(len(mutation_list)):
    data_yeni = ""
    with open(str(mutation_list[i][:-2])+'_Protein.txt') as fp:
        data2 = fp.read()

    # Merging 2 files
    # To add the data of file2
    # from next line
    data_yeni = data+ "\n"+">Mutated protein" + "\n" + data2
       
    
    with open("Ref_"+str(mutation_list[i][:-2])+".txt", 'w') as fp:
        fp.write(data_yeni)
    

