#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 19 21:11:54 2022

@author: daria
"""


import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

color = sns.color_palette("Greys", 2)
color =  "rocket"

# Pindel duplikacje raw i clean

duplikacje_raw = pd.read_csv('/Users/daria/Desktop/test2/lista_raw_dup_razem.txt', sep =' ')
duplikacje_clean = pd.read_csv('/Users/daria/Desktop/test2/lista_clean_dup_razem.txt', sep =' ')
delecje_raw = duplikacje_raw
delecje_clean = duplikacje_clean

print(len(delecje_raw))
print(len(delecje_clean))

duplikacje_clean_1 = []

duplikacje_clean_1 = duplikacje_clean_1.append(len(delecje_clean))
'''


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



delecje_clean.to_csv('duplikacje_clean_Pindel')
'''
'''
# Set up the matplotlib figure
f, (ax1, ax2) = plt.subplots(2, 1, figsize=(10,10))

# Generate some sequential data
sns.barplot(x=dane2['Chromosom'], y=delecje_raw['Liczba_CNV'], palette=color, ax = ax1)
ax1.grid()
ax1.set(xlabel=None)
ax1.set(ylabel=None)
#ax1.set(title='Penguins: Body Mass by Species for Gender')
ax1.set(ylim=(0, 65000))

# Center the data to make it diverging
sns.barplot(x=dane2['Chromosom'], y=delecje_clean['Liczba_CNV'], palette=color, ax = ax2)
ax2.grid()
ax2.set(xlabel=None)
ax2.set(ylabel=None)
#ax2.set(title='Penguins: Body Mass by Species for Gender')
ax2.set(ylim=(0, 65000))


f.suptitle('Liczba duplikacji dla Pindla przed i po filtracji')
f.text(0.5, 0.04, 'Chromosom', ha='center')
f.text(0.04, 0.5, 'Liczba CNV', va='center', rotation='vertical')

f.savefig('Liczba_Duplikacji_Pindel.png')
'''
# -----------------------------------------------------------------------------
'''
duplikacje_raw = pd.read_csv('/Users/daria/Desktop/test2/lista_raw_dup_razem.txt', sep =' ')
duplikacje_clean = pd.read_csv('/Users/daria/Desktop/test2/lista_clean_dup_razem.txt', sep =' ')
delecje_raw = duplikacje_raw
delecje_clean = duplikacje_clean

# Set up the matplotlib figure
f, (ax1, ax2) = plt.subplots(2, 1, figsize=(10,10))

# Generate some sequential data
sns.boxplot(y=delecje_raw["dlug"], x=delecje_raw["Chr"],palette=color , ax = ax1)
ax1.set(xlabel=None)
ax1.set(ylabel=None)
#ax2.set(title='Penguins: Body Mass by Species for Gender')
ax1.set(ylim=(0, 10000000))
ax1.grid()

# Center the data to make it diverging
sns.boxplot(y=delecje_clean["dlug"], x=delecje_clean["Chr"],palette=color , ax = ax2)
ax2.grid()
ax2.set(xlabel=None)
ax2.set(ylabel=None)
#ax2.set(title='Penguins: Body Mass by Species for Gender')
ax2.set(ylim=(0, 10000000))

f.suptitle('Długość duplikacji dla Pindla przed i po filtracji')
f.text(0.5, 0.04, 'Chromosom', ha='center')
f.text(0.04, 0.5, 'Długość CNV', va='center', rotation='vertical')


f.savefig('Dlugosc_Duplikacji_Pindel_2.png')
'''

'''
duplikacje_raw = pd.read_csv('/Users/daria/Desktop/test2/lista_raw_dup_razem.txt', sep =' ')
duplikacje_clean = pd.read_csv('/Users/daria/Desktop/test2/lista_clean_dup_razem.txt', sep =' ')
delecje_raw = duplikacje_raw
delecje_clean = duplikacje_clean

# Set up the matplotlib figure
f, (ax1, ax2) = plt.subplots(2, 1, figsize=(10,10))

# Generate some sequential data
sns.boxplot(y=delecje_raw["dlug"], x=delecje_raw["Chr"],palette='Blues' , ax = ax1)
ax1.set(xlabel=None)
ax1.set(ylabel=None)
#ax2.set(title='Penguins: Body Mass by Species for Gender')
ax1.set(ylim=(0, 10000000))
ax1.grid()

# Center the data to make it diverging
sns.boxplot(y=delecje_clean["dlug"], x=delecje_clean["Chr"],palette='Blues' , ax = ax2)
ax2.grid()
ax2.set(xlabel=None)
ax2.set(ylabel=None)
#ax2.set(title='Penguins: Body Mass by Species for Gender')
ax2.set(ylim=(0, 10000000))

ax3 = plt.axes([0.4, 0.35, .5, .1])
sns.boxplot(y=delecje_clean["dlug"], x=delecje_clean["Chr"],palette= 'Blues' , ax = ax3)
#ax3.set_title('zoom')
ax3.set(xlabel=None)
ax3.set(ylabel=None)
ax3.set(ylim=(50, 600000))
ax3.grid()


f.suptitle('Długość duplikacji dla Pindla przed i po filtracji')
f.text(0.5, 0.04, 'Chromosom', ha='center')
f.text(0.04, 0.5, 'Długość CNV', va='center', rotation='vertical')


f.savefig('Dlugosc_Duplikacji_Pindel_2.png')




# -----------------------------------------------------------------------------

duplikacje_raw = pd.read_csv('/Users/daria/Desktop/test2/lista_raw_dup_razem.txt', sep =' ')
duplikacje_clean = pd.read_csv('/Users/daria/Desktop/test2/lista_clean_dup_razem.txt', sep =' ')
delecje_raw = duplikacje_raw
delecje_clean = duplikacje_clean

# Set up the matplotlib figure
f, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10,10))

# Generate some sequential data
sns.boxplot(y=delecje_raw["dlug"], x=delecje_raw["Chr"],palette=color , ax = ax1)
ax1.set(xlabel=None)
ax1.set(ylabel=None)
#ax2.set(title='Penguins: Body Mass by Species for Gender')
ax1.set(ylim=(0, 10000000))
ax1.grid()

# Center the data to make it diverging
sns.boxplot(y=delecje_clean["dlug"], x=delecje_clean["Chr"],palette=color , ax = ax2)
ax2.grid()
ax2.set(xlabel=None)
ax2.set(ylabel=None)
#ax2.set(title='Penguins: Body Mass by Species for Gender')
ax2.set(ylim=(0, 10000000))

sns.boxplot(y=delecje_clean["dlug"], x=delecje_clean["Chr"],palette=color , ax = ax3)
ax3.grid()
ax3.set(xlabel=None)
ax3.set(ylabel=None)
#ax2.set(title='Penguins: Body Mass by Species for Gender')
ax3.set(ylim=(0, 5000000))

f.suptitle('Długość duplikacji dla Pindla przed i po filtracji')
f.text(0.5, 0.04, 'Chromosom', ha='center')
f.text(0.04, 0.5, 'Długość CNV', va='center', rotation='vertical')


f.savefig('Dlugosc_Duplikacji_Pindel_3.png')
'''

#________________



delecje_raw = pd.read_csv('/Users/daria/Desktop/test2/lista_raw_dup_razem.txt', sep =' ')
delecje_clean = pd.read_csv('/Users/daria/Desktop/test2/lista_clean_dup_razem.txt', sep =' ')
delecje_raw = delecje_raw.drop(columns = ['Unnamed: 0']) 
delecje_clean = delecje_clean.drop(columns = ['Unnamed: 0']) 
print(len(delecje_raw))
print(len(delecje_clean))


#przeszlo
lista = []
for i in range (1,19):
    lista.append(len(delecje_raw[delecje_raw['Chr'] == i]))

print('tutaj')
lista2 = [i for i in range(1,19)]  
delecje_raw = pd.DataFrame(lista, columns = ['Liczba_CNV'])
dane2 = pd.DataFrame(lista2, columns = ['Chromosom'])

print('tutaj')
lista = []
for i in range (1,19):
    lista.append(len(delecje_clean[delecje_clean['Chr'] == i]))
    
delecje_clean = pd.DataFrame(lista, columns = ['Liczba_CNV'])


delecje_clean.to_csv('delecje_clean_Pindel')


print('tutaj3')
# Set up the matplotlib figure
f, (ax1, ax2) = plt.subplots(2, 1, figsize=(10,10))

# Generate some sequential data
sns.barplot(x=dane2['Chromosom'], y=delecje_raw['Liczba_CNV'], palette=color, ax = ax1)
ax1.grid()
ax1.set(xlabel=None)
ax1.set(ylabel=None)
#ax1.set(title='Penguins: Body Mass by Species for Gender')
ax1.set(ylim=(0, 2600000))

# Center the data to make it diverging
sns.barplot(x=dane2['Chromosom'], y=delecje_clean['Liczba_CNV'], palette=color, ax = ax2)
ax2.grid()
ax2.set(xlabel=None)
ax2.set(ylabel=None)
#ax2.set(title='Penguins: Body Mass by Species for Gender')
ax2.set(ylim=(0, 2600000))

ax3 = plt.axes([0.4, 0.35, .5, .1])
sns.barplot(x=dane2['Chromosom'], y=delecje_clean['Liczba_CNV'], palette=color, ax = ax3)
ax3.grid()
ax3.set(xlabel=None)
ax3.set(ylabel=None)
#ax3.set(title='Po czyszczeniu')
ax3.set(ylim=(0, 250000))

f.suptitle('Liczba duplikacji dla Pindla przed i po filtracji')
f.text(0.5, 0.04, 'Chromosom', ha='center')
f.text(0.04, 0.5, 'Liczba CNV', va='center', rotation='vertical')

f.savefig('Liczba_Duplikacji_Pindel.png')

#end = time.time()
#print(end - start)