### Solution Using Only HashMap ###
# Problem: Implement a Data Structure with AllOne Operations
# Description: Design a data structure `AllOne` that supports the following operations:
# - `inc(key)`: Increments the count of the key. If the key doesn't exist, it's initialized with a value of 1.
# - `dec(key)`: Decrements the count of the key. If the key's count reaches 0, it is removed from the data structure.
# - `getMaxKey()`: Returns one of the keys with the highest count. If no keys exist, return an empty string.
# - `getMinKey()`: Returns one of the keys with the lowest count. If no keys exist, return an empty string.

class AllOne:

    def __init__(self):
        """
        Initializes the data structure. The dictionary `d` holds the keys and their respective counts.
        """
        self.d = {}

    def inc(self, key: str) -> None:
        """
        Increments the count of the specified key. If the key doesn't exist, it is initialized with a count of 1.
        :param key: str, the key to increment.
        :return: None
        """
        if key not in self.d:
            self.d[key] = 0
        self.d[key] += 1

    def dec(self, key: str) -> None:
        """
        Decrements the count of the specified key. If the count reaches 0, the key is removed from the dictionary.
        :param key: str, the key to decrement.
        :return: None
        """
        if key in self.d:
            self.d[key] -= 1
            if self.d[key] == 0:
                del self.d[key]

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with the maximum count. If no keys exist, returns an empty string.
        :return: str, the key with the maximum count, or an empty string if no keys exist.
        """
        if not self.d:
            return ""
        max_val = max(self.d.values())
        for key, val in self.d.items():
            if val == max_val:
                return key
        return ""

    def getMinKey(self) -> str:
        """
        Returns one of the keys with the minimum count. If no keys exist, returns an empty string.
        :return: str, the key with the minimum count, or an empty string if no keys exist.
        """
        if not self.d:
            return ""
        min_val = min(self.d.values())
        for key, val in self.d.items():
            if val == min_val:
                return key
        return ""


## Time Complexity:
# - `inc`: O(1), since dictionary operations (insertion and updating values) are on average O(1).
# - `dec`: O(1), similarly to `inc`.
# - `getMaxKey`: O(n), where n is the number of keys, since we need to find the maximum value.
# - `getMinKey`: O(n), same as `getMaxKey`.

## Space Complexity: O(n), where n is the number of keys in the data structure.

# Example usage:
# obj = AllOne()
# obj.inc("key1")   # key1 -> 1
# obj.inc("key1")   # key1 -> 2
# obj.inc("key2")   # key2 -> 1
# obj.dec("key2")   # key2 -> removed
# print(obj.getMaxKey())  # Expected output: "key1"
# print(obj.getMinKey())  # Expected output: "key1"
