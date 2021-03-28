class Solution:
		"""
    :param n, an integer
    :return an integer
		"""
    def reverseBits(self, n):

        #: Solution (1) do '&' operation then shift and decrease power value
        ans, power = 0, 31
        while n:
            ans += (n&1) << power
            n = n >> 1
            power -= 1
        return ans


        # ===================================================================== #


        #: Solution (2) Byte by Byte with Cache (Memoization)
        def reverseByte( byte, cache ):
            cache[byte] = cache.get( byte, (byte * 0x0202020202 & 0x010884422010) % 1023 )
            return cache[byte]

        ans, power, cache = 0, 24, dict()
        while n:
            ans += reverseByte( n & 0xff, cache ) << power
            n >>= 8
            power -= 8
        return ans


        # ===================================================================== #


        #: Solution (3) divide and conquer
        #: - bin(0xff00ff00) = 0b11111111000000001111111100000000
        #: - bin(0xf0f0f0f0) = 0b11110000111100001111000011110000
        #: - bin(0xcccccccc) = 0b11001100110011001100110011001100
        #: - bin(0xaaaaaaaa) = 0b10101010101010101010101010101010
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n
