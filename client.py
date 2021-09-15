import os
import json
import re
import random
import requests
import logic

import importlib.util

class GroupMeException(Exception):
    pass

@app.route()
class GroupMeClient(object):
    def __init__(self, client_id):
        self.client_id = client_id
        self.bot_id = self.client_id
    def __repr__(self):
        return "GroupMeClient(%s)" % self.client_id
    
    def send_message(self, text):
        # Sends a message to the group chat
