import os
import json
import math
import psycopg2

# Data Locations
#json_data = 'C:\\Users\\erick\\OneDrive\\Git\\Datasets\\distros.json'
json_data = '/home/erick/Downloads/distros.json'

#Load JSON Files
with open(json_data, 'r') as f:
    distros_dict = json.load(f) 

#Load file size in bytes (1+e6)
file_size = os.path.getsize(json_data)
print(file_size)


for i in distros_dict:
    print(i['Name'])


# Load data into PostgreSQL
con = psycopg2.connect(database='sanctionsdb', user='dbuser') 
cur = con.cursor()
q = "INSERT INTO bill_summary VALUES(%(title)s, %(summary-text)s, %(action-date)s, %(action-desc)s)"
cur.execute(q, data)
con.commit()