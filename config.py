import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://cloud-api.yandex.net/v1/disk"
OAUTH_TOKEN = os.getenv("YANDEX_DISK_TOKEN", "ваш_тестовый_токен")

HEADERS = {
    "Authorization": f"OAuth {OAUTH_TOKEN}",
    "Content-Type": "application/json"
}