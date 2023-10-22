from flask import Flask, render_template
import feedparser
from bs4 import BeautifulSoup

app = Flask(__name__)

noticias_url = str("https://tarragonadigital.com/rss")
tiempo_url = str("https://www.aemet.es/es/noticias.rss")

@app.route("/noticias")
def noticias_route():
    d = feedparser.parse(noticias_url)
    entradas = [(entry.title, entry.description, entry.published)  for entry in d.entries]
    return render_template('main.html', entradas=entradas)

@app.route("/tiempo")
def tiempo_route():
    d = feedparser.parse(tiempo_url)
    entradas = [(entry.title, entry.description, entry.published)  for entry in d.entries]
    return render_template('main.html', entradas=entradas)

@app.route("/")
def index_route():
    return render_template('index.html')
