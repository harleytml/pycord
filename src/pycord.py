import requests
import json

class Bot:
    def __init__(self, token):
        self.token = token
    def sendMessage(self, content, channelid):
        baseURL = "https://discordapp.com/api/channels/{}/messages".format(channelid)

        headers = {
            "Authorization": "Bot {}".format(self.token),
            "UserAgent": "myBotThing (http://some.url, v0.1)",
            "Content-Type": "application/json"
        }
        POSTedJSON = json.dumps( {"content": content} )
        r = requests.post(baseURL, headers=headers, data=POSTedJSON)