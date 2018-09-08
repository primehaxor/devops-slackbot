from datetime import datetime
from slackclient import SlackClient
import json


import yaml
with open("conf.yml") as blogs:
   conf = yaml.load(blogs)

today = datetime.now()
brl_date = today.strftime('%d-%m-%Y')
slack_token = conf['slack_token']
slack_channel = conf['slack_channel']
sc = SlackClient(slack_token)

def ReportNews(title, link, summary):
    att = [
        {
            "text": "*New Blog Post* \n *Title:* %s \nMore details at %s" %(title, link),
        }
    ]
    sc.api_call(
    "chat.postMessage",
    channel=slack_channel,
    reply_broadcast=True,
    username="BeepBoop",
    icon_emoji=':robot_face:',
    attachments=json.dumps(att)

    )
