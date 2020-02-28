class Node:
	def __init__(self, data, pointer = None):
		self.data = data
		self.pointer = pointer

	def getData(self):
		return(self.data)

	def setData(self, d):
		self.data = d

	def getPointer(self):
		return(self.pointer)

	def setPointer(self, p):
		self.pointer = p

def main():
	n1 = Node(data = 1)
	print(n1.getData())
	n1.setData(2)
	print(n1.getData())

if __name__ == '__main__':
	main()