"""
Простой RSS reader

При добавлении ленты (например https://habrahabr.ru/rss/interesting/)
записи из добавленной ленты сканируются и заносятся в базу (например sqlite)

При нажатии на кнопку обновить - новое сканирование и добавление новых записей (без дублрования существующих)

Отображение ленты начиная с самых свежих записей с пагинацией (несколько записей на странице)

Записи из разных лент хранить и показывать отдельно (по названию ленты).

Вгимание:
После сдачи и визирования отчета принести его на лекцию (за 5 мин до начала)
+ Продублировать отчет и исходник(.zip, github и т.п.) письмом на isu
"""

import sqlite3
import requests
import bs4
from bs4 import BeautifulSoup

from flask import request
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

db_path = "/Users/a.musabekov/pylab6.db"

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn
    
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        c.close()
    except Exception as e:
        print(e)

def create_table_if_needed(conn):
    sql_query = """ CREATE TABLE IF NOT EXISTS posts (
                        guid text PRIMARY KEY,
                        title text NOT NULL,
                        description text
                    ); """
    create_table(conn, sql_query)
    
def feed_parse():
    article_list = []
    try:
        r = requests.get('https://habrahabr.ru/rss/interesting/')
        soup = BeautifulSoup(r.content, features = 'xml')
        articles = soup.findAll('item')
        for a in articles:
            article = {}
            article['guid'] = a.guid.get_text()
            article['title'] = a.title.get_text()
            
            dd = a.description.get_text()
            desc = BeautifulSoup(dd, features = 'xml')
            article['description'] = " ".join([item for item in desc.find_all(text=True)])
            
            article_list.append(article)
    except Exception as e:
        print(e)

    return article_list

def save_feed(feed, conn):
    cursor = conn.cursor()
    for a in feed:
        query = f"INSERT OR IGNORE INTO posts (guid, title, description) VALUES (\"{a['guid']}\", \"{a['title']}\", \"{a['description']}\");"
        cursor.execute(query, a)
        conn.commit()
    cursor.close()

def main():
    conn = create_connection(db_path)
    cursor = conn.cursor()
    create_table_if_needed(conn)

@app.route('/startgame', methods=['GET'])
def start_game():
    conn = create_connection(db_path)
    cursor = conn.cursor()
    
    feed = feed_parse()
    save_feed(feed, conn)
    
    sqlite_select_query = """SELECT * from posts"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    cursor.close()
    
    articles = []
    
    for row in records:
        article = {}
        article['title'] = row[1]
        article['description'] = row[2]
        articles.append(article)
        
    return {'answer': articles}
   
if __name__ == '__main__':
    main()
    app.run()
