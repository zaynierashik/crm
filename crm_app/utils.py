import requests
from django.core.cache import cache

API_KEY = '1ee71ebf17e1283098833da1'
EXCHANGE_RATE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"

def get_exchange_rates():
    exchange_rates = cache.get('exchange_rates')
    
    if not exchange_rates:
        try:
            response = requests.get(EXCHANGE_RATE_URL)
            data = response.json()

            if data['result'] == "success":
                rates = data['conversion_rates']
                exchange_rates = {
                    'USD': rates['USD'],
                    'NPR': rates['NPR'],
                    'INR': rates['INR']
                }
                cache.set('exchange_rates', exchange_rates, timeout=60 * 60)
            else:
                exchange_rates = {'USD': 1, 'NPR': 0.0076, 'INR': 0.012}
        except requests.RequestException:
            exchange_rates = {'USD': 1, 'NPR': 0.0076, 'INR': 0.012}
    return exchange_rates