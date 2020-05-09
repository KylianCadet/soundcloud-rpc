import rpc
import websockets
import asyncio
import json
import nest_asyncio


rpc.connect()

async def echo(websocket, path):
    i = 0
    async for message in websocket:
        obj = json.loads(message)
        nest_asyncio.apply()
        rpc.update(obj['valuetext'])
        # await websocket.send(message)

asyncio.get_event_loop().run_until_complete(websockets.serve(echo, 'localhost', 8765))
asyncio.get_event_loop().run_forever()