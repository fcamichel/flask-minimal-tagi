import feedparser
import requests
from requests_html import HTMLSession
from flask import render_template, flash, redirect, url_for, request
from app import app


@app.route('/')
@app.route('/index')
def index():
    front = feedparser.parse('https://www.tagesanzeiger.ch/rss.html')
    posts = front.entries
    return render_template('index.html', title='Übersicht', posts=posts)


@app.route('/get/<int:post_id>')
def get(post_id):
    session = HTMLSession()
    r = session.get('https://tagesanzeiger.ch/'+str(post_id))
    article = r.html.find('#article', first=True)
    if article == None:
        # not supported on repl.it
        r.html.render()
        article = r.html.find('#app', first=True)
    return render_template('article.html', title='Artikel', article_html=article.html)
