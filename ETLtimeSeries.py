import pandas as pd
df = pd.read_csv('C:\\Users\\FITEC\\OneDrive\\Documents\\Projet ElasticSearch\\time_series_covid19_confirmed_global_with_etl.csv')
df_melted = pd.melt(df, id_vars=['Province/State','Country/Region', 'Lat', 'Long'], value_vars= row[4:])
#print(df_melted)
df_melted.to_csv('C:\\Users\\FITEC\\OneDrive\\Documents\\Projet ElasticSearch\\time_series_covid19_confirmed_global_with_etl.csv', index=False)