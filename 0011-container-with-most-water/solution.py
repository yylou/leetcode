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

        ##  start from the right-most and left-most since 'WIDTH' is more important than 'HEIGHT DIFFERENCE'
        ##  move the pointer with the smaller height
        while front < back :
            if height[front] < height[back] :
                area = ( back-front ) * height[front]
                front += 1
            else :
                area = ( back-front ) * height[back]
                back -= 1

            if area > ret_value : ret_value = area

        return ret_value
