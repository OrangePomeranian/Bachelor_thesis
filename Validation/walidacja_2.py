#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 23 23:50:03 2022

@author: daria
"""

# Walidacja dla delecji
import pandas as pd
import os
import numpy as np
import time

start = time.time()

delecje = pd.read_csv('/Users/daria/Desktop/Dane_licencjat/Walidacja_1/delecje.txt', sep =' ')
duplikacje = pd.read_csv('/Users/daria/Desktop/Dane_licencjat/Walidacja_1/duplikacje.txt', sep = ' ')
delecje, duplikacje = delecje[['path','Nr','Pindel']], duplikacje[['path','Nr','Pindel']]



#kolumny_pindel = ['chr', 'pocz', 'kon','dlug']

#delecje.drop([4], axis = 0, inplace = True)
#duplikacje.drop([10], axis = 0, inplace = True)


output = pd.DataFrame()
brudnopis = pd.DataFrame()


#len(delecje)
for numer_osobnika in range(4, 5):
    print(numer_osobnika)
    output = pd.DataFrame()
    #output_kon = pd.DataFrame()
    CNVnator_input = pd.read_csv(delecje['path'].iloc[numer_osobnika], sep = ' ')
    CNVnator_input = CNVnator_input.drop(columns=['Unnamed: 0','0'])
    Pindel_input = pd.read_csv(delecje['Pindel'].iloc[numer_osobnika], sep = ',')
    #Pindel_input = Pindel_input.drop(columns=['dlug'])
    Pindel_input.rename(columns = {'dane1' :'pocz', 'dane2':'kon'}, inplace = True)
    CNVnator_input.rename(columns = {'dane1' :'pocz', 'dane2':'kon'}, inplace = True)
    Pindel_grouped = Pindel_input.groupby(by = 'Chr')
    CNVnator_grouped = CNVnator_input.groupby(by = 'Chr')
    for chromosom in range(1, 19):
        print(chromosom)
        Pindel_walidacja = Pindel_grouped.get_group(chromosom)
        CNVnator_walidacja = CNVnator_grouped.get_group(chromosom)        
        
        for numer_indeksu_CNVnator in range (0, len(CNVnator_walidacja)): #len(CNVnator_walidacja)
            CNVnator_pocz = CNVnator_walidacja['pocz'].iloc[numer_indeksu_CNVnator].astype(np.int32)
            CNVnator_kon = CNVnator_walidacja['kon'].iloc[numer_indeksu_CNVnator].astype(np.int32)
            CNVnator_dlug = CNVnator_walidacja['dlug'].iloc[numer_indeksu_CNVnator].astype(np.int32)
            #print(CNVnator_pocz, CNVnator_kon)
            #print(numer_indeksu_CNVnator)
            #print(CNVnator_dlug)
            
            for numer_indeksu_Pindel in range (0, len(Pindel_walidacja)): #len(Pindel_walidacja)
                Pindel_pocz = Pindel_walidacja['pocz'].iloc[numer_indeksu_Pindel].astype(np.int32)
                Pindel_kon = Pindel_walidacja['kon'].iloc[numer_indeksu_Pindel].astype(np.int32)  
                Pindel_dlug = Pindel_walidacja['dlug'].iloc[numer_indeksu_Pindel].astype(np.int32)     
                #print(Pindel_pocz, Pindel_kon, Pindel_dlug)
        
                if (CNVnator_kon > Pindel_kon) and (Pindel_pocz > CNVnator_pocz) and (Pindel_dlug / CNVnator_dlug > 0.7):
                    #print('a1')
                    brudnopis = pd.DataFrame({'Chr':[chromosom], 'pocz_CNV':[CNVnator_pocz], 'kon_CNV':[CNVnator_kon], 'pocz_Pin':[Pindel_pocz], 'kon_Pin':[Pindel_kon]})
                    output = pd.concat([output, brudnopis])
                    
                    
                    #typ_1 = pd.concat([typ_1, brudnopis])
                    #output = pd.concat([output, typ_1])
                    
                    
                    #print(brudnopis)
                  
                elif (CNVnator_kon < Pindel_kon) and (Pindel_pocz < CNVnator_pocz):
                    #print('a2')
                    brudnopis = pd.DataFrame({'Chr':[chromosom], 'pocz_CNV':[CNVnator_pocz], 'kon_CNV':[CNVnator_kon], 'pocz_Pin':[Pindel_pocz], 'kon_Pin':[Pindel_kon]})
                    output = pd.concat([output, brudnopis])
                    #print(brudnopis)
                    
                elif (CNVnator_kon > Pindel_pocz) and (CNVnator_kon < Pindel_kon) and (CNVnator_pocz < Pindel_pocz) and ((CNVnator_kon - Pindel_pocz) / CNVnator_dlug > 0.7):
                    #print('a3')
                    brudnopis = pd.DataFrame({'Chr':[chromosom], 'pocz_CNV':[CNVnator_pocz], 'kon_CNV':[CNVnator_kon], 'pocz_Pin':[Pindel_pocz], 'kon_Pin':[Pindel_kon]})
                    output = pd.concat([output, brudnopis])
                    #print(brudnopis)
                    
                elif (Pindel_kon > CNVnator_pocz) and (Pindel_kon < CNVnator_kon) and (Pindel_pocz < CNVnator_pocz) and ((CNVnator_pocz - Pindel_kon) / CNVnator_dlug > 0.7):
                    print('a4')
                    brudnopis = pd.DataFrame({'Chr':[chromosom], 'pocz_CNV':[CNVnator_pocz], 'kon_CNV':[CNVnator_kon], 'pocz_Pin':[Pindel_pocz], 'kon_Pin':[Pindel_kon]})
                    output = pd.concat([output, brudnopis])
                    #print(brudnopis)
        #output.to_csv("%s%s" % ('Brudny_output_delecje_', delecje['Nr'].iloc[numer_osobnika] ))# poprawic bedzie bral po indexie), sep = ' ')            

        
           
    output.to_csv("%s%s" % ('Brudny_output_delecje_', delecje['Nr'].iloc[numer_osobnika] ))# poprawic bedzie bral po indexie), sep = ' ')
    
                      


end = time.time()
print(end - start)


# ------------------------------------------------------------------------------------------------------

print('dziala')
# len(duplikacje)
for numer_osobnika in range(10, 11):
    print(numer_osobnika)
    print(duplikacje['Nr'].iloc[numer_osobnika] )
    #typ_1 = pd.DataFrame()
    #typ_2 = pd.DataFrame()
    #typ_3 = pd.DataFrame()
    #typ_4 = pd.DataFrame()
    output = pd.DataFrame()
    #output_kon = pd.DataFrame()
    CNVnator_input = pd.read_csv(duplikacje['path'].iloc[numer_osobnika], sep = ' ')
    CNVnator_input = CNVnator_input.drop(columns=['Unnamed: 0','0'])
    Pindel_input = pd.read_csv(duplikacje['Pindel'].iloc[numer_osobnika], sep = ',')
    #Pindel_input = Pindel_input.drop(columns=['dlug'])
    Pindel_input.rename(columns = {'dane1' :'pocz', 'dane2':'kon'}, inplace = True)
    CNVnator_input.rename(columns = {'dane1' :'pocz', 'dane2':'kon'}, inplace = True)
    Pindel_grouped = Pindel_input.groupby(by = 'Chr')
    CNVnator_grouped = CNVnator_input.groupby(by = 'Chr')
    for chromosom in range(1, 19):
        print(chromosom)
        Pindel_walidacja = Pindel_grouped.get_group(chromosom)
        CNVnator_walidacja = CNVnator_grouped.get_group(chromosom)        
        
        for numer_indeksu_CNVnator in range (0, len(CNVnator_walidacja)): #len(CNVnator_walidacja)
            CNVnator_pocz = CNVnator_walidacja['pocz'].iloc[numer_indeksu_CNVnator].astype(np.int32)
            CNVnator_kon = CNVnator_walidacja['kon'].iloc[numer_indeksu_CNVnator].astype(np.int32)
            CNVnator_dlug = CNVnator_walidacja['dlug'].iloc[numer_indeksu_CNVnator].astype(np.int32)
            #print(CNVnator_pocz, CNVnator_kon)
            #print(numer_indeksu_CNVnator)
            #print(CNVnator_dlug)
            
            for numer_indeksu_Pindel in range (0, len(Pindel_walidacja)): #len(Pindel_walidacja)
                Pindel_pocz = Pindel_walidacja['pocz'].iloc[numer_indeksu_Pindel].astype(np.int32)
                Pindel_kon = Pindel_walidacja['kon'].iloc[numer_indeksu_Pindel].astype(np.int32)  
                Pindel_dlug = Pindel_walidacja['dlug'].iloc[numer_indeksu_Pindel].astype(np.int32)     
                #print(Pindel_pocz, Pindel_kon, Pindel_dlug)
        
                if (CNVnator_kon > Pindel_kon) and (Pindel_pocz > CNVnator_pocz) and (Pindel_dlug / CNVnator_dlug > 0.7):
                    #print('a1')
                    brudnopis = pd.DataFrame({'Chr':[chromosom], 'pocz_CNV':[CNVnator_pocz], 'kon_CNV':[CNVnator_kon], 'pocz_Pin':[Pindel_pocz], 'kon_Pin':[Pindel_kon]})
                    output = pd.concat([output, brudnopis])
                    '''typ_1 = pd.concat([typ_1, brudnopis])
                    output = pd.concat([output, typ_1])
                    '''
                    #print(brudnopis)
                  
                elif (CNVnator_kon < Pindel_kon) and (Pindel_pocz < CNVnator_pocz):
                    #print('a2')
                    brudnopis = pd.DataFrame({'Chr':[chromosom], 'pocz_CNV':[CNVnator_pocz], 'kon_CNV':[CNVnator_kon], 'pocz_Pin':[Pindel_pocz], 'kon_Pin':[Pindel_kon]})
                    output = pd.concat([output, brudnopis])
                    #print(brudnopis)
                    
                elif (CNVnator_kon > Pindel_pocz) and (CNVnator_kon < Pindel_kon) and (CNVnator_pocz < Pindel_pocz) and ((CNVnator_kon - Pindel_pocz) / CNVnator_dlug > 0.7):
                    #print('a3')
                    brudnopis = pd.DataFrame({'Chr':[chromosom], 'pocz_CNV':[CNVnator_pocz], 'kon_CNV':[CNVnator_kon], 'pocz_Pin':[Pindel_pocz], 'kon_Pin':[Pindel_kon]})
                    output = pd.concat([output, brudnopis])
                    #print(brudnopis)
                    
                elif (Pindel_kon > CNVnator_pocz) and (Pindel_kon < CNVnator_kon) and (Pindel_pocz < CNVnator_pocz) and ((CNVnator_pocz - Pindel_kon) / CNVnator_dlug > 0.7):
                    print('a4')
                    brudnopis = pd.DataFrame({'Chr':[chromosom], 'pocz_CNV':[CNVnator_pocz], 'kon_CNV':[CNVnator_kon], 'pocz_Pin':[Pindel_pocz], 'kon_Pin':[Pindel_kon]})
                    output = pd.concat([output, brudnopis])
                    #print(brudnopis)     
        '''
        output = pd.concat([output, typ_1])
        output = pd.concat([output, typ_2])
        output = pd.concat([output, typ_3])
        output = pd.concat([output, typ_4])
        '''
        
           
    output.to_csv("%s%s" % ('Brudny_output_duplikacje_', duplikacje['Nr'].iloc[numer_osobnika] ))# poprawic bedzie bral po indexie), sep = ' ')
    
                      
end = time.time()
print(end - start)
