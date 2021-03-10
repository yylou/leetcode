class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """

        boxTypes.sort( key=lambda x:x[1], reverse=True )
        maxUnit = 0

        for element in boxTypes:
            ##  check whether truckSize is available for ALL current boxes
            if truckSize - element[0] < 0:
                maxUnit += truckSize * element[1]
                break
            else:
                maxUnit += element[0] * element[1]
                truckSize -= element[0]

        return maxUnit
