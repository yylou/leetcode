class Solution:
    def intToRoman(self, num: int) -> str:
        digits = [(1000, "M"),  (900, "CM"), 
                  (500, "D"),   (400, "CD"), 
                  (100, "C"),   (90, "XC"), 
                  (50, "L"),    (40, "XL"), 
                  (10, "X"),    (9, "IX"), 
                  (5, "V"),     (4, "IV"), 
                  (1, "I")]
        
        # ==================================================
        #  Math + Greedy                                   =
        # ==================================================
        # time  : O(1)
        # space : O(1)
        
        ret = ''
        
        for value, symbol in digits:
            if num == 0: break
            
            if num == value:
                ret += symbol
                break
                
            count, num = divmod( num, value )
            ret += symbol * count
            
        return ret
    
'''
Java Solution
==================================================================================================
class Solution {
    /**  
     * @time  : O(1)
     * @space : O(1)
     */

    public String intToRoman(int num) {
        
    }
}
==================================================================================================
'''
