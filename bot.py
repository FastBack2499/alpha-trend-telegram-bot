import os
import json
from flask import Flask, request
from dotenv import load_dotenv
import requests

load_dotenv()
app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"
ALLOWED_EXCHANGES = ['BINANCE', 'COINBASE', 'BYBIT', 'KRAKEN', 'BITSTAMP', 'CRYPTO', 'CRYPTOCAP', 'OKX']
USERS_FILE = "users.json"

# Load or initialize users
if os.path.exists(USERS_FILE):
    with open(USERS_FILE, "r") as f:
        users = json.load(f)
else:
    users = []

def save_users():
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)

def is_crypto_ticker(ticker):
    if ":" in ticker:
        exchange, _ = ticker.split(":")
        return exchange.upper() in ALLOWED_EXCHANGES
    return False

def send_message(user_id, text):
    payload = {"chat_id": user_id, "text": text, "parse_mode": "Markdown"}
    requests.post(f"{API_URL}/sendMessage", json=payload)

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    data = request.get_json()
    ticker = data.get("ticker", "")
    action = data.get("action", "").upper()
    price = data.get("price", "")

    if not is_crypto_ticker(ticker):
        return "Ignored — not a crypto asset", 200

    message = f"📈 *{action} Signal* for `{ticker}` 💰 Price: `{price}`"
    for user_id in users:
        send_message(user_id, message)
    return "OK", 200

@app.route(f"/{BOT_TOKEN}/start", methods=["POST"])
def start():
    data = request.get_json()
    chat_id = data["message"]["chat"]["id"]
    if chat_id not in users:
        users.append(chat_id)
        save_users()
        send_message(chat_id, "✅ You're now subscribed to AlphaTrend crypto signals.")
    return "OK", 200

if __name__ == "__main__":
    app.run(port=5000)
