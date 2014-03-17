__author__ = 'mackaiver'

from flask import render_template
from seins.PageParser import DBPageParser, PageContentError
from seins.HtmlFetcher import FetcherException
import json
from app import app



@app.route('/')
@app.route('/index')
def index():
    text = "Hello biotches with teh bitch bioprodukte!"
    return render_template("main.html", delaystring='Pünktlich', text=text)


@app.route('/connections/')
def connections():

    try:
        page = DBPageParser("Universität Dortmund S-Bahnhof", "Dortmund Hbf")
        traintuples = page.connections
        trains = list()
        for t in traintuples:
            trains.append({"departure_time": t[0], "arrival_time": t[1], "delay": t[2], "connection_type": t[3]})
        jsonObj = json.dumps(trains)
        return (jsonObj)

    except PageContentError as e:
        print('Webpage returned an error message: ' + str(e))
        return "Error page content"

    except FetcherException as e:
        print('Fetcher could not get valid response from server: ' + str(e))
        return "Error fetcher"