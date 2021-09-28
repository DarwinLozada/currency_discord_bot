from furl import furl
import requests
import os  

CURRENCY_TOKEN = os.getenv('CURRENCY_API_KEY')

CURRENCY_API_BASE_URL = os.getenv('CURRENCY_API_BASE_URL')

def with_api_key(url):
  return furl(url).add({'api_key': CURRENCY_TOKEN}).url

def latest_value(base_currency):
  url_with_key = with_api_key(CURRENCY_API_BASE_URL + '/latest')
  url_with_base_currency = furl(url_with_key).add({'base': base_currency}).url

  response = requests.get(with_api_key(url_with_base_currency)).json()

  return 'El valor de {} es de {}'.format(base_currency, response['response']['rates']['USD'])

latest_value('AUD')