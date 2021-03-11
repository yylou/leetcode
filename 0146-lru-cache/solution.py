class ListNode(object):
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val

        self.next = None
        self.prev = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

        ##  initialize a NULL node with key, value = (-1, -1)
        self.head = ListNode()
        self.tail = self.head

        self.nodeMap = {}


    def _move_to_tail(self, node):
        ##  BREAK links
        node.prev.next = node.next
        node.next.prev = node.prev

        ##  MOVE to TAIL
        node.prev = self.tail
        self.tail.next = node
        self.tail = node


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

        if key not in self.nodeMap: return -1

        targetNode = self.nodeMap[key]
        val = targetNode.val

        ##  (recently used) MOVE to TAIL
        if targetNode != self.tail: self._move_to_tail( targetNode )

        return val


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        ##  node not existing
        ##  (1) add NEW node to TAIL
        ##  (2) CHECK capacity to remove LRU data (HEAD.next node)
        if key not in self.nodeMap:
            newNode = ListNode( key, value )

            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

            self.nodeMap[key] = newNode

            if len( self.nodeMap ) > self.capacity:
                targetNode = self.head.next
                self.head.next = targetNode.next
                self.head.next.prev = self.head

                del self.nodeMap[targetNode.key]

        ##  node existing
        ##  (1) UPDATE node's value
        ##  (2) move the node to TAIL (recently used)
        else:
            targetNode = self.nodeMap[key]
            targetNode.val = value

            if targetNode != self.tail: self._move_to_tail( targetNode )



##  Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
