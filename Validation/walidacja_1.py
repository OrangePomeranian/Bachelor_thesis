#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 20:46:11 2022

@author: daria
"""
import os
import pandas as pd

#Pindel

       
lista = pd.DataFrame()
for filename in os.scandir('/Users/daria/Desktop/Dane_licencjat/Pindel'):
    path = pd.DataFrame({'path':[filename.path]})
    lista = pd.concat([lista,path])
    

lista = lista.reset_index().drop([2,14])

lista['dup/del']= lista['path'].map(lambda row: row.split('Pindel/')[1]) 
lista['Nr']= lista['dup/del'].map(lambda row: row.split('_')[1]) 
lista['dup/del']= lista['Nr'].map(lambda row: row.split('.')[1]) 
lista['Nr']= lista['Nr'].map(lambda row: row.split('.')[0]) 


stare_delecje, stare_duplikacje = pd.DataFrame(), pd.DataFrame()
for i in range(0, len(lista)):
    Nr = lista['Nr'].iloc[i]
    if lista['dup/del'].iloc[i] == 'D':
        stare_delecje = pd.concat([stare_delecje, pd.DataFrame({'Pindel' : lista['path'].iloc[i], 'Nr' : Nr}, index = [0])])
    else:
        stare_duplikacje = pd.concat([stare_duplikacje, pd.DataFrame({'Pindel' : lista['path'].iloc[i], 'Nr' : Nr}, index = [0])])

#CNVnator

lista = pd.DataFrame()
for filename in os.scandir('/Users/daria/Desktop/Dane_licencjat/CNVnator'):
    path = pd.DataFrame({'path':[filename.path]})
    lista = pd.concat([lista,path])
    
lista = lista.reset_index().drop([0,22])
lista['dup/del']= lista['path'].map(lambda row: row.split('CNVnator/')[1]) 
lista['Nr'] = lista['dup/del'].map(lambda row: row.split('S4389')[1])
lista['Nr'] = lista['Nr'].map(lambda row: row.split('.')[0])
lista['dup/del'] = lista['dup/del'].map(lambda row: row.split('_')[0])


lista_duplikacje = lista.drop(lista[lista['dup/del'] == 'del'].index).reset_index()
lista_delecje = lista.drop(lista[lista['dup/del'] == 'dup'].index).reset_index()

lista_delecje, lista_duplikacje = lista_delecje.drop(columns = ['level_0','index']), lista_duplikacje.drop(columns = ['level_0','index'])


# Plik ostateczny

delecje = pd.merge(lista_delecje, stare_delecje, how = 'outer', on = 'Nr')
delecje.to_csv('delecje.txt', sep = ' ')

duplikacje = pd.merge(lista_duplikacje, stare_duplikacje, how = 'outer', on = 'Nr')
duplikacje.to_csv('duplikacje.txt', sep = ' ')
