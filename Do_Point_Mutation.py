# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 16:51:57 2023

@author: Rabia KAŞIKCI
"""
import sys
A=sys.argv[1]
B=sys.argv[2]
with open(A) as file:
    output=file.readlines()
seq_name=output[0]
seq=output[1]



with open(B) as file:
    mutation_list=file.readlines()
print(mutation_list)


for i in range(len(mutation_list)):
    f = open(str(mutation_list[i][:-2])+"_Mutated.txt", "w")

    new_seq=""
    for j in range(len(seq)):
        
        
        if j==int(mutation_list[i][1]):
            print(j)
            new_seq=new_seq+str(mutation_list[i][2])
            
        else:
            new_seq=new_seq+str(seq[j])
            
    f.write(new_seq)
    print(new_seq)       
    f.close()      
    