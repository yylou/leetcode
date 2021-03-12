class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        hash_table = {}
        ret_value = 0

        for stone in stones :
            if stone not in hash_table : hash_table[stone] = 1
            else : hash_table[stone] += 1

        for jewel in jewels :
            if jewel not in hash_table : continue
            ret_value += hash_table[jewel]

        return ret_value
