#! /usr/bin/env python2.6
import sys
from zipfsong import Album, Song

if __name__=='__main__':
	lines = []
	for line in sys.stdin:
		lines.append(line)

	counts = dict(zip(['totalTracks', 'selectTracks'], map(int, lines[0].split())))
		
	album = Album(counts['totalTracks'], counts['selectTracks'])

	for index in range(0, album.totalSongs):
		song = dict(zip(['playcount', 'title'], lines[index+1].split()))
		album.append(index+1, song['playcount'], song['title'])

	for song in album.extract():
		print song


		

		
