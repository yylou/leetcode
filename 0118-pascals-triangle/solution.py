class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #: (base case)
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1], [1, 1]]
        
        # ==================================================
        #  Array                                           =
        # ==================================================
        # time  : O(n^2)
        # space : O(n^2)
        
        ret = [[1], [1, 1]]
        
        for i in range(numRows - 2):
            tmp = [1]
            
            for j in range(0, len(ret[-1]) - 1):
                tmp += [ret[-1][j] + ret[-1][j+1]]
            
            tmp += [1]
            
            ret.append(tmp)
            
        return ret
    
'''
Java Solution
==================================================================================================
class Solution {
    /**
     * @time  : O(n^2)
     * @space : O(n^2)
     */

    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        
        ret.add(new ArrayList<>());
        ret.get(0).add(1);
        
        /* base case */
        if(numRows == 1) return ret;
        
        for(int i=0 ; i<numRows-1 ; i++) {
            List<Integer> tmp  = new ArrayList<>();
            List<Integer> prev = ret.get(i);
            
            tmp.add(1);
            
            for(int j=0 ; j<prev.size()-1 ; j++) {
                tmp.add(prev.get(j) + prev.get(j+1));
            }
            
            tmp.add(1);
            
            ret.add(tmp);
        }
        
        return ret;
    }
}
==================================================================================================
'''
