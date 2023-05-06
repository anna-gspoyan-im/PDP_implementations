class HashMap:
    def __init__(self, size):
        self.size = size
        self.map = [None] * self.size

    def _get_hash(self, key) -> int:
        """
        Generate a hash value for the key
        """
        hash_code = 0
        for char in str(key):
            hash_code += ord(char)
        return hash_code % self.size

    def add(self, key, value: int) -> bool:
        """
        Add a key-value pair to the hash map
        """
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for item in self.map[key_hash]:
                if item[0] == key:
                    item[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key) -> int or None:
        # Get the value associated with a key
        """
        Get the value associated with a key
        """
        hash_key = self._get_hash(key)
        if self.map[hash_key] is not None:
            for item in self.map[hash_key]:
                if item[0] == key:
                    return item[1]
        return None

    def delete(self, key) -> bool:
        """
        Remove a key-value pair from the hash map
        """
        hash_key = self._get_hash(key)
        if self.map[hash_key] is None:
            return False
        for i in range(0, len(self.map[hash_key])):
            if self.map[hash_key][i][0] == key:
                self.map[hash_key].pop(i)
                return True
        return False


hash_map_size = int(input("Input HashMap size: "))
hash_map = HashMap(hash_map_size)
hash_map.add('one', 1)
hash_map.add('two', 2)
hash_map.add('three', 3)
print(hash_map.get('one'))  # Output: 1
print(hash_map.get('two'))  # Output: 2
print(hash_map.get('four'))  # Output: None
hash_map.delete('two')
print(hash_map.get('two'))  # Output: None
