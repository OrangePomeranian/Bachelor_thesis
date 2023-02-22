# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

color = sns.color_palette("Greys", 2)
color =  "rocket"

# CNVnator duplikacje raw i clean

duplikacje_raw = pd.read_csv('/Users/daria/Desktop/test/lista_raw_dup_razem.txt' , sep =' ')
duplikacje_clean = pd.read_csv('/Users/daria/Desktop/test/lista_clean_dup_razem.txt', sep =' ')
print(len(duplikacje_raw))
print(len(duplikacje_clean))

'''
print(max(duplikacje_clean['dlug']))
print(max(duplikacje_raw['dlug']))
print(min(duplikacje_clean['dlug']))
print(min(duplikacje_raw['dlug']))

'''

lista = []
for i in range (1,(max(duplikacje_raw['Chr']+1))):
    lista.append(len(duplikacje_raw[duplikacje_raw['Chr'] == i]))

lista2 = [i for i in range(1,19)]  
duplikacje_raw = pd.DataFrame(lista, columns = ['Liczba_CNV'])
dane2 = pd.DataFrame(lista2, columns = ['Chromosom'])


lista = []
for i in range (1,(max(duplikacje_clean['Chr']+1))):
    lista.append(len(duplikacje_clean[duplikacje_clean['Chr'] == i]))
    
duplikacje_clean = pd.DataFrame(lista, columns = ['Liczba_CNV'])


duplikacje_clean.to_csv('duplikacje_clean_CNVnator')

# Set up the matplotlib figure
f, (ax1) = plt.subplots(1, 1, figsize=(10,10))

# Generate some sequential data
sns.barplot(x=dane2['Chromosom'], y=duplikacje_raw['Liczba_CNV'], palette=color , ax = ax1)
ax1.axhline(0, color="k", clip_on=False)
ax1.grid()
ax1.set(xlabel=None)
ax1.set(ylabel=None)
#ax2.set(title='Penguins: Body Mass by Species for Gender')
ax1.set(ylim=(0, 1400))


f.suptitle('Liczba duplikacji dla CNVnatora przed i po filtracji')
f.text(0.5, 0.04, 'Chromosom', ha='center')
f.text(0.04, 0.5, 'Liczba CNV', va='center', rotation='vertical')

f.savefig('Liczba_Duplikacji_CNVnator.png')

# -----------------------------------------------------------------------------
'''
duplikacje_raw = pd.read_csv('/Users/daria/Desktop/test/lista_raw_dup_razem.txt' , sep =' ')
duplikacje_clean = pd.read_csv('/Users/daria/Desktop/test/lista_clean_dup_razem.txt', sep =' ')
print(duplikacje_raw['Chr'].value_counts())
print(duplikacje_clean['Chr'].value_counts())

#sns.boxplot(y=delecje_raw["2"], x=delecje_raw["Chr"],palette="Blues" )
#plt.show()



# Set up the matplotlib figure
f, (ax1, ax2) = plt.subplots(2, 1, figsize=(10,10))

# Generate some sequential data
sns.boxplot(y=duplikacje_raw["dlug"], x=duplikacje_raw["Chr"],palette=color , ax = ax1)
ax1.set(xlabel=None)
ax1.set(ylabel=None)
#ax2.set(title='Penguins: Body Mass by Species for Gender')
#ax1.set(ylim=(0, 500000))
ax1.grid()

# Center the data to make it diverging
sns.boxplot(y=duplikacje_clean["dlug"], x=duplikacje_clean["Chr"],palette=color  , ax = ax2)
ax2.grid()
ax2.set(xlabel=None)
ax2.set(ylabel=None)
#ax2.set(title='Penguins: Body Mass by Species for Gender')
#ax2.set(ylim=(0, 500000))

f.suptitle('Długość duplikacji dla CNVnatora przed i po filtracji')
f.text(0.5, 0.04, 'Chromosom', ha='center')
f.text(0.04, 0.5, 'Długość CNV', va='center', rotation='vertical')

f.savefig('Dlugosc_Duplikacji_CNVnator.png')
'''
# -----------------------------------------------------------------------------

duplikacje_raw = pd.read_csv('/Users/daria/Desktop/test/lista_raw_dup_razem.txt' , sep =' ')
duplikacje_clean = pd.read_csv('/Users/daria/Desktop/test/lista_clean_dup_razem.txt', sep =' ')
print(duplikacje_raw['Chr'].value_counts())
print(duplikacje_clean['Chr'].value_counts())

#sns.boxplot(y=delecje_raw["2"], x=delecje_raw["Chr"],palette="Blues" )
#plt.show()



# Set up the matplotlib figure
f, (ax1) = plt.subplots(1, 1, figsize=(10,10))

# Generate some sequential data
sns.boxplot(y=duplikacje_raw["dlug"], x=duplikacje_raw["Chr"],palette='Blues' , ax = ax1)
ax1.set(xlabel=None)
ax1.set(ylabel=None)
#ax2.set(title='Penguins: Body Mass by Species for Gender')
ax1.set(ylim=(0, 500000))
ax1.grid()



f.suptitle('Długość duplikacji dla CNVnatora przed i po filtracji')
f.text(0.5, 0.04, 'Chromosom', ha='center')
f.text(0.04, 0.5, 'Długość CNV', va='center', rotation='vertical')

f.savefig('Dlugosc_Duplikacji_CNVnator.png')









'''

duplikacje_raw = pd.read_csv('/Users/daria/Desktop/test/lista_raw_dup_razem.txt' , sep =' ')
duplikacje_clean = pd.read_csv('/Users/daria/Desktop/test/lista_clean_dup_razem.txt', sep =' ')
print(len(duplikacje_raw))
print(len(duplikacje_clean))
'''
'''
print(max(duplikacje_clean['dlug']))
print(max(duplikacje_raw['dlug']))
print(min(duplikacje_clean['dlug']))
print(min(duplikacje_raw['dlug']))
'''
'''
lista = []
for i in range (1,(max(duplikacje_raw['Chr']+1))):
    lista.append(len(duplikacje_raw[duplikacje_raw['Chr'] == i]))

lista2 = [i for i in range(1,19)]  
duplikacje_raw = pd.DataFrame(lista, columns = ['Liczba_CNV'])
dane2 = pd.DataFrame(lista2, columns = ['Chromosom'])


lista = []
for i in range (1,(max(duplikacje_clean['Chr']+1))):
    lista.append(len(duplikacje_clean[duplikacje_clean['Chr'] == i]))
    
duplikacje_clean = pd.DataFrame(lista, columns = ['Liczba_CNV'])


duplikacje_clean.to_csv('duplikacje_clean_CNVnator')


# Set up the matplotlib figure
f, (ax1) = plt.subplots(1, 1, figsize=(10,10))

# Generate some sequential data
sns.boxplot(y=duplikacje_raw["dlug"], x=duplikacje_raw["Chr"],palette=color , ax = ax1)
ax1.set(xlabel=None)
ax1.set(ylabel=None)
#ax2.set(title='Penguins: Body Mass by Species for Gender')
#ax1.set(ylim=(0, 500000))
ax1.grid()



f.suptitle('Liczba duplikacji dla CNVnatora')
f.text(0.5, 0.04, 'Chromosom', ha='center')
f.text(0.04, 0.5, 'Długość CNV', va='center', rotation='vertical')

f.savefig('Dlugosc_Duplikacji_CNVnator.png')
'''