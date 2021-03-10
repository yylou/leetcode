class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        lengthS = len( s )
        lengthT = len( t )

        ##  (edge case) lengthS == lengthT == 1
        if lengthS == lengthT == 1:
            if s[0] != t[0]: return ""
            else: return s
        ##  (edge case) lengthT > lengthS
        elif lengthT > lengthS: return ""

        counterT = Counter( t )
        target = len( counterT )
        counterS = {}

        start, end, counter = 0, 0, 0
        minLen, minStr = float( 'inf' ), ''

        while end < lengthS:
            if s[end] not in counterS: counterS[s[end]] = 1
            else: counterS[s[end]] += 1

            if s[end] in counterT and counterS[s[end]] == counterT[s[end]]: counter += 1

            ##  FIND the match
            if start <= end and counter == target:
                ##  (1) SHRINK the current window
                while True:
                    tmpChar = s[start]
                    if tmpChar in counterT and counterS[tmpChar] == counterT[tmpChar]: break
                    else:
                        counterS[tmpChar] -= 1

                    start += 1

                ##  (2) DEFINE the MIN length and MIN string
                tmpLen = end - start + 1
                if tmpLen < minLen:
                    minLen = tmpLen
                    minStr = s[start:end+1]

                ##  (3) MOVE forward START to destroy current match (reduce redundant iteration)
                counterS[s[start]] -= 1
                start += 1
                counter -= 1

            end += 1

        return minStr
