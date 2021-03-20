class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        ##  (edge case) length < 3 (cannot form a gap)
        if len(height) < 3: return 0


        ##  Solution (1) two-pointer (both start from the begining)
        def calculateArea( height ):
            slowP, fastP = 0, 0

            ##  (a) Find the first non-Zero element
            while True:
                if height[slowP] != 0: break
                slowP += 1
            fastP = slowP+1

            area = 0
            tmpSum = height[slowP]
            tmpMin = height[slowP]

            ##  (b) Using two pointers to visit the rest of array
            while fastP < len(height):
                ##  move fast-pointer until meet the HIGHER bar
                if height[fastP] < height[slowP]:
                    if height[fastP] < tmpMin: tmpMin = height[fastP]
                    tmpSum += height[fastP]
                    fastP += 1

                else:
                    ##  find gap, calcuate the area
                    if tmpMin < height[slowP]:
                        gap = fastP - slowP
                        area += gap * height[slowP] - tmpSum

                    slowP = fastP
                    fastP += 1

                    tmpSum = height[slowP]
                    tmpMin = height[slowP]

            return slowP, tmpMin, area

        ##  (c) remaining part handling
        slowP, tmpMin, area = calculateArea( height )

        if slowP != len(height)-1 and tmpMin < height[slowP]:
            area += calculateArea( height[slowP:][::-1] )[2]

        return area


        # ========================================================= #


        ##  Solution (2) find the each GAP and accumulate
        ##  - time complexity: O(n^2)
        ##  - space complexity: O(1)
        area = 0

        for i in range( len(height) ):
            leftMax = max( height[0:i+1] )
            rightMax = max( height[i:len(height)] )

            area += min( leftMax, rightMax ) - height[i]

        return area
