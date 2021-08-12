class Solution {
    /**
     * @time  : O(max(m,n))
     * @space : O(1)
     */
    
    public String addBinary(String a, String b) {
        int n1 = a.length() - 1, n2 = b.length() - 1, carry = 0;
        StringBuilder ans = new StringBuilder();
        
        while(n1 >= 0 || n2 >= 0) {
            int bit1 = (n1 >= 0) ? a.charAt(n1) - '0' : 0;
            int bit2 = (n2 >= 0) ? b.charAt(n2) - '0' : 0;
            
            int sum = bit1 + bit2 + carry;
            if(sum > 1) {
                sum -= 2;
                carry = 1;
            } else {
                carry = 0;
            }
            
            ans.append(sum);
            
            n1--;
            n2--;
        }
        
        if(carry != 0) ans.append(carry);
        return ans.reverse().toString();
    }
}