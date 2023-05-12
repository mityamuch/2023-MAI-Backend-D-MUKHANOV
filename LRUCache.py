class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dict:
            node = self.dict[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def set(self, key, value):
        if key in self.dict:
            self._remove(self.dict[key])
        node = Node(key, value)
        self._add(node)
        self.dict[key] = node
        if len(self.dict) > self.capacity:
            node = self.head.next
            self._remove(node)
            del self.dict[node.key]

    def rem(self, key):
        if key in self.dict:
            node = self.dict[key]
            self._remove(node)
            del self.dict[key]


cache = LRUCache(10)
cache.set('Jesse', 'Pinkman')
cache.set('Walter', 'White')
cache.set('Jesse', 'James')

print(cache.get('Jesse'))  # вернёт 'James'
cache.rem('Walter')
print(cache.get('Walter'))  # вернёт '-1'
