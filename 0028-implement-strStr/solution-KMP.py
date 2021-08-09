class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # (base case)
        if not needle: return 0
        if not haystack: return -1
        if len(needle) > len(haystack): return -1

        # ==================================================
        #  KMP Pattern Matching (Substring search)         =
        # ==================================================
        # n = length of haystack
        # m = length of needls
        # time  : O(n+m)
        # space : O(m)

        # (1) build LPS table (Longest proper Prefix also Suffix)
        # time  : O(n)
        # space : O(n)
        def LPS(string: str, length: int) -> list:
            '''
            Two pointers, jump and move, point to GOLDEN string
            '''
            jumpP, moveP = 0, 1
            table = [0] + [-1]*( length - 1 )

            while moveP < length:
                if string[jumpP] != string[moveP]:
                    if jumpP == 0:
                        table[moveP] = 0
                        moveP += 1
                    else:
                        jumpP = table[jumpP-1]

                else:
                    table[moveP] = jumpP + 1

                    jumpP += 1
                    moveP += 1

            return table

        # (2) use LPS table to do pattern matching
        # time  : O(m)
        # space : O(1)
        def KMP(str1: str, str2: str, LPSTable: list) -> int:
            '''
            Two pointers:
            - jump pointer point to LPS table / GOLDEN string
            - move pointer point to TARGET string
            '''
            jumpP, moveP = 0, 0

            while moveP < len(str1):
                if str2[jumpP] != str1[moveP]:
                    if jumpP == 0:
                        moveP += 1
                    else:
                        jumpP = LPSTable[jumpP-1]

                else:
                    jumpP += 1
                    moveP += 1

                #:  Meet the end, return starting index
                if jumpP == len(str2): return moveP - len(str2)

            return -1

        LPSTable = LPS(needle, len(needle))
        return KMP(haystack, needle, LPSTable)
