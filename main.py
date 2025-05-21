from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
URL_API = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

def responder_telegram(chat_id, texto):
    requests.post(f"{URL_API}/sendMessage", json={
        "chat_id": chat_id,
        "text": texto
    })

@app.route('/', methods=["GET"])
def home():
    return "Bot do Telegram está funcionando!"

@app.route('/webhook', methods=["POST"])
def webhook():
    data = request.get_json()
    
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        texto = data["message"].get("text", "")
        
        if texto.lower() == "/start":
            responder_telegram(chat_id, "Bot iniciado com sucesso!")
        else:
            responder_telegram(chat_id, f"Você disse: {texto}")

    return {"ok": True}