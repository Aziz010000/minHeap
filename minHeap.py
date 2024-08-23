
class minHeap:
	def __init__(self): 
		self.L = []
		self.size = 0
	
	def __swap(self, i, j): 
		temp = self.L[i]
		self.L[i] = self.L[j]
		self.L[j] = temp
		
	def __ordinateUp(self,i): 
		index = (int)((i-1)/2)
		if self.L[i] != 0 and self.L[i] < self.L[index] :
			self.__swap(i, index)
			self.__ordinateUp(index)
			
	def enqueque(self, num): 
		self.L.append(num)
		self.size = self.size+1
		self.__ordinateUp(self.size-1)
	
	def __ordinateDown(self,i):
		index = i
		if 2*i+1 < self.size and self.L[index] > self.L[i*2+1]: 
			index = i*2+1
		if 2*i+2 < self.size and self.L[index] > self.L[i*2+2]: 
			index = i*2+2
		if index != i :
			self.__swap(i, index) 
			self.__ordinateDown(index)
	
	def dequeque(self) : 
		if(self.size > 0): 
			elem = self.L[0]
			self.size = self.size -1
			self.L[0] = self.L[len(self.L)-1]
			self.L.pop(len(self.L)-1)
			self.__ordinateDown(0)
			return elem
		return -1
	
	def visualize(self): 
		print(self.L)


myHeap = minHeap() 
myHeap.enqueque(27)
myHeap.enqueque(5)
myHeap.dequeque()
myHeap.enqueque(2)
myHeap.enqueque(4)
myHeap.enqueque(1)
myHeap.enqueque(28)
myHeap.dequeque()
myHeap.enqueque(9)
myHeap.enqueque(6)
myHeap.enqueque(11)
myHeap.enqueque(77)
myHeap.enqueque(14)
myHeap.enqueque(10)
myHeap.enqueque(21)
myHeap.enqueque(108)
myHeap.visualize()
myHeap.dequeque()
myHeap.dequeque()
myHeap.dequeque()
myHeap.dequeque()
myHeap.dequeque()
print("VISUALIZZANDO")
myHeap.visualize()
