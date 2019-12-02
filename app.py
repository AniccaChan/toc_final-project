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
import random
app = Flask(__name__)
class foo(object):
    pass
# Channel Access Token
line_bot_api = LineBotApi(
    'kqdZOUNiHm/IgKxWwtjPH2sKpjwgiy0oPan2W6Jv1NpIDFumqV4KDwDnDRZ7o9wn2BTpmfmiHRmH9wxgRTggr0NwWkAU+MMgBBASB3KCF0WIRpKcDuWNmwcEPDcG+Rr2K13BhD/Nzp0FwK7S8lIR2QdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('fadfbe7cb1fe9875c7c9699e3a64a5d4')
class toc_machine(object):
    passing = "not "
    quotes =['夏天的漂鳥飛來我的窗前歌唱又飛走了.而那無歌的,秋天的黃葉,隨風飄落以一聲歎息',
            '世上流浪兒的隊伍啊, 願留你們的足跡在我的話語之中.',
            '這世界面對它的戀人脫下"巨大"這個面具.它變得微小如歌,如永恆的吻.',
            '如果你因為錯失陽光而流淚,你也將錯失群星',
            '我不能選擇最好, 而是最好選擇了我',
            '將燈籠背負在背上的人們, 他們將影子投射到身前來.',
            '不要因為你自己沒有食慾而責怪食物.',
            '我們錯認這世界卻說它欺騙了我們.'
            ]
    def __init__(self,**machine_configs):
        self.machine = Machine(model=self, **machine_configs)
    def quots(self):
        self.passing = '夏天的漂鳥飛來我的窗前歌唱又飛走了.而那無歌的,秋天的黃葉,隨風飄落以一聲歎息'
    
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

def not_hungry(self):
    passing = "hmm? what are you doing then"
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    try:
        if(event.message.text == 'now'):
            line_bot_api.reply_message(event.reply_token,TextSendMessage(machine.state))
        else:
            machine.trigger(event.message.text)
            line_bot_api.reply_message(event.reply_token,TextSendMessage(machine.passing))
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage("error occur"))

if __name__ == "__main__":
    states = ['user', 'hungry', 'breakfast', 'lunch', 'dinner']
    transition = [
        {'trigger': '0', 'source': 'user', 'dest': 'user','after':'quots'},
        {'trigger': 'no', 'source': 'user', 'dest': 'user'},
        {'trigger': 'dinner', 'source': 'hungry', 'dest': 'dinner'},
        {'trigger': 'lunch', 'source': 'hungry', 'dest': 'lunch'},
        {'trigger': 'breakfast', 'source': 'hungry', 'dest': 'breakfast'},
        {'trigger': 'another', 'source':['breakfast','lunch','dinner'], 'dest': None},
        {'trigger':'goback','source':['breakfast','lunch','dinner','hungry'],'dest':'user'}
    ]
    machine = toc_machine(states=states,transitions=transition,initial='user')
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
