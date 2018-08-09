class node:
	def __init__(self, data):
		self.data = data
		self.next = None

class linkedList:
	def __init__(self, data):
		self.head = node(data)

	#travel through list by setting current node to the next node until the current nodes next value is null.
	#append by making a new node and setting that old last nodes next value to the new node
	def append(self,data):
		currentNode = self.head
		while currentNode.next != None:
			currentNode = currentNode.next

		currentNode.next = node(data)

	#change the head to your new node and make it link to the old head
	def prepend(self,data):
		newNode = node(data)
		newNode.next = self.head
		self.head = newNode

	#go through the list until you get to the element before your specified position. 
	#then, set the next value of the new element to that of the old element
	#and the next value of the old element to the new element
	def insert(self,data,position):
		#prepend if you want to insert at the start of the list
		if position == 0:
			self.prepend(data)
			return

		if position < 0:
			raise IndexError('Negative indexes are not supported')

		currentNode = self.head
		while currentNode.next != None:
			position -= 1
			if position == 0:
				newNode = node(data)
				newNode.next = currentNode.next
				currentNode.next = newNode
				return
			currentNode = currentNode.next

		if position == 1:
			self.append(data)
		else:
			raise IndexError('Index out of range')

	#go through list and once you reach node before node you want to delete,
	#change that node's next value to the node after the node you want to delete
	def remove(self,position):
		currentNode = self.head

		if position == 0:
			self.head = currentNode.next
			return

		if position < 0:
			raise IndexError('Negative indexes are not supported')

		while currentNode.next != None:
			position -= 1
			if position <= 0:
				currentNode.next = currentNode.next.next
				return
			currentNode = currentNode.next

		raise IndexError('Index out of range')

	#go through the list and append the value of each element to a human-readable array
	def display(self):
		elements = []
		currentNode = self.head
		elements.append(currentNode.data)
		while currentNode.next != None:
			currentNode = currentNode.next
			elements.append(currentNode.data)
		return elements

#testing functions
myList = linkedList(2)
myList.append(4)
myList.append(7)
myList.append(5)
myList.append(6)
myList.append(7)
myList.append(8)
myList.prepend(1)
myList.insert(3,2)
myList.remove(4)
print(myList.display())