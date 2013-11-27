#! /usr/bin/env python2.6
import sys
from catvsdog import Vote, Challenge

if __name__=='__main__':
	lines = []
	for line in sys.stdin:
		lines.append(line)
	lines.reverse()
	
	cases = int(lines.pop())

	for i in range(0, cases):	
		[ catsTotal, dogsTotal, votesTotal ] = map(int, lines.pop().split())
		c = Challenge(catsTotal, dogsTotal, votesTotal)

		for x in range(0, votesTotal):
			[ keepName, throwName ] = lines.pop().split()
			v = Vote(keepName, throwName)
			c.cast(v)
		
		print c.maximizedTotal()
 
