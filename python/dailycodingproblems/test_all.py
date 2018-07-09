import unittest
import problem1

class TestProbs(unittest.TestCase):

	#problem1.py
	def test_addCheck(self):
		self.assertEqual(problem1.addCheck([10, 3, 7], 10), True)
		self.assertEqual(problem1.addCheck([2, 5, 1, 1, 1, 5], 0), False)
		self.assertEqual(problem1.addCheck([10, -4, 3, -100], -1), True)
		self.assertEqual(problem1.addCheck([-1, -1, 2, -4, 4, -1], -2), True)
		self.assertEqual(problem1.addCheck([10, -4, 7, -1], -1), False)
		self.assertEqual(problem1.addCheck([-1, 0, 2], -2), False)
		self.assertEqual(problem1.addCheck([], -2), False)

if __name__ == '__main__':
	unittest.main()