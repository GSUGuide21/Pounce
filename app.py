import os
import sys
import re
import json
import importlib.util
from flask import Flask, request
from urllib.parse import urlencode
from urllib.request import Request, urlopen

class PounceException(Exception):
	pass

app = Flask(__name__)

@app.route("/", methods=["POST"])
def webhook():
	data = request.get_json()
	print(data)
	if data["name"] != "Pounce":
		msg = logic.respond(data)
		print(msg)
		send_message(msg)
	
	return "ok", 200

def send_message(msg):
	url = "https://api.groupme.com/v3/bots/post"

	data = {
		"bot_id": os.getenv("GROUPME_BOT_ID"),
		"text": msg
	}

	print(data)

	request = Request(url, urlencode(data).encode())
	json = urlopen(request).read().decode()
	print(json)

def log(msg):
	print(str(msg))
	sys.stdout.flush()

if __name__ == "__main__":
	app.run(debug=True)