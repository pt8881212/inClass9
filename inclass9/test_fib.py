#Fibonacci unit test

import unittest
import fibonacci

class TestCase(unittest.TestCase):
	def test1(self):
		self.assertEqual(fibonacci.look(1), 1)

	def test2(self):
		self.assertEqual(fibonacci.look(5), 5)

	def test3(self):
		self.assertEqual(fibonacci.look(9), 34)

if __name__ == '__main__':
	unittest.main(verbosity=2)