# HashMap classed used to create hashmap object to store package objects in
class HashMap:
    def __init__(self):
        self.size = 40
        self.map = [None] * self.size

    # O(1) - takes package id as key and returns hashed value
    def _get_hash(self, key):
        return key % self.size

    # Average Case: O(1) - Worst Case: O(N) - takes package key, and package object and adds them to the hashmap
    def add(self, key, package):
        key_hash = self._get_hash(key)
        key_value = [key, package]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = package
                    return True
            # chaining implemented to fulfill self adjusting data structure requirement
            self.map[key_hash].append(key_value)
            return True

    # Average Case: O(1) - Worst Case: O(N) - takes package id as key and returns the package from the hashmap
    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    # Average Case: O(1) - Worst Case: O(N) - takes package id as key and removes that package object from hashmap
    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range (0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    # # prints hashmap
    # def print(self):
    #     print('---Packages---')
    #     for item in self.map:
    #         if item is not None:
    #             print(str(item))
