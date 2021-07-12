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
