import requests
import logging
from config import BASE_URL, HEADERS

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class YaDiskClient:
    @staticmethod
    def get(path, params=None):
        logging.info(f"GET {path} params={params}")
        return requests.get(f"{BASE_URL}{path}", headers=HEADERS, params=params)

    @staticmethod
    def post(path, params=None, json=None):
        logging.info(f"POST {path} params={params}")
        return requests.post(f"{BASE_URL}{path}", headers=HEADERS, params=params, json=json)

    @staticmethod
    def put(path, params=None, json=None):
        logging.info(f"PUT {path} params={params}")
        return requests.put(f"{BASE_URL}{path}", headers=HEADERS, params=params, json=json)

    @staticmethod
    def delete(path, params=None):
        logging.info(f"DELETE {path} params={params}")
        return requests.delete(f"{BASE_URL}{path}", headers=HEADERS, params=params)