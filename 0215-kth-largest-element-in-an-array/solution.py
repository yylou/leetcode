class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        ##  (edge case) k == 1
        if k == 1: return max(nums)


        #:  Solution (1) sort
        #:  - time complexity: O(nlogn)
        #:  - space complexity: O(1)
        def mergeSort( array ):
            if len(array) > 1:
                mid = len(array) // 2
                arrayL, arrayR = array[:mid], array[mid:]

                mergeSort(arrayL)
                mergeSort(arrayR)

                lenL, lenR = len(arrayL), len(arrayR)

                pL = pR = curP = 0

                #: merge two sorted lists
                while pL < lenL and pR < lenR:
                    if arrayL[pL] < arrayR[pR]:
                        array[curP] = arrayL[pL]
                        pL += 1
                    else:
                        array[curP] = arrayR[pR]
                        pR += 1
                    curP += 1

                #: checking remaining elements
                while pL < lenL:
                    array[curP] = arrayL[pL]
                    pL += 1
                    curP += 1

                while pR < lenR:
                    array[curP] = arrayR[pR]
                    pR += 1
                    curP += 1

        # mergeSort( nums )
        # nums.sort()
        # return nums[len(nums)-k]


        # ======================================================================== #


        #:  Solution (2) "Hoare's selection algorithm"
        #:  - time complexity: O(n)
        #:  - space complexity: O(1)
        def partition( left, right, index ):
            pivot = nums[index]

            #:  move pivot to the last (right)
            nums[index], nums[right] = nums[right], nums[index]

            #:  move all smaller elements to the left
            placeIndex = left
            for i in xrange( left, right ):
                if pivot > nums[i]:
                    nums[placeIndex], nums[i] = nums[i], nums[placeIndex]
                    placeIndex += 1

            #:  move pivot back to split point
            nums[placeIndex], nums[right] = nums[right], nums[placeIndex]

            return placeIndex


        def quickSelect( left, right, k_smallest ):
            if left == right: return nums[left]

            #:  randomly assign pivot and do partition
            index = partition( left, right, random.randint( left, right ) )

            if index == k_smallest: return nums[index]
            elif index > k_smallest: return quickSelect( left, index-1, k_smallest )
            else: return quickSelect( index+1, right, k_smallest )


        n = len(nums)
        return quickSelect( 0, n-1, n-k )  #:  convert to k-smallest problem


        # ======================================================================== #


        #:  Solution (3) using python built-in priority-queue (heap)
        #:  - time complexity: O(nlogk)
        #:  - space complexity: O(k)
        return heapq.nlargest(k, nums)[-1]
