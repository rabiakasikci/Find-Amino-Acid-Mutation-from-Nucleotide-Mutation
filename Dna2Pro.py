# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 18:19:24 2023

@author: Rabia KAŞIKCI

"""

import sys

def translate (seq,dislocation):
    table = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': '-', 'TAG': '-',
        'TGC': 'C', 'TGT': 'C', 'TGA': '-', 'TGG': 'W',
    }

    
    protein = ""

    if dislocation == 0:
        size=int(len(seq)/3)
    elif dislocation == 1 or dislocation == 2:
        size = int(len(seq) / 3) - 1
    for i in range (size):
      codon = seq[3 * i + 0 + dislocation] + seq[3 * i + 1 + dislocation] + seq[3 * i + 2 + dislocation]  
      protein += table[codon]

    return protein








A=sys.argv[1]
with open(A) as file:
    mutation_list=file.readlines()
    
    





for i in range(len(mutation_list)):
    file=open(str(mutation_list[i][:-2])+"_Mutated.txt", "r")
    protein_file=open(str(mutation_list[i][:-2])+"_Protein.txt", "w")
    seq=file.read()
    protein=translate(seq,0)
    protein_file.write(str(protein))
    protein_file.close()
