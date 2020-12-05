# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 22:27:51 2020

@author: stefa
"""



import csv

#ADJECTIFS

def data_preparation(csv): 
    type_adj = []
    kanji = []
    kana = []
    trad = []
    
    for l in csv[1:]:
        l.strip()
        ligne = l.split(',') 
        if 'null' not in ligne:
            type_adj.append(ligne[0])
            kanji.append(ligne[1])
            kana.append(ligne[2])
            trad.append(ligne[3][:-1])
            
    
    return type_adj, kanji, kana, trad 
        
fi = open("Japan_English_Adjectifs_Dict.csv",'r', encoding="utf32")
csv_liste = fi.readlines()
fi.close()

type_adj, kanji, kana, trad = data_preparation(csv_liste)


len_kanji = []

for kan in kanji:
    len_kanji.append(len(kan))
    
len_kanji, kanji, type_adj, kana, trad = zip(*sorted(zip(len_kanji, kanji, type_adj, kana, trad)))

kanji = kanji[::-1]
type_adj = type_adj[::-1]
kana = kana[::-1]
trad = trad[::-1]


rows = []

for i in range(len(type_adj)):  #Parcours tous les adjectifs de la liste tiré de JMDict
    type_adjectif = type_adj[i]
    adjectif_kanji = kanji[i]
    adjectif_kana = kana[i]
    adjectif_trad = trad[i]
    all_conj_adjectif = ['affirmatif neutre', 'affirmatif passé neutre', 'négatif neutre', 'négatif passé neutre', 'négatif neutre', 'négatif passé neutre', 'fonction épithète', 'sans le i de fin', 'adverbe', 'ba affirmatif', 'ba négatif', 'tara']
    if type_adjectif == 'na':
        for conj in all_conj_adjectif:
            row = [type_adjectif]
            if adjectif_kanji != '':
                adjectif_simple = adjectif_kanji
                if conj == 'affirmatif neutre':
                    #affirmatif neutre
                    new_adjectif = adjectif_simple
                    row.append(new_adjectif)
                elif conj == 'affirmatif passé neutre':
                    #affirmatif passé neutre
                    new_adjectif = adjectif_simple + 'だった'
                    row.append(new_adjectif)
                elif conj == 'négatif neutre':
                    #négatif neutre 1
                    new_adjectif = adjectif_simple + 'じゃない'
                    row.append(new_adjectif)
                elif conj == 'négatif passé neutre':
                    #négatif passé neutre 1
                    new_adjectif = adjectif_simple + 'じゃなかった'
                    row.append(new_adjectif)
                elif conj == 'négatif neutre':
                    #négatif neutre 2
                    new_adjectif = adjectif_simple + 'ではない'
                    row.append(new_adjectif)
                elif conj == 'négatif passé neutre':
                    #négatif passé neutre 2
                    new_adjectif = adjectif_simple + 'ではなかった'
                    row.append(new_adjectif)
                elif conj == 'fonction épithète':
                    #fonction épithète
                    new_adjectif = adjectif_simple + 'な'
                    row.append(new_adjectif)
                elif conj == 'sans le i de fin': 
                    row.append('') #Existe seulement pour les adjectifs en i
                elif conj == 'adverbe':
                    #adverbe'
                    new_adjectif = adjectif_simple + 'に'
                    row.append(new_adjectif)
                elif conj == 'ba affirmatif':
                    new_adjectif = '' #ce sera dans la grammaire
                    row.append(new_adjectif)
                elif conj == 'ba négatif':
                    new_adjectif = '' #ce sera dans la grammaire
                    row.append(new_adjectif)
                elif conj == 'tara':
                    new_adjectif = adjectif_simple + 'だったら'
                    row.append(new_adjectif)
               
                
            else:
                row.append('')
                
            if adjectif_kana != '':
                adjectif_simple = adjectif_kana
                if conj == 'affirmatif neutre':
                    #affirmatif neutre
                    new_adjectif = adjectif_simple
                    row.append(new_adjectif)
                elif conj == 'affirmatif passé neutre':
                    #affirmatif passé neutre
                    new_adjectif = adjectif_simple + 'だった'
                    row.append(new_adjectif)
                elif conj == 'négatif neutre':
                    #négatif neutre 1
                    new_adjectif = adjectif_simple + 'じゃない'
                    row.append(new_adjectif)
                elif conj == 'négatif passé neutre':
                    #négatif passé neutre 1
                    new_adjectif = adjectif_simple + 'じゃなかった'
                    row.append(new_adjectif)
                elif conj == 'négatif neutre':
                    #négatif neutre 2
                    new_adjectif = adjectif_simple + 'ではない'
                    row.append(new_adjectif)
                elif conj == 'négatif passé neutre':
                    #négatif passé neutre 2
                    new_adjectif = adjectif_simple + 'ではなかった'
                    row.append(new_adjectif)
                elif conj == 'fonction épithète':
                    #fonction épithète
                    new_adjectif = adjectif_simple + 'な'
                    row.append(new_adjectif)
                elif conj == 'sans le i de fin': 
                    row.append('') #Existe seulement pour les adjectifs en i
                elif conj == 'adverbe':
                    #adverbe'
                    new_adjectif = adjectif_simple + 'に'
                    row.append(new_adjectif)
                elif conj == 'ba affirmatif':
                    new_adjectif = '' #ce sera dans la grammaire
                    row.append(new_adjectif)
                elif conj == 'ba négatif':
                    new_adjectif = '' #ce sera dans la grammaire
                    row.append(new_adjectif)
                elif conj == 'tara':
                    new_adjectif = adjectif_simple + 'だったら'
                    row.append(new_adjectif)
                
            else:
                row.append('')
            row.append(conj)
            row.append(adjectif_kanji)
            row.append(adjectif_kana)
            row.append(adjectif_trad)
            rows.append(row)
            
        
    elif type_adjectif == 'i':
        for conj in all_conj_adjectif:
            row = [type_adjectif]
            if adjectif_kanji != '':
                adjectif_simple = adjectif_kanji
                if conj == 'affirmatif neutre':
                    #affirmatif neutre
                    new_adjectif = adjectif_simple 
                    row.append(new_adjectif)
                elif conj == 'affirmatif passé neutre':
                    #affirmatif passé neutre
                    new_adjectif = adjectif_simple[:-1] + 'かった'
                    row.append(new_adjectif)
                elif conj == 'négatif neutre':
                    #négatif neutre 1
                    new_adjectif = adjectif_simple[:-1] + 'くない'
                    row.append(new_adjectif)
                elif conj == 'négatif passé neutre':
                    #négatif passé neutre 1
                    new_adjectif = adjectif_simple[:-1] + 'くなかった'
                    row.append(new_adjectif)
                elif conj == 'négatif neutre':
                    #négatif neutre 2
                    new_adjectif = adjectif_simple[:-1] + 'くない'
                    row.append(new_adjectif)
                elif conj == 'négatif passé neutre':
                    #négatif passé neutre 2
                    new_adjectif = adjectif_simple[:-1] + 'くなかった'
                    row.append(new_adjectif)
                elif conj == 'fonction épithète':
                    #fonction épithète
                    new_adjectif = adjectif_simple 
                    row.append(new_adjectif)
                elif conj == 'sans le i de fin': 
                    new_adjectif = adjectif_simple[:-1]
                    row.append(new_adjectif) 
                elif conj == 'adverbe':
                    #adverbe'
                    new_adjectif = adjectif_simple[:-1] + 'く'
                    row.append(new_adjectif)
                elif conj == 'ba affirmatif':
                    new_adjectif = adjectif_simple[:-1] + 'ければ'
                    row.append(new_adjectif)
                elif conj == 'ba négatif':
                    new_adjectif = adjectif_simple[:-1] + 'くなければ'
                    row.append(new_adjectif)
                elif conj == 'tara':
                    #affirmatif passé neutre
                    new_adjectif = adjectif_simple[:-1] + 'かったら'
                    row.append(new_adjectif)
                
            else:
                row.append('')
                
            if adjectif_kana != '':
                adjectif_simple = adjectif_kana
                if conj == 'affirmatif neutre':
                    #affirmatif neutre
                    new_adjectif = adjectif_simple 
                    row.append(new_adjectif)
                elif conj == 'affirmatif passé neutre':
                    #affirmatif passé neutre
                    new_adjectif = adjectif_simple[:-1] + 'かった'
                    row.append(new_adjectif)
                elif conj == 'négatif neutre':
                    #négatif neutre 1
                    new_adjectif = adjectif_simple[:-1] + 'くない'
                    row.append(new_adjectif)
                elif conj == 'négatif passé neutre':
                    #négatif passé neutre 1
                    new_adjectif = adjectif_simple[:-1] + 'くなかった'
                    row.append(new_adjectif)
                elif conj == 'négatif neutre':
                    #négatif neutre 2
                    new_adjectif = adjectif_simple[:-1] + 'くない'
                    row.append(new_adjectif)
                elif conj == 'négatif passé neutre':
                    #négatif passé neutre 2
                    new_adjectif = adjectif_simple[:-1] + 'くなかった'
                    row.append(new_adjectif)
                elif conj == 'fonction épithète':
                    #fonction épithète
                    new_adjectif = adjectif_simple 
                    row.append(new_adjectif)
                elif conj == 'sans le i de fin': 
                    new_adjectif = adjectif_simple[:-1]
                    row.append(new_adjectif) 
                elif conj == 'adverbe':
                    #adverbe'
                    new_adjectif = adjectif_simple[:-1] + 'く'
                    row.append(new_adjectif)
                elif conj == 'ba affirmatif':
                    new_adjectif = adjectif_simple[:-1] + 'ければ'
                    row.append(new_adjectif)
                elif conj == 'ba négatif':
                    new_adjectif = adjectif_simple[:-1] + 'くなければ'
                    row.append(new_adjectif)
                elif conj == 'tara':
                    #affirmatif passé neutre
                    new_adjectif = adjectif_simple[:-1] + 'かったら'
                    row.append(new_adjectif)
            else:
                row.append('')
            row.append(conj)
            row.append(adjectif_kanji)
            row.append(adjectif_kana)
            row.append(adjectif_trad)
            rows.append(row)
            
        
        

    

   
# field names  
fields = ['Type adj', 'Kanji', 'Kana', 'Conjugaison', 'Adjectif simple kanji', 'Adjectif simple kana', 'Trad']  
    

# name of csv file  
filename = "all_adjectifs.csv"
    
# writing to csv file  
with open(filename, 'w', newline='', encoding='utf-32') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(fields)  
        
    # writing the data rows  
    csvwriter.writerows(rows)         
