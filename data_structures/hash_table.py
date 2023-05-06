class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _get_hash(self, key) -> int:
        """
        Generate a hash value for the key
        """
        hash_code = 0
        for char in str(key):
            hash_code += ord(char)
        return hash_code % self.size

    def add(self, key, value) -> None:
        """
        Add a key-value pair to the hash table
        """
        hash_key = self._get_hash(key)
        for i, item in enumerate(self.table[hash_key]):
            if item[0] == key:
                self.table[hash_key][i] = (key, value)
                break
        else:
            self.table[hash_key].append((key, value))

    def get(self, key) -> None:
        """
        Get the value associated with a key
        """
        hash_key = self._get_hash(key)
        for item in self.table[hash_key]:
            if item[0] == key:
                return item[1]
        raise KeyError(key)

    def delete(self, key):
        """
        Remove a key-value pair from the hash table
        """
        hash_key = self._get_hash(key)
        for i, item in enumerate(self.table[hash_key]):
            if item[0] == key:
                del self.table[hash_key][i]
                break
        else:
            raise KeyError(key)


hash_table_size = int(input("Input HashTable size: "))
h_table = HashTable(hash_table_size)
h_table.add('one', 1)
h_table.add('two', 2)
h_table.add('three', 3)
print(h_table.get('one'))  # Output: 1
print(h_table.get('two'))  # Output: 2
try:
    print(h_table.get('four'))  # Output: KeyError: 'four'
except Exception as exc:
    print("Key error:", exc)
h_table.delete('two')
try:
    print(h_table.get('two'))  # Output: KeyError: 'two'
except Exception as exc:
    print("Key Error: ", exc)
