import requests
import json
import os
import sys

# We communicate with this server.
# For this challenge, no changes should be made here.
SERVER = os.getenv('SERVER', 'http://warmup.monkeymusicchallenge.com')

# Teamname and API key are both provided as environmental variables
# For an easy example on how to specify these see README.md
TEAM = os.getenv('TEAM', None)
API = os.getenv('API', None)

if TEAM == None or API == None:
	print('ERROR: Please provide teamname and api key as follows: \nTEAM=myteamname API=XXXX python src/index.py')
	sys.exit()

# The ai module should be the entry-point to your code
import ai

def post(data):
	"""Posts the provided data along with the apiKey to the server

	Args:
		data: A dict with at least the key 'command'.
					Some commands might require additional keys too.
	"""
	# Append the api key to all post requests
	data.update({ 'apiKey': API })

	# Send the request to our server, expect JSON back
	r = requests.post(
		SERVER + '/' + TEAM,
		data=json.dumps(data),
		headers={ 'Content-Type': 'application/json' }
		)

	# All responses that are not okay are treated as critical
	if r.status_code is not 200:
		print('Error', r.text)

	return r


# Make an initial post to start the game
data = { 'command': 'new game' }
r = post(data)

# Start making move requests
while r:
	# Read response from last request
	gameState = r.json()

	# Make a move
	direction = ai.move(gameState)

	if gameState['turns'] <= 0:
		print('Game over.')
		break

	data = {
		'command': 'move',
		'direction': direction
	}

	# Post next move to server
	r = post(data)
