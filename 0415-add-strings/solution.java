class Solution {
    /**
     * @time  : O(max(m,n))
     * @space : O(1)
     */
    
    public String addStrings(String num1, String num2) {
        int p1 = num1.length() - 1, p2 = num2.length() - 1, carry = 0;
        
        StringBuilder ans = new StringBuilder();
        
        while(p1 >= 0 || p2 >= 0 || carry > 0) {
            int val1 = (p1 >= 0) ? num1.charAt(p1--) - '0' : 0;
            int val2 = (p2 >= 0) ? num2.charAt(p2--) - '0' : 0;
            int val = val1 + val2 + carry;
            carry = val / 10;
            val = val % 10;
            
            ans.append(val);
        }
        
        return ans.reverse().toString();
    }
}