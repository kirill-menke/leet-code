class TimeMap:
    
    def __init__(self):
        self.dict = dict()    

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dict:
            self.dict[key].append((timestamp, value))
        else:
            self.dict[key] = [(timestamp, value)]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""
        
        l = self.dict[key]
        left, right = 0, len(l) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if timestamp >= l[mid][0]:
                left = mid
            else:
                right = mid - 1
        
        # print(l, key, timestamp)
        return l[left][1] if l[left][0] <= timestamp else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)