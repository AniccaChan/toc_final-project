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
    #[['name'],['add'],['open_time']]
    breakfast=[['麥當勞-台南大學店',' 701台南市東區大學路26號','24/7'],
            ['7-ELEVEN 育樂門市','台南市東區勝利路118號','24/7'],
            ['勝利早點','台南市東區勝利路119號','16:30-10:30'],
            ['老丘早餐','台南市東區勝利路135號','06:00-12:00'],
            ['大成美食','台南市東區大學路西段47號','06:00-12:00（週日公休）'],
            ]
    lunch=[['麥當勞-台南大學店',' 701台南市東區大學路26號','24/7'],
            ['7-ELEVEN 育樂門市','台南市東區勝利路118號','24/7'],
            ['勝利早點','台南市東區勝利路119號','16:30-10:30'],
            ['紅樓小館','台南市東區勝利路165巷11號','11:00~22:00周一公休'],
            ['水餃之家','台南市北區長勝路5號','週一~週五 11:10-14:00;17:00-20:00;週六 11:10-14:00'],
            ['廣越美食','台南市北區長榮路四段108號','11:00-15:00、16:30-20:00'],
            ['老友小吃','台南市北區勝利路268號','10:00-21:30'],
            ['紅番茄生活餐飲屋','台南市東區勝利路22號之1','10:30-20:30']
            ]
    dinner =[['麥當勞-台南大學店',' 701台南市東區大學路26號','24/7'],
            ['7-ELEVEN 育樂門市','台南市東區勝利路118號','24/7'],
            ['紅樓小館','台南市東區勝利路165巷11號','11:00~22:00周一公休'],
            ['水餃之家','台南市北區長勝路5號','週一~週五 11:10-14:00;17:00-20:00;週六 11:10-14:00'],
            ['廣越美食','台南市北區長榮路四段108號','11:00-15:00、16:30-20:00'],
            ['老友小吃','台南市北區勝利路268號','10:00-21:30'],
            ['紅番茄生活餐飲屋','台南市東區勝利路22號之1','10:30-20:30']]
    def __init__(self,**machine_configs):
        self.machine = Machine(model=self, **machine_configs)
    def quots(self):
        self.passing = random.choice(self.quotes)+'\n\n餓了按1 再來一句按0'
    def welcome(self):
        self.passing = "餓了嗎? 餓了按1 不餓 就想聽聽幹話按0"
    def is_hungry(self):
        self.passing = "找早餐按1 找午餐按2 找晚餐按3 返回按0"
    def find_dinner(self):
        din = random.choice(self.dinner)
        self.passing = "我找到 {0}\n地址在: {1}\n營業時間: {2}\n再找一家按1, 返回按0".format(din[0],din[1],din[2])
    def find_lunch(self):
        lun = random.choice(self.lunch)
        self.passing = "我找到 {0}\n地址在: {1}\n營業時間: {2}\n再找一家按1, 返回按0".format(lun[0],lun[1],lun[2])
    def find_breakfast(self):
        bre = random.choice(self.breakfast)
        self.passing = "我找到 {0}\n地址在: {1}\n營業時間: {2}\n再找一家按1, 返回按0".format(bre[0],bre[1],bre[2])
    
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
    except Exception:
        line_bot_api.reply_message(event.reply_token,TextSendMessage("error occur"))

if __name__ == "__main__":
    
    states = ['user', 'hungry', 'breakfast', 'lunch', 'dinner']
    transition = [
        {'trigger': '0', 'source': 'user', 'dest': 'user','after':'quots'},
        {'trigger': '1', 'source': 'user', 'dest': 'hungry','after':'is_hungry'},
        {'trigger': '3', 'source': 'hungry', 'dest': 'dinner','after':'find_dinner'},
        {'trigger': '2', 'source': 'hungry', 'dest': 'lunch','after':'find_lunch'},
        {'trigger': '1', 'source': 'hungry', 'dest': 'breakfast','after':'find_breakfast'},
        {'trigger': '1', 'source':['breakfast','lunch','dinner'], 'dest': None,'after':['find_breakfast','find_lunch','find_dinner']},
        {'trigger':'0','source':['breakfast','lunch','dinner','hungry'],'dest':'user','before':'welcome'}
    ]
    machine = toc_machine(states=states,transitions=transition,initial='user')
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
