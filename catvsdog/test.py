import unittest
from catvsdog import Vote, Challenge

class TestVote(unittest.TestCase):
	def setUp(self):
		self.vote = Vote('D1', 'C1')

	def testEdgeIsNone(self):
		assert self.vote.edge == None

	def testKeepAndThrow(self):
		assert self.vote.keepName == 'D1'
		assert self.vote.throwName == 'C1'
	
	def testFamily(self):
		assert Vote('D1', 'C1').getFamily() == 'D'
		assert Vote('C1', 'D1').getFamily() == 'C'
	
	def testCompatibility(self):
		dogFixture = Vote('D1', 'C1')
		catFixture = Vote('C1', 'D1')
		cat2Fixture = Vote('C2', 'D1')
		assert dogFixture.isCompatible(catFixture) == False
		assert dogFixture.isCompatible(dogFixture) == True
		assert catFixture.isCompatible(cat2Fixture) == True

	def testCollision(self):
		cat = Vote('D1', 'C1')
		dog = Vote('C1', 'D1')
		dog.nodeId = 10
		cat.addCollisionId(dog)
		self.assertEquals(cat.getCollisionsId(), [ 10 ])

class TestChallenge(unittest.TestCase):
	def setUp(self):
		self.challenge = Challenge(2, 3, 6)
	
	def testSetParameters(self):
		self.challenge.catsTotal == 2
		self.challenge.dogsTotal == 3
		self.challenge.votesTotal == 6

	def testCastVotes(self):
		self.challenge.cast(Vote('C1', 'D1'))
		self.challenge.cast(Vote('D1', 'C1'))		
		self.assertEquals(len(self.challenge.nodes_u), 1) 
		self.assertEquals(len(self.challenge.nodes_v), 1) 
		self.challenge.drawIncompatibilityGraph()
		self.assertEquals(self.challenge.nodes_u[0].getCollisionsId(), [ 1 ])	
		self.assertEquals(self.challenge.nodes_v[0].getCollisionsId(), [])	

	def testIncompatibilityMatcher(self):
		c = Challenge(1, 1, 2)
		c.cast(Vote('C1', 'D1'))
		c.cast(Vote('D1', 'C1'))
		c.cast(Vote('D1', 'C1'))
		c.drawIncompatibilityGraph()
		assert c.nodes_u[0].collisionsId == [ 1, 2 ]	
		total = c.minimumNodesCoverage()
		self.assertEquals(c.nodes_v_explored, [ 1 ])

class TestFunctionalLayer(unittest.TestCase):
	def testSampleOneToOne(self):
		c = Challenge(1, 1, 2)
		c.cast(Vote('C1', 'D1'))
		c.cast(Vote('D1', 'C1'))
		c.drawIncompatibilityGraph()
		self.assertEquals(c.maximizedTotal(), 1)
	
	def testSampleLargeMajority(self):
		c = Challenge(1, 2, 4)
		c.cast(Vote('C1', 'D1'))
		c.cast(Vote('C1', 'D1'))
		c.cast(Vote('C1', 'D2'))
		c.cast(Vote('D2', 'C1'))
		self.assertEquals(c.maximizedTotal(), 3)

	def testSampleEquity(self):
		c = Challenge(3, 3, 6)
		c.cast(Vote('C1', 'D1'))
		c.cast(Vote('C2', 'D2'))
		c.cast(Vote('C3', 'D3'))
		c.cast(Vote('D1', 'C1'))
		c.cast(Vote('D2', 'C2'))
		c.cast(Vote('D3', 'C3'))
		self.assertEquals(c.maximizedTotal(), 3)

	def testSampleGeneric(self):
		c = Challenge(2, 2, 11)
		c.cast(Vote('C2', 'D1'))
		c.cast(Vote('C2', 'D1'))
		c.cast(Vote('C2', 'D1'))
		c.cast(Vote('C1', 'D2'))
		c.cast(Vote('D2', 'C2'))
		c.cast(Vote('D2', 'C2'))
		c.cast(Vote('D2', 'C2'))	
		c.cast(Vote('D2', 'C1'))
		c.cast(Vote('D2', 'C1'))
		c.cast(Vote('D2', 'C1'))
		c.cast(Vote('D2', 'C1'))
		self.assertEquals(c.maximizedTotal(), 7)

if __name__ == '__main__':
	unittest.main();
