class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False
        self.count = 0

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for i in word:
            idx = ord(i) - ord('a')    
            if current.children[idx] == None:       
                current.children[idx] = TrieNode()
            current = current.children[idx] 
            current.count += 1 
        current.is_end = True 

    def search(self, word,ans):   
        current = self.root
        counter = 0
        for i in word:
            idx = ord(i) - ord('a')
            if current.children[idx] == None:   
                return
            current = current.children[idx]
            counter += current.count

        ans.append(counter) 

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        ans = []
        for word in words:
            self.insert(word)

        for word in words:
            self.search(word,ans)

        return ans
        
        