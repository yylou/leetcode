##  two pointers solution with reduced calculation
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        length = len( height )

        front, back = 0, length -1
        ret_value = 0

        ##  searching for the HEIGHTest elements costs, instead, WIDTH is also an equally important metric.
        ##  Therefore, using two pointers starting from the right-most and left-most respectively (WIDEST)
        while front < back :
            if height[front] < height[back] :
                area = ( back-front ) * height[front]
                front += 1
            else :
                area = ( back-front ) * height[back]
                back -= 1

            if area > ret_value : ret_value = area

        return ret_value
