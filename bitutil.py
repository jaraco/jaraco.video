
try:
	from jaraco.util.bitutil import *
except ImportError:
	# jaraco.util.bitutil is authoritative, but
	# keep a local copy to alleviate the dependency

	def get_bit_values(number, size=32):
		"""
		Get bit values as a list for a given number

		>>> get_bit_values(1) == [0]*31 + [1]
		True

		>>> get_bit_values(0xDEADBEEF)
		[1L, 1L, 0L, 1L, 1L, 1L, 1L, 0L, 1L, 0L, 1L, 0L, 1L, 1L, 0L, 1L, 1L, 0L, 1L, 1L, 1L, 1L, 1L, 0L, 1L, 1L, 1L, 0L, 1L, 1L, 1L, 1L]

		You may override the default word size of 32-bits to match your actual
		application.
		>>> get_bit_values(0x3, 2)
		[1L, 1L]
		
		>>> get_bit_values(0x3, 4)
		[0L, 0L, 1L, 1L]
		"""
		values = list(gen_bit_values(number))
		# 0-pad the most significant bit
		res = [0L]*(size-len(values))
		res.extend(reversed(values))
		return res

	def gen_bit_values(number):
		"""
		Return a zero or one for each bit of a numeric value up to the most
		significant 1 bit, beginning with the least significant bit.
		"""
		number = long(number)
		while number:
			yield number & 0x1
			number >>= 1

	def coalesce(bits):
		"""
		Take a sequence of bits, most significant first, and
		coalesce them into a number.
		
		>>> coalesce([1,0,1])
		5
		"""
		operation = lambda a, b: (a << 1 | b)
		return reduce(operation, bits)

	class Flags(object):
		"""
		Subclasses should define _names, a list of flag names beginning
		with the least-significant bit.
		
		>>> MyFlags = type('MyFlags', (Flags,), dict(_names=tuple('abc')))
		>>> mf = MyFlags.from_number(5)
		>>> mf['a']
		1L
		>>> mf['b']
		0L
		>>> mf['c'] == mf[2]
		True
		>>> mf['b'] = 1
		>>> mf['a'] = 0
		>>> mf.number
		6L
		"""
		def __init__(self, values):
			self._values = list(values)
			if hasattr(self, '_names'):
				n_missing_bits = len(self._names) - len(self._values)
				self._values.extend([0]*n_missing_bits)

		@classmethod
		def from_number(cls, number):
			return cls(gen_bit_values(number))

		@property
		def number(self):
			return coalesce(reversed(self._values))

		def __setitem__(self, key, value):
			# first try by index, then by name
			try:
				self._values[key] = value
			except TypeError:
				index = self._names.index(key)
				self._values[index] = value

		def __getitem__(self, key):
			# first try by index, then by name
			try:
				return self._values[key]
			except TypeError:
				index = self._names.index(key)
				return self._values[index]
