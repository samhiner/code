import unittest
import problem0001
import problem0002
import problem0003
import problem0004
import problem0005
import problem0007
import problem0011
import problem0019

class TestProbs(unittest.TestCase):

	def test_problem0001(self):
		self.assertEqual(problem0001.addCheck([10, 3, 7], 10), True)
		self.assertEqual(problem0001.addCheck([2, 5, 1, 1, 1, 5], 0), False)
		self.assertEqual(problem0001.addCheck([10, -4, 3, -100], -1), True)
		self.assertEqual(problem0001.addCheck([-1, -1, 2, -4, 4, -1], -2), True)
		self.assertEqual(problem0001.addCheck([10, -4, 7, -1], -1), False)
		self.assertEqual(problem0001.addCheck([-1, 0, 2], -2), False)
		self.assertEqual(problem0001.addCheck([], -2), False)

	def test_problem0002(self):
		self.assertEqual(problem0002.multArray([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])
		self.assertEqual(problem0002.multArray([3, 2, 1]), [2, 3, 6])

	def test_problem0003(self):
		binaryTree = problem0003.Node('root', problem0003.Node('left', problem0003.Node('left.left')), problem0003.Node('right'))
		self.assertEqual(problem0003.deserialize(problem0003.serialize(binaryTree)).left.left.val,'left.left')
		self.assertEqual(problem0003.deserialize(problem0003.serialize(binaryTree)).left.val,'left')
		self.assertEqual(problem0003.deserialize(problem0003.serialize(binaryTree)).right.val,'right')

	def test_problem0004(self):
		self.assertEqual(problem0004.lowestAbsentInt([3, 4, -1, 1]), 2)
		self.assertEqual(problem0004.lowestAbsentInt([1, 2, 0]), 3)

	def test_problem0005(self):
		self.assertEqual(problem0005.car(problem0005.cons(3, 4)),3)
		self.assertEqual(problem0005.cdr(problem0005.cons(3, 4)),4)

	def test_problem0007(self):
		self.assertEqual(problem0007.decodeWays('111'),3)
		self.assertEqual(problem0007.decodeWays('001'),0)

	def test_problem0011(self):
		self.assertEqual(problem0011.autocomplete('de',['dog','deer','deal']),['deer','deal'])
		self.assertEqual(problem0011.autocomplete('deo',['dog','deer','deal']),[])

	def test_problem0019(self):
		self.assertEqual(problem0019.cheapestRow([[1,2,3],[1,2,7],[2,3,4]]),5)
		self.assertEqual(problem0019.cheapestRow([[1,2,3],[1,2,-3],[8,6,4]]),4)


'''
Template Unit Test:

	def test_(self):
		self.assertEqual(problemX.function(input),output)
'''

if __name__ == '__main__':
	unittest.main()