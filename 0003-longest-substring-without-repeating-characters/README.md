# Problem
[3. Longest Substring w/o Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters)

# Performance
![result](./result.png)

# Python Solution
```Python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, slowP, fastP = 0, 0, 0
        hashTable = dict()
        
        length = len( s )
        
        #:  (edge case)
        if length == 0: return 0
        
        # ==================================================
        #  Hash Table + Sliding Window (Two Pointer)       =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        
        while slowP < length and fastP < length:
            #:  (1) new char: record char in hash table and extend sliding window by fast pointer
            if s[fastP] not in hashTable:
                hashTable[s[fastP]] = fastP
                fastP += 1
                ans = max( ans, fastP-slowP )
                
            #:  (2) repeating char: delete record in hash table and shrink sliding window by slow pointer
            else:
                del hashTable[s[slowP]]
                slowP += 1
                
        return ans
```
   
# Java Solution
```Java
class Solution {
    /**  
     * @time  : O(n)
     * @space : O(n)
     */
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> hashTable = new HashMap<>();
        int ans = 0, slowP = 0, fastP = 0;
        
        int length = s.length();
        if( length == 0 ){ return 0; }
        
        while( fastP < length ){
            char curChar = s.charAt( fastP );
            
            if( !hashTable.containsKey( curChar ) ){
                hashTable.put( curChar, fastP );
                fastP++;
                ans = Math.max( ans, fastP-slowP );
                
            } else {
                curChar = s.charAt( slowP );
                hashTable.remove( curChar );
                slowP++;
            }
        }
        
        return ans;
    }
}
```
