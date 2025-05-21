from flask import Flask, request
import telegram
import os

TOKEN = os.environ.get('TELEGRAM_TOKEN')  # Seu token deve estar na variável de ambiente
bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat_id
    message = update.message.text

    bot.send_message(chat_id=chat_id, text=f"Você disse: {message}")
    return 'ok'

@app.route('/')
def index():
    return 'Bot está vivo!'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
