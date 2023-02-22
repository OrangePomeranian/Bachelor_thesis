#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 28 23:18:59 2022

@author: daria
"""

import pandas as pd
import os
import numpy as np
import time
import statistics

start = time.time()

delecje = pd.read_csv('/Users/daria/Desktop/Dane_licencjat/Walidacja_1/delecje.txt', sep =' ')
duplikacje = pd.read_csv('/Users/daria/Desktop/Dane_licencjat/Walidacja_1/duplikacje.txt', sep = ' ')
delecje, duplikacje = delecje[['path','Nr','Pindel']], duplikacje[['path','Nr','Pindel']]

#delecje.drop([4], axis = 0, inplace = True)
#duplikacje.drop([10], axis = 0, inplace = True)

list_del_CNV = []
list_del_Pin = []
list_dup_CNV = []
list_dup_Pin = []
roznice = []

# Znaki
for numer_osobnika in range(0, len(delecje)):
    CNVnator_input = pd.read_csv(delecje['path'].iloc[numer_osobnika], sep = ' ')
    CNVnator_input = CNVnator_input.drop(columns=['Unnamed: 0','0'])
    Pindel_input = pd.read_csv(delecje['Pindel'].iloc[numer_osobnika], sep = ',')
    list_del_CNV.append(len(CNVnator_input['dane1'])) 
    list_del_Pin.append(len(Pindel_input['pocz']))
    print(len(CNVnator_input['dane1']) - len(Pindel_input['pocz']))
    roznice.append(len(CNVnator_input['dane1']) - len(Pindel_input['pocz']))
    #print(len(Pindel_input['pocz']))
    
    

for numer_osobnika in range(0, len(duplikacje)):
    CNVnator_input = pd.read_csv(duplikacje['path'].iloc[numer_osobnika], sep = ' ')
    CNVnator_input = CNVnator_input.drop(columns=['Unnamed: 0','0'])
    Pindel_input = pd.read_csv(duplikacje['Pindel'].iloc[numer_osobnika], sep = ',')
    list_dup_CNV.append(len(CNVnator_input['dane1'])) 
    list_dup_Pin.append(len(Pindel_input['pocz']))
    print(len(CNVnator_input['dane1']) - len(Pindel_input['pocz']))

'''
# Wlicoxon 
Wilcoxon_CNVnator_delecje = list()
Wilcoxon_Pindel_delecje = list()

for numer_osobnika in range(0, len(delecje)):
    CNVnator_input = pd.read_csv(delecje['path'].iloc[numer_osobnika], sep = ' ')
    CNVnator_input = CNVnator_input.drop(columns=['Unnamed: 0','0'])
    Pindel_input = pd.read_csv(delecje['Pindel'].iloc[numer_osobnika], sep = ',')
    Wilcoxon_CNVnator_delecje.append(CNVnator_input['dlug'].mean())
    Wilcoxon_Pindel_delecje.append(Pindel_input['dlug'].mean())
 
Wilcoxon_CNVnator = pd.DataFrame({'Dlug'  : Wilcoxon_CNVnator_delecje})
Wilcoxon_CNVnator['Program'] = 'CNVnator'
Wilcoxon_Pindel = pd.DataFrame({'Dlug'  : Wilcoxon_Pindel_delecje})
Wilcoxon_Pindel['Program'] = 'Pindel'

Wilcoxon_delecje = pd.concat([Wilcoxon_CNVnator, Wilcoxon_Pindel])

Wilcoxon_CNVnator_duplikacje = list()
Wilcoxon_Pindel_duplikacje = list()

for numer_osobnika in range(0, len(duplikacje)):
    CNVnator_input = pd.read_csv(duplikacje['path'].iloc[numer_osobnika], sep = ' ')
    CNVnator_input = CNVnator_input.drop(columns=['Unnamed: 0','0'])
    Pindel_input = pd.read_csv(duplikacje['Pindel'].iloc[numer_osobnika], sep = ',')
    Wilcoxon_CNVnator_duplikacje.append(CNVnator_input['dlug'].mean())
    Wilcoxon_Pindel_duplikacje.append(Pindel_input['dlug'].mean())
    
Wilcoxon_CNVnator = pd.DataFrame({'Dlug'  : Wilcoxon_CNVnator_duplikacje})
Wilcoxon_CNVnator['Program'] = 'CNVnator'
Wilcoxon_Pindel = pd.DataFrame({'Dlug'  : Wilcoxon_Pindel_duplikacje})
Wilcoxon_Pindel['Program'] = 'Pindel'

Wilcoxon_duplikacje = pd.concat([Wilcoxon_CNVnator, Wilcoxon_Pindel])
    

'''

print(list_del_CNV)
print(list_del_Pin)
print(roznice)

end = time.time()
print(end - start)