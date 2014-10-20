import random

def randomDirection():
	return ['up', 'down', 'left', 'right'][random.randint(0, 3)]

def move(gameState):
	"""Returns

	Args:
		gameState: A dict describing the gameState as sent by the server

	Return:
		a string 'up'|'down'|'right'|'left'
	"""

	return randomDirection()
