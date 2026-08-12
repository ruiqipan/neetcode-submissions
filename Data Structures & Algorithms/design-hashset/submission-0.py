class MyHashSet:

    def __init__(self):
        self.size = 10000
        self.buckets = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        idx = key % 10000
        bucket = self.buckets[idx]
        if bucket is None or key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        idx = key % 10000
        bucket = self.buckets[idx]
        if bucket is None or key not in bucket:
            return
        bucket.remove(key)

    def contains(self, key: int) -> bool:
        idx = key % 10000
        bucket = self.buckets[idx]
        if bucket is None or key not in bucket:
            return False
        return True
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)