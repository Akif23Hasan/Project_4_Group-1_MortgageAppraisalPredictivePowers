import csv
import pandas as pd
from sqlalchemy import create_engine
import sqlite3
from flask import Flask, request, render_template, jsonify
from sqlalchemy.orm import Session 


data = pd.read_csv('imdb_top_1000_cleaned.csv')

engine= create_engine('sqlite:///movies.db')

data.to_sql('movies',engine,index=False,if_exists= 'replace')

session = Session(engine)


################################################
# Flask Setup
################################################
app = Flask(__name__)


# SQLite database connection
conn = sqlite3.connect('movies.db', check_same_thread=False)
cursor = conn.cursor()
    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/movies/')
def get_all_movies():
    query = f'SELECT * FROM movies'
    cursor.execute(query)
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    result = [dict(zip(columns, row)) for row in rows]
    return jsonify(result)

# Sorted movies by attribute for index page
@app.route('/api/sorted_movies/<attribute>')
def get_sorted_movies(attribute):
    if attribute in ["Certificate", "Genre1"]:
        order = "ASC"
    else:
        order = "DESC"
    
    if attribute == "~Randomized~":
        query = "SELECT * FROM movies ORDER BY RANDOM() DESC LIMIT 10"
    else:
        query = f'SELECT * FROM movies ORDER BY {attribute} {order}'

    cursor.execute(query)
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    result = [dict(zip(columns, row)) for row in rows]
    return jsonify(result)

# Sorted movies by attribute for index page
@app.route('/api/filtered_movies')
def get_filtered_movies():
    sortByValue  = request.args.get('sortByValue', None)
    filterValue  = request.args.get('filterValue', None)
    if (type(filterValue) == str):
        if filterValue=='null':
            query = f'SELECT * FROM movies WHERE {sortByValue} IS NULL ORDER BY IMDB DESC'
        elif  filterValue=='MA15':
            query = f'SELECT * FROM movies WHERE {sortByValue} = "MA 15+" ORDER BY IMDB DESC'
        else:
            query = f'SELECT * FROM movies WHERE {sortByValue} = "{filterValue}" ORDER BY IMDB DESC'
    else:
        query = f'SELECT * FROM movies WHERE {sortByValue} = {filterValue} ORDER BY {sortByValue} DESC'


    cursor.execute(query)
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    result = [dict(zip(columns, row)) for row in rows]
    return jsonify(result)

# Top 10 movies by attribute for dashboard
@app.route('/api/top_movies/<attribute>')
def get_top_movies(attribute):
    query = f'SELECT * FROM movies ORDER BY {attribute} DESC LIMIT 10'
    cursor.execute(query)
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    result = [dict(zip(columns, row)) for row in rows]
    return jsonify(result)

@app.route('/api/genre/')
def get_genre_data():
    query = f'SELECT Genre1, COUNT(Genre1) as count FROM movies GROUP BY Genre1 ORDER BY count DESC'
    cursor.execute(query)
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    result = [dict(zip(columns, row)) for row in rows]
    return jsonify(result)

@app.route('/api/director/Gross')
def get_top_director_by_gross():
    query = f'SELECT Director, COUNT(Director) as count, SUM(Gross) as gross, AVG(Gross) as avg_gross  FROM movies GROUP BY Director ORDER BY gross DESC LIMIT 10'
    cursor.execute(query)
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    result = [dict(zip(columns, row)) for row in rows]
    return jsonify(result)


@app.route('/api/director/IMDB')
def get_top_director_by_imdb():
    query = f'SELECT Director, COUNT(Director) as count, AVG(IMDB) as imdb FROM movies GROUP BY Director ORDER BY imdb DESC LIMIT 10'
    cursor.execute(query)
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    result = [dict(zip(columns, row)) for row in rows]
    return jsonify(result)

@app.route('/api/genre/Gross')
def get_top_genre_by_gross():
    query = f'SELECT Genre1, COUNT(Genre1) as count, SUM(Gross) as gross, AVG(Gross) as avg_gross FROM movies GROUP BY Genre1 ORDER BY avg_gross DESC LIMIT 10'
    cursor.execute(query)
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    result = [dict(zip(columns, row)) for row in rows]
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)