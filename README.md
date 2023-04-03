# EslasticSearchCassandra  
## Description du Projet:  
Le but de ce projet est de collecter, d'analyser et de visualiser les données de Covid-19 à partir de
sources publiques telles que l'Organisation mondiale de la santé (OMS) ou les centres de contrôle et de
prévention des maladies (CDC).  
Nous devrons d'abord collecter les données de Covid-19 et les stocker dans une base de données
Cassandra, en utilisant les outils appropriés pour extraire les données et les charger dans la base de
données.  
Ensuite, nous indexerons les données dans Elastic Search pour faciliter leur recherche et leur
traitement. Il devra utiliser les fonctionnalités d'Elastic Search pour créer des index, définir des
mappings et configurer des paramètres de recherche.
Enfin, nous utiliserons Kibana pour visualiser les données de Covid-19 et créer des tableaux de
bord interactifs pour suivre l'évolution de la pandémie. Il pourra utiliser les fonctionnalités de
visualisation de Kibana pour créer des graphiques, des cartes et des diagrammes pour mieux
comprendre les données.

## 1/ Collecte des données :   
La collecte se fait par le téléchargement via github des 3 fichiers.  

## 2/ Concevoir un schéma de base de données approprié pour stocker les données dans Cassandra  
Afin de pouvoir exploiter les données dans Cassandra,  il faut d'abord effectuer des transformation sur les données. 
Nous devons donc utiliser un ETL, nous avons choisi d'utiliser la puissance spark et le language python afin d'effectuer toutes les transformations.
Vous trouverez les 3 sprits, "ETLtimeSeries.py","ETLdeathGlobal.py"et "ETLrecoveredGlobal.py" qui sont les codes pour rendre les données exploitables. Dans le dossier "Données transformées" vous trouverez les 3 fichiers csv transformées.  
Il faut prendre la premiere ligne en tant que header et faire un pivot pour avoir une colone année car il y a une colone par jour ce qui est bien trop !  
On utilise la fonction "melt" pour faire un pivot sur toutes les colones après la colone 4 comprise. 
Ensuite il faut transformer le type de toutes les données.
Une fois les données transformés, il faut creer des tables Cassandra et faire la lecture des fichiers transformés à l'aide d'un script python. Voir dossier ETL : liaisonCassandra.py  


## 3/ Indexer les données de Covid-19 dans Elastic Search pour permettre une recherche facile  

Le code "Indexation.py" permet de se connecter à une base de données Cassandra et à un cluster Elastic Search, puis de récupérer les données de Covid-19 à partir de Cassandra et de les indexer dans Elastic Search. Les données récupérées sont la date, le pays, les cas confirmés, les décès et les guérisons.

L'indexation dans Elasticsearch consiste à stocker des données structurées dans un index, ce qui permet de les rechercher et de les analyser rapidement. Dans le code donné, chaque ligne de la table covid_data de Cassandra est récupérée sous forme de dictionnaire Python, avec des clés pour chaque colonne (date, pays, cas confirmés, décès, guérisons). Cette ligne est ensuite indexée dans Elasticsearch en tant que document, avec l'index "covid19" spécifiés. 


## 4/ Utiliser Kibana/Microsoft Power BI Desktop pour visualiser les données de Covid-19  
  Nous avons utiliser PowerBi pour visualiser les données.
 
## 5/ Créer des tableaux de bord interactifs pour suivre l'évolution de la pandémie  
* Visualisation des données sous forme de graphiques, de tableaux et de cartes
Voir les différentes captures d'écrans, nombre de morts au cours des années et nombre de morts en fonction du pays.

* Analyse des données pour en extraire des informations utiles sur la propagation de la
pandémie, les taux de mortalité et de guérison, et les tendances au fil du temps :  

On peut observer différents pics concernant le nombre de morts confirmé au cours du temps.   
En effet, quelque soit le pays, le nombre de morts va d'abord augmenter de facon exponentielle, pour ensuite diminuer progressivement. 
On remrarque également que le nombre de décès varie grandement selon le pays et la politique que son gouvernement à adopté pour faire face à la pandémie. 
En effet, certain pays comme l'Australie arrive à réduire le nombre de décés plus rapidement que d'autres pays Européen comme la france qui ont eu une politique plus laxiste. 

## 6/ Créer un docker-compose.yml pour automatiser tout le processus
Afin d'automatiser tout le processus nous avons du procéder aux étapes suivantes : 
* Créer un cluster cassandra
* Créer in cluster elastic kibana
* Lancer un conteneur ETL 
* Lancer un conteneur d’indexation  
  
Le code se trouve dans le fichier docker-compose-yml.
