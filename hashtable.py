"""
Author: Armao Thao

Description:
    This file is a simple hash table example.
"""

HASH_TABLE_SIZE = 10


class HashData(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable(object):
    """
    HashTable class

    """
    def __init__(self,):
        self._table_size = 10
        self._threshold_size = (0.7 * self._size_table())
        self._hashtable = []
        self.resize()

    @property
    def _size_table(self):
        pass

    def _get_hash(self, key):
        return key % self._table_size

    def set_resize_threshold(self, threshold):
        pass

    def put(self, key, value):
        hash = self._get_hash(key)
        if self._hashtable[hash] is []:
            self._hashtable[hash].append(HashData(key, value))
        else:
            for item in self._hashtable[hash]:
                if item.key == key:
                    item.value = value
                    return
            self._hashtable[hash].append(HashData(key, value))

    def get(self, key):
        hash = self._get_hash(key)
        if self._hashtable[hash] is []:
            return None
        for item in self._hashtable:
            if item.key == key:
                return item.value

    def remove(self, key):
        hash = self._get_hash(key)
        if self._hashtable[hash] is []:
            return
        for item in self._hashtable[hash]:
            if item.key == key:
                del item

    def resize(self):
        if not self._hashtable:
            self._hashtable = [[] for i in range(self._table_size)]
        else:
            self._table_size = 2 * self._table_size
            temp = self._hashtable[:]
            self._hashtable = [[] for i in range(self._table_size)]
            for lst in temp:
                for item in lst:
                    hash = self._get_hash(item.key)
                    self._hashtable[hash].append(item)


if __name__ == "__main__":
    print("Hash Table")

