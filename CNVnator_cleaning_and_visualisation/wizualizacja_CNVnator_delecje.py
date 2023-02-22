#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 20 21:14:57 2022

@author: daria
"""
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

color = sns.color_palette("Greys", 2)
color =  "rocket"

# CNVnator delecje raw i clean

delecje_raw = pd.read_csv('/Users/daria/Desktop/test/lista_raw_del_razem.txt', sep =' ')
delecje_clean = pd.read_csv('/Users/daria/Desktop/test/lista_clean_del_razem.txt', sep =' ')

print(len(delecje_raw))
print(len(delecje_clean))


lista = []
for i in range (1,(max(delecje_raw['Chr']+1))):
    lista.append(len(delecje_raw[delecje_raw['Chr'] == i]))

lista2 = [i for i in range(1,19)]  
delecje_raw = pd.DataFrame(lista, columns = ['Liczba_CNV'])
dane2 = pd.DataFrame(lista2, columns = ['Chromosom'])


lista = []
for i in range (1,(max(delecje_clean['Chr']+1))):
    lista.append(len(delecje_clean[delecje_clean['Chr'] == i]))
    
delecje_clean = pd.DataFrame(lista, columns = ['Liczba_CNV'])


delecje_clean.to_csv('delecje_clean_CNVnator')
# Set up the matplotlib figure
f, (ax1) = plt.subplots(1, 1, figsize=(10,10))


# Center the data to make it diverging
sns.barplot(x=dane2['Chromosom'], y=delecje_clean['Liczba_CNV'], palette=color , ax = ax1)
ax1.grid()
ax1.set(xlabel=None)
ax1.set(ylabel=None)
#ax1.set(title='Penguins: Body Mass by Species for Gender')

#ax1.set(ylim=(0, 2500))

f.suptitle('Liczba delecji dla CNVnatora przed i po filtracji')
f.text(0.5, 0.04, 'Chromosom', ha='center')
f.text(0.04, 0.5, 'Liczba CNV', va='center', rotation='vertical')

f.savefig('Liczba_Delecji_CNVnator.png')

# -----------------------------------------------------------------------------

delecje_raw = pd.read_csv('/Users/daria/Desktop/Dane_licencjat/Testy_Statystyczne/CNVnator/del_raw_razem/del_raw_CNVnator_razem.txt', sep =' ')
delecje_clean = pd.read_csv('/Users/daria/Desktop/Dane_licencjat/Testy_Statystyczne/CNVnator/del_clean_razem/del_clean_CNVnator_razem.txt', sep =' ')




# Set up the matplotlib figure
f, (ax1, ax2) = plt.subplots(2, 1, figsize=(10,10))

# Generate some sequential data
sns.boxplot(y=delecje_raw["dlug"], x=delecje_raw["Chr"],palette=color  , ax = ax1)
ax1.set(xlabel=None)
ax1.set(ylabel=None)
#ax2.set(title='Penguins: Body Mass by Species for Gender')
#ax1.set(ylim=(0, 400000))
ax1.grid()

# Center the data to make it diverging
sns.boxplot(y=delecje_clean["dlug"], x=delecje_clean["Chr"],palette=color , ax = ax2)
ax2.grid()
ax2.set(xlabel=None)
ax2.set(ylabel=None)
#ax2.set(title='Penguins: Body Mass by Species for Gender')
#ax2.set(ylim=(0, 400000))

f.suptitle('Długość delecji dla CNVnatora przed i po filtracji')
f.text(0.5, 0.04, 'Chromosom', ha='center')
f.text(0.04, 0.5, 'Długość CNV', va='center', rotation='vertical')


f.savefig('Dlugosc_Delecji_CNVnator.png')

# -----------------------------------------------------------------------------

delecje_raw = pd.read_csv('/Users/daria/Desktop/Dane_licencjat/Testy_Statystyczne/CNVnator/del_raw_razem/del_raw_CNVnator_razem.txt', sep =' ')
delecje_clean = pd.read_csv('/Users/daria/Desktop/Dane_licencjat/Testy_Statystyczne/CNVnator/del_clean_razem/del_clean_CNVnator_razem.txt', sep =' ')




# Set up the matplotlib figure
f, (ax1) = plt.subplots(1, 1, figsize=(10,10))

# Generate some sequential data
sns.boxplot(y=delecje_raw["dlug"], x=delecje_raw["Chr"],palette= 'Blues'  , ax = ax1)
ax1.set(xlabel=None)
ax1.set(ylabel=None)
#ax2.set(title='Penguins: Body Mass by Species for Gender')
ax1.set(ylim=(0, 400000))
ax1.grid()



f.suptitle('Długość delecji dla CNVnatora przed i po filtracji')
f.text(0.5, 0.04, 'Chromosom', ha='center')
f.text(0.04, 0.5, 'Długość CNV', va='center', rotation='vertical')


f.savefig('Dlugosc_Delecji_CNVnator.png')