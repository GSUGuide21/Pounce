import os
import sys
import re
import json

import importlib.util

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

import logic

app = Flask(__name__)

@app.route("/", methods=["POST"])
def webhook():
	data = request.get_json()

	if data["name"] != "Pounce":
		msg = logic.respond(data)
		send_message(msg)
	
	return "ok", 200

def send_message(msg):
	url = "https://api.groupme.com/v3/bots/post"

	data = {
		"bot_id": os.getenv("GROUPME_BOT_ID"),
		"text": msg
	}

	request = Request(url, urlencode(data).encode())
	json = urlopen(request).read().decode()

def log(msg):
	print(str(msg))
	sys.stdout.flush()