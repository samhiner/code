# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
#
# For example, given the following Node class:
class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

# The following test should pass:
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

def serialize(root, string=''):
	string += root.val
	string += '('
	if root.left != None:
		string = serialize(root.left,string)
	string += '|'
	if root.right != None:
		string = serialize(root.right,string)
	string += ')'
	return string
		

def deserialize(string):
	nestDepth = 0
	end = None

	for x in range(0,len(string)):
		if string[x] == ')':
			nestDepth -= 1

		if string[x] == '(':
			if nestDepth == 0:
				val = string[:x]
				argStart = x
			nestDepth += 1

		if string[x] == '|' and nestDepth <= 1:
			left = deserialize(string[argStart + 1:x])
			right = deserialize(string[x + 1:-1])
			end = Node(val, left, right)

	return end


node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'