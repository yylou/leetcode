class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """

        ##  (edge case) 'isConnected' only has 1 element
        if len( isConnected ) == 1: return 1


        ##  Solution (1) recursively EXPLORE and RECORD the connected city as explored
        def explore( city, isConnected ):
            self.explored.add( city )
            for curCity in xrange( len(isConnected) ):
                if city == curCity: continue
                if isConnected[city][curCity] == 1 and curCity not in self.explored:
                    explore( curCity, isConnected )


        self.explored = set()
        groups = 0
        for curCity in xrange( len(isConnected) ):
            if curCity not in self.explored:
                groups += 1
                explore( curCity, isConnected )

        return groups


        # ====================================================================== #


        ##  Solution (2) BUILD the COMPLETE connection map and then COUNT
        hashTable = {}
        for i in xrange( len(isConnected) ):
            hashTable[i], connection = set(), set()

            for j in xrange( len( isConnected[i] ) ):
                if i == j: continue

                ##  build connection
                if isConnected[i][j] == 1: hashTable[i].add( j )

                ##  update connection by "checking other cities' record"
                if j in hashTable and i in hashTable[j]:
                    connection.add( j )
                    hashTable[i] |= hashTable[j]

            ##  update other connected cities' connection
            for element in connection:
                if element in hashTable: hashTable[element] |= hashTable[i]


        ##  CALCULATE the number of groups (using SORTED TUPLE to store in set)
        groups, isolated = set(), 0
        for key in hashTable:
            if len( hashTable[key] ) == 0: isolated += 1
            else:
                sortedTuple = tuple( sorted( hashTable[key] ) )
                if sortedTuple not in groups: groups.add( sortedTuple )

        return len( groups ) + isolated
