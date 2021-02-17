##  (1) divide any possible case and conquer
##  (2) using 'set' instead of 'list' to eliminate duplicat numbers and accelerate FIND operation
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        length = len( nums )

        ##  (edge case handling) input list has less than 3 numbers
        if length < 3 : return []

        ##  (edge case handling) nums only contains 3 numbers, do the math immediately
        if length == 3 :
            if sum( nums ) != 0 : return []
            else : return [nums]

        else :
            zero_nums     = []
            negative_nums = []
            positive_nums = []

            for num in nums :
                if   num < 0 : negative_nums.append( num )
                elif num > 0 : positive_nums.append( num )
                else : zero_nums.append( num )

            len_z_nums = len( zero_nums )
            len_n_nums = len( negative_nums )
            len_p_nums = len( positive_nums )

            if len_n_nums == 0 :
                ##  if there is no "NEGATIVE value and ZERO" in the input list, return null
                if len_z_nums == 0 : return []

                ##  if the larget number is 0 and the number of 0 less than 3, return null
                if len_p_nums == 0 and len_z_nums < 3 : return []

                ##  if only ZERO in the input list
                if len_p_nums == 0 and len_p_nums == 3 : return [[0, 0, 0]]

            ret_value = set()

            set_n_nums = set( negative_nums )
            set_p_nums = set( positive_nums )

            ##  (0, 0, 0)
            if len_z_nums >= 3 : ret_value.add( (0, 0, 0) )

            ##  (-num, 0, +num)
            if zero_nums :
                for num in set_n_nums :
                    if -1 * num in set_p_nums : ret_value.add( (-1*num, 0, num) )

            ##  (-num1, -num2, -1 * (-num1 + -num2))
            for i in range( len_n_nums ) :
                for j in range( i+1, len_n_nums ) :
                    remain = -1 * ( negative_nums[i] + negative_nums[j] )
                    if remain in set_p_nums :
                        ret_value.add( tuple( sorted( [remain, negative_nums[i], negative_nums[j]] ) ) )

            ##  (num1, num2, -1 * (num1 + num2))
            for i in range( len_p_nums ) :
                for j in range( i+1, len_p_nums ) :
                    remain = -1 * ( positive_nums[i] + positive_nums[j] )
                    if remain in set_n_nums :
                        ret_value.add( tuple( sorted( [remain, positive_nums[i], positive_nums[j]] ) ) )

            return ret_value
