from cassandra.cluster import Cluster
import csv

# Connexion à Cassandra
cluster = Cluster(['localhost'])
session = cluster.connect()

# Création de la clé d'espace pour stocker les données
session.execute("CREATE KEYSPACE IF NOT EXISTS covid19 WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}")

# Création de la table pour stocker les données
session.execute("CREATE TABLE IF NOT EXISTS covid19.cases (country text, province text, date timestamp, confirmed int, deaths int, recovered int, PRIMARY KEY ((country, province), date))")

# Lecture du fichier CSV et insertion des données dans Cassandra
with open('covid19_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # skip the header
    for row in reader:
        session.execute("INSERT INTO covid19.cases (country, province, date, confirmed, deaths, recovered) VALUES (%s, %s, %s, %s, %s, %s)", (row[1], row[0], row[2], int(row[3]), int(row[4]), int(row[5])))

# Fermeture de la connexion à Cassandra
cluster.shutdown()