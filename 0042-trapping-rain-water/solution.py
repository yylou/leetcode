class Solution:
    def trap(self, height: List[int]) -> int:
        # (base case)
        if len(height) < 3: return 0

        l, r = 0, len(height) - 1
        while l < len(height) and height[l] == 0: l += 1
        while r >= 0 and height[r] == 0: r -= 1
        if r - l + 1 < 3: return 0

        return self.monotonic_stack(height, l, r)
        return self.dp(height, l, r)
        return self.two_pointers(height, l, r)
        return self.max_func(height, l, r)

        """
            |           |
        |ooo|           |ooo|
        ||o||           ||o||


             |
        |oooo|
        |oo|o|                |
        ||o|||            |ooo||o|
        ||o|||          |o||o||||||
        """

    def two_pointers(self, height: List[int], l: int, r: int) -> int:
        # ==================================================
        #  Two pointers                                    =
        # ==================================================
        # time  : O(n)
        # space : O(1)

        area = 0
        maxL, maxR = height[l], height[r]

        while l < r:
            if height[l] > height[r]:
                if height[r] > maxR: maxR = height[r]
                elif not height[r] == maxR: area += maxR - height[r]
                r -= 1

            else:
                if height[l] > maxL: maxL = height[l]
                elif not height[l] == maxL: area += maxL - height[l]
                l += 1

        return area


    def dp(self, height: List[int], l: int, r: int) -> int:
        # ==================================================
        #  Dynamic Programming                             =
        # ==================================================
        # time  : O(n)
        # space : O(n)

        area = 0
        n, recL, recR = r - l + 1, float('-inf'), float('-inf')
        maxL, maxR = [0] * len(height), [0] * len(height)

        for i in range(l, r+1):
            recL = max(recL, height[i])
            maxL[i] = recL

        for i in range(r, l-1, -1):
            recR = max(recR, height[i])
            maxR[i] = recR

        for i in range(l, r+1):
            area += min(maxL[i], maxR[i]) - height[i]

        return area

    def monotonic_stack(self, height: List[int], l: int, r: int) -> int:
        # ==================================================
        #  Monotonic Stack                                 =
        # ==================================================
        # time  : O(n)
        # space : O(n)

        area, stack = 0, []
        for i in range(l, r+1):
            cur = height[i]

            while stack and stack[-1][1] < cur:
                index, val = stack.pop()
                if not stack: break

                depth = min(cur, stack[-1][1]) - val
                gap   = i - stack[-1][0] - 1
                area += depth * gap

            stack.append((i, cur))

        return area

    def max_func(self, height: List[int], l: int, r: int) -> int:
        # ==================================================
        #  MAX for each iteration                          =
        # ==================================================
        # time  : O(n^2)
        # space : O(1)

        area = 0
        for i in range(l, len(height)):
            leftMax  = max(height[0:i+1])
            rightMax = max(height[i:len(height)])

            area += min(leftMax, rightMax) - height[i]

        return area
