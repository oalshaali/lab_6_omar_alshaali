from lab_006_1 import Node

class LinkedList:
	def __init__(self, head = None, tail = None, size = 0):
		self.head = head
		self.tail = tail
		self.size = size

	def getHead(self):
		return(self.head)

	def setHead(self, h):
		self.head = h

	def getTail(self):
		return(self.tail)

	def setTail(self, t):
		self.tail = t

	def getSize(self):
		return(self.size)

	def setSize(self, s):
		self.size = s

	def isEmpty(self):
		if (self.getSize() == 0):
			return(True)
		return(False)

	def addNode(self, d):
		newNode = Node(data = d)
		if(self.isEmpty()):
			self.setHead(newNode)
		else:
			self.getTail().setPointer(newNode)
		self.setTail(newNode)
		self.setSize(self.size + 1)

def main():
	ll1 = LinkedList()
	ll1.addNode(10)
	ll1.addNode(20)
	ll1.addNode("AU")
	print(ll1.getTail().getData())

if __name__ == '__main__':
	main()