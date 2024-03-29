# Problem
[14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

# Performance
![result](./result.png)

# Python
```Python
class Trie:
    def __init__(self):
        self.root = {}
        
    def insert(self, word):
        curNode = self.root
        
        for char in word:
            if char not in curNode: curNode[char] = {}
            curNode = curNode[char]
            
        curNode['#'] = True
        
    def longestCommonPrefix(self):
        prefix  = ''
        curNode = self.root
        
        while True:
            if len(curNode) == 1 and '#' not in curNode: 
                curChar = list(curNode.keys())[0]
                prefix += curChar
                curNode = curNode[curChar]
            else: 
                return prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # (base case)
        if not strs: return ''
        if len(strs) == 1: return strs[0]
        
        # ==================================================
        #  Trie                                            =
        # ==================================================
        # time  : O(n), n = number of all characters in the array
        # space : O(n) 

        trie = Trie()
        for word in strs: trie.insert(word)
            
        return trie.longestCommonPrefix()
```

```Python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # (base case)
        if not strs: return ''
        if len(strs) == 1: return strs[0]
        
        # ==================================================
        #  Array + Sort                                    =
        # ==================================================
        # time  : O(nlog(n))
        # space : O(1)
        
        strs.sort()
        
        shortStr = strs[0]
        longStr  = strs[-1]
        prefix   = ''
        
        for i in range(len(shortStr)):
            if shortStr[i] != longStr[i]: return prefix
            else: prefix += shortStr[i]
                
        return prefix
        
        '''
        # ==================================================
        #  Python Built-in Functions                       =
        # ==================================================
        os.path.commonprefix(strs)     
        '''
```