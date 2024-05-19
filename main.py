from telethon import TelegramClient, sync, events
import json
import random 

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

api_id = config['login']['api_id']
api_hash = config['login']['api_hash']


with TelegramClient('session', api_id, api_hash) as client:
    for dialog in client.iter_dialogs():
        if dialog.is_channel:
            continue  
        else:
            @client.on(events.NewMessage(chats= -1001196831703, blacklist_chats=True))
            async def handler(event):
                await event.reply(random.choice(list(config['message'])))
                
        client.run_until_disconnected()
