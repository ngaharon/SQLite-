import sqlite3

Connection = sqlite3.connect('lab2.db')

Connection.execute('''
    CREATE TABLE IF NOT EXISTS samples(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   sample_no. INT,
                   description TEXT,
                   location INT,
    )
''')

Connection.execute('''
    CREATE TABLE IF NOT EXISTS aliquots(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   sample_id INT,
                   volume INT,
                   concentration INT
    )
''')

Connection.execute('''
    CREATE TABLE IF NOT EXISTS experiments(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   experiment_id INT,,
                   experiment_name TEXT,
                   experiment_description
    )               
''')

Connection.execute('''
    CREATE TABLE IF NOT EXISTS inventorys(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   sample_id INT,
                   quantity INT,
                   storage_location TEXT
    )
''')

samples_data = [
    {'name': 'Sample 1', 'description': 'This is sample 1', 'location': 'Room 1'},
    {'name': 'Sample 2', 'description': 'This is sample 2', 'location': 'Room 2'}
]

aliquots_data = [
    {'sample_id': 1, 'volume': 10, 'concentration': 10},
    {'sample_id': 2, 'volume': 20, 'concentration': 20}
]

experiments_data = [
    {'sample_id': 1, 'experiment_name': 'Experiment 1', 'experiment_description': 'This is experiment 1'},
    {'sample_id': 2, 'experiment_name': 'Experiment 2', 'experiment_description': 'This is experiment 2'} 
]

inventorys_data = [
    {'sample_id': 1, 'quantity': 5, 'storage_location': 'Fridge'},
    {'sample_id': 2, 'quantity': 10, 'storage_location': 'Freezer'}
]

Connection.executemany('INSERT INTO samples(name, sample_no, description, location) VALUES(?,?,?,?)', samples_data)
Connection.executemany('INSERT INTO aliquots(sample_id, volume, concentrate) VALUES(?,?,?)', aliquots_data)
Connection.executemany('INSERT INTO experiments(sample_id, experiment_name, experiment_description) VALUES(?,?,?)', experiments_data)
Connection.executemany('INSERT INTO inventorys(sample_id, quantity, storage_location) VALUES(?,?,?)', aliquots_data)

results = Connection.execute('''
    SELECT samples.sample_id, aliquots.sample_id, experiments.sample_id, inventory_id
                             FROM samples
                             INNER JOIN aliquots, experiments, inventorys ON samples.id = 
''')