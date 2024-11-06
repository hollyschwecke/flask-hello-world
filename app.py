import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Holly Schwecke in 3308!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://schwecke_lab10_database_user:4NeoO85Ipw8AavH2X3IOOflP6aOlVbfA@dpg-csluug1u0jms73b9eflg-a/schwecke_lab10_database")
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgresql://schwecke_lab10_database_user:4NeoO85Ipw8AavH2X3IOOflP6aOlVbfA@dpg-csluug1u0jms73b9eflg-a/schwecke_lab10_database")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball (
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"

@app.route('/db_insert')
def inserting():
    conn = psycopg2.connect("postgresql://schwecke_lab10_database_user:4NeoO85Ipw8AavH2X3IOOflP6aOlVbfA@dpg-csluug1u0jms73b9eflg-a/schwecke_lab10_database")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated"