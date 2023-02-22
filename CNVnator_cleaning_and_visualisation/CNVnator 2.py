# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# CNVnator

import pandas as pd
import os


def czyszczenie_cnvnator_raw(nazwa, title):
    dane = pd.read_csv(nazwa, sep = '\s+', header = None)
    dane['Chr'], dane['dane1'] = dane[1].map(lambda row: row.split(':')[0]), dane[1].map(lambda row: row.split(':')[1])
    dane['dane2'], dane['dane1'] = dane['dane1'].map(lambda row: row.split('-')[1]), dane['dane1'].map(lambda row: row.split('-')[0])
    #print(len(dane))
    dane = dane[dane['Chr'] != 'X']
    dane = dane[dane['Chr'] != 'Y']
    #print(len(dane))  
    dane = dane.drop(columns = [1, 3, 4, 5, 6, 7, 8])
    dane.rename(columns = {2 :'dlug'}, inplace = True)
    duplikacje = dane[dane[0] == 'duplication']
    delecje = dane[dane[0] == 'deletion']
    duplikacje.to_csv("%s%s" % ('raw_dup_', title,), sep = ' ')
    delecje.to_csv("%s%s" % ('raw_del_', title,), sep = ' ')
    
    #print(duplikacje[duplikacje['dlug'] < 5000000])
    #cnvnator = cnvnator.drop(cnvnator[cnvnator.ciag_sesji == 0].index)    
    #dane = dane[dane['dlug'] > 50]
    #cnvnator = cnvnator[cnvnator['dlug'] < 5000000]

def czyszczenie_cnvnator_clean(nazwa,title):
    dane = pd.read_csv(nazwa, sep = '\s+', header = None)
    dane['Chr'], dane['dane1'] = dane[1].map(lambda row: row.split(':')[0]), dane[1].map(lambda row: row.split(':')[1])
    dane['dane2'], dane['dane1'] = dane['dane1'].map(lambda row: row.split('-')[1]), dane['dane1'].map(lambda row: row.split('-')[0])
    dane.rename(columns = {2 :'dlug'}, inplace = True)
    print(len(dane))
    dane = dane[dane['dlug'] > 50]
    dane = dane[dane['dlug'] < 5000000]
    print(len(dane))  
    dane = dane[dane['Chr'] != 'X']
    dane = dane[dane['Chr'] != 'Y']
    print(len(dane))
    

    dane = dane.drop(columns = [1, 3, 4, 5, 6, 7, 8])
    #print(dane.head())
    duplikacje = dane[dane[0] == 'duplication']
    delecje = dane[dane[0] == 'deletion']
    duplikacje.to_csv("%s%s" % ('clean_dup_', title,), sep = ' ')
    delecje.to_csv("%s%s" % ('clean_del_', title,), sep = ' ')
    
    #print(duplikacje[duplikacje['dlug'] < 5000000])
    #cnvnator = cnvnator.drop(cnvnator[cnvnator.ciag_sesji == 0].index)    
    #dane = dane[dane['dlug'] > 50]
    #cnvnator = cnvnator[cnvnator['dlug'] < 5000000]


for filename in os.scandir('/Users/daria/Downloads/dane/bin200'):
    nazwa = filename.path.split('_',1)[1]
    czyszczenie_cnvnator_raw(filename,nazwa)


for filename in os.scandir('/Users/daria/Downloads/dane/bin200'):
    nazwa = filename.path.split('_',1)[1]
    czyszczenie_cnvnator_clean(filename,nazwa)


lista = []
for filename in os.scandir('/Users/daria/Desktop/test'):
    lista.append(filename.path)
#print(lista)

lista.remove('/Users/daria/Desktop/test/.DS_Store')
lista.sort() 
#print(lista)
#print('--------------------------------------------------------')

# podzielic na 4 listy 
lista_clean_del = lista[1:13] # git
print(lista_clean_del)
print(len(lista_clean_del))

lista_clean_dup = lista[13:25] #git
print(lista_clean_dup)
print(len(lista_clean_dup))

lista_raw_del = lista[25:37] #git
print(lista_raw_del)
print(len(lista_raw_del))

lista_raw_dup = lista[37:len(lista)]
print(lista_raw_dup)
print(len(lista_raw_dup))



'''
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
'''