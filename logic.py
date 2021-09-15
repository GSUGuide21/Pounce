import os
import sys
import re
import importlib.util
import commands

def respond(data):
	content = data["text"]
	name = data["name"]

	command_prefixes = ["pounce\s+", "p!\s*", "$", "(?:He(?:llo|y)\s+Pounce\,\s+)"]
	command_pattern = r"^(?:{})(.*)".format("|".join(command_prefixes))

	if re.search(command_pattern, content):
		match = re.search(command_pattern, content)
		target = match.group()

		parts = target.split("\s+")
		command_name = parts[0]

		args = parts[1:]

		if commands[command_name]:
			return dispatch_command(command_name, args, message = { 
				"content": content,
				"user": name
			})
		return dispatch_response(content)
		
	return content

def dispatch_command(command_name, args, message, user):
	content = message["content"]
	return content

def dispatch_response(message):
	content = message["content"]
	return content