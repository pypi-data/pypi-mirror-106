class tempDatabase:
	def __init__(self, dataList, name):
		self.data = {}
		self.name = name
		for point in dataList:
			self.data[point] = dataList[point]

	def findByName(self, index):
		if index in self.data:
			return True
		else:
			return False

	def findByValue(self, index):
		gotKey = False
		for key in self.data:
			if self.data[key] == index and gotKey == False:
				gotKey = True
				return True
			elif self.data[key] != index and gotKey == False:
				continue
			return False

	def add(self, keyName, keyValue):
		if keyName in self.data:
			return False
		else:
			self.data[keyName] = keyValue

	def printall(self):
		for key in self.data:
			print("{}: {}".format(key, str(self.data[key])))

	def maketext(self):
		text = open("tmp.txt", "w")
		for key in self.data:
			text.write(key + ": " + str(self.data[key]))
		text.close()

def cooltext(text, its):
	listoftext = list(text)
	tok = ""
	x = 0
	while x != its + 1:
		if tok == text:
			tok = ""
		for char in listoftext:
			tok += char
			print(tok)
		x += 1

