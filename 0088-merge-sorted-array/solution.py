class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.

        reference: https://www.geeksforgeeks.org/in-place-merge-sort/
        """

        #:  (edge case) nums2 is empty
        if not nums2: return


        #:  Solution (1) place from the end of 'nums1'
        lastElement = m+n-1
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[lastElement] = nums1[m-1]
                m -= 1
                lastElement -= 1
            else:
                nums1[lastElement] = nums2[n-1]
                n -= 1
                lastElement -= 1

        while n > 0:
            nums1[lastElement] = nums2[n-1]
            n -= 1
            lastElement -= 1


        # ============================================================================= #


        """
        #:  Solution (2) two pointers to modify in-place and shift (without copy)
        p1, p2 = 0, 0
        while p1 < m and p2 < n:
            if nums1[p1] <= nums2[p2]:
                p1 += 1

            elif nums1[p1] > nums2[p2]:
                ##  shift element
                tmpP = m
                while tmpP > p1:
                    nums1[tmpP] = nums1[tmpP-1]
                    tmpP -= 1

                nums1[p1] = nums2[p2]

                p1 += 1
                p2 += 1
                m += 1

        #:  for the remaining elements in nums2
        if p2 != n:
            while p2 < n:
                nums1[m] = nums2[p2]
                m += 1
                p2 += 1
        """


        # ============================================================================= #


        """
        #:  Solution (3) using python built-in sorting function
        for i in xrange( m, len(nums1) ): nums1[i] = nums2[i-m]
        nums1.sort()
        """
