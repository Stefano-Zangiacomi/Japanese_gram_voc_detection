# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 02:25:23 2020

@author: stefa
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 18:11:54 2020

@author: stefa
"""
"""
vocabulaire = []

phrase = "12345"

liste_mots = []
for i in range(len(phrase)+1):
    for j in range(i,len(phrase)+1):
        mot = phrase[i:j]
        if mot in vocabulaire: 
            liste_mots.append(mot)
"""
import numpy as np          
from fugashi import Tagger

tagger = Tagger('-Owakati')




text = "今日はパリから東京まで散歩するつもりだ"

text = "この暑い焼き鳥お食べ次第すぐにビールお飲みます"

text = '僕は自分中心'

text = "この暑い焼き鳥お食べ次第すぐにビールお飲みます"

text = 'でないと'


filter_text = text.replace(' ','');
filter_text = text.replace('?',''); 
filter_text = text.replace('!','');
filter_text = text.replace('...','');
filter_text = text.replace('(','');
filter_text = text.replace(')','');    

text_binary = np.zeros(len(filter_text))  # 1 si des mots ont été trouvés à cet emplacement, sinon 0


text_kana = text  #Texte qui sera traduit en kana

tagger.parse(text)
# => '麩 菓子 は 、 麩 を 主材 料 と し た 日本 の 菓子 。'

 
def data_preparation(csv): 
    regles = []
    explications = []
    for l in csv:  
        l.strip()
        ligne = l.split(';') 
        if 'null' not in ligne:
            regles.append(ligne[0])
            explications.append(ligne[1])
    
    return regles, explications

def data_preparation_adjectifs(csv): 
    type_adjectif = []
    kanji = []
    kana = []
    conjugaison = []
    kanji_neutre = []
    kana_neutre = []
    traduction = []
    for l in csv:  
        l.strip()
        ligne = l.split(',') 
        if 'null' not in ligne:
            type_adjectif.append(ligne[0])
            kanji.append(ligne[1])
            kana.append(ligne[2])
            conjugaison.append(ligne[3])
            kanji_neutre.append(ligne[4])
            kana_neutre.append(ligne[5])
            traduction.append(ligne[6][:-1])
    
    return type_adjectif, kanji, kana, conjugaison, kanji_neutre, kana_neutre, traduction

def data_preparation_verbes(csv):
    type_verbe = []
    kanji = []
    kana = []
    conjugaison = []
    kanji_neutre = []
    kana_neutre = []
    traduction = []
    for l in csv:  
        l.strip()
        ligne = l.split(',') 
        if 'null' not in ligne:
            type_verbe.append(ligne[0])
            kanji.append(ligne[1])
            kana.append(ligne[2])
            conjugaison.append(ligne[3])
            kanji_neutre.append(ligne[4])
            kana_neutre.append(ligne[5])
            traduction.append(ligne[6][:-1])
    
    return type_verbe, kanji, kana, conjugaison, kanji_neutre, kana_neutre, traduction

def data_preparation_noms(csv): 
    kanji = []
    kana = []
    trad = []
    for l in csv:  
        l.strip()
        ligne = l.split(',') 
        if 'null' not in ligne:
            kanji.append(ligne[0])
            kana.append(ligne[1])
            trad.append(ligne[2])
    
    return kanji, kana, trad

def data_preparation_pronoms(csv): 
    kanji = []
    kana = []
    trad = []
    for l in csv:  
        l.strip()
        ligne = l.split(',') 
        if 'null' not in ligne:
            kanji.append(ligne[0])
            kana.append(ligne[1])
            trad.append(ligne[2][:-1])
    
    return kanji, kana, trad

def data_preparation_particules(csv):
    kana = []
    explanation_particules = []
    for l in csv:
        l.strip()
        ligne = l.split(';')
        if 'null' not in ligne:
            kana.append(ligne[0])
            explanation_particules.append(ligne[1])
    return kana, explanation_particules



#OPEN LA LISTE DES VERBES
fi = open("all_verbes_test.csv",'r', encoding="utf8")
csv = fi.readlines()
fi.close()
type_verbe, verbe_kanji, verbe_kana, conjugaison_verbe, verbe_neutre_kanji, verbe_neutre_kana, traduction_verbe = data_preparation_verbes(csv)


#OPEN LA LISTE DES ADJECTIFS
fi = open("all_adjectifs.csv",'r', encoding="utf32")
csv = fi.readlines()
fi.close()
type_adjectifs, adjectif_kanji, adjectif_kana, conjugaisons_adjectifs, adjectif_neutre_kanji, adjectif_neutre_kana, traduction_adjectif = data_preparation_adjectifs(csv)

#OPEN LA LISTE DES NOMS
fi = open("Japan_English_Autres_Dict.csv",'r', encoding="utf32")
csv = fi.readlines()
fi.close()
kanji, kana, nom_trad = data_preparation_noms(csv)

#OPEN LA LISTE DES PRONOMS
fi = open("Japan_English_Pronouns_Dict.csv",'r', encoding="utf32")
csv = fi.readlines()
fi.close()
pronom_kanji, pronom_kana, pronom_trad = data_preparation_pronoms(csv)


#LISTES QUI CONTIENNENT LES REGLES DE GRAMMAIRE ET LES MOTS

inside_grammaire = []
inside_verbes = []
inside_adjectifs = []
inside_autres = []
inside_adjectifs = []
inside_particules = []
inside_pronoms = []
inside_particules = []

nbr_verbes = 0 #Nombre de verbes trouvés dans la phrase.
nbr_adjectifs = 0 #Nombre d'adjectifs trouvés dans la phrase.


noms = []
adjectifs = []
verbes = []

#PARSER
last_types = ['','','','','','',''] #On crée des champs vides pour éviter un 'list out of range'
last_type_word = ''


def detect_particules(word, wordpos):
    if wordpos.split(',')[1] == '格助詞' and (str(word) == 'が' or str(word) == 'の' or str(word) == 'を' or str(word) == 'に' or str(word) == 'へ' or str(word) == 'で'):
        return True
    elif wordpos.split(',')[1] == '係助詞' and (str(word) == 'は' or str(word) == 'も'):
        return True
    elif wordpos.split(',')[1] == '終助詞' and (str(word) == 'か' or str(word) == 'な' or str(word) == 'ね' or str(word) == 'よ' or str(word) == 'わ' or str(word) == 'っけ' or str(word) == 'ぜ' or str(word) == 'ぞ' or str(word) == 'さ'): 
        return True
    elif wordpos.split(',')[1] == '副助詞' and str(word) == 'か':
        return True
  

for word in tagger(text):
    print(word, word.pos, sep='\t')
    
    if detect_particules(word,word.pos) == True:
        inside_particules.append(str(word))
        
    
    """
    if (word.pos[0:3] == "接尾辞") and (last_type_word == '名詞'):
        inside_noms[-1] = inside_noms[-1] + str(word)
    """
    if word.pos[0:3] == '代名詞':
        inside_pronoms.append(str(word))
    elif word.pos[0:2] == '動詞': #verbe
        inside_verbes.append(str(word))
    elif word.pos[0:3] == '助動詞' and ((last_type_word == '動詞') or (last_types[-2] == '動詞' and last_types[-1] == '助動詞') or (last_types[-3] == '動詞' and last_types[-2] == '助動詞' and last_types[-1] == '助動詞') or (last_types[-4] == '動詞' and last_types[-3] == '助動詞' and last_types[-2] == '助動詞' and last_types[-1] == '助動詞')): # """suffixe du verbe - conjugaison"""
        if len(inside_verbes) != 0: #Liste vide (Pour éviter une erreur avec notamment 不安だったら)
            inside_verbes[-1] = inside_verbes[-1] + str(word)
    elif word.pos.split(',')[0] == '助詞' and word.pos.split(',')[1] == '接続助詞' and (last_type_word == '動詞' or last_type_word == '助動詞'):
        if (len(inside_verbes) != 0 and (str(word) == 'ば' or str(word) == "て" or str(word) == "で")): #Liste vide (Pour éviter une erreur avec notamment 不安だったら)
            inside_verbes[-1] = inside_verbes[-1] + str(word)
    elif (str(word) == 'なかっ' or str(word) == 'ない') and last_type_word == '助動詞':
        if len(inside_verbes) != 0: #Liste vide (Pour éviter une erreur avec notamment 不安だったら)
            inside_verbes[-1] = inside_verbes[-1] + str(word)
            last_types.append('助動詞')
            last_type_word = last_types[-1] #On enregistre le type de mot trouvé
            continue
        last_types.append('助動詞')
        last_type_word = last_types[-1] #On enregistre le type de mot trouvé
        continue
    elif word.pos.split(',')[0] == '形容詞' and last_type_word == '形容詞':
        if (len(inside_adjectifs) != 0 and str(word) == 'なけれ'):
            inside_adjectifs[-1] = inside_adjectifs[-1] + str(word)
    elif word.pos[0:3] == "形容詞" or word.pos[0:3] == "形状詞":
        inside_adjectifs.append(str(word))
    elif word.pos.split(',')[0] == '助詞' and word.pos.split(',')[1] == '接続助詞' and last_type_word == '形容詞':
        if (len(inside_adjectifs) != 0 and str(word) == 'ば'):
            inside_adjectifs[-1] = inside_adjectifs[-1] + str(word)
    elif word.pos.split(',')[0] == '助動詞' and (last_type_word == '形容詞' or last_type_word == '形状詞' or (last_type_word == '助動詞' and (last_types[-2] == last_type_word == '形容詞' or last_type_word == '形状詞'))):
        inside_adjectifs[-1] = inside_adjectifs[-1] + str(word)
    elif word.pos.split(',')[0] == '名詞' and word.pos.split(',')[2] != '副詞可能' and last_type_word == '名詞':
        inside_autres[-1] = inside_autres[-1] + str(word)
    elif '助' not in word.pos.split(',')[0] and word.pos[0:3] != '接頭辞': #Tout le reste sauf 
        inside_autres.append(str(word))
        #text = text.replace(str(word),'')
    
    last_types.append(word.pos.split(',')[0])
    last_type_word = last_types[-1] #On enregistre le type de mot trouvé



#FIND NOMS
liste_autres = []

for nom in inside_autres:
    for i in range(len(kanji)):
        mot_kanji = kanji[i]
        mot_kana = kana[i]
        trad = nom_trad[i]
        if mot_kanji == nom:
            new_voc = mot_kanji + ' ' + mot_kana + ' : ' + trad
            liste_autres.append(new_voc)
            text_binary[filter_text.index(mot_kanji):filter_text.index(mot_kanji)+len(mot_kanji)] = np.ones(len(mot_kanji)) 
            break
        elif mot_kana == nom:
            new_voc = mot_kana + ' : ' + trad
            liste_autres.append(new_voc)
            text_binary[filter_text.index(mot_kana):filter_text.index(mot_kana)+len(mot_kana)] = np.ones(len(mot_kana))
            break
        
#FIND VERBES
liste_verbes = []

for verbe in inside_verbes:
    for i in range(len(verbe_kanji)):
        mot_kanji = verbe_kanji[i]
        mot_kana = verbe_kana[i]
        conj = conjugaison_verbe[i]
        neutre_kanji = verbe_neutre_kanji[i]
        neutre_kana = verbe_neutre_kana[i]
        trad = traduction_verbe[i]

        if mot_kanji == verbe:
            new_voc = explication = mot_kanji + ' ' + mot_kana + " est de la forme " + conj + " du verbe " + neutre_kanji  + ' ' + neutre_kana + ' qui signifie : ' + trad
            liste_verbes.append(new_voc)
            text_binary[filter_text.index(mot_kanji):filter_text.index(mot_kanji)+len(mot_kanji)] = np.ones(len(mot_kanji))
            break
        elif mot_kana == verbe:
            new_voc = mot_kana + " est de la forme " + conj + " du verbe " + neutre_kanji  + ' ' + neutre_kana + ' qui signifie : ' + trad
            liste_verbes.append(new_voc)
            text_binary[filter_text.index(mot_kana):filter_text.index(mot_kana)+len(mot_kana)] = np.ones(len(mot_kana))
            break
            
            
#FIND ADJECTIFS
liste_adjectifs = []

for nom in inside_adjectifs:
    for i in range(len(adjectif_kanji)):
        mot_kanji = adjectif_kanji[i]
        mot_kana = adjectif_kana[i]
        conj = conjugaisons_adjectifs[i]
        neutre_kanji = adjectif_neutre_kanji[i]
        neutre_kana = adjectif_neutre_kana[i]
        trad = traduction_adjectif[i]

        if mot_kanji == nom:
            new_voc = explication = mot_kanji + ' ' + mot_kana + " est de la forme " + conj + " de l'adjectif " + neutre_kanji  + ' ' + neutre_kana + ' qui signifie : ' + trad
            liste_adjectifs.append(new_voc)
            text_binary[filter_text.index(mot_kanji):filter_text.index(mot_kanji)+len(mot_kanji)] = np.ones(len(mot_kanji))
            break
        elif mot_kana == nom:
            new_voc = mot_kana + " est de la forme " + conj + " de l'adjectif " + neutre_kanji  + ' ' + neutre_kana + ' qui signifie : ' + trad
            liste_adjectifs.append(new_voc)
            text_binary[filter_text.index(mot_kana):filter_text.index(mot_kana)+len(mot_kana)] = np.ones(len(mot_kana))
            break
        
#FIND PRONOMS
liste_pronoms = []

for nom in inside_pronoms:
    for i in range(len(kanji)):
        mot_kanji = pronom_kanji[i]
        mot_kana = pronom_kana[i]
        trad = pronom_trad[i]
        if mot_kanji == nom:
            new_voc = mot_kanji + ' ' + mot_kana + ' : ' + trad
            liste_pronoms.append(new_voc)
            text_binary[filter_text.index(mot_kanji):filter_text.index(mot_kanji)+len(mot_kanji)] = np.ones(len(mot_kanji))
            break
        elif mot_kana == nom:
            new_voc = mot_kana + ' : ' + trad
            liste_pronoms.append(new_voc)
            text_binary[filter_text.index(mot_kana):filter_text.index(mot_kana)+len(mot_kana)] = np.ones(len(mot_kana))
            break


#PARTICULES
            
fi = open("particules.csv",'r', encoding="utf8")
csv = fi.readlines()
fi.close()
particules, explanation_particules = data_preparation_particules(csv)           

liste_particules = []

for in_particule in inside_particules:
    for i in range(len(particules)):
        particule = particules[i]
        if in_particule == particule:
            new_voc = particule
            liste_particules.append(new_voc)
            text_binary[filter_text.index(particule):filter_text.index(particule)+len(particule)] = np.ones(len(particule))
                
#FIND GRAMMAR RULES
            
#OPEN LA LISTE DE GRAMAIRE N4
fi = open("grammaireN4.csv",'r', encoding="utf8")
csv = fi.readlines()
fi.close()
gram_kanji, gram_kana = data_preparation(csv)


text_gram = text

for i in range(len(gram_kanji)):
    kanji = gram_kanji[i]
    kana = gram_kana[i]
    if '～' in kanji:
        kanji_liste = kanji.split('～')
        kana_liste = kana.split('～')
        kanji1, kanji2 = kanji_liste[0], kanji_liste[1]
        kana1, kana2 = kana_liste[0], kana_liste[1]
        if kanji1 in text_gram and kanji2 in text_gram:
            grammaire = kanji + ' ' + kana
            inside_grammaire.append(grammaire)
            text_binary[filter_text.index(kanji1):filter_text.index(kanji1)+len(kanji1)] = np.ones(len(kanji1))
            text_binary[filter_text.index(kanji2):filter_text.index(kanji2)+len(kanji2)] = np.ones(len(kanji2))
            text_gram = text_gram.replace(kanji, '-')
        elif kana1 in text_gram and kana2 in text_gram:
            grammaire = kana
            inside_grammaire.append(grammaire)
            text_binary[filter_text.index(kana1):filter_text.index(kanji1)+len(kana1)] = np.ones(len(kana1))
            text_binary[filter_text.index(kana2):filter_text.index(kana2)+len(kana2)] = np.ones(len(kana2))
            text_gram = text_gram.replace(kana, '-')
    elif '+' in kanji:
        kanji_liste = kanji.split('+')
        kana_liste = kana.split('+')
        abrev = kanji_liste[0]
        kanji = kanji_liste[1]
        kana = kana_liste[1]
        if kanji in text_gram:
            phrase_avant_regle = text.split(kanji)[0]
            nature = tagger(phrase_avant_regle)[-1].pos.split(',')[0]
            if abrev == nature:
                grammaire = kanji + ' ' + kana
                inside_grammaire.append(grammaire)
                text_binary[filter_text.index(kanji):filter_text.index(kanji)+len(kanji)] = np.ones(len(kanji))
                text_gram = text_gram.replace(kanji, '-')
        elif kana in text_gram:
            phrase_avant_regle = text.split(kana)[0]
            nature = tagger(phrase_avant_regle)[-1].pos.split(',')[0]
            if abrev == nature:
                grammaire = kana
                inside_grammaire.append(grammaire)
                text_binary[filter_text.index(kana):filter_text.index(kana)+len(kana)] = np.ones(len(kana))
                text_gram = text_gram.replace(kana, '-')
    else: 
        if kanji in text_gram:
            grammaire = kanji + ' ' + kana
            inside_grammaire.append(grammaire)
            text_binary[filter_text.index(kanji):filter_text.index(kanji)+len(kanji)] = np.ones(len(kanji))
            text_gram = text_gram.replace(kanji, '-')
        elif kana in text_gram:
            grammaire = kana
            inside_grammaire.append(grammaire)
            text_binary[filter_text.index(kana):filter_text.index(kana)+len(kana)] = np.ones(len(kana))
            text_gram = text_gram.replace(kana, '-')
         
        

    
    



    
print(text)

print(liste_verbes)
print(liste_adjectifs)
print(liste_autres)
print(liste_pronoms)
print(inside_grammaire)
print(liste_particules)

print(text_binary)
nbr_1 = np.count_nonzero(text_binary == 1.0);
ratio = nbr_1 / len(text_binary)

print(ratio)


    