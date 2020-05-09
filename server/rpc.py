import pypresence
import time
import os

from threading import Thread


class RPC():
    def __init__(self, loop=None, handler=None):
        self._RPC = pypresence.Presence(self.client_id, loop=loop, handler=handler)

    client_id = os.environ['CLIENT_ID']
    state = None
    details = None
    start = None
    end = None
    large_image = None
    large_text = None
    small_image = None
    small_text = None
    party_id = None
    party_size = None
    join = None
    spectate = None
    match = None
    instance = True
    _connected = False

    def connect(self):
        self._RPC.connect()
        self._connected = True

    def clear(self):
        self._RPC.clear()

    def update_progress(self, time):
        self.details = time

    def set_state(self, new_state):
        self.state = new_state

    def set_details(self, new_details):
        self.details = new_details

    def set_start(self, new_start):
        self.start = new_start

    def set_end(self, new_end):
        self.end = new_end

    def set_large_image(self, new_large_image):
        self.large_image = new_large_image

    def set_large_text(self, new_large_text):
        self.large_text = new_large_text

    def set_small_image(self, new_small_image):
        self.small_image = new_small_image

    def set_small_text(self, new_small_text):
        self.small_text = new_small_text

    def set_party_id(self, new_party_id):
        self.party_id = new_party_id

    def set_party_size(self, new_party_size):
        self.party_size = new_party_size

    def set_join(self, new_join):
        self.join = new_join

    def set_spectate(self, new_spectate):
        self.spectate = new_spectate

    def set_match(self, new_match):
        self.match = new_match

    def set_instance(self, new_instance):
        self.instance = new_instance

    def _update(self):
        self._RPC.update(state=self.state,
                         details=self.details,
                         start=self.start,
                         end=self.end,
                         large_image=self.large_image,
                         large_text=self.large_text,
                         small_image=self.small_image,
                         small_text=self.small_text,
                         party_id=self.party_id,
                         party_size=self.party_size,
                         join=self.join,
                         spectate=self.spectate,
                         match=self.match,
                         instance=self.instance)

    def update(self):
        if not self._connected:
            print("Receive update call but not connected")
            return
        self._update()
