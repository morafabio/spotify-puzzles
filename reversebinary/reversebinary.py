class ReverseBinary:
	def convert(self, number):
		return int(bin(int(number))[2:][::-1], 2)
