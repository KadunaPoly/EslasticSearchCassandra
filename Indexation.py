from cassandra.cluster import Cluster
from elasticsearch import Elasticsearch

# Connexion à la base de données Cassandra
cluster = Cluster(['127.0.0.1'])
session = cluster.connect('covid19')

# Connexion au cluster Elastic Search
es = Elasticsearch(['http://localhost:9200'])

# Récupération des données de Covid-19 à partir de Cassandra
rows = session.execute('SELECT * FROM covid_data')

# Indexation des données dans Elastic Search
for row in rows:
    doc = {
        'date': row.date,
        'country': row.country,
        'confirmed_cases': row.confirmed_cases,
        'deaths': row.deaths,
        'recovered': row.recovered
    }
    res = es.index(index='covid19', body=doc)