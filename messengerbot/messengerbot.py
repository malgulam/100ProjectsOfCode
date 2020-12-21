#simple messenger bot.I know this does not count fully as a bot more or less a
#pc with the graph api.But it can be extended and modified.
#In a haste at the moment with school.Will come back to modify this!
#let me know your suggestions on what the bot should do.

#!/usr/bin/python3

#messengerbot.py

#imports
import request

print('BOT STARTED')
print('THE BOT WILL TAKE INPUT YOU WISH TO SHARE')


def send_msg(msg:str):
    url = 'https://graph.facebook.com/v9.0/me/messages?access_token=<PAGE_ACCESS_TOKEN>'
    data_to_send = {
                'recipient': {
                    'id': sender_id
                },
                'message': {"text":f"{msg}"}
            }
    resp = requests.post(str(url)+f',json={data_to_send}').json()
    return response
return 'ok'

running = True
while running:
    try:
        msg_to_send = input(str('What will you like to publish?'))
        send_msg(msg=msg_to_send)
    except KeyboardInterrupt:
        print('quitting program')
        exit(1)
