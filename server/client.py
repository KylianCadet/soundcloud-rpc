import websockets
import asyncio

async def hello(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello world!")
        print("send")
        await websocket.recv()
        print("recv")

asyncio.get_event_loop().run_until_complete(
    hello('ws://localhost:8765'))