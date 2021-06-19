class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        #: (base case)
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1, 1]
        
        # ==================================================
        #  Array + Math                                    =
        # ==================================================
        # time  : O(n^2)
        # space : O(1)
        
        ret = [1, 1]
        
        #: (reverse-tracking for n-1 times)
        #: calculate BACKWARDS to replace values without affecting the other elements
        for i in range(rowIndex-1):
            for j in range(len(ret)-1, 0, -1):
                ret[j] = ret[j] + ret[j-1]
            ret += [1]
        
        return ret
            
'''
Java Solution
==================================================================================================
class Solution {
    /**
     * @time  : O(n^2)
     * @space : O(1)
     */

    public List<Integer> getRow(int rowIndex) {
        List<Integer> ret = new ArrayList<Integer>();
        
        ret.add(1);
        
        /* base case */
        if(rowIndex == 0) return ret;
        
        ret.add(1);
        
        for(int i=0 ; i<rowIndex-1 ; i++) {
            for(int j=ret.size()-1 ; j>0 ; j--) {
                ret.set(j, ret.get(j) + ret.get(j-1));
            }
            ret.add(1);            
        }
        
        return ret;
    }
}
==================================================================================================
'''
