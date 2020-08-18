
from pandas import Series, DataFrame
import pandas as pd
import numpy as np 
########################## Series #################################
obj = Series([4,5,-7,3])
# Series est un objet similaire à un tabeleau unidimensionnel qui
    # contien un ensemble de données et un ensemble d'étiquettes applées index
print(obj)
obj.values # donne les vvaleurs de Series
obj.index # donne l'index de Series

# on peut spécifier un index
obj2 = Series([4,5,-7,3], index = ['d','b','a','c'])
print(obj2)
obj2['a'] # donne -7
obj2['b'] # donne  5
obj2[['c','a','d']] # donne 3   -7  4
obj2[obj2 > 0]
obj2 * 2
np.exp(obj2)
'b' in obj2 # donne Trued
'e' in obj2 # donne False

# Création d'un objet Series à partir d'un dict
sdata = {'Ohio' : 35000, 'Texas' : 71000, 'Oregon' : 16000, 'Utah' : 5000}
obj3 = Series(sdata) # l'index correspend aux clés du dict dans l'ordre de tri 
print(obj3)

states = ['California', 'Ohio','Oregon','Texas']
obj4 = Series(sdata, index = states) # les index qui ne correspendent pas a des valeurs sont representés comme NAN (valeurs manquantes) 
print(obj4)
pd.isnull(obj4) # donne un booleen True pour les NAN 
pd.notnull(obj4) # donne un booleen False pour les NAN
obj4.isnull() #méthode d'instance

# Un objet sSeries aligne auto des données indixées différemment dans les opérations arithmétiques
print(obj3 + obj4)

obj4.name = 'Population'
obj4.index.name = 'State'
print(obj4)

# Modifier un Index d'un Series par affectation 
obj.index = ['Bob','Steve','Jeff','Ryan']
print(obj)

######################## DataFrame #########################

data = {'state' : ['Ohio', 'Ohio','Ohio','Nevada','Nevada'], 'year' : [2000,2001,2002,2001,2002], 'pop' : [1.5,1.7,3.6,2.4,2.9]}
print(data)
print(data)
frame = DataFrame(data)
print(frame) 
# Un DataFrame represente un structure de données en tableau à la manière d'une feuille de calcul
    # contenant une collection ordonnée de colonnes 
    # chacune des colonnes peut être d'un type de valeurs différents
    # il possède à la fois un index de lignes et un de colonnes

DataFrame(data, columns = ['year','state','pop']) # permet de changer la place des colonnes

 # spéifier l'index de lignes et des colonnes. 
frame2 = DataFrame(data, columns = ['year','state','pop','debt'], index = ['one', 'two','three', 'four', 'five'])
print(frame2)

frame2.columns # donne l'index des colonnes 
frame2.index # donne l'index des lignes 
frame2['state'] # récupère les valeurs d'une colonnes 
frame2.year # récupère les valeurs d'une colonnes 
frame2.loc['three'] # récupèrer les vleurs d'un ligne 
frame2.iloc[2] # récupérer les valeurs d'une ligne 
frame2['debt'] =  16.5 # affectation d'une valeur à une colonne
frame2['debt'] = np.arange(5.) # affectation d'une valeur à une colonne

# affectation d'un Series à une colonne d'un DataFrame 
val = Series([-1.2,-1.5,-1.7], index = ['two','four','five'])
frame2['debt'] = Val
print(frame2)

# l'affectation d'une colonne qui n'existe pas crée la colonne 
frame2['estern'] = frame2.state == 'Ohio' 
print(frame2)
del frame2['estern'] # supprime la colonne 

# Création d'un DataFrame à partir d'un dict de dict imbriqués
pop = {'Nevada' : {2001 : 2.4, 2002 : 2.9}, 'Ohio' : {2000 : 1.5, 2001 : 1.5, 2002 : 3.6}}
print(pop)

frame3 = DataFrame(pop)
print(frame3)
    # les clés de dict externes sont interprétées comme les colonnes et les clés internes comme les indices des lignes

# transposer les colonnes et les lignes
frame3.T 
    # les clés externes -> lignes et clés internes -> colonnes 

frame3.index.name = 'year'; frame3.columns.name = 'state'
print(frame3)

frame3.values # retourne les valeurs d'un DataFrame sous forme d'un array












