#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 21 12:45:49 2022

@author: daria
"""

# Pindel

import pandas as pd
import os

import os

kolumny = ['chr_kosz','Chr', 'pocz', 'kon','dlug', 'kosz']

def pindel_raw(dane, nazwa, del_dup):
    dane = pd.read_csv(dane, sep = ' ', names = kolumny)
    #dane['ciag_sesji'] = dane.apply(lambda row: 0 if (row['Chr'] == 'X' or row['Chr'] == 'Y') else (1), axis = 1)
    #dane = dane.drop(dane[dane.ciag_sesji == 0].index)
    dane = dane[dane['Chr'] != 'X']
    dane = dane[dane['Chr'] != 'Y']
    dane = dane.drop(columns = ['chr_kosz', 'kosz'])
    dane.to_csv("%s%s%s%s" % ('raw_', del_dup,'_', nazwa,), sep = ' ')
    
    
for filename in os.scandir('/Users/daria/Downloads/dane/pindel'):
    nazwa = filename.path.split('_',1)[1]
    print(nazwa)
    
    if nazwa == 'Store':
        continue
    else:
        del_dup = nazwa.split('.',1)[1].split('.',1)[0]
        pindel_raw(filename.path, nazwa, del_dup)
    

    
def pindel_clean(dane, nazwa, del_dup):
    dane = pd.read_csv(dane, sep = ' ', names = kolumny)
    #dane['ciag_sesji'] = dane.apply(lambda row: 0 if (row['Chr'] == 'X' or row['Chr'] == 'Y') else (1), axis = 1)
    #dane = dane.drop(dane[dane.ciag_sesji == 0].index)
    #print(len(dane))

    #print(len(dane))
    dane = dane[dane['Chr'] != 'X']
    dane = dane[dane['Chr'] != 'Y']
    dane = dane[dane['dlug'] > 50]
    dane = dane[dane['dlug'] < 5000000]
    dane = dane.drop(columns = ['chr_kosz', 'kosz'])
    dane.to_csv("%s%s%s%s" % ('clean_', del_dup,'_', nazwa,), sep = ' ')
    
for filename in os.scandir('/Users/daria/Downloads/dane/pindel'):
    nazwa = filename.path.split('_',1)[1]
    print(nazwa)
    if nazwa == 'Store':
        continue
    else:
        del_dup = nazwa.split('.',1)[1].split('.',1)[0]
        pindel_clean(filename.path, nazwa, del_dup) 
        

lista = []
for filename in os.scandir('/Users/daria/Desktop/test2'):
    lista.append(filename.path)
lista.sort() 
print(lista)

print('tutaj')
lista.remove('/Users/daria/Desktop/test2/.DS_Store')
lista.remove('/Users/daria/Desktop/test2/Pindel.py')

lista.sort() 
#print(lista)
#print('--------------------------------------------------------')
# podzielic na 4 listy 
lista_clean_del = lista[0:11] # git
#print(lista_clean_del)
#print(len(lista_clean_del))

lista_clean_dup = lista[11:22] #git
#print(lista_clean_dup)
#print(len(lista_clean_dup))
#print('--------------------------------------------------------')
lista_raw_del = lista[22:33] #git
#print(lista_raw_del)
#print(len(lista_raw_del))
#print('--------------------------------------------------------')
lista_raw_dup = lista[33:len(lista)]
#print(lista_raw_dup)
#print(len(lista_raw_dup))




# merging two csv files
dane = pd.concat(
    map(pd.read_csv, lista_clean_del), ignore_index=True)

dane.to_csv('lista_clean_del_razem.txt', index = False)



dane = pd.concat(
    map(pd.read_csv, lista_clean_dup), ignore_index=True)

dane.to_csv('lista_clean_dup_razem.txt', index = False)



dane = pd.concat(
    map(pd.read_csv, lista_raw_del), ignore_index=True)

dane.to_csv('lista_raw_del_razem.txt', index = False)



dane = pd.concat(
    map(pd.read_csv, lista_raw_dup), ignore_index=True)

dane.to_csv('lista_raw_dup_razem.txt', index = False)        
