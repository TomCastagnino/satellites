import requests
import sys


PORT = sys.argv[-1]
NAME = 'satellite_' + PORT

def setUp():
    """Saving satellite in Earth's db"""
    
    endpoint = 'http://127.0.0.1:8000/api/register_satellite/'

    print(sys.argv)

    payload = {
        'name': NAME,
        'port': PORT
    }

    try:
        r = requests.post(endpoint, data=payload)
        print(r)
    except requests.exceptions.ConnectionError as e:
        print("Earth's server is probably down", e)
