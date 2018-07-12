import unittest
import problem1
import problem2
import problem3
import problem4

class TestProbs(unittest.TestCase):

	def test_problem1(self):
		self.assertEqual(problem1.addCheck([10, 3, 7], 10), True)
		self.assertEqual(problem1.addCheck([2, 5, 1, 1, 1, 5], 0), False)
		self.assertEqual(problem1.addCheck([10, -4, 3, -100], -1), True)
		self.assertEqual(problem1.addCheck([-1, -1, 2, -4, 4, -1], -2), True)
		self.assertEqual(problem1.addCheck([10, -4, 7, -1], -1), False)
		self.assertEqual(problem1.addCheck([-1, 0, 2], -2), False)
		self.assertEqual(problem1.addCheck([], -2), False)

	def test_problem2(self):
		self.assertEqual(problem2.multArray([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])
		self.assertEqual(problem2.multArray([3, 2, 1]), [2, 3, 6])

	def test_problem3(self):
		binaryTree = problem3.Node('root', problem3.Node('left', problem3.Node('left.left')), problem3.Node('right'))
		self.assertEqual(problem3.deserialize(problem3.serialize(binaryTree)).left.left.val,'left.left')
		self.assertEqual(problem3.deserialize(problem3.serialize(binaryTree)).left.val,'left')
		self.assertEqual(problem3.deserialize(problem3.serialize(binaryTree)).right.val,'right')

	def test_problem4(self):
		self.assertEqual(problem4.lowestAbsentInt([3, 4, -1, 1]), 2)
		self.assertEqual(problem4.lowestAbsentInt([1, 2, 0]), 3)

'''
Template Unit Test:

	def test_(self):
		self.assertEqual(problemX.function(input),output)
'''

if __name__ == '__main__':
	unittest.main()