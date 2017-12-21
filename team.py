class team(object):
	name = ""
	players = []
	def __init__(self, name):
		self.name = name
	# def gp(self, gp):
	# 	self.gp = gp
	def setPlayers(self, players):
		self.players = players