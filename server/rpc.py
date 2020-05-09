import pypresence
import time
import os

client_id = os.environ['CLIENT_ID']
RPC = pypresence.Presence(client_id)

def connect():
    RPC.connect()

def update(state):
    RPC.update(state=state)