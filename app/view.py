__author__ = 'mackaiver'

from flask import render_template
from seins.PageParser import DBPageParser, PageContentError
from seins.HtmlFetcher import FetcherException
from app import app



@app.route('/')
@app.route('/index')
def index():
    text = "Hello biotches with teh bitch bioprodukte!"
    return render_template("main.html", delaystring='Pünktlich', text=text)


@app.route('/connections/')
def connections():


    try:
        page = DBPageParser(departing_station, arrival_station)

    except PageContentError as e:
        print('Webpage returned an error message: ' + str(e))

    except FetcherException as e:
        print('Fetcher could not get valid response from server: ' + str(e))
