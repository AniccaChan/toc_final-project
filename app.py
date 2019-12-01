import os
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
from transitions import Machine
app = Flask(__name__)

class foo(object):
    pass
# Channel Access Token
line_bot_api = LineBotApi(
    'kqdZOUNiHm/IgKxWwtjPH2sKpjwgiy0oPan2W6Jv1NpIDFumqV4KDwDnDRZ7o9wn2BTpmfmiHRmH9wxgRTggr0NwWkAU+MMgBBASB3KCF0WIRpKcDuWNmwcEPDcG+Rr2K13BhD/Nzp0FwK7S8lIR2QdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('fadfbe7cb1fe9875c7c9699e3a64a5d4')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token,TextSendMessage(machine.state))
    

if __name__ == "__main__":
    states = ['user', 'hungry', 'breakfast', 'lunch', 'dinner']
    transition = [
        {'trigger': 'I\'m hungry', 'source': 'user', 'dest': 'hungry'},
        {'trigger': 'no', 'source': 'user', 'dest': 'user'},
        {'trigger': 'dinner', 'source': 'hungry', 'dest': 'dinner'},
        {'trigger': 'lunch', 'source': 'hungry', 'dest': 'lunch'},
        {'trigger': 'breakfast', 'source': 'hungry', 'dest': 'breakfast'},
        {'trigger': 'another', 'source':['breakfast,lunch,dinner'], 'dest': None},
        {'trigger':'goback,','source':['breakfast,lunch,dinner'],'dest':'user'}
    ]
    machine = Machine(states=states,transitions=transition,initial='user')
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
