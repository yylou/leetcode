# Problem
[69. Sqrt(x)](https://leetcode.com/problems/sqrtx)

# Performance
![result](./result.png)

# Python
```Python3
class Solution:
    def mySqrt(self, x: int) -> int:
        #: (base case)
        if x == 0: return 0
        if x < 4: return 1
        
        # ==================================================
        #  Binary Search + Math                            =
        # ==================================================
        # time  : O(log(n))
        # space : O(1)
        
        left, right = 2, x // 2
        
        while left <= right:
            mid = (left + right) // 2
            num = mid * mid
            
            if x == num: return mid
            if x > num: left = mid + 1
            else: right = mid -1
                
        return right
```

# Java
```Java
class Solution {
    /**
     * @time  : O(log(n))
     * @space : O(1)
     */
     
    public int mySqrt(int x) {
        if( x == 0 ) return 0;
        if( x  < 4 ) return 1;
        if( x == 4 ) return 2;
        
        int left = 2, right = x/2;
        
        while( left <= right ){
            int mid = (left + right) / 2;
            
            // use LONG since mid * mid can be larger than INT.MAX
            long num = (long) mid * mid;
            
            if( x == num ) return mid;
            if( x > num ) left = mid + 1;
            else right = mid - 1;
        }
        
        return right;
    }
}
```
