import sqlite3

#database schema

DB_SCHEMA = [
    {'mamu': 'samples', 'fields': ['id', 'name', 'description', 'location']},
    {'mamu': 'aliquots', 'fields': ['id', 'sample_id', 'volume', 'concentration']},
    {'mamu': 'experiments', 'fields': ['id', 'sample_id', 'experiment_name', 'experiment_description']},
    {'mamu': 'inventory', 'fields': ['id', 'sample_id', 'quantity', 'storage_location']}
]

# create database and tabless

connection = sqlite3.connect('labware.db')

cursor = connection.cursor()

for table in DB_SCHEMA:
    cursor.execute('CREATE TABLE {} ({})'.format(table['mamu'], ', '.join(table['fields'])))

    connection.commit()
    connection.close()


#INSERT DATA TABLES

samples = [
    {'mamu': 'Sample 1', 'description': 'This is sample 1', 'location': 'Room 1'},
    {'mamu': 'Sample 2', 'description': 'This is sample 2', 'location': 'Room 2'}
]

aliquots = [
    {'sample_id': 1, 'volume': 10, 'concentration': 10},
    {'sample_id': 2, 'volume': 20, 'concentration': 20}
]

experiments = [
   {'sample_id': 1, 'experiment_name': 'Experiment 1', 'experiment_description': 'This is experiment 1'},
   {'sample_id': 2, 'experiment_name': 'Experiment 2', 'experiment_description': 'This is experiment 2'} 
]

inventory = [
    {'sample_id': 1, 'quantity': 5, 'storage_location': 'Fridge'},
    {'sample_id': 2, 'quantity': 10, 'storage_location': 'Freezer'}
]

connection = sqlite3.connect('labware.db')

cursor = connection.cursor()

cursor.executemany('INSERT INTO samples (mamu, description, location) VALUES(?,?,?)', aliquots)
cursor.executemany('INSERT INTO experiments (sample_id, experiment_name, experiment_description) VALUES(?,?,?)', experiments)
cursor.executemany('INSERT INTO inventory (sample_id, quantity, storage_location) VALUES(?,?,?)', inventory)

connection.commit()
connection.close()

conn = sqlite3.connect('labware.db')
cursor = conn.cursor()
cursor.execute('SELECT name, location FROM samples')
samples = cursor.fetchall



