import os
import sys
import re
from random import randint, randrange

def fy(message):
	return "Fuck you, {}!".format(message["user"]["name"])

def flip(message, args):
	coins = ["Heads", "Tails"]
	types = ["lower", "upper", "letter"]
	type = (args and args[0] and isinstance(args[0], int) and args[0] > -1) or 0
	current_type = (type < len(types) and type) or ""

	coin_name = coins[randint(0, len(coins) - 1)]
	
	coin = ""

	if current_type == "lower": coin = coin_name.lower()
	elif current_type == "upper": coin = coin_name.upper()
	elif current_type == "letter": coin = coin_name[0]
	else: coin = coin_name

	return "Pounce has flipped the coin. The side of the coin is {}".format(coin)