from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)
TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
TELEGRAM_API_URL = f'https://api.telegram.org/bot{TOKEN}'

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = request.get_json()
    if 'message' in update:
        chat_id = update['message']['chat']['id']
        text = update['message'].get('text')
        if text:
            # پاسخ "اکو" به کاربر
            reply_url = f'{TELEGRAM_API_URL}/sendMessage'
            reply_data = {'chat_id': chat_id, 'text': f'شما گفتید: {text}'}
            requests.post(reply_url, json=reply_data)
    return 'OK', 200

@app.route('/')
def index():
    return "Bot is running!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
