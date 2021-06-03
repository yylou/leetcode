class Solution:
    def myAtoi(self, s: str) -> int:
        #:  (edge case)
        if len( s ) == 0: return 0
        
        # ==================================================
        #  String + Math                                   =
        # ==================================================
        # time  : O(n)
        # space : O(1)
        
        integer = []
        sign    = ''
        
        
        for char in s:
            #:  (1) leading whitespace
            if char == ' ' and not integer and not sign: continue
            
            #:  (2) duplicated sign
            if sign and ( char == '-' or char == '+' ): break                
                
            #:  (a) first sign
            if ( char == '+' or char == '-' ) and not integer and not sign: sign = char
            
            #:  (b) non-decimal char
            elif not 48 <= ord(char) <= 57: break
                
            #:  (c) decimal char
            else: integer.append( char )
                
        
        #:  no decimal char is recorded
        if not integer: return 0
        
        ans = int( ''.join( integer ) )
        if sign == '-': ans *= -1
            
        #:  boundary check
        if   ans < -2**31    : return -2**31
        elif ans >  2**31 -1 : return  2**31 - 1

        return ans
'''
Java Solution
==================================================================================================
class Solution {
    /**
     * @time  : O(n)
     * @space : O(1)
     */
    public int myAtoi(String s) {
        
    }
}
==================================================================================================
'''
