import rpc
import websockets
import asyncio
import json
import nest_asyncio
import requests

# RPC handshake
rpc = rpc.RPC()
rpc.connect()


def update(obj):
    rpc.set_details(obj['title'])
    rpc.set_large_text(obj['title'])
    rpc.set_large_image('sc')
    rpc.update()
    pass

def progress(obj):
    rpc.set_state(obj['valuetext'])
    rpc.update()
    pass

def play(obj):
    if obj['value'] == True:
        rpc.update()
    else:
        rpc.clear()
    pass

fn_map = {
    'update': update,
    'progress': progress,
    'play': play
}

async def echo(websocket, path):
    i = 0
    async for message in websocket:
        obj = json.loads(message)
        nest_asyncio.apply()
        try:
            fn_map[obj['type']](obj)
        except:
            print("Wrong type key : " + obj['type'])

asyncio.get_event_loop().run_until_complete(websockets.serve(echo, 'localhost', 8765))
asyncio.get_event_loop().run_forever()
