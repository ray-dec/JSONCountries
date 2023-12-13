# JSONCountries

Ce projet a pour but de créer un référentiel pays basé sur le projet GitHub suivant : https://github.com/stefangabos/world_countries/

Le but est de traiter en entrée l'ensemble des fichiers ayant pour information le pays, le code et l'intitulé du pays (dans la langue sélectionné) vers un format de type JSON utilisable sur un site internet et qui viendra sélectionner le bon nom d'usage du pays en fonction de la langue du navigateur. 
Le fichier final permettra d'obtenir un référentiel unique par pays du nom en anglais (référence) vers le nom d'appellation dans la langue sélectionnée.

Ce script pourra être augmenté aux pays voulu, et les informations telles que l'ID Pays, le code Alpha 2 et 3 seront retrouvables dans le fichier initial, pourront faire l'objet d'ajouts au référentiel.


### Par exemple, pour la France :

#### Input : 

{"id":250,"alpha2":"fr","alpha3":"fra","name":"Francia"},
{"id":250,"alpha2":"fr","alpha3":"fra","name":"France"},
{"id":250,"alpha2":"fr","alpha3":"fra","name":"France"},
{"id":250,"alpha2":"fr","alpha3":"fra","name":"Frankreich"},
{"id":250,"alpha2":"fr","alpha3":"fra","name":"Francia"},
{"id":250,"alpha2":"fr","alpha3":"fra","name":"França"},

#### Output : 

    "France": {
        "en": "France",
        "fr": "France",
        "es": "Francia",
        "de": "Frankreich",
        "it": "Francia",
        "pt": "França"
    },
