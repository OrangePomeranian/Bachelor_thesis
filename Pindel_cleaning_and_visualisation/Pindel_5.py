#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 23:15:35 2022

@author: daria
"""
import pandas as pd

lista_clean_del = pd.read_csv('/Users/daria/Desktop/test2/lista_clean_del_razem.txt', sep = ' ')
lista_clean_dup = pd.read_csv('/Users/daria/Desktop/test2/lista_clean_dup_razem.txt', sep = ' ')
lista_raw_del = pd.read_csv('/Users/daria/Desktop/test2/lista_raw_del_razem.txt', sep = ' ')
lista_raw_dup = pd.read_csv('/Users/daria/Desktop/test2/lista_raw_dup_razem.txt', sep = ' ')

clean_del = pd.read_csv('/Users/daria/Desktop/test2/clean_D_D_Nr5.D.txt', sep = ',')
clean_dup= pd.read_csv('/Users/daria/Desktop/test2/clean_TD_D_Nr5.TD.txt', sep = ',')
raw_del = pd.read_csv('/Users/daria/Desktop/test2/raw_D_D_Nr5.D.txt', sep = ',')
raw_dup = pd.read_csv('/Users/daria/Desktop/test2/raw_TD_D_Nr5.TD.txt', sep = ',')



clean_del['Unnamed: 0'] = 0 
clean_dup['Unnamed: 0'] = 0 
raw_del['Unnamed: 0'] = 0 
raw_dup['Unnamed: 0'] = 0 


lista_clean_del.columns = sorted(lista_clean_del.columns)
x = len(lista_clean_del)
lista_clean_dup.columns = sorted(lista_clean_dup.columns)
lista_raw_del.columns = sorted(lista_raw_del.columns)  
z = len(lista_raw_del)
lista_raw_dup.columns = sorted(lista_raw_dup.columns)  



clean_del.columns = sorted(clean_del.columns)
y = len(clean_del)
clean_dup.columns = sorted(clean_dup.columns)
raw_del.columns = sorted(raw_del.columns)
h = len(raw_del)
raw_dup.columns = sorted(raw_dup.columns)



# merging two csv files
dane = pd.concat([lista_clean_del, clean_del], axis = 0, ignore_index=True)

dane.to_csv('lista_clean_del_razem1.txt', index = False, sep = ' ')

print( x + y )
print(x,y)
print(len(dane))


dane = pd.concat([lista_clean_dup, clean_dup], axis = 0, ignore_index=True)

dane.to_csv('lista_clean_dup_razem1.txt', index = False, sep = ' ')

print( h + z )
print(len(dane))


dane = pd.concat([lista_raw_del, raw_del], axis = 0, ignore_index=True)

dane.to_csv('lista_raw_del_razem1.txt', index = False, sep = ' ')



dane = pd.concat([lista_raw_dup, raw_dup], axis = 0, ignore_index=True)

dane.to_csv('lista_raw_dup_razem1.txt', index = False, sep = ' ')    
