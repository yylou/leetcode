class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        #: (base case)
        if m == 0: 
            for i in range(n): nums1[i] = nums2[i]
        if n == 0: return    
        
        # ==================================================
        #  Array + Three Pointers        (Start from End)  =
        # ==================================================        
        # time  : O(m+n)
        # space : O(1)
        
        p1 = m - 1
        p2 = n - 1
        
        for placeP in range(m+n-1, -1, -1):
            #: use p2 for termination since p1 could be left due to the final return
            if p2 < 0: break
                
            if p1 >= 0 and nums1[p1] >= nums2[p2]:
                nums1[placeP] = nums1[p1]
                p1 -= 1
            else:
                nums1[placeP] = nums2[p2]
                p2 -= 1
        
        '''
        # ==================================================
        #  Array + Three Pointers   (Start from Begining)  =
        # ==================================================        
        # time  : O(m+n)
        # space : O(n)
        
        nums1_copy = nums1[:m]
        
        #: pointers for nums1Copy and nums2 respectively
        p1, p2 = 0, 0
        
        for p in range(n + m):
            if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
                nums1[p] = nums1_copy[p1] 
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1
        '''

'''
Java Solution
==================================================================================================
class Solution {
    /**
     * @time  : O(m+n)
     * @space : O(1)
     */

    public void merge(int[] nums1, int m, int[] nums2, int n) {
        /* base case */
        if(m == 0){
            for(int i = 0 ; i < n ; i++){
                nums1[i] = nums2[i];
            }
        }
        if(n == 0) return;
        
        int p1 = m - 1, p2 = n - 1;
        
        for(int p = m+n-1 ; p > -1 ; p--){
            if(p2 < 0) break;
            
            if(p1 >= 0 && nums1[p1] >= nums2[p2]){
                nums1[p] = nums1[p1];
                p1--;
            } else{
                nums1[p] = nums2[p2];
                p2--;
            }
        }
    }
}
==================================================================================================
'''
