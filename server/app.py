import time
import rpc
import websockets
import asyncio
import json
import requests
import sys
import nest_asyncio


def update(obj):
    rpc.set_details(obj['title'])
    rpc.set_large_text(obj['title'])
    rpc.set_large_image('sc')
    rpc.set_small_image('sc')
    rpc.set_small_text("By: " + obj['user'])
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


def connect(obj):
    rpc.connect()


fn_map = {
    'update': update,
    'progress': progress,
    'play': play,
    'connect': connect
}

async def server_fn(websocket, path):
    async for message in websocket:
        obj = json.loads(message)
        try:
            fn_map[obj['type']](obj)
        except:
            print("Error in function : " + obj['type'])
            print(sys.exc_info())
            print()


rpc = rpc.RPC()

loop = asyncio.get_event_loop()

server = websockets.serve(server_fn, 'localhost', 8765)
loop.run_until_complete(server)

# Patch nested run_until_complete
nest_asyncio.apply(loop)

loop.run_forever()