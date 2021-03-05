class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        ##  (edge case) intervals only has one pair
        if len( intervals ) == 1: return [[intervals[0][0], intervals[0][1]]]

        ##  SORT at first so that interval could be updated correctly
        intervals.sort( key=lambda x: x[0] )

        startIndex, endIndex = 0, 0
        prevStartIndex, prevEndIndex = intervals[0][0], intervals[0][1]
        interval = [prevStartIndex, prevEndIndex]

        retVal = []

        ##  prev            |-----|
        ##  cur-1       |-----|
        ##  cur-2               |-----|
        ##  cur-3       |-------------|
        ##  cur-4             |-|
        ##  cur-5   |-----|        |-----|

        for element in intervals[1:]:
            startIndex, endIndex = element[0], element[1]

            ##  OVERLAP (NOTE: update previous indexes)
            if startIndex <= prevEndIndex:
                ##  (cur-4)
                if startIndex >= prevStartIndex and endIndex <= prevEndIndex:
                    continue

                ##  (cur-1)
                elif endIndex < prevEndIndex:
                    interval[0] = startIndex
                    prevStartIndex = startIndex

                ##  (cur-2)
                elif startIndex > prevStartIndex:
                    interval[1] = endIndex
                    prevEndIndex = endIndex

                ##  (cur-3)
                else:
                    interval = [startIndex, endIndex]
                    prevStartIndex, prevEndIndex = startIndex, endIndex

            ##  OUT of interval (cur-5)
            else:
                retVal.append( interval )

                prevStartIndex, prevEndIndex = element[0], element[1]
                interval = [prevStartIndex, prevEndIndex]


        ##  LAST element handling
        if interval not in retVal:
            ##  check whether OVERLAP
            if startIndex <= prevEndIndex:
                if startIndex >= prevStartIndex and endIndex <= prevEndIndex: pass
                elif endIndex < prevEndIndex: interval[0] = startIndex
                elif startIndex > prevStartIndex: interval[1] = endIndex
                else: interval = [startIndex, endIndex]

                retVal.append( interval )

            ##  OUT of interval
            else:
                retVal.append( interval )

        return retVal
