class Solution:
    def maxArea(self, height: List[int]) -> int:
        # (base case)
        if len( height ) == 2: return min( height )

        # ==================================================
        #  Array + Two Pointer                             =
        # ==================================================
        # time  : O(n)
        # space : O(1)

        area = 0
        l, r = 0, len(height) - 1

        # start from both-side (due to the LARGEST gap)
        # move the pointer with SHORTER height
        while r > l:
            tmp = min(height[l], height[r]) * (r - l)
            if tmp > area: area = tmp

            if height[r] > height[l]: l += 1
            else: r -= 1

        return area
