class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        indexTable = {}

        for i in range( len(arr) ):
            sign = 1 if arr[i] > 0 else -1
            absVal = abs( arr[i] )

            if arr[i] % 2 == 0 and ( absVal // 2 * sign in indexTable or absVal * 2 * sign in indexTable): return True
            if arr[i] % 2 != 0 and  absVal * 2 * sign in indexTable: return True

            indexTable[arr[i]] = i

        return False
