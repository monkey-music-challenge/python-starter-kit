import random

def move(current_game_state):
    '''This is where you put your AI code!

    The AI looks at the current game state and decides
    the monkey's next move.'''

    # Go to http://github.com/monkey-music-challenge/core
    # for more info about the rules of Monkey Music Challenge

    # TODO: You may want to do something smarter here
    return {'command': 'move',
            'direction': random.choice(['up', 'down', 'left', 'right'])}
