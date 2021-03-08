##  Example
#       Input: moves = "LDRRLRUULR"
#       Output: false
#
#       Input: moves = "RRDD"
#       Output: false
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """

        ##  Solution (1) using COUNT
        if( moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R") ):
            return True
        else:
            return False

        # =================================================================================== #

        ##  Solution (2) iterative
        counter_U = 0
        counter_R = 0

        for move in moves :
            if   move == 'U' : counter_U += 1
            elif move == 'D' : counter_U -= 1
            elif move == 'R' : counter_R += 1
            elif move == 'L' : counter_R -= 1

        if counter_U == 0 and counter_R == 0 : return True
        else : return False
