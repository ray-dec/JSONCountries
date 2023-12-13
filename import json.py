import json
import os


dossier_principal = 'world-countries\countries'
langues = ['fr', 'es', 'en', 'de', 'it', 'pt']

resultats = {}

chemin_fichier_anglais = os.path.join("world-countries\countries\en\world.json")
with open(chemin_fichier_anglais, 'r',encoding='utf-8') as fichier:
    pays_anglais = json.load(fichier)
    for p in pays_anglais:
        id_pays = p['id']
        nom_pays_anglais = p['name']
        resultats[id_pays] = {'en': nom_pays_anglais}


for langue in langues:
    chemin_dossier = os.path.join(dossier_principal, langue)
    nom_fichier = '\\world.json'
    chemin_complet = os.path.abspath(chemin_dossier+nom_fichier)

    with open(chemin_complet, 'r',encoding='utf-8') as fichier:
        pays = json.load(fichier)
        for p in pays:
            id_pays = p['id']
            if id_pays in resultats:
                resultats[id_pays][langue.lower()] = p['name']


resultats_final = {resultats[id_pays]['en']: val for id_pays, val in resultats.items()}


with open('resultats_pays.json', 'w',encoding='utf-8') as fichier_sortie:
    json.dump(resultats_final, fichier_sortie,ensure_ascii=False, indent=4)
