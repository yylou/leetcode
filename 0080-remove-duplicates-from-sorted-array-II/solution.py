##  related problem: 26. Remove Duplicates from Sorted Array. For this problem, only need to add one counter and an if-else statement
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len( nums )

        ##  edge case handling
        if length == 0 : return 0
        if length == 1 : return 1

        counter = 0
        ret_value = 0

        for i in range( 1, length ) :
            if nums[i] == nums[ret_value] :
                counter += 1

                ##  not exceeding 2 times, move to the next element but CANNOT renew counter
                if counter < 2 : ret_value += 1

            ##  uneqal condition: renew counter and move to the next element concurrently (ret_value and i)
            else :
                counter = 0
                ret_value += 1

            ##  assign element by two pointers: ret_value and i
            nums[ret_value] = nums[i]


        return ret_value + 1
