class TrieNode: 
	
	def __init__(self): 
		self.children = [None]*70
		self.isEndOfWord = False
		self.myList = list()

class Trie: 
	
	def __init__(self): 
		self.root = self.getNode() 

	def getNode(self): 
	
		return TrieNode() 

	def _charToIndex(self,ch): 
		
		index = -1
		if(ord(ch) >= 48 and ord(ch) <= 57):
			index = ord(ch)-ord('1')+27
		elif(ord(ch) >= 65 and ord(ch) <= 90):
			index = ord(ch)-ord('A')+36
		else:
			index = ord(ch)-ord('a')
        
		return index

	def insert(self,key,url): 

		pCrawl = self.root 
		length = len(key) 
		for level in range(length): 
			index = self._charToIndex(key[level])
			
			if not pCrawl.children[index]:
				pCrawl.children[index] = self.getNode() 
			pCrawl = pCrawl.children[index] 
 
		pCrawl.isEndOfWord = True
		pCrawl.myList.append(url)

	def search(self, key): 
		
		pCrawl = self.root 
		length = len(key) 
		for level in range(length): 
			index = self._charToIndex(key[level]) 
			if not pCrawl.children[index]: 
				return False
			pCrawl = pCrawl.children[index] 

		test_list = list(set(pCrawl.myList))
		return test_list[0]