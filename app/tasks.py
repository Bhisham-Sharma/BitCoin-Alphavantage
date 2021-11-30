from __future__ import absolute_import, unicode_literals

from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from celery import shared_task
from .serializers import PriceSerializer
from django.conf import settings
import requests
import io
import json

url_params_excgange_price_BTCtoUSD = {
    "function" : "CURRENCY_EXCHANGE_RATE",
    "from_currency" : "BTC",
    "to_currency" : "USD",
    "apikey": settings.API_KEY,
    }

# this will fetch BTC to USD exchnage rate info
@shared_task
def exchangeRate():
    alphavantage_api_response = requests.get(settings.API_URL, params=url_params_excgange_price_BTCtoUSD)
    data = alphavantage_api_response.json()
    return data


url_params_BTC_Price = {
    "function" : "DIGITAL_CURRENCY_DAILY",
    "symbol" : "BTC",
    "market" : "USD",
    "apikey": settings.API_KEY,
    }

# this will fetch the opening and closing price for BTC in USD market every hour and save to db
@shared_task(bind=True)
def getPriceBtc(self):
    alphavantage_api_response = requests.get(settings.API_URL, params=url_params_BTC_Price)
    data = alphavantage_api_response.json()
    date_keys_ls = list(data.get('Time Series (Digital Currency Daily)'))

    for date_key in date_keys_ls:
        open_price = data.get('Time Series (Digital Currency Daily)').get(date_key).get('1a. open (USD)')
        close_price = data.get('Time Series (Digital Currency Daily)').get(date_key).get('4b. close (USD)')
        date = date_key
        data_dict = {
            'date' : date,
            'open_price' : open_price,
            'close_price' : close_price,
        }
        json_data = json.dumps(data_dict) # str
        stream = io.BytesIO(bytes(json_data, 'utf-8'))
        pythondata = JSONParser().parse(stream=stream)
        serializer = PriceSerializer(data=pythondata) # create
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
            break


