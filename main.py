# Hi! Welcome to the Monkey Music Challenge Python starter kit!

import sys
import os

# You control your monkey by sending POST requests to the Monkey Music server
server_url = 'http://warmup.monkeymusicchallenge.com';

# Don't forget to provide the right command line arguments
if len(sys.argv) < 3:
    print('Usage: python index.py <your-team-name> <your-api-key>\n')
    if len(sys.argv) < 1:
        print('  Missing argument: <your-team-name>')
    if len(sys.argv) < 2:
        print('  Missing argument: <your-api-key>')
    sys.exit(1)

# You identify yourselves by your team name
team_name = sys.argv[1]
api_key = sys.argv[2]

# You POST to a team-specific URL:
# warmup.monkeymusicchallenge.com/team/<your-team-name>
# Surf to this URL and watch your monkey carry out your commands!
team_url = '%s/team/%s' % (server_url, team_name)

# We've put the AI-code in a separate module
import ai

def post_to_server(command):
    '''We use the requests library to POST JSON commands to the server.'''
    import json
    import requests

    # Every time we POST a command to the server, we get a reply back
    reply = requests.post(team_url,
                          data=json.dumps(command),
                          headers={'Content-Type': 'application/json'})

    # Hopefully, our server will always be able to handle your requests
    # but you never know...
    if reply.status_code != requests.codes.ok:
        print('Error! We seem to have trouble talking to the server...\n')
        print('  The server replied with status code %d and message: %s' % (reply.status_code, reply.text))
        sys.exit(1)

    # The server replies with the current state of the game
    current_game_state = reply.json()

    return current_game_state

# Allright, time to get started!

# Make an initial post to start the game
new_game_command = {
    'command': 'new game',
    'apiKey': api_key,
}

# The server replies with the initial game state
current_game_state = post_to_server(new_game_command)

# The current game state tells you if you have any turns left
while current_game_state['turns'] > 0:

    print('Remaining turns: %d' % current_game_state['turns'])

    # Use your AI to decide in which direction to move...
    next_move_direction = ai.move(current_game_state)

    # ...and send a new move command to the server
    next_move_command = {
        'command': 'move',
        'direction': next_move_direction,
        'apiKey': api_key,
    }

    # After sending your next move, you'll get a new reply
    # and we start at the top of the loop again
    current_game_state = post_to_server(next_move_command)

# If the game is over, our server will tell you how you did
# Go to warmup.monkeymusicchallenge.com/team/<your-team-name> for more details
print('\nGame over.\n')
print('  ' + current_game_state['hint'])
