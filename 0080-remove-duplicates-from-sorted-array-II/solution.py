##  Related problem: 26. Remove Duplicates from Sorted Array
##  For this problem, only need to add one counter and additional if-else statements
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len( nums )

        ##  (edge case)
        if length == 0 : return 0
        if length == 1 : return 1

        counter = 0
        retVal = 0

        for i in range( 1, length ) :
            if nums[i] == nums[retVal] :
                counter += 1

                ##  not exceeding 2 times, move to the next element but CANNOT renew counter
                if counter < 2 : retVal += 1

            ##  uneqal condition: renew counter and move to the next element concurrently (ret_value and i)
            else :
                counter = 0
                retVal += 1

            ##  assign element by two pointers: ret_value and i
            nums[retVal] = nums[i]


        return retVal + 1
