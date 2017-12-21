class player(object):
	stats = []
	statNames = ["gp", "gs", "min", "ppg", "offr", "defr", "rpg", "apg", "spg", "bpg", "tpg", "fpg", "ato", "per"]
	name = ""
	gp = 0
	gs = 0
	min = 0
	ppg = 0
	offr = 0
	defr = 0
	rpg = 0
	apg = 0
	spg = 0
	bpg = 0
	tpg = 0
	fpg = 0
	ato = 0
	per = 0
	
	def __init__(self, name):
		self.name = name
	# def gp(self, gp):
	# 	self.gp = gp
	def setStats(self, gp, gs, min, ppg, offr, defr, rpg, apg, spg, bpg, tpg, fpg, ato, per):
		self.gp = gp
		self.gs = gs
		self.min = min
		self.ppg = ppg
		self.offr = offr
		self.defr = defr
		self.rpg = rpg
		self.apg = apg
		self.spg = spg
		self.bpg = bpg
		self.tpg = tpg
		self.fpg = fpg
		self.ato = ato
		self.per = per
		self.stats = [gp, gs, min, ppg, offr, defr, rpg, apg, spg, bpg, tpg, fpg, ato, per]