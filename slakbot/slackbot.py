#simple slack bot to send hello to channel!
#!/usr/bin/python3
#slackbot.py

#imports
from slackclient import SlackClient

token = 'your_token'

#connection to slackapi
slack_client = SlackClient(token)

#check the connection 
conn_bool = slack_client.rtm_connect(with_team_state=False)

#read the messages in the channel
events = slack_client.rtm_read()

#if events not none send a message
channel = 'your_channel'
text = 'your_text'
if events:
    slack_client.api_call("chat.postMessage", channel=channel, text=t)
