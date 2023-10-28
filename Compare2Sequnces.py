# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 18:46:11 2023

@author: Rabia KAŞIKCI
"""
import sys


A=sys.argv[1]


with open(A) as file:
    mutation_list=file.readlines()

for i in range(len(mutation_list)):
    mutation_file=open("Aminoacid_Mut_"+str(mutation_list[i][:-2])+str(".txt"),"w") 
    with open("CO_Ref_"+str(mutation_list[i][:-2])+str(".txt")) as file:
        output=file.readlines()
    seq1=output[1]
    seq2=output[3]
    for track in range(len(seq1)):		
	    #print(len(seq1), len(seq2))	
	    if seq1[track] != seq2[track]:	
		    mutation_file.write(str(seq1[track]) + str(track + 1) + str(seq2[track])+"\n")
    mutation_file.close()			
				


