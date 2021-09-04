class Solution {
    /**
     * @time  : O(n)
     * @space : O(n)
     */
     
    public boolean isValid(String s) {
        /* base case */
        if(s.length() == 1) return false;
        
        HashMap<Character, Character> table = new HashMap<Character, Character>();
        table.put( ')', '(' );
        table.put( '}', '{' );
        table.put( ']', '[' );
        
        if( table.containsKey( s.charAt(0) ) ) return false;
        
        Stack<Character> stack = new Stack<Character>();
        
        for(int i=0 ; i<s.length() ; i++) {
            char c = s.charAt(i);
            
            if(table.containsKey(c)){
                if(stack.isEmpty()) return false;
                
                char top = stack.pop();
                
                if(top != table.get(c)) return false;
                
            } else{
                stack.push(c);
            }
        }
        
        return stack.isEmpty();
    }
}