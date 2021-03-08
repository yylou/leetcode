class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        # =========================================================================
        #  'intervals' are initially sorted according to their start times        =
        # =========================================================================

        ##  (edge case) intervals is null
        if not intervals: return [newInterval]

        ##  (edge case) only exist 1 interval
        length = len( intervals )
        if length == 1:
            if newInterval[0] > intervals[0][1]:
                return intervals + [newInterval]
            elif newInterval[1] < intervals[0][0]:
                return [newInterval] + intervals
            else:
                return [[ min( intervals[0][0], newInterval[0] ), max( intervals[0][1], newInterval[1] ) ]]


        ##  (edge case) OUT of all intervals
        if newInterval[0] > intervals[-1][1]:
            return intervals + [newInterval]

        ##  (edge case) PRIOR to all intervals
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals


        def merge( old, new ):
            '''
            prev            |-----|
            cur-1       |-----|
            cur-2               |-----|
            cur-3       |-------------|
            cur-4             |-|
            '''
            prevStartIndex, prevEndIndex = old[0], old[1]
            startIndex, endIndex = new[0], new[1]

            ##  cur-4
            if startIndex >= prevStartIndex and endIndex <= prevEndIndex:
                return old
            ##  cur-1
            elif endIndex < prevEndIndex:
                return [startIndex, prevEndIndex]
            ##  cur-2
            elif startIndex > prevStartIndex:
                return [prevStartIndex, endIndex]
            ##  cur-3
            else:
                return [startIndex, endIndex]


        statusCode = -1
        retVal = []
        curInterval = [newInterval[0], newInterval[1]]

        for i in range( length ):
            interval = intervals[i]

            ##  PRIOR to current interval
            if curInterval[0] > interval[1]:
                retVal.append( interval )
                statusCode = 1

            ##  BEYOND current interval
            elif curInterval[1] < interval[0]:
                retVal.append( curInterval )
                retVal += intervals[i:]
                statusCode = 2
                break

            ##  OVERLAP
            else:
                curInterval = merge( curInterval, interval )
                statusCode = 3

        if statusCode == 3:
            retVal.append( curInterval )

        return retVal
