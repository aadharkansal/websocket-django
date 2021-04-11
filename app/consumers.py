import json 
from random import randint
from time import sleep

from channels.generic.websocket import WebsocketConsumer

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        i = 0
        while(True):
            m = 'Here comes a new notification no: ' + str(i)
            self.send(json.dumps({'message':m}))
            i = i+1
            sleep(10)
