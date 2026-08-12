class MyHashMap:

    def __init__(self):
        self.size = 10000
        self.buckets = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        idx = key % self.size
        bucket = self.buckets[idx]
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])

    def get(self, key: int) -> int:
        idx = key % self.size
        bucket = self.buckets[idx]
        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key: int) -> None:
        idx = key % self.size
        bucket = self.buckets[idx]
        for i in range(len(bucket)):
            item = bucket[i]
            if item[0] == key:
                val = item[1]
                bucket.remove([key, val])
                break
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)