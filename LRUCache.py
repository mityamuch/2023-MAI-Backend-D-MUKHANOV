class LRUCache:
    def __init__(self, capacity: int=10) -> None:
        self.capacity = capacity
        self.cache = {}
        self.key_order = []
    
    def get(self, key: str) -> str:
        if key in self.cache:
            self.key_order.remove(key)
            self.key_order.append(key)
            return self.cache[key]
        else:
            return None

    def set(self, key: str, value: str) -> None:
        if key in self.cache:
            self.key_order.remove(key)
            self.key_order.append(key)
        else:
            self.key_order.append(key)
        self.cache[key] = value
        if len(self.key_order) > self.capacity:
            oldest_key = self.key_order.pop(0)
            del self.cache[oldest_key]

    def rem(self, key: str) -> None:
        if key in self.cache:
            self.key_order.remove(key)
            del self.cache[key]



cache = LRUCache()
cache.set('Jesse', 'Pinkman')
cache.set('Walter', 'White')
cache.set('Jesse', 'James')

print(cache.get('Jesse')) # вернёт 'James'
cache.rem('Walter')
print(cache.get('Walter')) # вернёт ''
