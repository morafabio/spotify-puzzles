class ReverseBinary:
    def convert(self, number):
        number = self.to_binary(number)
        number = self.reverse(number)
        return self.to_decimal(number)

    def to_binary(self, number):
        return bin(int(number))[2:]

    def reverse(self, string):
        return string[::-1]

    def to_decimal(self, number):
        return int(number, 2)
