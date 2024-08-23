
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
		if i+1<self.size and self.L[i] > self.L[i+1]: 
			self.__swap(i, i+1)
			self.__ordinateDown(i+1)
		elif +2<self.size and self.L[i] > self.L[i+2]:
			self.__swap(i, i+2)
			self.__ordinateDown(i+2)
	
	def dequeque(self) : 
		if(self.size > 0): 
			elem = self.L[0]
			self.L.pop(0)
			self.size = self.size -1
			self.__ordinateDown(0)
			return elem
		return -1
	
	def visualize(self): 
		print(self.L)

