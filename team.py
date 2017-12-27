#Team object
#Holds team name and an array of players with their respective game statistics
class team(object):
	name = ""
	players = []
	#constructor sets the name of the team
	def __init__(self, name):
		self.name = name
	#appends to the player array with given player objects
	def setPlayers(self, players):
		self.players = players