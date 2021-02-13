##  non-merge solution: using two pointers that start at the 1st element of both two lists
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        len1 = len( nums1 )
        len2 = len( nums2 )
        length = len1 + len2

        ##  edge case handling
        if   length == 1 and len1 == 0 and len2 != 0 : return nums2[0]
        elif length == 1 and len1 != 0 and len2 == 0 : return nums1[0]

        ##  flag for indicating calculating median by two numbers (even length)
        flag = False
        if length % 2 == 0 : flag = True; target_index = [length/2-1, length/2]
        else : target_index = [length/2]

        record = []
        i, j = 0, 0

        while i <= len1 or j <= len2 :
            ##  achieving target length, return the answer
            if   not flag and len( record ) - 1 == target_index[0] : return record[-1]
            elif     flag and len( record ) - 1 == target_index[1] : return ( record[-1] + record[-2] ) / 2.

            ##  compare to find the smaller integer, then append it into the list
            if i < len1 and j < len2 :
                if   nums1[i] <= nums2[j] :
                    record.append( nums1[i] )
                    i += 1
                elif nums1[i] > nums2[j] :
                    record.append( nums2[j] )
                    j += 1

            ## reaching the end of the second list of integers, append the integer without comparison
            elif i < len1 and j >= len2 :
                record.append( nums1[i] )
                i += 1

            ## reaching the end of the first list of integers, append the integer without comparison
            elif i >= len1 and j < len2 :
                record.append( nums2[j] )
                j += 1
