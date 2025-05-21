from flask import Flask, request
import telegram
import os

TOKEN = os.environ.get('TELEGRAM_TOKEN')  # Seu token deve estar na variável de ambiente
bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

# Dicionário de comandos e respostas
comandos = {
    "/miajuda": """OIEEEE, TOMA OS COMANDOSSS 🐝🐝🐝🐝🐝🐝

Destrava esses APDs caraio

/miajuda
/bora
/AZ
/TTP
/ICX
/OGX
/RECU
/APL""",

    "/bora": "FALAAA @AB 🐝🐝🐝🐝🐝 bora chegar no top 1 da BAZI? tô aqui para ajudar na animação da galera, usa /miajuda pra ver meus comandos e bora dar APDDDDDD🐝🐝🐝🐝",

    "/AZ": "AHHHHHH! EU QUERO VER O ABC IR DO A ATÉ Z!!!!!!",

    "/TTP": "TUMTUMPA TUMTUMPA TUMTUMPA",

    "/ICX": "CX É DO CARALHOWWWWW 🌿 WELCOME TO THE JUNGLEEEE",

    "/OGX": "OGX É GRITARIAAAAAAAAAAAAAA 🗣️ BATE META TODO DIAAAAAAAAAAAAAAA",

    "/RECU": "ME DA UM REEEE ME DA UM CUUUU 🍑 TODO MUNDO AMA RECUUUU",

    "/APL": "EM ALGUM LUGAR ENTRE LIDERANÇA E DOIDEIRA: APL 🧠💥"
}

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat_id
    message = update.message.text.strip()

    # Verifica se o texto é um comando
    resposta = comandos.get(message)
    if resposta:
        bot.send_message(chat_id=chat_id, text=resposta)
    else:
        bot.send_message(chat_id=chat_id, text="Comando não reconhecido. Use /miajuda para ver os comandos disponíveis 🐝")
    return 'ok'

@app.route('/')
def index():
    return 'Bot está vivo!'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
