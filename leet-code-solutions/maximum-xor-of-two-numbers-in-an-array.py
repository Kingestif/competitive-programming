class TrieNode:
    def __init__(self):
        self.is_end = False
        self.child = [None for _ in range(2)]
class Solution:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, a) -> None:
        myTrie = self.trie
        for i in range(32):
            if myTrie.child[a[i]] == None:
                myTrie.child[a[i]] = TrieNode()
            myTrie = myTrie.child[a[i]]

        myTrie.is_end = True

    def search(self, arr):
        myTrie = self.trie
        ans = []
        for i in range(32):
            if myTrie.child[1-arr[i]] != None:
                ans.append(str(1-arr[i]))
                myTrie = myTrie.child[1-arr[i]]
            else:
                ans.append(str(arr[i]))
                myTrie = myTrie.child[arr[i]]
        ans = ''.join(ans)
        return int(ans, 2)

               

    def findMaximumXOR(self, nums: List[int]) -> int:
        arr = []
        maxx = 0
        for num in nums:
            myTrie = bin(num)[2:]
            a = [0] * (32 - len(myTrie))
            a.extend(int(t) for t in list(myTrie))
            # print(a)
            self.insert(a)
            maxx = max(maxx, num ^ self.search(a))
            arr.append(a)
        return maxx
        
    

            
        
        