import re
import whois
import requests
from News import SecurityNewsApi as kbs
from flask import Flask, request, json, jsonify
from flask_cors import CORS
from Features import PhishingDetection


app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'], methods=['POST'])


@app.route("/detect", methods=['POST'])
def detect():
    input_url = request.get_json("url")
    headers = {
        'Access-Control-Allow-Origin': 'http://localhost:3000',
        'Access-Control-Allow-Methods': 'POST',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Content-Type': 'application/json'
    }
    data = PhishingDetection.isPhising(input_url)
    response = app.response_class(response=json.dumps(data), status=200, mimetype='application/json', headers=headers)
    return response


@app.route("/geolocation", methods=['POST'])
def geolocation():
    url = "https://ip-geolocation-ipwhois-io.p.rapidapi.com/json/"

    input_IP = request.get_json('IP')

    # print(input_IP)

    IP = input_IP.get('IP')

    querystring = {'ip': IP}

    rapid_headers = {
        "X-RapidAPI-Key": "4efd8534a6msh6f1a454900be4b7p1fc6afjsnba1c03f20006",
        "X-RapidAPI-Host": "ip-geolocation-ipwhois-io.p.rapidapi.com"
    }

    phish_headers = {
        'Access-Control-Allow-Origin': 'http://localhost:3000',
        'Access-Control-Allow-Methods': 'POST',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Content-Type': 'application/json'
    }

    ip_pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'

    match = re.findall(ip_pattern, querystring.get('ip'))

    if len(match) != 0:
        response = requests.request("GET", url, headers=rapid_headers, params=querystring)
        # print(response)
        data = json.loads(response.text)
        if data.get('success'):
            data.pop("completed_requests")
            data.pop("currency_symbol")
            data.pop("currency_code")
            data.pop("currency")
            data.pop("currency_rates")
            data.pop("currency_plural")
            # return jsonify(data)
            response = app.response_class(response=json.dumps(data), status=200, headers=phish_headers,
                                          mimetype='application/json')
            return response
        else:
            response = app.response_class(response=json.dumps(data), status=200, mimetype='application/json')
            return response
    else:
        data = {"IP": "Please enter IP Address"}
        # return jsonify(data)
        response = app.response_class(response=json.dumps(data), status=200, headers=phish_headers,
                                      mimetype='application/json')
        return response


@app.route("/news", methods=['POST'])
def news():
    input_category = request.get_json('category')

    category = input_category.get('category')

    headers = {
        'Access-Control-Allow-Origin': 'http://localhost:3000',
        'Access-Control-Allow-Methods': 'POST',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Content-Type': 'application/json'
    }
    # print(input_category,"\n", category)
    news = kbs.getNews(category)

    # data = {'News':news}
    # print(news)
    message = json.dumps(news)
    return app.response_class(response=message, status=200, mimetype='application/javascript, png', headers=headers)


app.run(port=7013)
