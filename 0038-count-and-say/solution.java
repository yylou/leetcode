class Solution {
    /**  
     * @time  : O(nk)
     * @space : O(1)
     */

    public String countAndSay(int n) {
        String ret = "1";
        
        /* base case */
        if(n == 1) return ret;
        
        for(int i=0 ; i<n-1 ; i++) {
            StringBuilder tmp = new StringBuilder();
            char prev = ret.charAt(0);
            int counter = 0;
            
            for(int j=0 ; j<ret.length() ; j++) {
                if(prev != ret.charAt(j)) {
                    tmp.append(counter);
                    tmp.append(prev);
                    prev = ret.charAt(j);
                    counter = 1;
                } else {
                    counter++;
                }
            }
            
            tmp.append(counter);
            tmp.append(prev);
            ret = tmp.toString();
        }
        
        return ret;
    }
}