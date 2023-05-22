import os
from dotenv import load_dotenv
load_dotenv()


BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMINS = [436733159]

ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

redis = {
    'adress': (ip, 6379),
    'encoding': 'utf8'
}