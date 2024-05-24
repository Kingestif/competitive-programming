class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        current = self.root
        for i in word:
            idx = ord(i) - ord('a')
            if current.children[idx] == None:
                current.children[idx] = TrieNode()
            current = current.children[idx]
        current.is_end = True

    def search(self, word: str) -> bool:
        current = self.root
        def dfs(curr,i):
            if i == len(word):
                return curr.is_end

            if word[i] == ".":
                for child in curr.children:  #works out for all children
                    if child and dfs(child,i+1):
                        return True
                return False

            else:
                idx = ord(word[i]) - ord('a')
                if not curr.children[idx]:
                    return False
                return dfs(curr.children[idx],i+1)

        return dfs(current,0)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)