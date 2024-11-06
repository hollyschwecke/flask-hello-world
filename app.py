import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Holly Schwecke in 3308!'

@app.route('/db_test')
def testing:
    conn = psycopg2.connect("postgresql://schwecke_lab10_database_user:4NeoO85Ipw8AavH2X3IOOflP6aOlVbfA@dpg-csluug1u0jms73b9eflg-a/schwecke_lab10_database")
    conn.close()
    return "Database Connection Successful"