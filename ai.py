import random

def move(gameState):
	"""Returns

	Args:
		gameState: A dict describing the gameState as sent by the server

	Return:
		a string 'up'|'down'|'right'|'left'
	"""
	# Note that the position comes in an array of [y,x]
	# while all other positions in this example are handled
	# as [x,y]
	position = {
		'x': gameState['position'][1],
		'y': gameState['position'][0]
	}

	d = random.randint(0, 3)
	if d is 0:
		return 'up'
	if d is 1:
		return 'down'
	if d is 2:
		return 'left'
	if d is 3:
		return 'right'
