class Vote:
	def __init__(self, keepName, throwName):
		self.keepName = keepName 
		self.throwName = throwName
		self.collisionsId = []
		self.edge = None

	def getFamily(self):
		return self.keepName[0]

	def isCompatible(self, vote):
		if vote.throwName == self.keepName: return False
		if vote.keepName == self.throwName: return False		
		return True
	
	def addCollisionId(self, vote):
		self.collisionsId.append(vote.nodeId)

	def getCollisionsId(self):
		return self.collisionsId

class Challenge:
	def __init__(self, catsTotal, dogsTotal, votesTotal):
		self.catsTotal = catsTotal
		self.dogsTotal = dogsTotal 
		self.votesTotal = votesTotal
		self.nodes_u = []
		self.nodes_v = []

	def cast(self, vote):
		vote.nodeId = len(self.nodes_u) + len(self.nodes_v)
		if vote.getFamily() == 'C':
			self.nodes_u.append(vote)
			return
		if vote.getFamily() == 'D':
			self.nodes_v.append(vote)
			return

	def drawIncompatibilityGraph(self):
		for uNode in self.nodes_u:
			for vNode in self.nodes_v:
				if not uNode.isCompatible(vNode):
					uNode.addCollisionId(vNode)

	def minimumNodesCoverage(self):
		total = 0
		for uNode in self.nodes_u:
			self.uNodesResetExplored()
			if self.uNodeMatch(uNode):
				total += 1
		return total
		
	def uNodeMatch(self, uNode):
		if uNode == None: return False
	
		for nodeId in uNode.getCollisionsId():
			if self.uNodeIsExplored(nodeId):
				return False
			self.uNodeMarkExplored(nodeId)
			vNode = self.uNodeGet(nodeId)
			isMatched = self.uNodeMatch(vNode.edge)
			if vNode.edge == None or isMatched:
				self.drawEdge(vNode, uNode)
				return True 

	def uNodeGet(self, nodeId):
		return filter(lambda v: v.nodeId == nodeId, self.nodes_v)[0]

	def uNodeMarkExplored(self, nodeId):
		self.nodes_v_explored.append(nodeId)

	def uNodesResetExplored(self):
		self.nodes_v_explored = []

	def uNodeIsExplored(self, nodeId):
		return nodeId in self.nodes_v_explored	
	
	def drawEdge(self, v, u):
		u.edge = v
		v.edge = u

	def maximizedTotal(self):
		self.drawIncompatibilityGraph()
		edgeNumber = self.minimumNodesCoverage()	
		return self.votesTotal - edgeNumber

