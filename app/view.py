__author__ = 'mackaiver'

from flask import render_template
from flask import request
from seins.PageParser import DBPageParser, PageContentError
from seins.HtmlFetcher import FetcherException
import json
import time
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template("main.html")


@app.route('/connections/')
def connections():
    #print(direction.lower())
    direction = request.args.get('direction', '')
    time.sleep(3)
    try:
        if direction and direction.lower().strip() == "solingen":
            #print("Requesting solingen")
            page = DBPageParser("Universität Dortmund S-Bahnhof", "Solingen Hbf")
        else:
            page = DBPageParser("Universität Dortmund S-Bahnhof", "Dortmund Hbf")

        traintuples = page.connections
        trains = list()
        #put tuples into a dict for json creation
        for t in traintuples:
            #filter out non sbahn connecitons
            if t[3] and str(t[3]).lower().strip() == 's':
                trains.append({"departure_time": t[0], "arrival_time": t[1], "delay": t[2], "connection_type": t[3]})

        json_obj = json.dumps(trains)
        return json_obj

    except PageContentError as e:
        print('Webpage returned an error message: ' + str(e))
        return json.dumps("Error")

    except FetcherException as e:
        print('Fetcher could not get valid response from server: ' + str(e))
        return json.dumps("Error DB")