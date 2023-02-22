#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 21 22:14:48 2022

@author: daria

"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
'''
# Porownanie delecji

delecje_clean_CNVnator = pd.read_csv('/Users/daria/Desktop/test3/delecje_clean_CNVnator', sep =',')
delecje_clean_Pindel = pd.read_csv('/Users/daria/Desktop/test3/delecje_clean_Pindel', sep =',')
duplikacje_clean_CNVnator = pd.read_csv('/Users/daria/Desktop/test3/duplikacje_clean_CNVnator', sep =',')
duplikacje_clean_Pindel = pd.read_csv('/Users/daria/Desktop/test3/duplikacje_clean_Pindel', sep =',')

delecje_clean_CNVnator['Program'] = 'CNVnator'
delecje_clean_Pindel['Program'] = 'Pindel'
duplikacje_clean_CNVnator['Program']= 'CNVnator'
duplikacje_clean_Pindel['Program'] = 'Pindel'

lista2 = [i for i in range(1,19)] 
lista = pd.DataFrame(lista2) 


delecje_clean_CNVnator = pd.concat([delecje_clean_CNVnator, lista], axis = 1)
delecje_clean_Pindel = pd.concat([delecje_clean_Pindel, lista], axis = 1)
duplikacje_clean_CNVnator = pd.concat([duplikacje_clean_CNVnator, lista], axis = 1)
duplikacje_clean_Pindel = pd.concat([duplikacje_clean_Pindel, lista], axis = 1)

delecje = pd.concat([delecje_clean_CNVnator,delecje_clean_Pindel]).reset_index()
duplikacje = pd.concat([duplikacje_clean_CNVnator, duplikacje_clean_Pindel]).reset_index()
#delecje = delecje.set_index(0)


f, (ax1, ax2) = plt.subplots(2, 1, figsize=(15,10))
sns.histplot(x = 0, data=delecje, bins=18, hue="Program", ax = ax1)
ax1.grid()
ax1.set(xlabel=None)
ax1.set(ylabel=None)
#ax2.set(title='Penguins: Body Mass by Species for Gender')
ax1.set(ylim=(0, 250000))
ax1.set(xlim=(1, 18))

sns.histplot(x= 0, data=duplikacje, bins=18, hue="Program", ax = ax2)
ax2.grid()
ax2.set(xlabel=None)
ax2.set(ylabel=None)
#ax2.set(title='Penguins: Body Mass by Species for Gender')
#ax2.set(ylim=(0, 42000))
ax2.set(xlim=(1, 18))

#f.set_xticklabels(f.get_xticklabels(), rotation=45)


delecje_clean_CNVnator['Program'] = 'CNVnator'
delecje_clean_Pindel['Program'] = 'Pindel'
duplikacje_clean_CNVnator['Program']= 'CNVnator'
duplikacje_clean_Pindel['Program'] = 'Pindel'



lista2 = [i for i in range(1,19)] 
lista = pd.DataFrame(lista2) 

#delecje_clean_CNVnator = pd.concat([delecje_clean_CNVnator, lista], axis = 1)
#delecje_clean_Pindel = pd.concat([delecje_clean_Pindel, lista], axis = 1)
#duplikacje_clean_CNVnator = pd.concat([duplikacje_clean_CNVnator, lista], axis = 1)
#duplikacje_clean_Pindel = pd.concat([duplikacje_clean_Pindel, lista], axis = 1)

delecje = pd.concat([delecje_clean_CNVnator,delecje_clean_Pindel])
duplikacje = pd.concat([duplikacje_clean_CNVnator, duplikacje_clean_Pindel])

print(delecje.columns)
delecje = delecje.reset_index()
duplikacje = duplikacje.reset_index()
#plt.figure(figsize=(9,6))


f, (ax1, ax2) = plt.subplots(2, 1, figsize=(15,10))
sns.histplot(x= 'Chr',y = 'dlug', data=delecje, bins=18, hue="Program", palette= 'rocket', ax = ax1)
ax1.grid()
ax1.set(xlabel=None)
ax1.set(ylabel=None)
#ax2.set(title='Penguins: Body Mass by Species for Gender')
ax1.set(ylim=(0, 250000))
ax1.set(xlim=(1, 18))

sns.histplot(x= 'Chr', data=duplikacje, bins=18, hue="Program", palette= 'rocket', ax = ax2)
ax2.grid()
ax2.set(xlabel=None)
ax2.set(ylabel=None)
#ax2.set(title='Penguins: Body Mass by Species for Gender')
ax2.set(ylim=(0, 42000))
ax2.set(xlim=(1, 18))

f.set_xticklabels(f.get_xticklabels(), rotation=45)



delecje_clean_CNVnator = pd.read_csv('/Users/daria/Desktop/test/lista_clean_del_razem.txt', sep =' ')
delecje_clean_Pindel = pd.read_csv('/Users/daria/Desktop/test2/lista_clean_del_razem.txt', sep =' ')
duplikacje_clean_CNVnator = pd.read_csv('//Users/daria/Desktop/test/lista_clean_dup_razem.txt', sep =' ')
duplikacje_clean_Pindel = pd.read_csv('/Users/daria/Desktop/test2/lista_clean_dup_razem.txt', sep =' ')

delecje_clean_CNVnator = delecje_clean_CNVnator[['dlug']]
delecje_clean_Pindel = delecje_clean_Pindel[['dlug']]
duplikacje_clean_CNVnator = duplikacje_clean_CNVnator[['dlug']]
duplikacje_clean_Pindel = duplikacje_clean_Pindel[['dlug']]

delecje = pd.concat([delecje_clean_CNVnator, delecje_clean_Pindel], axis = 1)


fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)

colors = ['red', 'tan']
ax1.hist(x = delecje, bins = 18, density=True, histtype='bar', color=colors, label = colors)
ax1.legend(prop={'size': 10})
ax1.set_title('bars with legend')

ax1.hist(x = delecje, bins = 18, density=True, histtype='bar', stacked=True)
ax1.set_title('stacked bar')

ax2.hist(x, n_bins, histtype='step', stacked=True, fill=False)
ax2.set_title('stack step (unfilled)')

# Make a multiple-histogram of data-sets with different length.
x_multi = [np.random.randn(n) for n in [10000, 5000, 2000]]
ax3.hist(x_multi, n_bins, histtype='bar')
ax3.set_title('different sample sizes')


fig.tight_layout()
plt.show()
'''


# ------------------------------------------------------------------------------------------------------------

delecje_clean_CNVnator = pd.read_csv('/Users/daria/Desktop/test/lista_clean_del_razem.txt', sep =' ')
delecje_clean_Pindel = pd.read_csv('/Users/daria/Desktop/test2/lista_clean_del_razem.txt', sep =' ')
duplikacje_clean_CNVnator = pd.read_csv('//Users/daria/Desktop/test/lista_clean_dup_razem.txt', sep =' ')
duplikacje_clean_Pindel = pd.read_csv('/Users/daria/Desktop/test2/lista_clean_dup_razem.txt', sep =' ')

delecje_clean_CNVnator['Program'] = 'CNVnator'
delecje_clean_Pindel['Program'] = 'Pindel'
duplikacje_clean_CNVnator['Program']= 'CNVnator'
duplikacje_clean_Pindel['Program'] = 'Pindel'



lista2 = [i for i in range(1,19)] 
lista = pd.DataFrame(lista2) 

#delecje_clean_CNVnator = pd.concat([delecje_clean_CNVnator, lista], axis = 1)
#delecje_clean_Pindel = pd.concat([delecje_clean_Pindel, lista], axis = 1)
#duplikacje_clean_CNVnator = pd.concat([duplikacje_clean_CNVnator, lista], axis = 1)
#duplikacje_clean_Pindel = pd.concat([duplikacje_clean_Pindel, lista], axis = 1)

delecje = pd.concat([delecje_clean_CNVnator,delecje_clean_Pindel])
duplikacje = pd.concat([duplikacje_clean_CNVnator, duplikacje_clean_Pindel])

print(delecje.columns)
delecje = delecje.reset_index()
duplikacje = duplikacje.reset_index()
#plt.figure(figsize=(9,6))


f, (ax1, ax2) = plt.subplots(2, 1, figsize=(10,10))
sns.histplot(x= 'Chr', data=delecje, bins=18, hue="Program", palette= 'rocket', ax = ax1)
ax1.grid()
ax1.set(xlabel=None)
ax1.set(ylabel=None)
#ax2.set(title='Penguins: Body Mass by Species for Gender')
ax1.set(ylim=(0, 230000))
ax1.set(xlim=(1, 18))
ax1.set(xticks=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])


sns.histplot(x= 'Chr', data=duplikacje, bins=18, hue="Program", palette= 'rocket', ax = ax2)
ax2.grid()
ax2.set(xlabel=None)
ax2.set(ylabel=None)
#ax2.set(title='Penguins: Body Mass by Species for Gender')
ax2.set(ylim=(0, 42000))
ax2.set(xlim=(1, 18))
ax2.set(xticks=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])


f.suptitle('Porównanie wykrytych CNV dla delecji i duplikacji')
f.text(0.5, 0.04, 'Chromosom', ha='center')
f.text(0.04, 0.5, 'Liczba CNV', va='center', rotation='vertical')

f.savefig('Liczba_Duplikacji_Delecji_razem.png')