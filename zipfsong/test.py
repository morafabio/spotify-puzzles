import unittest
from zipfsong import Song, Album

class TestSong(unittest.TestCase):
	
	def setUp(self):
		self.song = Song(2, 10, 'yellow_submarine')
	
	def testParameters(self):
		assert self.song.index == 2
		assert self.song.playcount == 10
		assert self.song.__repr__() == 'yellow_submarine'
	
	def testFi(self):
		self.song.fi = 1.23
		assert self.song.fi == 1.23

class TestAlbum(unittest.TestCase):
	def setUp(self):
		self.album = Album(5, 2)

	def testParameters(self):
		assert self.album.totalSongs == 5
		assert self.album.selectSongs == 2
		
	def testAppendSong(self):
		self.album.append(1, 30, 'one')
		assert len(self.album.songs) == 1

	def testZipfSortKeepingTracklistPrecedence(self):
		album = Album(5, 2)
		album.append(1, 30, 'one')
		album.append(2, 30, 'two')
		album.append(3, 15, 'three')
		album.append(4, 25, 'four')
		album.append(5, 6, 'five')
		
		songs = album.zipfSort()

		assert songs[0].title == 'four'	
		assert songs[1].title == 'two'	
		assert songs[2].title == 'three'
	
		assert songs[3].fi == songs[4].fi
		assert songs[3].title == 'one'	
		assert songs[4].title == 'five'	

if __name__ == '__main__':
	unittest.main();
