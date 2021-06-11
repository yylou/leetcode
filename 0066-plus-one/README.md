# Problem
[66. Plus One](https://leetcode.com/problems/plus-one)

# Performance
![result](./result.png)

# Python
```Python3
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #: (edge case)
        if len(digits) == 1: return [1, 0] if digits[0] == 9 else [digits[0] + 1]
        
        # ==================================================
        #  Array + Math                                    =
        # ==================================================
        # time  : O(n)
        # space : O(1) 
        
        carry = 1
        for i in range( len(digits)-1, -1, -1 ):
            digits[i] += carry
            carry = digits[i] // 10
            
            #: if carry == 0, return; otherwise, keep tracking and assign 0 to current element
            if carry: digits[i] = 0
            else: return digits
            
        return [1] + digits
```

# Java
```Java
class Solution {
    /**
     * @time  : O(n)
     * @space : O(n)
     */
    public int[] plusOne(int[] digits) {
        int n = digits.length;
        
        for( int i=n-1 ; i>-1 ; i-- ){
            if( digits[i] == 9 ){
                digits[i] = 0;
            } else{
                digits[i]++;
                return digits;
            }
        }
        
        digits = new int[n+1];
        digits[0] = 1;
        return digits;
    }
}
```
