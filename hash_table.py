# Hash Map can be also called as Hash Table
class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        hash_index = 0
        if not isinstance(key, str):
            key = str(key)
        for char in key:
            hash_index += ord(char)
        return hash_index % self.MAX

    def __setitem__(self, key, value):
        hash_index = self.get_hash(key)
        self.arr[hash_index] = value

    def __getitem__(self, key):
        return self.arr[self.get_hash(key)]

    def print(self):
        for index, element in enumerate(self.arr):
            if element != None:
                print(index, '-->', element)


t = HashTable()
print(t.get_hash('march 6'))
print(t.get_hash('marble'))
t['marble 6'] = 123
print(t['marble 6'])
t['marble 7'] = 12345
print(t['marble 7'])
print(t['marble 6'])
t.print()
# print(t.arr)