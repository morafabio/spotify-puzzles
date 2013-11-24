class Album:
	def __init__(self, totalSongs, selectSongs):
		self.totalSongs = int(totalSongs)
		self.selectSongs = int(selectSongs)
		self.songs = []

	def append(self, index, playcount, title):
		song = Song(index, playcount, title)
		self.songs.append(song)

	def zipfSort(self):
		c = self.songs[0].playcount
		for song in self.songs:
			song.fi = song.playcount / float(c / song.index)	
		return sorted(self.songs, key=lambda song: song.fi, reverse=True)

	def extract(self):
		return self.zipfSort()[:self.selectSongs]
	
class Song:
	def __init__(self, index, playcount, title):
		self.index = int(index)
		self.playcount = int(playcount)
		self.title = title

	def __repr__(self):
		return self.title
