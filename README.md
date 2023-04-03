# EslasticSearchCassandra
Description du Projet:
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

1/ Collecte des données : 
La collecte se fait par le téléchargement via github des 3 fichiers.

2/ Concevoir un schéma de base de données approprié pour stocker les données dans Cassandra
Afin de pouvoir exploiter les données dans Cassandra,  il faut d'abord effectuer des transformation sur les données.
Nous devons donc utiliser un ETL, nous avons choisi d'utiliser la puissance spark et le language python afin d'effectuer toutes les transformations.



• Indexer les données de Covid-19 dans Elastic Search pour permettre une recherche facile
• Charger les données dans Cassandra (un script Python dans un conteneur docker)
• Indexer les données dans Elastic Search (un script Python dans un conteneur docker)
• Utiliser Kibana/Microsoft Power BI Desktop pour visualiser les données de Covid-19
• Créer des tableaux de bord interactifs pour suivre l'évolution de la pandémie
• Visualiser les données sous forme de graphiques, de tableaux et de cartes
• Analyser les données pour en extraire des informations utiles sur la propagation de la
pandémie, les taux de mortalité et de guérison, et les tendances au fil du temps
• Créer un docker-compose.yml pour automatiser tout le processus
• Créer un cluster cassandra
• Créer in cluster elastic kibana
• Lancer un conteneur ETL
• Lancer un conteneur d’indexation