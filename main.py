# Hi! Welcome to the Monkey Music Challenge Python starter kit!

import sys
import os
import urllib

# You control your monkey by sending POST requests to the Monkey Music server
GAME_URL = 'http://competition.monkeymusicchallenge.com/game';

# Don't forget to provide the right command line arguments
if len(sys.argv) < 4:
    print('Usage: python index.py <your-team-name> <your-api-key> <game-id>\n')
    if len(sys.argv) < 1:
        print('  Missing argument: <your-team-name>')
    if len(sys.argv) < 2:
        print('  Missing argument: <your-api-key>')
    if len(sys.argv) < 3:
        print('  Missing argument: <game-id>')
    sys.exit(1)

# You identify yourselves by your team name
team_name = sys.argv[1]
api_key = sys.argv[2]
game_id = sys.argv[3]

# We've put the AI-code in a separate module
import ai

def post_to_server(command):
    '''We use the requests library to POST JSON commands to the server.'''
    import json
    import requests

    command['team'] = team_name
    command['apiKey'] = api_key
    command['gameId'] = game_id

    print(command)
    print(json.dumps(command))

    # Every time we POST a command to the server, we get a reply back
    reply = requests.post(GAME_URL,
                          data=json.dumps(command),
                          headers={'Content-Type': 'application/json'})

    # Hopefully, our server will always be able to handle your requests
    # but you never know...
    if reply.status_code != requests.codes.ok:
        print('  The server replied with status code %d' % reply.status_code)
        try:
            print('  %s' % reply.json()['message'])
        except:
            pass
        sys.exit(1)

    # The server replies with the current state of the game
    current_game_state = reply.json()
    return current_game_state

# Allright, time to get started!

# Send a join game command and the server replies with the initial game state
current_game_state = post_to_server({'command': 'join game'})

# The current game state tells you if you have any turns left
while not current_game_state['isGameOver']:
    print('Remaining turns: %d' % current_game_state['remainingTurns'])

    # Use your AI to decide in which direction to move...
    next_command = ai.move(current_game_state)

    # After sending your next move, you'll get the new game state back
    current_game_state = post_to_server(next_command)

print('\nGame over.\n')
