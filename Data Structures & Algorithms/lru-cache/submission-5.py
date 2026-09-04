class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.recent_keys = []

    def get(self, key: int) -> int:
        if key in self.cache:
            self.recent_keys.append(key)
            self.recent_keys.remove(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.recent_keys.append(key)
            self.recent_keys.remove(key)
        else:
            self.cache[key] = value
            self.recent_keys.append(key)
            if len(self.recent_keys) > self.capacity:
                del_key = self.recent_keys.pop(0)
                self.cache.pop(del_key)
                
