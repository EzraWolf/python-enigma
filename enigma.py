
"""
The uncrackable enigma
Made by Ezra W, or elixyr#0001
Version: 1.0
"""

# =========================================================================================== #
# =========================================================================================== #

import os
import sys
import git
import json
import string
import base64
import random
import itertools
from   pyenigma import enigma
from   pyenigma import rotor

# =========================================================================================== #
# =========================================================================================== #

# Update the program before anything else
#repo = git.Repo('<your repository folder location>')
#repo.remotes.origin.pull()


# =========================================================================================== #
# =========================================================================================== #

# Do JSON stuff
def JSON():

	# Set globals
	global ID
	global charEncode

	# Read file
	with open('config.json', 'r') as config:
		data = config.read()

	# Parse file
	obj = json.loads(data)

	# Read values
	ID         = (str(obj['ID']))
	charEncode = (str(obj['charEncode']))

	# Print values
	print('Your ID is: ' + ID)
	print('You are bas64 encoding with ' + charEncode)

# =========================================================================================== #
# =========================================================================================== #

# Generates random plug combos
def PLUGS():

	# Set globals
	global plugsStr

	# Make a random 20 letter string
	sample = 'ABCDEFGHIJKLMOPQRSTUVWXYZ'
	ID = ''.join((random.choice(sample) for i in range(20)))

	# Make a space every 2 letters to make 10 plug connectionss
	t = iter(ID)
	plugsStr = ' '.join(a + b for a, b in zip(t, t))

	# Print plugs
	print('\nThese are the plugs:')
	print(plugsStr)

# =========================================================================================== #
# =========================================================================================== #

# The enigma itself!
def ENIGMA(msg):

	# Set globals
	global enigmaMsg
	global engine

	# Set enigma rotars
	engine = enigma.Enigma(
		rotor.ROTOR_Reflector_A, 
		rotor.ROTOR_I,
		rotor.ROTOR_II, 
	    rotor.ROTOR_III, 
		key="ABC", plugs=plugsStr)

	# print(engine)

	# Encode the text!!
	enigmaMsg = engine.encipher(msg)

	# Print encoded text
	print('\nEncoded text:')
	print(enigmaMsg)

# =========================================================================================== #
# =========================================================================================== #

# Base64 encoding
def BASE64(msg):

	# Set globals
	global base64msg
	global base64msgBytes

	# Base64 encoded enigma encoded text
	base64msgBytes = msg.encode('UTF-8')
	base64bytes    = base64.b64encode(base64msgBytes)
	base64msg      = base64bytes.decode('UTF-8')

	# Print base64 stuff
	print('\nbase64 encoded enigma encoded text:')
	print(base64msg)

	# Print pre encoded message
	print('\nThis message is in UTF-8')
	print(base64msgBytes)
	

# =========================================================================================== #
# =========================================================================================== #

def RANDOM():

	# Set globals
	global seeed

	seeed = random.randrange(sys.maxsize)
	rng = random.Random(seeed)

	# Print seed
	print("This seed was ms ago")
	print(seeed)

# =========================================================================================== #
# =========================================================================================== #

# Start program

message1 = "Hello world"

JSON()
PLUGS()
ENIGMA(msg=message1)

# Jam it all in together as a base64
message2 = enigmaMsg + ' ' + tokenID
BASE64(msg=message2)

