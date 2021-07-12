# Problem
[3. Longest Substring w/o Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters)

# Performance
![result](./result.png)

# Python
```Python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # (base case)
        if not s: return 0
        
        # ==================================================
        #  Hash Table + Sliding Window (Two Pointer)       =
        # ==================================================
        # time  : O(n)
        # space : O(n)
        
        table = set()
        slowP, fastP = 0, 0
        ans = float('-inf')
        
        while fastP < len(s):
            if s[fastP] not in table:
                table.add(s[fastP])
                fastP += 1
                ans = max(ans, fastP - slowP)
                
            else:
                table.remove(s[slowP])
                slowP += 1
                
        return ans
```
   
# Java
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
