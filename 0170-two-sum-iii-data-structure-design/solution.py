class TwoSum:

    def __init__(self):
        self.data = []
        self.sorted = False

    def add(self, number: int) -> None:
        self.data.append(number)
        self.sorted = False

    def find(self, value: int) -> bool:
        if not self.sorted:
            self.data.sort()
            self.sorted = True
            
        start, end = 0, len(self.data) - 1
            
        while start < end:
            if self.data[start] + self.data[end] == value:
                return True
            elif self.data[start] + self.data[end] > value:
                # result may be on left side
                end = bisect_right(self.data, value - self.data[start], start + 1, end) - 1
            else:
                # result may be on right side
                start = bisect_left(self.data, value - self.data[end], start + 1, end - 1)
            
        return False

    def bisect_right(target: int, start: int, end: int) -> int:
        while start < end:
            mid = (start + end) // 2
            if self.data[mid] <= target: start = mid + 1
            else: end = mid
        return start

    def bisect_left(target: int, start: int, end: int) -> int:
        while start < end:
            mid = (start + end) // 2
            if self.data[mid] < target: start = mid + 1
            else: end = mid
        return start