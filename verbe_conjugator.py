# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 16:18:48 2020

@author: stefa
"""

import csv

#ADJECTIFS

def data_preparation(csv): 
    type_verbes = []
    kanji = []
    kana = []
    trad = []
    
    for l in csv[1:]:
        l.strip()
        ligne = l.split(',') 
        if 'null' not in ligne:
            type_verbes.append(ligne[0])
            kanji.append(ligne[1])
            kana.append(ligne[2])
            trad.append(ligne[3][:-1])
            
    
    return type_verbes, kanji, kana, trad 
        
fi = open("Japan_English_Verbes_Dict.csv",'r', encoding="utf32")
csv_liste = fi.readlines()
fi.close()

type_verbes, kanji, kana, trad = data_preparation(csv_liste)


#ON TRIE LA LISTE PAR LONGUEUR DES KANJI POUR EVITER DE TROUVER PLUSIEURS VERBES DANS LA RECHERCHE A POSTERIORI

len_kanji = []

for kan in kanji:
    len_kanji.append(len(kan))
    
len_kanji, kanji, type_verbes, kana, trad = zip(*sorted(zip(len_kanji, kanji, type_verbes, kana, trad)))

kanji = kanji[::-1]
type_verbes = type_verbes[::-1]
kana = kana[::-1]
trad = trad[::-1]




rows = []

print(len(type_verbes))

for i in range(len(type_verbes)):  #Parcours tous les adjectifs de la liste tiré de JMDict
    type_verbe = type_verbes[i]
    verbe_kanji = kanji[i]
    verbe_kana = kana[i]
    verbe_trad = trad[i]

    all_conj_verbe = ['présent affirmatif neutre', 'présent négatif neutre', 'passé affirmatif neutre', 'passé négatif neutre', 'présent affirmatif formel', 'présent négatif formel', 'passé affirmatif formel', 'passé négatif formel', 'forme en て　affirmatif neutre', 'forme en て　négatif neutre', 'forme en て　affirmatif formel', 'forme potentiel affirmatif neutre', 'forme potentiel négatif neutre', 'forme potentiel affirmatif formel', 'forme potentiel négatif formel', 'forme passif affirmatif neutre', 'forme passif négatif neutre', 'forme passif affirmatif formel', 'forme passif négatif formel', 'forme causatif affirmatif neutre', 'forme causatif négatif neutre', 'forme causatif affirmatif formel', 'forme causatif négatif formel', 'forme causatif passif affirmatif neutre', 'forme causatif passif négatif neutre', 'forme causatif passif affirmatif formel', 'forme causatif passif négatif formel', 'forme volutive affirmatif neutre', 'forme volutive négatif neutre', 'forme volutive affirmatif formel', 'forme volutive négatif formel', 'forme conjecturale neutre', 'forme conjecturale formel', 'forme conditionnel neutre', 'forme conditionnel négatif', 'impératif affirmatif', 'impératif négatif', 'radical - masu-forme', 'tara', 'zu', 'kucha', 'kya']
    
    if type_verbe == 'ichidan':
        for conj in all_conj_verbe:
            row = [type_verbe]
            if verbe_kanji != '':
                masu_forme = verbe_kanji[:-1] 
                if conj == 'présent affirmatif neutre':
                    new_verbe = masu_forme + 'る'
                    row.append(new_verbe)
                if conj == 'présent négatif neutre':
                    new_verbe = masu_forme + 'ない'
                    row.append(new_verbe)
                if conj == 'passé affirmatif neutre':
                    new_verbe = masu_forme + 'た'
                    row.append(new_verbe)
                if conj == 'passé négatif neutre':
                    new_verbe = masu_forme + 'なかった'
                    row.append(new_verbe)
                if conj == 'présent affirmatif formel':
                    new_verbe = masu_forme + 'ます'
                    row.append(new_verbe)
                if conj == 'présent négatif formel':
                    new_verbe = masu_forme + 'ません'
                    row.append(new_verbe)
                if conj == 'passé affirmatif formel':
                    new_verbe = masu_forme + 'ました'
                    row.append(new_verbe)
                if conj == 'passé négatif formel':
                    new_verbe = masu_forme + 'ませんでした'
                    row.append(new_verbe)
                if conj == 'forme en て　affirmatif neutre':
                    new_verbe = masu_forme + 'て'
                    row.append(new_verbe)
                if conj == 'forme en て　négatif neutre':
                    new_verbe = masu_forme + 'なくて'
                    row.append(new_verbe)
                if conj == 'forme en て　affirmatif formel':
                    new_verbe = masu_forme + 'まして'
                    row.append(new_verbe)
                if conj == 'forme potentiel affirmatif neutre':
                    new_verbe = masu_forme + 'られる'
                    row.append(new_verbe)
                if conj == 'forme potentiel négatif neutre':
                    new_verbe = masu_forme + 'られない'
                    row.append(new_verbe)
                if conj == 'forme potentiel affirmatif formel':
                    new_verbe = masu_forme + 'られます'
                    row.append(new_verbe)
                if conj == 'forme potentiel négatif formel':
                    new_verbe = masu_forme + 'られません'
                    row.append(new_verbe)
                if conj == 'forme passif affirmatif neutre':
                    new_verbe = masu_forme + 'られる'
                    row.append(new_verbe)
                if conj == 'forme passif négatif neutre':
                    new_verbe = masu_forme + 'られない'
                    row.append(new_verbe)
                if conj == 'forme passif affirmatif formel':
                    new_verbe = masu_forme + 'られます'
                    row.append(new_verbe)
                if conj == 'forme passif négatif formel':
                    new_verbe = masu_forme + 'られません'
                    row.append(new_verbe)
                if conj == 'forme causatif affirmatif neutre':
                    new_verbe = masu_forme + 'させる'
                    row.append(new_verbe)
                if conj == 'forme causatif négatif neutre':
                    new_verbe = masu_forme + 'させない'
                    row.append(new_verbe)
                if conj == 'forme causatif affirmatif formel':
                    new_verbe = masu_forme + 'させます'
                    row.append(new_verbe)
                if conj == 'forme causatif négatif formel':
                    new_verbe = masu_forme + 'させません'
                    row.append(new_verbe)
                if conj == 'forme causatif passif affirmatif neutre':
                    new_verbe = masu_forme + 'させられる'
                    row.append(new_verbe)
                if conj == 'forme causatif passif négatif neutre':
                    new_verbe = masu_forme + 'させられない'
                    row.append(new_verbe)
                if conj == 'forme causatif passif affirmatif formel':
                    new_verbe = masu_forme + 'させられます'
                    row.append(new_verbe)
                if conj == 'forme causatif passif négatif formel':
                    new_verbe = masu_forme + 'させられません'
                    row.append(new_verbe)
                if conj == 'forme volutive affirmatif neutre':
                    new_verbe = masu_forme + 'たい'
                    row.append(new_verbe)
                if conj == 'forme volutive négatif neutre':
                    new_verbe = masu_forme + 'たくない'
                    row.append(new_verbe)
                if conj == 'forme volutive affirmatif formel':
                    new_verbe = masu_forme + 'たかった'
                    row.append(new_verbe)
                if conj == 'forme volutive négatif formel':
                    new_verbe = masu_forme + 'たくなかった'
                    row.append(new_verbe)
                if conj == 'forme conjecturale neutre':
                    new_verbe = masu_forme + 'よう'
                    row.append(new_verbe)
                if conj == 'forme conjecturale formel':
                    new_verbe = masu_forme + 'ましょう'
                    row.append(new_verbe)
                if conj == 'forme conditionnel neutre':
                    new_verbe = masu_forme + 'れば'
                    row.append(new_verbe)
                if conj == 'forme conditionnel négatif':
                    new_verbe = masu_forme + 'なければ'
                    row.append(new_verbe)
                if conj == 'impératif affirmatif':
                    new_verbe = masu_forme + 'ろ'
                    row.append(new_verbe)
                if conj == 'impératif négatif':
                    new_verbe = masu_forme + 'るな'
                    row.append(new_verbe)
                if conj == 'radical - masu-forme': 
                    #radical masu-form
                    row.append(masu_forme)
                if conj == 'tara':
                    new_verbe = masu_forme + 'たら'
                    row.append(new_verbe)
                if conj == 'zu':
                    new_verbe = masu_forme + 'ず'
                    row.append(new_verbe)
                if conj == 'kucha':
                    new_verbe = masu_forme + 'なくちゃ'
                    row.append(new_verbe)
                if conj == 'kya':
                    new_verbe = masu_forme + 'なきゃ'
                    row.append(new_verbe)
                
            else:
                row.append('')
                
            if verbe_kana != '':
                masu_forme = verbe_kana[:-1]
                if conj == 'présent affirmatif neutre':
                    new_verbe = masu_forme + 'る'
                    row.append(new_verbe)
                if conj == 'présent négatif neutre':
                    new_verbe = masu_forme + 'ない'
                    row.append(new_verbe)
                if conj == 'passé affirmatif neutre':
                    new_verbe = masu_forme + 'た'
                    row.append(new_verbe)
                if conj == 'passé négatif neutre':
                    new_verbe = masu_forme + 'なかった'
                    row.append(new_verbe)
                if conj == 'présent affirmatif formel':
                    new_verbe = masu_forme + 'ます'
                    row.append(new_verbe)
                if conj == 'présent négatif formel':
                    new_verbe = masu_forme + 'ません'
                    row.append(new_verbe)
                if conj == 'passé affirmatif formel':
                    new_verbe = masu_forme + 'ました'
                    row.append(new_verbe)
                if conj == 'passé négatif formel':
                    new_verbe = masu_forme + 'ませんでした'
                    row.append(new_verbe)
                if conj == 'forme en て　affirmatif neutre':
                    new_verbe = masu_forme + 'て'
                    row.append(new_verbe)
                if conj == 'forme en て　négatif neutre':
                    new_verbe = masu_forme + 'なくて'
                    row.append(new_verbe)
                if conj == 'forme en て　affirmatif formel':
                    new_verbe = masu_forme + 'まして'
                    row.append(new_verbe)
                if conj == 'forme potentiel affirmatif neutre':
                    new_verbe = masu_forme + 'られる'
                    row.append(new_verbe)
                if conj == 'forme potentiel négatif neutre':
                    new_verbe = masu_forme + 'られない'
                    row.append(new_verbe)
                if conj == 'forme potentiel affirmatif formel':
                    new_verbe = masu_forme + 'られます'
                    row.append(new_verbe)
                if conj == 'forme potentiel négatif formel':
                    new_verbe = masu_forme + 'られません'
                    row.append(new_verbe)
                if conj == 'forme passif affirmatif neutre':
                    new_verbe = masu_forme + 'られる'
                    row.append(new_verbe)
                if conj == 'forme passif négatif neutre':
                    new_verbe = masu_forme + 'られない'
                    row.append(new_verbe)
                if conj == 'forme passif affirmatif formel':
                    new_verbe = masu_forme + 'られます'
                    row.append(new_verbe)
                if conj == 'forme passif négatif formel':
                    new_verbe = masu_forme + 'られません'
                    row.append(new_verbe)
                if conj == 'forme causatif affirmatif neutre':
                    new_verbe = masu_forme + 'させる'
                    row.append(new_verbe)
                if conj == 'forme causatif négatif neutre':
                    new_verbe = masu_forme + 'させない'
                    row.append(new_verbe)
                if conj == 'forme causatif affirmatif formel':
                    new_verbe = masu_forme + 'させます'
                    row.append(new_verbe)
                if conj == 'forme causatif négatif formel':
                    new_verbe = masu_forme + 'させません'
                    row.append(new_verbe)
                if conj == 'forme causatif passif affirmatif neutre':
                    new_verbe = masu_forme + 'させられる'
                    row.append(new_verbe)
                if conj == 'forme causatif passif négatif neutre':
                    new_verbe = masu_forme + 'させられない'
                    row.append(new_verbe)
                if conj == 'forme causatif passif affirmatif formel':
                    new_verbe = masu_forme + 'させられます'
                    row.append(new_verbe)
                if conj == 'forme causatif passif négatif formel':
                    new_verbe = masu_forme + 'させられません'
                    row.append(new_verbe)
                if conj == 'forme volutive affirmatif neutre':
                    new_verbe = masu_forme + 'たい'
                    row.append(new_verbe)
                if conj == 'forme volutive négatif neutre':
                    new_verbe = masu_forme + 'たくない'
                    row.append(new_verbe)
                if conj == 'forme volutive affirmatif formel':
                    new_verbe = masu_forme + 'たかった'
                    row.append(new_verbe)
                if conj == 'forme volutive négatif formel':
                    new_verbe = masu_forme + 'たくなかった'
                    row.append(new_verbe)
                if conj == 'forme conjecturale neutre':
                    new_verbe = masu_forme + 'よう'
                    row.append(new_verbe)
                if conj == 'forme conjecturale formel':
                    new_verbe = masu_forme + 'ましょう'
                    row.append(new_verbe)
                if conj == 'forme conditionnel neutre':
                    new_verbe = masu_forme + 'れば'
                    row.append(new_verbe)
                if conj == 'forme conditionnel négatif':
                    new_verbe = masu_forme + 'なければ'
                    row.append(new_verbe)
                if conj == 'impératif affirmatif':
                    new_verbe = masu_forme + 'ろ'
                    row.append(new_verbe)
                if conj == 'impératif négatif':
                    new_verbe = masu_forme + 'るな'
                    row.append(new_verbe)
                if conj == 'radical - masu-forme': 
                    #radical masu-form
                    row.append(masu_forme)
                if conj == 'tara':
                    new_verbe = masu_forme + 'たら'
                    row.append(new_verbe)
                if conj == 'zu':
                    new_verbe = masu_forme + 'ず'
                    row.append(new_verbe)
                if conj == 'kucha':
                    new_verbe = masu_forme + 'なくちゃ'
                    row.append(new_verbe)
                if conj == 'kya':
                    new_verbe = masu_forme + 'なきゃ'
                    row.append(new_verbe)
               
            else:
                row.append('')
            row.append(conj)
            row.append(verbe_kanji)
            row.append(verbe_kana)
            row.append(verbe_trad)
            rows.append(row)
            
        
    elif type_verbe == 'godan':
    
        end_verbe = verbe_kana[-1]
        
        if end_verbe == 'く':
            if verbe_kanji != '':
                verbe_kanji = verbe_kanji[:-1] + 'き'
            verbe_kana = verbe_kana[:-1] + 'き'
        elif end_verbe == "ぐ":
            if verbe_kanji != '':
                verbe_kanji = verbe_kanji[:-1] + 'ぎ'
            verbe_kana = verbe_kana[:-1] + 'ぎ'
        elif end_verbe == "つ":
            if verbe_kanji != '':
                verbe_kanji = verbe_kanji[:-1] + 'ち'
            verbe_kana = verbe_kana[:-1] + 'ち'
        elif end_verbe == "ぬ":
            if verbe_kanji != '':
                verbe_kanji = verbe_kanji[:-1] + 'に'
            verbe_kana = verbe_kana[:-1] + 'に'
        elif end_verbe == "う":
            if verbe_kanji != '':
                verbe_kanji = verbe_kanji[:-1] + 'い'
            verbe_kana = verbe_kana[:-1] + 'い'
        elif end_verbe == "す":
            if verbe_kanji != '':
                verbe_kanji = verbe_kanji[:-1] + 'し'
            verbe_kana = verbe_kana[:-1] + 'し'
        elif end_verbe == "る":
            if verbe_kanji != '':
                verbe_kanji = verbe_kanji[:-1] + 'り'
            verbe_kana = verbe_kana[:-1] + 'り'
        elif end_verbe == "ぶ":
            if verbe_kanji != '':
                verbe_kanji = verbe_kanji[:-1] + 'び'
            verbe_kana = verbe_kana[:-1] + ''
        elif end_verbe == "む":
            if verbe_kanji != '':
                verbe_kanji = verbe_kanji[:-1] + 'み'
            verbe_kana = verbe_kana[:-1] + 'み'
            
        end_verbe = verbe_kana[-1]
        
        if end_verbe == "き":
            for conj in all_conj_verbe:
                row = [type_verbe]
                if verbe_kanji != '':
                    masu_forme = verbe_kanji
                    if conj == 'présent affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'く'
                        row.append(new_verbe)
                        verbe_kanji_neutre = new_verbe
                    if conj == 'présent négatif neutre':
                        new_verbe = masu_forme[:-1] + 'かない'
                        row.append(new_verbe)
                    if conj == 'passé affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'いた'
                        row.append(new_verbe)
                    if conj == 'passé négatif neutre':
                        new_verbe = masu_forme[:-1] + 'かなかった'
                        row.append(new_verbe)
                    if conj == 'présent affirmatif formel':
                        new_verbe = masu_forme + 'ます'
                        row.append(new_verbe)
                    if conj == 'présent négatif formel':
                        new_verbe = masu_forme + 'ません'
                        row.append(new_verbe)
                    if conj == 'passé affirmatif formel':
                        new_verbe = masu_forme + 'ました'
                        row.append(new_verbe)
                    if conj == 'passé négatif formel':
                        new_verbe = masu_forme + 'ませんでした'
                        row.append(new_verbe)
                    if conj == 'forme en て　affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'いて'
                        row.append(new_verbe)
                    if conj == 'forme en て　négatif neutre':
                        new_verbe = masu_forme[:-1] + 'かなくて'
                        row.append(new_verbe)
                    if conj == 'forme en て　affirmatif formel':
                        new_verbe = masu_forme + 'まして'
                        row.append(new_verbe)
                    if conj == 'forme potentiel affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'ける'
                        row.append(new_verbe)
                    if conj == 'forme potentiel négatif neutre':
                        new_verbe = masu_forme[:-1] + 'けない'
                        row.append(new_verbe)
                    if conj == 'forme potentiel affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'けます'
                        row.append(new_verbe)
                    if conj == 'forme potentiel négatif formel':
                        new_verbe = masu_forme[:-1] + 'けません'
                        row.append(new_verbe)
                    if conj == 'forme passif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'かれる'
                        row.append(new_verbe)
                    if conj == 'forme passif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'かれない'
                        row.append(new_verbe)
                    if conj == 'forme passif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'かれます'
                        row.append(new_verbe)
                    if conj == 'forme passif négatif formel':
                        new_verbe = masu_forme[:-1] + 'かれません'
                        row.append(new_verbe)
                    if conj == 'forme causatif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'かせる'
                        row.append(new_verbe)
                    if conj == 'forme causatif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'かせない'
                        row.append(new_verbe)
                    if conj == 'forme causatif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'かせます'
                        row.append(new_verbe)
                    if conj == 'forme causatif négatif formel':
                        new_verbe = masu_forme[:-1] + 'かせません'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'かせられる'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'かせられない'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'かせられます'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif négatif formel':
                        new_verbe = masu_forme[:-1] + 'かせられません'
                        row.append(new_verbe)
                    if conj == 'forme volutive affirmatif neutre':
                        new_verbe = masu_forme + 'たい'
                        row.append(new_verbe)
                    if conj == 'forme volutive négatif neutre':
                        new_verbe = masu_forme + 'たくない'
                        row.append(new_verbe)
                    if conj == 'forme volutive affirmatif formel':
                        new_verbe = masu_forme + 'たかった'
                        row.append(new_verbe)
                    if conj == 'forme volutive négatif formel':
                        new_verbe = masu_forme + 'たくなかった'
                        row.append(new_verbe)
                    if conj == 'forme conjecturale neutre':
                        new_verbe = masu_forme[:-1] + 'こう'
                        row.append(new_verbe)
                    if conj == 'forme conjecturale formel':
                        new_verbe = masu_forme + 'ましょう'
                        row.append(new_verbe)
                    if conj == 'forme conditionnel neutre':
                        new_verbe = masu_forme[:-1] + 'けば'
                        row.append(new_verbe)
                    if conj == 'forme conditionnel négatif':
                        new_verbe = masu_forme[:-1] + 'かなければ'
                        row.append(new_verbe)
                    if conj == 'impératif affirmatif':
                        new_verbe = masu_forme[:-1] + 'け'
                        row.append(new_verbe)
                    if conj == 'impératif négatif':
                        new_verbe = masu_forme[:-1] + 'くな'
                        row.append(new_verbe)
                    if conj == 'radical - masu-forme': 
                        #radical masu-form
                        row.append(masu_forme)
                    if conj == 'tara':
                        new_verbe = masu_forme[:-1] + 'いたら'
                        row.append(new_verbe)
                    if conj == 'zu':
                        new_verbe = masu_forme[:-1] + 'かず'
                        row.append(new_verbe)
                    if conj == 'kucha':
                        new_verbe = masu_forme[:-1] + 'かなくちゃ'
                        row.append(new_verbe)
                    if conj == 'kya':
                        new_verbe = masu_forme[:-1] + 'かなきゃ'
                        row.append(new_verbe)
                    
                else:
                    row.append('')
                    
                if verbe_kana != '':
                    masu_forme = verbe_kana
                    if conj == 'présent affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'く'
                        row.append(new_verbe)
                        verbe_kana_neutre = new_verbe
                    if conj == 'présent négatif neutre':
                        new_verbe = masu_forme[:-1] + 'かない'
                        row.append(new_verbe)
                    if conj == 'passé affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'いた'
                        row.append(new_verbe)
                    if conj == 'passé négatif neutre':
                        new_verbe = masu_forme[:-1] + 'かなかった'
                        row.append(new_verbe)
                    if conj == 'présent affirmatif formel':
                        new_verbe = masu_forme + 'ます'
                        row.append(new_verbe)
                    if conj == 'présent négatif formel':
                        new_verbe = masu_forme + 'ません'
                        row.append(new_verbe)
                    if conj == 'passé affirmatif formel':
                        new_verbe = masu_forme + 'ました'
                        row.append(new_verbe)
                    if conj == 'passé négatif formel':
                        new_verbe = masu_forme + 'ませんでした'
                        row.append(new_verbe)
                    if conj == 'forme en て　affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'いて'
                        row.append(new_verbe)
                    if conj == 'forme en て　négatif neutre':
                        new_verbe = masu_forme[:-1] + 'かなくて'
                        row.append(new_verbe)
                    if conj == 'forme en て　affirmatif formel':
                        new_verbe = masu_forme + 'まして'
                        row.append(new_verbe)
                    if conj == 'forme potentiel affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'ける'
                        row.append(new_verbe)
                    if conj == 'forme potentiel négatif neutre':
                        new_verbe = masu_forme[:-1] + 'けない'
                        row.append(new_verbe)
                    if conj == 'forme potentiel affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'けます'
                        row.append(new_verbe)
                    if conj == 'forme potentiel négatif formel':
                        new_verbe = masu_forme[:-1] + 'けません'
                        row.append(new_verbe)
                    if conj == 'forme passif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'かれる'
                        row.append(new_verbe)
                    if conj == 'forme passif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'かれない'
                        row.append(new_verbe)
                    if conj == 'forme passif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'かれます'
                        row.append(new_verbe)
                    if conj == 'forme passif négatif formel':
                        new_verbe = masu_forme[:-1] + 'かれません'
                        row.append(new_verbe)
                    if conj == 'forme causatif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'かせる'
                        row.append(new_verbe)
                    if conj == 'forme causatif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'かせない'
                        row.append(new_verbe)
                    if conj == 'forme causatif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'かせます'
                        row.append(new_verbe)
                    if conj == 'forme causatif négatif formel':
                        new_verbe = masu_forme[:-1] + 'かせません'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'かせられる'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'かせられない'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'かせられます'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif négatif formel':
                        new_verbe = masu_forme[:-1] + 'かせられません'
                        row.append(new_verbe)
                    if conj == 'forme volutive affirmatif neutre':
                        new_verbe = masu_forme + 'たい'
                        row.append(new_verbe)
                    if conj == 'forme volutive négatif neutre':
                        new_verbe = masu_forme + 'たくない'
                        row.append(new_verbe)
                    if conj == 'forme volutive affirmatif formel':
                        new_verbe = masu_forme + 'たかった'
                        row.append(new_verbe)
                    if conj == 'forme volutive négatif formel':
                        new_verbe = masu_forme + 'たくなかった'
                        row.append(new_verbe)
                    if conj == 'forme conjecturale neutre':
                        new_verbe = masu_forme[:-1] + 'こう'
                        row.append(new_verbe)
                    if conj == 'forme conjecturale formel':
                        new_verbe = masu_forme + 'ましょう'
                        row.append(new_verbe)
                    if conj == 'forme conditionnel neutre':
                        new_verbe = masu_forme[:-1] + 'けば'
                        row.append(new_verbe)
                    if conj == 'forme conditionnel négatif':
                        new_verbe = masu_forme[:-1] + 'かなければ'
                        row.append(new_verbe)
                    if conj == 'impératif affirmatif':
                        new_verbe = masu_forme[:-1] + 'け'
                        row.append(new_verbe)
                    if conj == 'impératif négatif':
                        new_verbe = masu_forme[:-1] + 'くな'
                        row.append(new_verbe)
                    if conj == 'radical - masu-forme': 
                        #radical masu-form
                        row.append(masu_forme)
                    if conj == 'tara':
                        new_verbe = masu_forme[:-1] + 'いたら'
                        row.append(new_verbe)
                    if conj == 'zu':
                        new_verbe = masu_forme[:-1] + 'かず'
                        row.append(new_verbe)
                    if conj == 'kucha':
                        new_verbe = masu_forme[:-1] + 'かなくちゃ'
                        row.append(new_verbe)
                    if conj == 'kya':
                        new_verbe = masu_forme[:-1] + 'かなきゃ'
                        row.append(new_verbe)
                   
                else:
                    row.append('')
                row.append(conj)
                row.append(verbe_kanji_neutre)
                row.append(verbe_kana_neutre)
                row.append(verbe_trad)
                
                rows.append(row)

            
        if end_verbe == "ぎ":
            for conj in all_conj_verbe:
                row = [type_verbe]
                if verbe_kanji != '':
                    masu_forme = verbe_kanji
                    if conj == 'présent affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'ぐ'
                        row.append(new_verbe)
                        verbe_kanji_neutre = new_verbe
                    if conj == 'présent négatif neutre':
                        new_verbe = masu_forme[:-1] + 'がない'
                        row.append(new_verbe)
                    if conj == 'passé affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'いだ'
                        row.append(new_verbe)
                    if conj == 'passé négatif neutre':
                        new_verbe = masu_forme[:-1] + 'がなかった'
                        row.append(new_verbe)
                    if conj == 'présent affirmatif formel':
                        new_verbe = masu_forme + 'ます'
                        row.append(new_verbe)
                    if conj == 'présent négatif formel':
                        new_verbe = masu_forme + 'ません'
                        row.append(new_verbe)
                    if conj == 'passé affirmatif formel':
                        new_verbe = masu_forme + 'ました'
                        row.append(new_verbe)
                    if conj == 'passé négatif formel':
                        new_verbe = masu_forme + 'ませんでした'
                        row.append(new_verbe)
                    if conj == 'forme en て　affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'いで'
                        row.append(new_verbe)
                    if conj == 'forme en て　négatif neutre':
                        new_verbe = masu_forme[:-1] + 'がなくて'
                        row.append(new_verbe)
                    if conj == 'forme en て　affirmatif formel':
                        new_verbe = masu_forme + 'まして'
                        row.append(new_verbe)
                    if conj == 'forme potentiel affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'げる'
                        row.append(new_verbe)
                    if conj == 'forme potentiel négatif neutre':
                        new_verbe = masu_forme[:-1] + 'げない'
                        row.append(new_verbe)
                    if conj == 'forme potentiel affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'げます'
                        row.append(new_verbe)
                    if conj == 'forme potentiel négatif formel':
                        new_verbe = masu_forme[:-1] + 'げません'
                        row.append(new_verbe)
                    if conj == 'forme passif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'がれる'
                        row.append(new_verbe)
                    if conj == 'forme passif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'がれない'
                        row.append(new_verbe)
                    if conj == 'forme passif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'がれます'
                        row.append(new_verbe)
                    if conj == 'forme passif négatif formel':
                        new_verbe = masu_forme[:-1] + 'がれません'
                        row.append(new_verbe)
                    if conj == 'forme causatif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'がせる'
                        row.append(new_verbe)
                    if conj == 'forme causatif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'がせない'
                        row.append(new_verbe)
                    if conj == 'forme causatif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'がせます'
                        row.append(new_verbe)
                    if conj == 'forme causatif négatif formel':
                        new_verbe = masu_forme[:-1] + 'がせません'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'がせられる'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'がせられない'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'がせられます'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif négatif formel':
                        new_verbe = masu_forme[:-1] + 'がせられません'
                        row.append(new_verbe)
                    if conj == 'forme volutive affirmatif neutre':
                        new_verbe = masu_forme + 'たい'
                        row.append(new_verbe)
                    if conj == 'forme volutive négatif neutre':
                        new_verbe = masu_forme + 'たくない'
                        row.append(new_verbe)
                    if conj == 'forme volutive affirmatif formel':
                        new_verbe = masu_forme + 'たかった'
                        row.append(new_verbe)
                    if conj == 'forme volutive négatif formel':
                        new_verbe = masu_forme + 'たくなかった'
                        row.append(new_verbe)
                    if conj == 'forme conjecturale neutre':
                        new_verbe = masu_forme[:-1] + 'ごう'
                        row.append(new_verbe)
                    if conj == 'forme conjecturale formel':
                        new_verbe = masu_forme + 'ましょう'
                        row.append(new_verbe)
                    if conj == 'forme conditionnel neutre':
                        new_verbe = masu_forme[:-1] + 'げば'
                        row.append(new_verbe)
                    if conj == 'forme conditionnel négatif':
                        new_verbe = masu_forme[:-1] + 'がなければ'
                        row.append(new_verbe)
                    if conj == 'impératif affirmatif':
                        new_verbe = masu_forme[:-1] + 'げ'
                        row.append(new_verbe)
                    if conj == 'impératif négatif':
                        new_verbe = masu_forme[:-1] + 'ぐな'
                        row.append(new_verbe)
                    if conj == 'radical - masu-forme': 
                        #radical masu-form
                        row.append(masu_forme)
                    if conj == 'tara':
                        new_verbe = masu_forme[:-1] + 'いだら'
                        row.append(new_verbe)
                    if conj == 'zu':
                        new_verbe = masu_forme[:-1] + 'がず'
                        row.append(new_verbe)
                    if conj == 'kucha':
                        new_verbe = masu_forme[:-1] + 'がなくちゃ'
                        row.append(new_verbe)
                    if conj == 'kya':
                        new_verbe = masu_forme[:-1] + 'がなきゃ'
                        row.append(new_verbe)
                   
                else:
                    row.append('')
                    
                    
                if verbe_kana != '':
                    masu_forme = verbe_kana
                    if conj == 'présent affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'ぐ'
                        row.append(new_verbe)
                        verbe_kana_neutre = new_verbe
                    if conj == 'présent négatif neutre':
                        new_verbe = masu_forme[:-1] + 'がない'
                        row.append(new_verbe)
                    if conj == 'passé affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'いだ'
                        row.append(new_verbe)
                    if conj == 'passé négatif neutre':
                        new_verbe = masu_forme[:-1] + 'がなかった'
                        row.append(new_verbe)
                    if conj == 'présent affirmatif formel':
                        new_verbe = masu_forme + 'ます'
                        row.append(new_verbe)
                    if conj == 'présent négatif formel':
                        new_verbe = masu_forme + 'ません'
                        row.append(new_verbe)
                    if conj == 'passé affirmatif formel':
                        new_verbe = masu_forme + 'ました'
                        row.append(new_verbe)
                    if conj == 'passé négatif formel':
                        new_verbe = masu_forme + 'ませんでした'
                        row.append(new_verbe)
                    if conj == 'forme en て　affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'いで'
                        row.append(new_verbe)
                    if conj == 'forme en て　négatif neutre':
                        new_verbe = masu_forme[:-1] + 'がなくて'
                        row.append(new_verbe)
                    if conj == 'forme en て　affirmatif formel':
                        new_verbe = masu_forme + 'まして'
                        row.append(new_verbe)
                    if conj == 'forme potentiel affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'げる'
                        row.append(new_verbe)
                    if conj == 'forme potentiel négatif neutre':
                        new_verbe = masu_forme[:-1] + 'げない'
                        row.append(new_verbe)
                    if conj == 'forme potentiel affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'げます'
                        row.append(new_verbe)
                    if conj == 'forme potentiel négatif formel':
                        new_verbe = masu_forme[:-1] + 'げません'
                        row.append(new_verbe)
                    if conj == 'forme passif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'がれる'
                        row.append(new_verbe)
                    if conj == 'forme passif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'がれない'
                        row.append(new_verbe)
                    if conj == 'forme passif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'がれます'
                        row.append(new_verbe)
                    if conj == 'forme passif négatif formel':
                        new_verbe = masu_forme[:-1] + 'がれません'
                        row.append(new_verbe)
                    if conj == 'forme causatif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'がせる'
                        row.append(new_verbe)
                    if conj == 'forme causatif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'がせない'
                        row.append(new_verbe)
                    if conj == 'forme causatif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'がせます'
                        row.append(new_verbe)
                    if conj == 'forme causatif négatif formel':
                        new_verbe = masu_forme[:-1] + 'がせません'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'がせられる'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'がせられない'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'がせられます'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif négatif formel':
                        new_verbe = masu_forme[:-1] + 'がせられません'
                        row.append(new_verbe)
                    if conj == 'forme volutive affirmatif neutre':
                        new_verbe = masu_forme + 'たい'
                        row.append(new_verbe)
                    if conj == 'forme volutive négatif neutre':
                        new_verbe = masu_forme + 'たくない'
                        row.append(new_verbe)
                    if conj == 'forme volutive affirmatif formel':
                        new_verbe = masu_forme + 'たかった'
                        row.append(new_verbe)
                    if conj == 'forme volutive négatif formel':
                        new_verbe = masu_forme + 'たくなかった'
                        row.append(new_verbe)
                    if conj == 'forme conjecturale neutre':
                        new_verbe = masu_forme[:-1] + 'ごう'
                        row.append(new_verbe)
                    if conj == 'forme conjecturale formel':
                        new_verbe = masu_forme + 'ましょう'
                        row.append(new_verbe)
                    if conj == 'forme conditionnel neutre':
                        new_verbe = masu_forme[:-1] + 'げば'
                        row.append(new_verbe)
                    if conj == 'forme conditionnel négatif':
                        new_verbe = masu_forme[:-1] + 'がなければ'
                        row.append(new_verbe)
                    if conj == 'impératif affirmatif':
                        new_verbe = masu_forme[:-1] + 'げ'
                        row.append(new_verbe)
                    if conj == 'impératif négatif':
                        new_verbe = masu_forme[:-1] + 'ぐな'
                        row.append(new_verbe)
                    if conj == 'radical - masu-forme': 
                        #radical masu-form
                        row.append(masu_forme)
                    if conj == 'tara':
                        new_verbe = masu_forme[:-1] + 'いだら'
                        row.append(new_verbe)
                    if conj == 'zu':
                        new_verbe = masu_forme[:-1] + 'がず'
                        row.append(new_verbe)
                    if conj == 'kucha':
                        new_verbe = masu_forme[:-1] + 'がなくちゃ'
                        row.append(new_verbe)
                    if conj == 'kya':
                        new_verbe = masu_forme[:-1] + 'がなきゃ'
                        row.append(new_verbe)
                    
                else:
                    row.append('')
                row.append(conj)
                row.append(verbe_kanji_neutre)
                row.append(verbe_kana_neutre)
                row.append(verbe_trad)
                
                rows.append(row)

            
        if end_verbe == "ち":
            for conj in all_conj_verbe:
                row = [type_verbe]
                if verbe_kanji != '':
                    masu_forme = verbe_kanji
                    if conj == 'présent affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'つ'
                        row.append(new_verbe)
                        verbe_kanji_neutre = new_verbe
                    if conj == 'présent négatif neutre':
                        new_verbe = masu_forme[:-1] + 'たない'
                        row.append(new_verbe)
                    if conj == 'passé affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'った'
                        row.append(new_verbe)
                    if conj == 'passé négatif neutre':
                        new_verbe = masu_forme[:-1] + 'たなかった'
                        row.append(new_verbe)
                    if conj == 'présent affirmatif formel':
                        new_verbe = masu_forme + 'ます'
                        row.append(new_verbe)
                    if conj == 'présent négatif formel':
                        new_verbe = masu_forme + 'ません'
                        row.append(new_verbe)
                    if conj == 'passé affirmatif formel':
                        new_verbe = masu_forme + 'ました'
                        row.append(new_verbe)
                    if conj == 'passé négatif formel':
                        new_verbe = masu_forme + 'ませんでした'
                        row.append(new_verbe)
                    if conj == 'forme en て　affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'って'
                        row.append(new_verbe)
                    if conj == 'forme en て　négatif neutre':
                        new_verbe = masu_forme[:-1] + 'たなくて'
                        row.append(new_verbe)
                    if conj == 'forme en て　affirmatif formel':
                        new_verbe = masu_forme + 'まして'
                        row.append(new_verbe)
                    if conj == 'forme potentiel affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'てる'
                        row.append(new_verbe)
                    if conj == 'forme potentiel négatif neutre':
                        new_verbe = masu_forme[:-1] + 'てない'
                        row.append(new_verbe)
                    if conj == 'forme potentiel affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'てます'
                        row.append(new_verbe)
                    if conj == 'forme potentiel négatif formel':
                        new_verbe = masu_forme[:-1] + 'てません'
                        row.append(new_verbe)
                    if conj == 'forme passif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'たれる'
                        row.append(new_verbe)
                    if conj == 'forme passif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'たれない'
                        row.append(new_verbe)
                    if conj == 'forme passif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'たれます'
                        row.append(new_verbe)
                    if conj == 'forme passif négatif formel':
                        new_verbe = masu_forme[:-1] + 'たれません'
                        row.append(new_verbe)
                    if conj == 'forme causatif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'たせる'
                        row.append(new_verbe)
                    if conj == 'forme causatif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'たせない'
                        row.append(new_verbe)
                    if conj == 'forme causatif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'たせます'
                        row.append(new_verbe)
                    if conj == 'forme causatif négatif formel':
                        new_verbe = masu_forme[:-1] + 'たせません'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'たせられる'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'たせられない'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'たせられます'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif négatif formel':
                        new_verbe = masu_forme[:-1] + 'たせられません'
                        row.append(new_verbe)
                    if conj == 'forme volutive affirmatif neutre':
                        new_verbe = masu_forme + 'たい'
                        row.append(new_verbe)
                    if conj == 'forme volutive négatif neutre':
                        new_verbe = masu_forme + 'たくない'
                        row.append(new_verbe)
                    if conj == 'forme volutive affirmatif formel':
                        new_verbe = masu_forme + 'たかった'
                        row.append(new_verbe)
                    if conj == 'forme volutive négatif formel':
                        new_verbe = masu_forme + 'たくなかった'
                        row.append(new_verbe)
                    if conj == 'forme conjecturale neutre':
                        new_verbe = masu_forme[:-1] + 'とう'
                        row.append(new_verbe)
                    if conj == 'forme conjecturale formel':
                        new_verbe = masu_forme + 'ましょう'
                        row.append(new_verbe)
                    if conj == 'forme conditionnel neutre':
                        new_verbe = masu_forme[:-1] + 'てば'
                        row.append(new_verbe)
                    if conj == 'forme conditionnel négatif':
                        new_verbe = masu_forme[:-1] + 'たなければ'
                        row.append(new_verbe)
                    if conj == 'impératif affirmatif':
                        new_verbe = masu_forme[:-1] + 'て'
                        row.append(new_verbe)
                    if conj == 'impératif négatif':
                        new_verbe = masu_forme[:-1] + 'つな'
                        row.append(new_verbe)
                    if conj == 'radical - masu-forme': 
                        #radical masu-form
                        row.append(masu_forme)
                    if conj == 'tara':
                        new_verbe = masu_forme[:-1] + 'ったら'
                        row.append(new_verbe)
                    if conj == 'zu':
                        new_verbe = masu_forme[:-1] + 'たず'
                        row.append(new_verbe)
                    if conj == 'kucha':
                        new_verbe = masu_forme[:-1] + 'たなくちゃ'
                        row.append(new_verbe)
                    if conj == 'kya':
                        new_verbe = masu_forme[:-1] + 'たなきゃ'
                        row.append(new_verbe)
                   
                else:
                    row.append('')
                    
                if verbe_kana != '':
                    masu_forme = verbe_kana
                    if conj == 'présent affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'つ'
                        row.append(new_verbe)
                        verbe_kana_neutre = new_verbe
                    if conj == 'présent négatif neutre':
                        new_verbe = masu_forme[:-1] + 'たない'
                        row.append(new_verbe)
                    if conj == 'passé affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'った'
                        row.append(new_verbe)
                    if conj == 'passé négatif neutre':
                        new_verbe = masu_forme[:-1] + 'たなかった'
                        row.append(new_verbe)
                    if conj == 'présent affirmatif formel':
                        new_verbe = masu_forme + 'ます'
                        row.append(new_verbe)
                    if conj == 'présent négatif formel':
                        new_verbe = masu_forme + 'ません'
                        row.append(new_verbe)
                    if conj == 'passé affirmatif formel':
                        new_verbe = masu_forme + 'ました'
                        row.append(new_verbe)
                    if conj == 'passé négatif formel':
                        new_verbe = masu_forme + 'ませんでした'
                        row.append(new_verbe)
                    if conj == 'forme en て　affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'って'
                        row.append(new_verbe)
                    if conj == 'forme en て　négatif neutre':
                        new_verbe = masu_forme[:-1] + 'たなくて'
                        row.append(new_verbe)
                    if conj == 'forme en て　affirmatif formel':
                        new_verbe = masu_forme + 'まして'
                        row.append(new_verbe)
                    if conj == 'forme potentiel affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'てる'
                        row.append(new_verbe)
                    if conj == 'forme potentiel négatif neutre':
                        new_verbe = masu_forme[:-1] + 'てない'
                        row.append(new_verbe)
                    if conj == 'forme potentiel affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'てます'
                        row.append(new_verbe)
                    if conj == 'forme potentiel négatif formel':
                        new_verbe = masu_forme[:-1] + 'てません'
                        row.append(new_verbe)
                    if conj == 'forme passif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'たれる'
                        row.append(new_verbe)
                    if conj == 'forme passif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'たれない'
                        row.append(new_verbe)
                    if conj == 'forme passif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'たれます'
                        row.append(new_verbe)
                    if conj == 'forme passif négatif formel':
                        new_verbe = masu_forme[:-1] + 'たれません'
                        row.append(new_verbe)
                    if conj == 'forme causatif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'たせる'
                        row.append(new_verbe)
                    if conj == 'forme causatif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'たせない'
                        row.append(new_verbe)
                    if conj == 'forme causatif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'たせます'
                        row.append(new_verbe)
                    if conj == 'forme causatif négatif formel':
                        new_verbe = masu_forme[:-1] + 'たせません'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'たせられる'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'たせられない'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'たせられます'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif négatif formel':
                        new_verbe = masu_forme[:-1] + 'たせられません'
                        row.append(new_verbe)
                    if conj == 'forme volutive affirmatif neutre':
                        new_verbe = masu_forme + 'たい'
                        row.append(new_verbe)
                    if conj == 'forme volutive négatif neutre':
                        new_verbe = masu_forme + 'たくない'
                        row.append(new_verbe)
                    if conj == 'forme volutive affirmatif formel':
                        new_verbe = masu_forme + 'たかった'
                        row.append(new_verbe)
                    if conj == 'forme volutive négatif formel':
                        new_verbe = masu_forme + 'たくなかった'
                        row.append(new_verbe)
                    if conj == 'forme conjecturale neutre':
                        new_verbe = masu_forme[:-1] + 'とう'
                        row.append(new_verbe)
                    if conj == 'forme conjecturale formel':
                        new_verbe = masu_forme + 'ましょう'
                        row.append(new_verbe)
                    if conj == 'forme conditionnel neutre':
                        new_verbe = masu_forme[:-1] + 'てば'
                        row.append(new_verbe)
                    if conj == 'forme conditionnel négatif':
                        new_verbe = masu_forme[:-1] + 'たなければ'
                        row.append(new_verbe)
                    if conj == 'impératif affirmatif':
                        new_verbe = masu_forme[:-1] + 'て'
                        row.append(new_verbe)
                    if conj == 'impératif négatif':
                        new_verbe = masu_forme[:-1] + 'つな'
                        row.append(new_verbe)
                    if conj == 'radical - masu-forme': 
                        #radical masu-form
                        row.append(masu_forme)
                    if conj == 'tara':
                        new_verbe = masu_forme[:-1] + 'ったら'
                        row.append(new_verbe)
                    if conj == 'zu':
                        new_verbe = masu_forme[:-1] + 'たず'
                        row.append(new_verbe)
                    if conj == 'kucha':
                        new_verbe = masu_forme[:-1] + 'たなくちゃ'
                        row.append(new_verbe)
                    if conj == 'kya':
                        new_verbe = masu_forme[:-1] + 'たなきゃ'
                        row.append(new_verbe)
                
                else:
                    row.append('')
                row.append(conj)
                row.append(verbe_kanji_neutre)
                row.append(verbe_kana_neutre)
                row.append(verbe_trad)
                
                rows.append(row)


        if end_verbe == "に":
            for conj in all_conj_verbe:
                row = [type_verbe]
                if verbe_kanji != '':
                    masu_forme = verbe_kanji
                    if conj == 'présent affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'ぬ'
                        row.append(new_verbe)
                        verbe_kanji_neutre = new_verbe
                    if conj == 'présent négatif neutre':
                        new_verbe = masu_forme[:-1] + 'なない'
                        row.append(new_verbe)
                    if conj == 'passé affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'んだ'
                        row.append(new_verbe)
                    if conj == 'passé négatif neutre':
                        new_verbe = masu_forme[:-1] + 'ななかった'
                        row.append(new_verbe)
                    if conj == 'présent affirmatif formel':
                        new_verbe = masu_forme + 'ます'
                        row.append(new_verbe)
                    if conj == 'présent négatif formel':
                        new_verbe = masu_forme + 'ません'
                        row.append(new_verbe)
                    if conj == 'passé affirmatif formel':
                        new_verbe = masu_forme + 'ました'
                        row.append(new_verbe)
                    if conj == 'passé négatif formel':
                        new_verbe = masu_forme + 'ませんでした'
                        row.append(new_verbe)
                    if conj == 'forme en て　affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'んで'
                        row.append(new_verbe)
                    if conj == 'forme en て　négatif neutre':
                        new_verbe = masu_forme[:-1] + 'ななくて'
                        row.append(new_verbe)
                    if conj == 'forme en て　affirmatif formel':
                        new_verbe = masu_forme + 'まして'
                        row.append(new_verbe)
                    if conj == 'forme potentiel affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'ねる'
                        row.append(new_verbe)
                    if conj == 'forme potentiel négatif neutre':
                        new_verbe = masu_forme[:-1] + 'ねない'
                        row.append(new_verbe)
                    if conj == 'forme potentiel affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'ねます'
                        row.append(new_verbe)
                    if conj == 'forme potentiel négatif formel':
                        new_verbe = masu_forme[:-1] + 'ねません'
                        row.append(new_verbe)
                    if conj == 'forme passif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'なれる'
                        row.append(new_verbe)
                    if conj == 'forme passif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'なれない'
                        row.append(new_verbe)
                    if conj == 'forme passif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'なれます'
                        row.append(new_verbe)
                    if conj == 'forme passif négatif formel':
                        new_verbe = masu_forme[:-1] + 'なれません'
                        row.append(new_verbe)
                    if conj == 'forme causatif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'なせる'
                        row.append(new_verbe)
                    if conj == 'forme causatif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'なせない'
                        row.append(new_verbe)
                    if conj == 'forme causatif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'なせます'
                        row.append(new_verbe)
                    if conj == 'forme causatif négatif formel':
                        new_verbe = masu_forme[:-1] + 'なせません'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'なせられる'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'なせられない'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'なせられます'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif négatif formel':
                        new_verbe = masu_forme[:-1] + 'なせられません'
                        row.append(new_verbe)
                    if conj == 'forme volutive affirmatif neutre':
                        new_verbe = masu_forme + 'たい'
                        row.append(new_verbe)
                    if conj == 'forme volutive négatif neutre':
                        new_verbe = masu_forme + 'たくない'
                        row.append(new_verbe)
                    if conj == 'forme volutive affirmatif formel':
                        new_verbe = masu_forme + 'たかった'
                        row.append(new_verbe)
                    if conj == 'forme volutive négatif formel':
                        new_verbe = masu_forme + 'たくなかった'
                        row.append(new_verbe)
                    if conj == 'forme conjecturale neutre':
                        new_verbe = masu_forme[:-1] + 'のう'
                        row.append(new_verbe)
                    if conj == 'forme conjecturale formel':
                        new_verbe = masu_forme + 'ましょう'
                        row.append(new_verbe)
                    if conj == 'forme conditionnel neutre':
                        new_verbe = masu_forme[:-1] + 'ねば'
                        row.append(new_verbe)
                    if conj == 'forme conditionnel négatif':
                        new_verbe = masu_forme[:-1] + 'ななければ'
                        row.append(new_verbe)
                    if conj == 'impératif affirmatif':
                        new_verbe = masu_forme[:-1] + 'ね'
                        row.append(new_verbe)
                    if conj == 'impératif négatif':
                        new_verbe = masu_forme[:-1] + 'ぬな'
                        row.append(new_verbe)
                    if conj == 'radical - masu-forme': 
                        #radical masu-form
                        row.append(masu_forme)
                    if conj == 'tara':
                        new_verbe = masu_forme[:-1] + 'んだら'
                        row.append(new_verbe)
                    if conj == 'zu':
                        new_verbe = masu_forme[:-1] + 'なず'
                        row.append(new_verbe)
                    if conj == 'kucha':
                        new_verbe = masu_forme[:-1] + 'ななくちゃ'
                        row.append(new_verbe)
                    if conj == 'kya':
                        new_verbe = masu_forme[:-1] + 'ななきゃ'
                        row.append(new_verbe)

                else:
                    row.append('')
                    
                if verbe_kana != '':
                    masu_forme = verbe_kana
                    if conj == 'présent affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'ぬ'
                        row.append(new_verbe)
                        verbe_kana_neutre = new_verbe
                    if conj == 'présent négatif neutre':
                        new_verbe = masu_forme[:-1] + 'なない'
                        row.append(new_verbe)
                    if conj == 'passé affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'んだ'
                        row.append(new_verbe)
                    if conj == 'passé négatif neutre':
                        new_verbe = masu_forme[:-1] + 'ななかった'
                        row.append(new_verbe)
                    if conj == 'présent affirmatif formel':
                        new_verbe = masu_forme + 'ます'
                        row.append(new_verbe)
                    if conj == 'présent négatif formel':
                        new_verbe = masu_forme + 'ません'
                        row.append(new_verbe)
                    if conj == 'passé affirmatif formel':
                        new_verbe = masu_forme + 'ました'
                        row.append(new_verbe)
                    if conj == 'passé négatif formel':
                        new_verbe = masu_forme + 'ませんでした'
                        row.append(new_verbe)
                    if conj == 'forme en て　affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'んで'
                        row.append(new_verbe)
                    if conj == 'forme en て　négatif neutre':
                        new_verbe = masu_forme[:-1] + 'ななくて'
                        row.append(new_verbe)
                    if conj == 'forme en て　affirmatif formel':
                        new_verbe = masu_forme + 'まして'
                        row.append(new_verbe)
                    if conj == 'forme potentiel affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'ねる'
                        row.append(new_verbe)
                    if conj == 'forme potentiel négatif neutre':
                        new_verbe = masu_forme[:-1] + 'ねない'
                        row.append(new_verbe)
                    if conj == 'forme potentiel affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'ねます'
                        row.append(new_verbe)
                    if conj == 'forme potentiel négatif formel':
                        new_verbe = masu_forme[:-1] + 'ねません'
                        row.append(new_verbe)
                    if conj == 'forme passif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'なれる'
                        row.append(new_verbe)
                    if conj == 'forme passif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'なれない'
                        row.append(new_verbe)
                    if conj == 'forme passif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'なれます'
                        row.append(new_verbe)
                    if conj == 'forme passif négatif formel':
                        new_verbe = masu_forme[:-1] + 'なれません'
                        row.append(new_verbe)
                    if conj == 'forme causatif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'なせる'
                        row.append(new_verbe)
                    if conj == 'forme causatif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'なせない'
                        row.append(new_verbe)
                    if conj == 'forme causatif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'なせます'
                        row.append(new_verbe)
                    if conj == 'forme causatif négatif formel':
                        new_verbe = masu_forme[:-1] + 'なせません'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'なせられる'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'なせられない'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'なせられます'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif négatif formel':
                        new_verbe = masu_forme[:-1] + 'なせられません'
                        row.append(new_verbe)
                    if conj == 'forme volutive affirmatif neutre':
                        new_verbe = masu_forme + 'たい'
                        row.append(new_verbe)
                    if conj == 'forme volutive négatif neutre':
                        new_verbe = masu_forme + 'たくない'
                        row.append(new_verbe)
                    if conj == 'forme volutive affirmatif formel':
                        new_verbe = masu_forme + 'たかった'
                        row.append(new_verbe)
                    if conj == 'forme volutive négatif formel':
                        new_verbe = masu_forme + 'たくなかった'
                        row.append(new_verbe)
                    if conj == 'forme conjecturale neutre':
                        new_verbe = masu_forme[:-1] + 'のう'
                        row.append(new_verbe)
                    if conj == 'forme conjecturale formel':
                        new_verbe = masu_forme + 'ましょう'
                        row.append(new_verbe)
                    if conj == 'forme conditionnel neutre':
                        new_verbe = masu_forme[:-1] + 'ねば'
                        row.append(new_verbe)
                    if conj == 'forme conditionnel négatif':
                        new_verbe = masu_forme[:-1] + 'ななければ'
                        row.append(new_verbe)
                    if conj == 'impératif affirmatif':
                        new_verbe = masu_forme[:-1] + 'ね'
                        row.append(new_verbe)
                    if conj == 'impératif négatif':
                        new_verbe = masu_forme[:-1] + 'ぬな'
                        row.append(new_verbe)
                    if conj == 'radical - masu-forme': 
                        #radical masu-form
                        row.append(masu_forme)
                    if conj == 'tara':
                        new_verbe = masu_forme[:-1] + 'んだら'
                        row.append(new_verbe)
                    if conj == 'zu':
                        new_verbe = masu_forme[:-1] + 'なず'
                        row.append(new_verbe)
                    if conj == 'kucha':
                        new_verbe = masu_forme[:-1] + 'ななくちゃ'
                        row.append(new_verbe)
                    if conj == 'kya':
                        new_verbe = masu_forme[:-1] + 'ななきゃ'
                        row.append(new_verbe)

                else:
                    row.append('')
                row.append(conj)
                row.append(verbe_kanji_neutre)
                row.append(verbe_kana_neutre)
                row.append(verbe_trad)
                
                rows.append(row)


        if end_verbe == "い":
            for conj in all_conj_verbe:
                row = [type_verbe]
                if verbe_kanji != '':
                    masu_forme = verbe_kanji
                    if conj == 'présent affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'う'
                        row.append(new_verbe)
                        verbe_kanji_neutre = new_verbe
                    if conj == 'présent négatif neutre':
                        new_verbe = masu_forme[:-1] + 'わない'
                        row.append(new_verbe)
                    if conj == 'passé affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'った'
                        row.append(new_verbe)
                    if conj == 'passé négatif neutre':
                        new_verbe = masu_forme[:-1] + 'わなかった'
                        row.append(new_verbe)
                    if conj == 'présent affirmatif formel':
                        new_verbe = masu_forme + 'ます'
                        row.append(new_verbe)
                    if conj == 'présent négatif formel':
                        new_verbe = masu_forme + 'ません'
                        row.append(new_verbe)
                    if conj == 'passé affirmatif formel':
                        new_verbe = masu_forme + 'ました'
                        row.append(new_verbe)
                    if conj == 'passé négatif formel':
                        new_verbe = masu_forme + 'ませんでした'
                        row.append(new_verbe)
                    if conj == 'forme en て　affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'って'
                        row.append(new_verbe)
                    if conj == 'forme en て　négatif neutre':
                        new_verbe = masu_forme[:-1] + 'わなくて'
                        row.append(new_verbe)
                    if conj == 'forme en て　affirmatif formel':
                        new_verbe = masu_forme + 'まして'
                        row.append(new_verbe)
                    if conj == 'forme potentiel affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'える'
                        row.append(new_verbe)
                    if conj == 'forme potentiel négatif neutre':
                        new_verbe = masu_forme[:-1] + 'えない'
                        row.append(new_verbe)
                    if conj == 'forme potentiel affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'えます'
                        row.append(new_verbe)
                    if conj == 'forme potentiel négatif formel':
                        new_verbe = masu_forme[:-1] + 'えません'
                        row.append(new_verbe)
                    if conj == 'forme passif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'われる'
                        row.append(new_verbe)
                    if conj == 'forme passif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'われない'
                        row.append(new_verbe)
                    if conj == 'forme passif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'われます'
                        row.append(new_verbe)
                    if conj == 'forme passif négatif formel':
                        new_verbe = masu_forme[:-1] + 'われません'
                        row.append(new_verbe)
                    if conj == 'forme causatif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'わせる'
                        row.append(new_verbe)
                    if conj == 'forme causatif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'わせない'
                        row.append(new_verbe)
                    if conj == 'forme causatif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'わせます'
                        row.append(new_verbe)
                    if conj == 'forme causatif négatif formel':
                        new_verbe = masu_forme[:-1] + 'わせません'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'わせられる'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'わせられない'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'わせられます'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif négatif formel':
                        new_verbe = masu_forme[:-1] + 'わせられません'
                        row.append(new_verbe)
                    if conj == 'forme volutive affirmatif neutre':
                        new_verbe = masu_forme + 'たい'
                        row.append(new_verbe)
                    if conj == 'forme volutive négatif neutre':
                        new_verbe = masu_forme + 'たくない'
                        row.append(new_verbe)
                    if conj == 'forme volutive affirmatif formel':
                        new_verbe = masu_forme + 'たかった'
                        row.append(new_verbe)
                    if conj == 'forme volutive négatif formel':
                        new_verbe = masu_forme + 'たくなかった'
                        row.append(new_verbe)
                    if conj == 'forme conjecturale neutre':
                        new_verbe = masu_forme[:-1] + 'おう'
                        row.append(new_verbe)
                    if conj == 'forme conjecturale formel':
                        new_verbe = masu_forme + 'ましょう'
                        row.append(new_verbe)
                    if conj == 'forme conditionnel neutre':
                        new_verbe = masu_forme[:-1] + 'えば'
                        row.append(new_verbe)
                    if conj == 'forme conditionnel négatif':
                        new_verbe = masu_forme[:-1] + 'わなければ'
                        row.append(new_verbe)
                    if conj == 'impératif affirmatif':
                        new_verbe = masu_forme[:-1] + 'え'
                        row.append(new_verbe)
                    if conj == 'impératif négatif':
                        new_verbe = masu_forme[:-1] + 'うな'
                        row.append(new_verbe)
                    if conj == 'radical - masu-forme': 
                        #radical masu-form
                        row.append(masu_forme)
                    if conj == 'tara':
                        new_verbe = masu_forme[:-1] + 'ったら'
                        row.append(new_verbe)
                    if conj == 'zu':
                        new_verbe = masu_forme[:-1] + 'わず'
                        row.append(new_verbe)
                    if conj == 'kucha':
                        new_verbe = masu_forme[:-1] + 'わなくちゃ'
                        row.append(new_verbe)
                    if conj == 'kya':
                        new_verbe = masu_forme[:-1] + 'わなきゃ'
                        row.append(new_verbe)
                else:
                    row.append('')
                    
                if verbe_kana != '':
                    masu_forme = verbe_kana
                    if conj == 'présent affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'う'
                        row.append(new_verbe)
                        verbe_kana_neutre = new_verbe
                    if conj == 'présent négatif neutre':
                        new_verbe = masu_forme[:-1] + 'わない'
                        row.append(new_verbe)
                    if conj == 'passé affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'った'
                        row.append(new_verbe)
                    if conj == 'passé négatif neutre':
                        new_verbe = masu_forme[:-1] + 'わなかった'
                        row.append(new_verbe)
                    if conj == 'présent affirmatif formel':
                        new_verbe = masu_forme + 'ます'
                        row.append(new_verbe)
                    if conj == 'présent négatif formel':
                        new_verbe = masu_forme + 'ません'
                        row.append(new_verbe)
                    if conj == 'passé affirmatif formel':
                        new_verbe = masu_forme + 'ました'
                        row.append(new_verbe)
                    if conj == 'passé négatif formel':
                        new_verbe = masu_forme + 'ませんでした'
                        row.append(new_verbe)
                    if conj == 'forme en て　affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'って'
                        row.append(new_verbe)
                    if conj == 'forme en て　négatif neutre':
                        new_verbe = masu_forme[:-1] + 'わなくて'
                        row.append(new_verbe)
                    if conj == 'forme en て　affirmatif formel':
                        new_verbe = masu_forme + 'まして'
                        row.append(new_verbe)
                    if conj == 'forme potentiel affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'える'
                        row.append(new_verbe)
                    if conj == 'forme potentiel négatif neutre':
                        new_verbe = masu_forme[:-1] + 'えない'
                        row.append(new_verbe)
                    if conj == 'forme potentiel affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'えます'
                        row.append(new_verbe)
                    if conj == 'forme potentiel négatif formel':
                        new_verbe = masu_forme[:-1] + 'えません'
                        row.append(new_verbe)
                    if conj == 'forme passif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'われる'
                        row.append(new_verbe)
                    if conj == 'forme passif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'われない'
                        row.append(new_verbe)
                    if conj == 'forme passif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'われます'
                        row.append(new_verbe)
                    if conj == 'forme passif négatif formel':
                        new_verbe = masu_forme[:-1] + 'われません'
                        row.append(new_verbe)
                    if conj == 'forme causatif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'わせる'
                        row.append(new_verbe)
                    if conj == 'forme causatif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'わせない'
                        row.append(new_verbe)
                    if conj == 'forme causatif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'わせます'
                        row.append(new_verbe)
                    if conj == 'forme causatif négatif formel':
                        new_verbe = masu_forme[:-1] + 'わせません'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'わせられる'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'わせられない'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'わせられます'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif négatif formel':
                        new_verbe = masu_forme[:-1] + 'わせられません'
                        row.append(new_verbe)
                    if conj == 'forme volutive affirmatif neutre':
                        new_verbe = masu_forme + 'たい'
                        row.append(new_verbe)
                    if conj == 'forme volutive négatif neutre':
                        new_verbe = masu_forme + 'たくない'
                        row.append(new_verbe)
                    if conj == 'forme volutive affirmatif formel':
                        new_verbe = masu_forme + 'たかった'
                        row.append(new_verbe)
                    if conj == 'forme volutive négatif formel':
                        new_verbe = masu_forme + 'たくなかった'
                        row.append(new_verbe)
                    if conj == 'forme conjecturale neutre':
                        new_verbe = masu_forme[:-1] + 'おう'
                        row.append(new_verbe)
                    if conj == 'forme conjecturale formel':
                        new_verbe = masu_forme + 'ましょう'
                        row.append(new_verbe)
                    if conj == 'forme conditionnel neutre':
                        new_verbe = masu_forme[:-1] + 'えば'
                        row.append(new_verbe)
                    if conj == 'forme conditionnel négatif':
                        new_verbe = masu_forme[:-1] + 'わなければ'
                        row.append(new_verbe)
                    if conj == 'impératif affirmatif':
                        new_verbe = masu_forme[:-1] + 'え'
                        row.append(new_verbe)
                    if conj == 'impératif négatif':
                        new_verbe = masu_forme[:-1] + 'うな'
                        row.append(new_verbe)
                    if conj == 'radical - masu-forme': 
                        #radical masu-form
                        row.append(masu_forme)
                    if conj == 'tara':
                        new_verbe = masu_forme[:-1] + 'ったら'
                        row.append(new_verbe)
                    if conj == 'zu':
                        new_verbe = masu_forme[:-1] + 'わず'
                        row.append(new_verbe)
                    if conj == 'kucha':
                        new_verbe = masu_forme[:-1] + 'わなくちゃ'
                        row.append(new_verbe)
                    if conj == 'kya':
                        new_verbe = masu_forme[:-1] + 'わなきゃ'
                        row.append(new_verbe)
                                
                else:
                    row.append('')
                row.append(conj)
                row.append(verbe_kanji_neutre)
                row.append(verbe_kana_neutre)
                row.append(verbe_trad)
                
                rows.append(row)

        if end_verbe == "し":
            for conj in all_conj_verbe:
                row = [type_verbe]
                if verbe_kanji != '':
                    masu_forme = verbe_kanji
                    if conj == 'présent affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'す'
                        row.append(new_verbe)
                        verbe_kanji_neutre = new_verbe
                    if conj == 'présent négatif neutre':
                        new_verbe = masu_forme[:-1] + 'さない'
                        row.append(new_verbe)
                    if conj == 'passé affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'した'
                        row.append(new_verbe)
                    if conj == 'passé négatif neutre':
                        new_verbe = masu_forme[:-1] + 'さなかった'
                        row.append(new_verbe)
                    if conj == 'présent affirmatif formel':
                        new_verbe = masu_forme + 'ます'
                        row.append(new_verbe)
                    if conj == 'présent négatif formel':
                        new_verbe = masu_forme + 'ません'
                        row.append(new_verbe)
                    if conj == 'passé affirmatif formel':
                        new_verbe = masu_forme + 'ました'
                        row.append(new_verbe)
                    if conj == 'passé négatif formel':
                        new_verbe = masu_forme + 'ませんでした'
                        row.append(new_verbe)
                    if conj == 'forme en て　affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'して'
                        row.append(new_verbe)
                    if conj == 'forme en て　négatif neutre':
                        new_verbe = masu_forme[:-1] + 'さなくて'
                        row.append(new_verbe)
                    if conj == 'forme en て　affirmatif formel':
                        new_verbe = masu_forme + 'まして'
                        row.append(new_verbe)
                    if conj == 'forme potentiel affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'せる'
                        row.append(new_verbe)
                    if conj == 'forme potentiel négatif neutre':
                        new_verbe = masu_forme[:-1] + 'せない'
                        row.append(new_verbe)
                    if conj == 'forme potentiel affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'せます'
                        row.append(new_verbe)
                    if conj == 'forme potentiel négatif formel':
                        new_verbe = masu_forme[:-1] + 'せません'
                        row.append(new_verbe)
                    if conj == 'forme passif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'される'
                        row.append(new_verbe)
                    if conj == 'forme passif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'されない'
                        row.append(new_verbe)
                    if conj == 'forme passif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'されます'
                        row.append(new_verbe)
                    if conj == 'forme passif négatif formel':
                        new_verbe = masu_forme[:-1] + 'されません'
                        row.append(new_verbe)
                    if conj == 'forme causatif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'させる'
                        row.append(new_verbe)
                    if conj == 'forme causatif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'させない'
                        row.append(new_verbe)
                    if conj == 'forme causatif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'させます'
                        row.append(new_verbe)
                    if conj == 'forme causatif négatif formel':
                        new_verbe = masu_forme[:-1] + 'させません'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'させられる'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'させられない'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'させられます'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif négatif formel':
                        new_verbe = masu_forme[:-1] + 'させられません'
                        row.append(new_verbe)
                    if conj == 'forme volutive affirmatif neutre':
                        new_verbe = masu_forme + 'たい'
                        row.append(new_verbe)
                    if conj == 'forme volutive négatif neutre':
                        new_verbe = masu_forme + 'たくない'
                        row.append(new_verbe)
                    if conj == 'forme volutive affirmatif formel':
                        new_verbe = masu_forme + 'たかった'
                        row.append(new_verbe)
                    if conj == 'forme volutive négatif formel':
                        new_verbe = masu_forme + 'たくなかった'
                        row.append(new_verbe)
                    if conj == 'forme conjecturale neutre':
                        new_verbe = masu_forme[:-1] + 'そう'
                        row.append(new_verbe)
                    if conj == 'forme conjecturale formel':
                        new_verbe = masu_forme + 'ましょう'
                        row.append(new_verbe)
                    if conj == 'forme conditionnel neutre':
                        new_verbe = masu_forme[:-1] + 'せば'
                        row.append(new_verbe)
                    if conj == 'forme conditionnel négatif':
                        new_verbe = masu_forme[:-1] + 'さなければ'
                        row.append(new_verbe)
                    if conj == 'impératif affirmatif':
                        new_verbe = masu_forme[:-1] + 'せ'
                        row.append(new_verbe)
                    if conj == 'impératif négatif':
                        new_verbe = masu_forme[:-1] + 'すな'
                        row.append(new_verbe)
                    if conj == 'radical - masu-forme': 
                        #radical masu-form
                        row.append(masu_forme)
                    if conj == 'tara':
                        new_verbe = masu_forme[:-1] + 'したら'
                        row.append(new_verbe)
                    if conj == 'zu':
                        new_verbe = masu_forme[:-1] + 'さず'
                        row.append(new_verbe)
                    if conj == 'kucha':
                        new_verbe = masu_forme[:-1] + 'さなくちゃ'
                        row.append(new_verbe)
                    if conj == 'kya':
                        new_verbe = masu_forme[:-1] + 'さなきゃ'
                        row.append(new_verbe)
                else:
                    row.append('')
                    
                if verbe_kana != '':
                    masu_forme = verbe_kana
                    if conj == 'présent affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'す'
                        row.append(new_verbe)
                        verbe_kana_neutre = new_verbe
                    if conj == 'présent négatif neutre':
                        new_verbe = masu_forme[:-1] + 'さない'
                        row.append(new_verbe)
                    if conj == 'passé affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'した'
                        row.append(new_verbe)
                    if conj == 'passé négatif neutre':
                        new_verbe = masu_forme[:-1] + 'さなかった'
                        row.append(new_verbe)
                    if conj == 'présent affirmatif formel':
                        new_verbe = masu_forme + 'ます'
                        row.append(new_verbe)
                    if conj == 'présent négatif formel':
                        new_verbe = masu_forme + 'ません'
                        row.append(new_verbe)
                    if conj == 'passé affirmatif formel':
                        new_verbe = masu_forme + 'ました'
                        row.append(new_verbe)
                    if conj == 'passé négatif formel':
                        new_verbe = masu_forme + 'ませんでした'
                        row.append(new_verbe)
                    if conj == 'forme en て　affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'して'
                        row.append(new_verbe)
                    if conj == 'forme en て　négatif neutre':
                        new_verbe = masu_forme[:-1] + 'さなくて'
                        row.append(new_verbe)
                    if conj == 'forme en て　affirmatif formel':
                        new_verbe = masu_forme + 'まして'
                        row.append(new_verbe)
                    if conj == 'forme potentiel affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'せる'
                        row.append(new_verbe)
                    if conj == 'forme potentiel négatif neutre':
                        new_verbe = masu_forme[:-1] + 'せない'
                        row.append(new_verbe)
                    if conj == 'forme potentiel affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'せます'
                        row.append(new_verbe)
                    if conj == 'forme potentiel négatif formel':
                        new_verbe = masu_forme[:-1] + 'せません'
                        row.append(new_verbe)
                    if conj == 'forme passif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'される'
                        row.append(new_verbe)
                    if conj == 'forme passif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'されない'
                        row.append(new_verbe)
                    if conj == 'forme passif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'されます'
                        row.append(new_verbe)
                    if conj == 'forme passif négatif formel':
                        new_verbe = masu_forme[:-1] + 'されません'
                        row.append(new_verbe)
                    if conj == 'forme causatif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'させる'
                        row.append(new_verbe)
                    if conj == 'forme causatif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'させない'
                        row.append(new_verbe)
                    if conj == 'forme causatif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'させます'
                        row.append(new_verbe)
                    if conj == 'forme causatif négatif formel':
                        new_verbe = masu_forme[:-1] + 'させません'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'させられる'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'させられない'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'させられます'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif négatif formel':
                        new_verbe = masu_forme[:-1] + 'させられません'
                        row.append(new_verbe)
                    if conj == 'forme volutive affirmatif neutre':
                        new_verbe = masu_forme + 'たい'
                        row.append(new_verbe)
                    if conj == 'forme volutive négatif neutre':
                        new_verbe = masu_forme + 'たくない'
                        row.append(new_verbe)
                    if conj == 'forme volutive affirmatif formel':
                        new_verbe = masu_forme + 'たかった'
                        row.append(new_verbe)
                    if conj == 'forme volutive négatif formel':
                        new_verbe = masu_forme + 'たくなかった'
                        row.append(new_verbe)
                    if conj == 'forme conjecturale neutre':
                        new_verbe = masu_forme[:-1] + 'そう'
                        row.append(new_verbe)
                    if conj == 'forme conjecturale formel':
                        new_verbe = masu_forme + 'ましょう'
                        row.append(new_verbe)
                    if conj == 'forme conditionnel neutre':
                        new_verbe = masu_forme[:-1] + 'せば'
                        row.append(new_verbe)
                    if conj == 'forme conditionnel négatif':
                        new_verbe = masu_forme[:-1] + 'さなければ'
                        row.append(new_verbe)
                    if conj == 'impératif affirmatif':
                        new_verbe = masu_forme[:-1] + 'せ'
                        row.append(new_verbe)
                    if conj == 'impératif négatif':
                        new_verbe = masu_forme[:-1] + 'すな'
                        row.append(new_verbe)
                    if conj == 'radical - masu-forme': 
                        #radical masu-form
                        row.append(masu_forme)
                    if conj == 'tara':
                        new_verbe = masu_forme[:-1] + 'したら'
                        row.append(new_verbe)
                    if conj == 'zu':
                        new_verbe = masu_forme[:-1] + 'さず'
                        row.append(new_verbe)
                    if conj == 'kucha':
                        new_verbe = masu_forme[:-1] + 'さなくちゃ'
                        row.append(new_verbe)
                    if conj == 'kya':
                        new_verbe = masu_forme[:-1] + 'さなきゃ'
                        row.append(new_verbe)
                else:
                    row.append('')
                row.append(conj)
                row.append(verbe_kanji_neutre)
                row.append(verbe_kana_neutre)
                row.append(verbe_trad)
                
                rows.append(row)
                
        if end_verbe == "り":
            for conj in all_conj_verbe:
                row = [type_verbe]
                if verbe_kanji != '':
                    masu_forme = verbe_kanji
                    if conj == 'présent affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'る'
                        row.append(new_verbe)
                        verbe_kanji_neutre = new_verbe
                    if conj == 'présent négatif neutre':
                        new_verbe = masu_forme[:-1] + 'らない'
                        row.append(new_verbe)
                    if conj == 'passé affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'った'
                        row.append(new_verbe)
                    if conj == 'passé négatif neutre':
                        new_verbe = masu_forme[:-1] + 'らなかった'
                        row.append(new_verbe)
                    if conj == 'présent affirmatif formel':
                        new_verbe = masu_forme + 'ます'
                        row.append(new_verbe)
                    if conj == 'présent négatif formel':
                        new_verbe = masu_forme + 'ません'
                        row.append(new_verbe)
                    if conj == 'passé affirmatif formel':
                        new_verbe = masu_forme + 'ました'
                        row.append(new_verbe)
                    if conj == 'passé négatif formel':
                        new_verbe = masu_forme + 'ませんでした'
                        row.append(new_verbe)
                    if conj == 'forme en て　affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'って'
                        row.append(new_verbe)
                    if conj == 'forme en て　négatif neutre':
                        new_verbe = masu_forme[:-1] + 'らなくて'
                        row.append(new_verbe)
                    if conj == 'forme en て　affirmatif formel':
                        new_verbe = masu_forme + 'まして'
                        row.append(new_verbe)
                    if conj == 'forme potentiel affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'れる'
                        row.append(new_verbe)
                    if conj == 'forme potentiel négatif neutre':
                        new_verbe = masu_forme[:-1] + 'れない'
                        row.append(new_verbe)
                    if conj == 'forme potentiel affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'れます'
                        row.append(new_verbe)
                    if conj == 'forme potentiel négatif formel':
                        new_verbe = masu_forme[:-1] + 'れません'
                        row.append(new_verbe)
                    if conj == 'forme passif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'られる'
                        row.append(new_verbe)
                    if conj == 'forme passif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'られない'
                        row.append(new_verbe)
                    if conj == 'forme passif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'られます'
                        row.append(new_verbe)
                    if conj == 'forme passif négatif formel':
                        new_verbe = masu_forme[:-1] + 'られません'
                        row.append(new_verbe)
                    if conj == 'forme causatif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'らせる'
                        row.append(new_verbe)
                    if conj == 'forme causatif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'らせない'
                        row.append(new_verbe)
                    if conj == 'forme causatif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'らせます'
                        row.append(new_verbe)
                    if conj == 'forme causatif négatif formel':
                        new_verbe = masu_forme[:-1] + 'らせません'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'らせられる'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'らせられない'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'らせられます'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif négatif formel':
                        new_verbe = masu_forme[:-1] + 'らせられません'
                        row.append(new_verbe)
                    if conj == 'forme volutive affirmatif neutre':
                        new_verbe = masu_forme + 'たい'
                        row.append(new_verbe)
                    if conj == 'forme volutive négatif neutre':
                        new_verbe = masu_forme + 'たくない'
                        row.append(new_verbe)
                    if conj == 'forme volutive affirmatif formel':
                        new_verbe = masu_forme + 'たかった'
                        row.append(new_verbe)
                    if conj == 'forme volutive négatif formel':
                        new_verbe = masu_forme + 'たくなかった'
                        row.append(new_verbe)
                    if conj == 'forme conjecturale neutre':
                        new_verbe = masu_forme[:-1] + 'ろう'
                        row.append(new_verbe)
                    if conj == 'forme conjecturale formel':
                        new_verbe = masu_forme + 'ましょう'
                        row.append(new_verbe)
                    if conj == 'forme conditionnel neutre':
                        new_verbe = masu_forme[:-1] + 'れば'
                        row.append(new_verbe)
                    if conj == 'forme conditionnel négatif':
                        new_verbe = masu_forme[:-1] + 'らなければ'
                        row.append(new_verbe)
                    if conj == 'impératif affirmatif':
                        new_verbe = masu_forme[:-1] + 'れ'
                        row.append(new_verbe)
                    if conj == 'impératif négatif':
                        new_verbe = masu_forme[:-1] + 'るな'
                        row.append(new_verbe)
                    if conj == 'radical - masu-forme': 
                        #radical masu-form
                        row.append(masu_forme)
                    if conj == 'tara':
                        new_verbe = masu_forme[:-1] + 'ったら'
                        row.append(new_verbe)
                    if conj == 'zu':
                        new_verbe = masu_forme[:-1] + 'らず'
                        row.append(new_verbe)
                    if conj == 'kucha':
                        new_verbe = masu_forme[:-1] + 'らなくちゃ'
                        row.append(new_verbe)
                    if conj == 'kya':
                        new_verbe = masu_forme[:-1] + 'らなきゃ'
                        row.append(new_verbe)
                else:
                    row.append('')
                    
                if verbe_kana != '':
                    masu_forme = verbe_kana
                    if conj == 'présent affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'る'
                        row.append(new_verbe)
                        verbe_kana_neutre = new_verbe
                    if conj == 'présent négatif neutre':
                        new_verbe = masu_forme[:-1] + 'らない'
                        row.append(new_verbe)
                    if conj == 'passé affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'った'
                        row.append(new_verbe)
                    if conj == 'passé négatif neutre':
                        new_verbe = masu_forme[:-1] + 'らなかった'
                        row.append(new_verbe)
                    if conj == 'présent affirmatif formel':
                        new_verbe = masu_forme + 'ます'
                        row.append(new_verbe)
                    if conj == 'présent négatif formel':
                        new_verbe = masu_forme + 'ません'
                        row.append(new_verbe)
                    if conj == 'passé affirmatif formel':
                        new_verbe = masu_forme + 'ました'
                        row.append(new_verbe)
                    if conj == 'passé négatif formel':
                        new_verbe = masu_forme + 'ませんでした'
                        row.append(new_verbe)
                    if conj == 'forme en て　affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'って'
                        row.append(new_verbe)
                    if conj == 'forme en て　négatif neutre':
                        new_verbe = masu_forme[:-1] + 'らなくて'
                        row.append(new_verbe)
                    if conj == 'forme en て　affirmatif formel':
                        new_verbe = masu_forme + 'まして'
                        row.append(new_verbe)
                    if conj == 'forme potentiel affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'れる'
                        row.append(new_verbe)
                    if conj == 'forme potentiel négatif neutre':
                        new_verbe = masu_forme[:-1] + 'れない'
                        row.append(new_verbe)
                    if conj == 'forme potentiel affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'れます'
                        row.append(new_verbe)
                    if conj == 'forme potentiel négatif formel':
                        new_verbe = masu_forme[:-1] + 'れません'
                        row.append(new_verbe)
                    if conj == 'forme passif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'られる'
                        row.append(new_verbe)
                    if conj == 'forme passif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'られない'
                        row.append(new_verbe)
                    if conj == 'forme passif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'られます'
                        row.append(new_verbe)
                    if conj == 'forme passif négatif formel':
                        new_verbe = masu_forme[:-1] + 'られません'
                        row.append(new_verbe)
                    if conj == 'forme causatif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'らせる'
                        row.append(new_verbe)
                    if conj == 'forme causatif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'らせない'
                        row.append(new_verbe)
                    if conj == 'forme causatif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'らせます'
                        row.append(new_verbe)
                    if conj == 'forme causatif négatif formel':
                        new_verbe = masu_forme[:-1] + 'らせません'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'らせられる'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'らせられない'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'らせられます'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif négatif formel':
                        new_verbe = masu_forme[:-1] + 'らせられません'
                        row.append(new_verbe)
                    if conj == 'forme volutive affirmatif neutre':
                        new_verbe = masu_forme + 'たい'
                        row.append(new_verbe)
                    if conj == 'forme volutive négatif neutre':
                        new_verbe = masu_forme + 'たくない'
                        row.append(new_verbe)
                    if conj == 'forme volutive affirmatif formel':
                        new_verbe = masu_forme + 'たかった'
                        row.append(new_verbe)
                    if conj == 'forme volutive négatif formel':
                        new_verbe = masu_forme + 'たくなかった'
                        row.append(new_verbe)
                    if conj == 'forme conjecturale neutre':
                        new_verbe = masu_forme[:-1] + 'ろう'
                        row.append(new_verbe)
                    if conj == 'forme conjecturale formel':
                        new_verbe = masu_forme + 'ましょう'
                        row.append(new_verbe)
                    if conj == 'forme conditionnel neutre':
                        new_verbe = masu_forme[:-1] + 'れば'
                        row.append(new_verbe)
                    if conj == 'forme conditionnel négatif':
                        new_verbe = masu_forme[:-1] + 'らなければ'
                        row.append(new_verbe)
                    if conj == 'impératif affirmatif':
                        new_verbe = masu_forme[:-1] + 'れ'
                        row.append(new_verbe)
                    if conj == 'impératif négatif':
                        new_verbe = masu_forme[:-1] + 'るな'
                        row.append(new_verbe)
                    if conj == 'radical - masu-forme': 
                        #radical masu-form
                        row.append(masu_forme)
                    if conj == 'tara':
                        new_verbe = masu_forme[:-1] + 'ったら'
                        row.append(new_verbe)
                    if conj == 'zu':
                        new_verbe = masu_forme[:-1] + 'らず'
                        row.append(new_verbe)
                    if conj == 'kucha':
                        new_verbe = masu_forme[:-1] + 'らなくちゃ'
                        row.append(new_verbe)
                    if conj == 'kya':
                        new_verbe = masu_forme[:-1] + 'らなきゃ'
                        row.append(new_verbe)
  
                else:
                    row.append('')
                row.append(conj)
                row.append(verbe_kanji_neutre)
                row.append(verbe_kana_neutre)
                row.append(verbe_trad)
                
                rows.append(row)
                

        if end_verbe == "び":
            for conj in all_conj_verbe:
                row = [type_verbe]
                if verbe_kanji != '':
                    masu_forme = verbe_kanji
                    if conj == 'présent affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'ぶ'
                        row.append(new_verbe)
                        verbe_kanji_neutre = new_verbe
                    if conj == 'présent négatif neutre':
                        new_verbe = masu_forme[:-1] + 'ばない'
                        row.append(new_verbe)
                    if conj == 'passé affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'んだ'
                        row.append(new_verbe)
                    if conj == 'passé négatif neutre':
                        new_verbe = masu_forme[:-1] + 'ばなかった'
                        row.append(new_verbe)
                    if conj == 'présent affirmatif formel':
                        new_verbe = masu_forme + 'ます'
                        row.append(new_verbe)
                    if conj == 'présent négatif formel':
                        new_verbe = masu_forme + 'ません'
                        row.append(new_verbe)
                    if conj == 'passé affirmatif formel':
                        new_verbe = masu_forme + 'ました'
                        row.append(new_verbe)
                    if conj == 'passé négatif formel':
                        new_verbe = masu_forme + 'ませんでした'
                        row.append(new_verbe)
                    if conj == 'forme en て　affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'んで'
                        row.append(new_verbe)
                    if conj == 'forme en て　négatif neutre':
                        new_verbe = masu_forme[:-1] + 'ばなくて'
                        row.append(new_verbe)
                    if conj == 'forme en て　affirmatif formel':
                        new_verbe = masu_forme + 'まして'
                        row.append(new_verbe)
                    if conj == 'forme potentiel affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'べる'
                        row.append(new_verbe)
                    if conj == 'forme potentiel négatif neutre':
                        new_verbe = masu_forme[:-1] + 'べない'
                        row.append(new_verbe)
                    if conj == 'forme potentiel affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'べます'
                        row.append(new_verbe)
                    if conj == 'forme potentiel négatif formel':
                        new_verbe = masu_forme[:-1] + 'べません'
                        row.append(new_verbe)
                    if conj == 'forme passif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'ばれる'
                        row.append(new_verbe)
                    if conj == 'forme passif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'ばれない'
                        row.append(new_verbe)
                    if conj == 'forme passif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'ばれます'
                        row.append(new_verbe)
                    if conj == 'forme passif négatif formel':
                        new_verbe = masu_forme[:-1] + 'ばれません'
                        row.append(new_verbe)
                    if conj == 'forme causatif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'ばせる'
                        row.append(new_verbe)
                    if conj == 'forme causatif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'ばせない'
                        row.append(new_verbe)
                    if conj == 'forme causatif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'ばせます'
                        row.append(new_verbe)
                    if conj == 'forme causatif négatif formel':
                        new_verbe = masu_forme[:-1] + 'ばせません'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'ばせられる'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'ばせられない'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'ばせられます'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif négatif formel':
                        new_verbe = masu_forme[:-1] + 'ばせられません'
                        row.append(new_verbe)
                    if conj == 'forme volutive affirmatif neutre':
                        new_verbe = masu_forme + 'たい'
                        row.append(new_verbe)
                    if conj == 'forme volutive négatif neutre':
                        new_verbe = masu_forme + 'たくない'
                        row.append(new_verbe)
                    if conj == 'forme volutive affirmatif formel':
                        new_verbe = masu_forme + 'たかった'
                        row.append(new_verbe)
                    if conj == 'forme volutive négatif formel':
                        new_verbe = masu_forme + 'たくなかった'
                        row.append(new_verbe)
                    if conj == 'forme conjecturale neutre':
                        new_verbe = masu_forme[:-1] + 'ぼう'
                        row.append(new_verbe)
                    if conj == 'forme conjecturale formel':
                        new_verbe = masu_forme + 'ましょう'
                        row.append(new_verbe)
                    if conj == 'forme conditionnel neutre':
                        new_verbe = masu_forme[:-1] + 'べば'
                        row.append(new_verbe)
                    if conj == 'forme conditionnel négatif':
                        new_verbe = masu_forme[:-1] + 'ばなければ'
                        row.append(new_verbe)
                    if conj == 'impératif affirmatif':
                        new_verbe = masu_forme[:-1] + 'べ'
                        row.append(new_verbe)
                    if conj == 'impératif négatif':
                        new_verbe = masu_forme[:-1] + 'ぶな'
                        row.append(new_verbe)
                    if conj == 'radical - masu-forme': 
                        #radical masu-form
                        row.append(masu_forme)
                    if conj == 'tara':
                        new_verbe = masu_forme[:-1] + 'んだら'
                        row.append(new_verbe)
                    if conj == 'zu':
                        new_verbe = masu_forme[:-1] + 'ばず'
                        row.append(new_verbe)
                    if conj == 'kucha':
                        new_verbe = masu_forme[:-1] + 'ばなくちゃ'
                        row.append(new_verbe)
                    if conj == 'kya':
                        new_verbe = masu_forme[:-1] + 'ばなきゃ'
                        row.append(new_verbe)
                else:
                    row.append('')
                    
                if verbe_kana != '':
                    masu_forme = verbe_kana
                    if conj == 'présent affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'ぶ'
                        row.append(new_verbe)
                        verbe_kana_neutre = new_verbe
                    if conj == 'présent négatif neutre':
                        new_verbe = masu_forme[:-1] + 'ばない'
                        row.append(new_verbe)
                    if conj == 'passé affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'んだ'
                        row.append(new_verbe)
                    if conj == 'passé négatif neutre':
                        new_verbe = masu_forme[:-1] + 'ばなかった'
                        row.append(new_verbe)
                    if conj == 'présent affirmatif formel':
                        new_verbe = masu_forme + 'ます'
                        row.append(new_verbe)
                    if conj == 'présent négatif formel':
                        new_verbe = masu_forme + 'ません'
                        row.append(new_verbe)
                    if conj == 'passé affirmatif formel':
                        new_verbe = masu_forme + 'ました'
                        row.append(new_verbe)
                    if conj == 'passé négatif formel':
                        new_verbe = masu_forme + 'ませんでした'
                        row.append(new_verbe)
                    if conj == 'forme en て　affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'んで'
                        row.append(new_verbe)
                    if conj == 'forme en て　négatif neutre':
                        new_verbe = masu_forme[:-1] + 'ばなくて'
                        row.append(new_verbe)
                    if conj == 'forme en て　affirmatif formel':
                        new_verbe = masu_forme + 'まして'
                        row.append(new_verbe)
                    if conj == 'forme potentiel affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'べる'
                        row.append(new_verbe)
                    if conj == 'forme potentiel négatif neutre':
                        new_verbe = masu_forme[:-1] + 'べない'
                        row.append(new_verbe)
                    if conj == 'forme potentiel affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'べます'
                        row.append(new_verbe)
                    if conj == 'forme potentiel négatif formel':
                        new_verbe = masu_forme[:-1] + 'べません'
                        row.append(new_verbe)
                    if conj == 'forme passif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'ばれる'
                        row.append(new_verbe)
                    if conj == 'forme passif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'ばれない'
                        row.append(new_verbe)
                    if conj == 'forme passif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'ばれます'
                        row.append(new_verbe)
                    if conj == 'forme passif négatif formel':
                        new_verbe = masu_forme[:-1] + 'ばれません'
                        row.append(new_verbe)
                    if conj == 'forme causatif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'ばせる'
                        row.append(new_verbe)
                    if conj == 'forme causatif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'ばせない'
                        row.append(new_verbe)
                    if conj == 'forme causatif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'ばせます'
                        row.append(new_verbe)
                    if conj == 'forme causatif négatif formel':
                        new_verbe = masu_forme[:-1] + 'ばせません'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'ばせられる'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'ばせられない'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'ばせられます'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif négatif formel':
                        new_verbe = masu_forme[:-1] + 'ばせられません'
                        row.append(new_verbe)
                    if conj == 'forme volutive affirmatif neutre':
                        new_verbe = masu_forme + 'たい'
                        row.append(new_verbe)
                    if conj == 'forme volutive négatif neutre':
                        new_verbe = masu_forme + 'たくない'
                        row.append(new_verbe)
                    if conj == 'forme volutive affirmatif formel':
                        new_verbe = masu_forme + 'たかった'
                        row.append(new_verbe)
                    if conj == 'forme volutive négatif formel':
                        new_verbe = masu_forme + 'たくなかった'
                        row.append(new_verbe)
                    if conj == 'forme conjecturale neutre':
                        new_verbe = masu_forme[:-1] + 'ぼう'
                        row.append(new_verbe)
                    if conj == 'forme conjecturale formel':
                        new_verbe = masu_forme + 'ましょう'
                        row.append(new_verbe)
                    if conj == 'forme conditionnel neutre':
                        new_verbe = masu_forme[:-1] + 'べば'
                        row.append(new_verbe)
                    if conj == 'forme conditionnel négatif':
                        new_verbe = masu_forme[:-1] + 'ばなければ'
                        row.append(new_verbe)
                    if conj == 'impératif affirmatif':
                        new_verbe = masu_forme[:-1] + 'べ'
                        row.append(new_verbe)
                    if conj == 'impératif négatif':
                        new_verbe = masu_forme[:-1] + 'ぶな'
                        row.append(new_verbe)
                    if conj == 'radical - masu-forme': 
                        #radical masu-form
                        row.append(masu_forme)
                    if conj == 'tara':
                        new_verbe = masu_forme[:-1] + 'んだら'
                        row.append(new_verbe)
                    if conj == 'zu':
                        new_verbe = masu_forme[:-1] + 'ばず'
                        row.append(new_verbe)
                    if conj == 'kucha':
                        new_verbe = masu_forme[:-1] + 'ばなくちゃ'
                        row.append(new_verbe)
                    if conj == 'kya':
                        new_verbe = masu_forme[:-1] + 'ばなきゃ'
                        row.append(new_verbe)
                else:
                    row.append('')
                row.append(conj)
                row.append(verbe_kanji_neutre)
                row.append(verbe_kana_neutre)
                row.append(verbe_trad)
                
                rows.append(row)
 
        if end_verbe == "み":
             for conj in all_conj_verbe:
                row = [type_verbe]
                if verbe_kanji != '':
                    masu_forme = verbe_kanji
                    if conj == 'présent affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'む'
                        row.append(new_verbe)
                        verbe_kanji_neutre = new_verbe
                    if conj == 'présent négatif neutre':
                        new_verbe = masu_forme[:-1] + 'まない'
                        row.append(new_verbe)
                    if conj == 'passé affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'んだ'
                        row.append(new_verbe)
                    if conj == 'passé négatif neutre':
                        new_verbe = masu_forme[:-1] + 'まなかった'
                        row.append(new_verbe)
                    if conj == 'présent affirmatif formel':
                        new_verbe = masu_forme + 'ます'
                        row.append(new_verbe)
                    if conj == 'présent négatif formel':
                        new_verbe = masu_forme + 'ません'
                        row.append(new_verbe)
                    if conj == 'passé affirmatif formel':
                        new_verbe = masu_forme + 'ました'
                        row.append(new_verbe)
                    if conj == 'passé négatif formel':
                        new_verbe = masu_forme + 'ませんでした'
                        row.append(new_verbe)
                    if conj == 'forme en て　affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'んで'
                        row.append(new_verbe)
                    if conj == 'forme en て　négatif neutre':
                        new_verbe = masu_forme[:-1] + 'まなくて'
                        row.append(new_verbe)
                    if conj == 'forme en て　affirmatif formel':
                        new_verbe = masu_forme + 'まして'
                        row.append(new_verbe)
                    if conj == 'forme potentiel affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'める'
                        row.append(new_verbe)
                    if conj == 'forme potentiel négatif neutre':
                        new_verbe = masu_forme[:-1] + 'めない'
                        row.append(new_verbe)
                    if conj == 'forme potentiel affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'めます'
                        row.append(new_verbe)
                    if conj == 'forme potentiel négatif formel':
                        new_verbe = masu_forme[:-1] + 'めません'
                        row.append(new_verbe)
                    if conj == 'forme passif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'まれる'
                        row.append(new_verbe)
                    if conj == 'forme passif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'まれない'
                        row.append(new_verbe)
                    if conj == 'forme passif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'まれます'
                        row.append(new_verbe)
                    if conj == 'forme passif négatif formel':
                        new_verbe = masu_forme[:-1] + 'まれません'
                        row.append(new_verbe)
                    if conj == 'forme causatif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'ませる'
                        row.append(new_verbe)
                    if conj == 'forme causatif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'ませない'
                        row.append(new_verbe)
                    if conj == 'forme causatif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'ませます'
                        row.append(new_verbe)
                    if conj == 'forme causatif négatif formel':
                        new_verbe = masu_forme[:-1] + 'ませません'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'ませられる'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'ませられない'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'ませられます'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif négatif formel':
                        new_verbe = masu_forme[:-1] + 'ませられません'
                        row.append(new_verbe)
                    if conj == 'forme volutive affirmatif neutre':
                        new_verbe = masu_forme + 'たい'
                        row.append(new_verbe)
                    if conj == 'forme volutive négatif neutre':
                        new_verbe = masu_forme + 'たくない'
                        row.append(new_verbe)
                    if conj == 'forme volutive affirmatif formel':
                        new_verbe = masu_forme + 'たかった'
                        row.append(new_verbe)
                    if conj == 'forme volutive négatif formel':
                        new_verbe = masu_forme + 'たくなかった'
                        row.append(new_verbe)
                    if conj == 'forme conjecturale neutre':
                        new_verbe = masu_forme[:-1] + 'もう'
                        row.append(new_verbe)
                    if conj == 'forme conjecturale formel':
                        new_verbe = masu_forme + 'ましょう'
                        row.append(new_verbe)
                    if conj == 'forme conditionnel neutre':
                        new_verbe = masu_forme[:-1] + 'めば'
                        row.append(new_verbe)
                    if conj == 'forme conditionnel négatif':
                        new_verbe = masu_forme[:-1] + 'まなければ'
                        row.append(new_verbe)
                    if conj == 'impératif affirmatif':
                        new_verbe = masu_forme[:-1] + 'め'
                        row.append(new_verbe)
                    if conj == 'impératif négatif':
                        new_verbe = masu_forme[:-1] + 'むな'
                        row.append(new_verbe)
                    if conj == 'radical - masu-forme': 
                        #radical masu-form
                        row.append(masu_forme)
                    if conj == 'tara':
                        new_verbe = masu_forme[:-1] + 'んだら'
                        row.append(new_verbe)
                    if conj == 'zu':
                        new_verbe = masu_forme[:-1] + 'まず'
                        row.append(new_verbe)
                    if conj == 'kucha':
                        new_verbe = masu_forme[:-1] + 'まなくちゃ'
                        row.append(new_verbe)
                    if conj == 'kya':
                        new_verbe = masu_forme[:-1] + 'まなきゃ'
                        row.append(new_verbe)
                else:
                    row.append('')
                    
                if verbe_kana != '':
                    masu_forme = verbe_kana
                    if conj == 'présent affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'む'
                        row.append(new_verbe)
                        verbe_kana_neutre = new_verbe
                    if conj == 'présent négatif neutre':
                        new_verbe = masu_forme[:-1] + 'まない'
                        row.append(new_verbe)
                    if conj == 'passé affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'んだ'
                        row.append(new_verbe)
                    if conj == 'passé négatif neutre':
                        new_verbe = masu_forme[:-1] + 'まなかった'
                        row.append(new_verbe)
                    if conj == 'présent affirmatif formel':
                        new_verbe = masu_forme + 'ます'
                        row.append(new_verbe)
                    if conj == 'présent négatif formel':
                        new_verbe = masu_forme + 'ません'
                        row.append(new_verbe)
                    if conj == 'passé affirmatif formel':
                        new_verbe = masu_forme + 'ました'
                        row.append(new_verbe)
                    if conj == 'passé négatif formel':
                        new_verbe = masu_forme + 'ませんでした'
                        row.append(new_verbe)
                    if conj == 'forme en て　affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'んで'
                        row.append(new_verbe)
                    if conj == 'forme en て　négatif neutre':
                        new_verbe = masu_forme[:-1] + 'まなくて'
                        row.append(new_verbe)
                    if conj == 'forme en て　affirmatif formel':
                        new_verbe = masu_forme + 'まして'
                        row.append(new_verbe)
                    if conj == 'forme potentiel affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'める'
                        row.append(new_verbe)
                    if conj == 'forme potentiel négatif neutre':
                        new_verbe = masu_forme[:-1] + 'めない'
                        row.append(new_verbe)
                    if conj == 'forme potentiel affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'めます'
                        row.append(new_verbe)
                    if conj == 'forme potentiel négatif formel':
                        new_verbe = masu_forme[:-1] + 'めません'
                        row.append(new_verbe)
                    if conj == 'forme passif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'まれる'
                        row.append(new_verbe)
                    if conj == 'forme passif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'まれない'
                        row.append(new_verbe)
                    if conj == 'forme passif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'まれます'
                        row.append(new_verbe)
                    if conj == 'forme passif négatif formel':
                        new_verbe = masu_forme[:-1] + 'まれません'
                        row.append(new_verbe)
                    if conj == 'forme causatif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'ませる'
                        row.append(new_verbe)
                    if conj == 'forme causatif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'ませない'
                        row.append(new_verbe)
                    if conj == 'forme causatif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'ませます'
                        row.append(new_verbe)
                    if conj == 'forme causatif négatif formel':
                        new_verbe = masu_forme[:-1] + 'ませません'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif affirmatif neutre':
                        new_verbe = masu_forme[:-1] + 'ませられる'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif négatif neutre':
                        new_verbe = masu_forme[:-1] + 'ませられない'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif affirmatif formel':
                        new_verbe = masu_forme[:-1] + 'ませられます'
                        row.append(new_verbe)
                    if conj == 'forme causatif passif négatif formel':
                        new_verbe = masu_forme[:-1] + 'ませられません'
                        row.append(new_verbe)
                    if conj == 'forme volutive affirmatif neutre':
                        new_verbe = masu_forme + 'たい'
                        row.append(new_verbe)
                    if conj == 'forme volutive négatif neutre':
                        new_verbe = masu_forme + 'たくない'
                        row.append(new_verbe)
                    if conj == 'forme volutive affirmatif formel':
                        new_verbe = masu_forme + 'たかった'
                        row.append(new_verbe)
                    if conj == 'forme volutive négatif formel':
                        new_verbe = masu_forme + 'たくなかった'
                        row.append(new_verbe)
                    if conj == 'forme conjecturale neutre':
                        new_verbe = masu_forme[:-1] + 'もう'
                        row.append(new_verbe)
                    if conj == 'forme conjecturale formel':
                        new_verbe = masu_forme + 'ましょう'
                        row.append(new_verbe)
                    if conj == 'forme conditionnel neutre':
                        new_verbe = masu_forme[:-1] + 'めば'
                        row.append(new_verbe)
                    if conj == 'forme conditionnel négatif':
                        new_verbe = masu_forme[:-1] + 'まなければ'
                        row.append(new_verbe)
                    if conj == 'impératif affirmatif':
                        new_verbe = masu_forme[:-1] + 'め'
                        row.append(new_verbe)
                    if conj == 'impératif négatif':
                        new_verbe = masu_forme[:-1] + 'むな'
                        row.append(new_verbe)
                    if conj == 'radical - masu-forme': 
                        #radical masu-form
                        row.append(masu_forme)
                    if conj == 'tara':
                        new_verbe = masu_forme[:-1] + 'んだら'
                        row.append(new_verbe)
                    if conj == 'zu':
                        new_verbe = masu_forme[:-1] + 'まず'
                        row.append(new_verbe)
                    if conj == 'kucha':
                        new_verbe = masu_forme[:-1] + 'まなくちゃ'
                        row.append(new_verbe)
                    if conj == 'kya':
                        new_verbe = masu_forme[:-1] + 'まなきゃ'
                        row.append(new_verbe)
                else:
                    row.append('')
                row.append(conj)
                row.append(verbe_kanji_neutre)
                row.append(verbe_kana_neutre)
                row.append(verbe_trad)
                
                rows.append(row)
                
 

   
# field names  
fields = ['Type verbe', 'Kanji', 'Kana', 'Conjugaison', 'verbe neutre kanji', 'verbe neutre kana', 'Trad']  
    

# name of csv file  
filename = "all_verbes_test.csv"
    
# writing to csv file  
with open(filename, 'w', newline='', encoding='utf-32') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(fields)  
        
    # writing the data rows  
    csvwriter.writerows(rows)         

