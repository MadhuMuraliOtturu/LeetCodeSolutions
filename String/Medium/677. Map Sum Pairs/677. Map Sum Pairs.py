# Problem: Map Sum Pairs
# Description: Implement a `MapSum` class that supports two operations:
# 1. `insert(key, val)`: Insert the key with the corresponding value. If the key already exists, update the value.
# 2. `sum(prefix)`: Return the sum of all values of keys that start with the given prefix.

class MapSum:
    
    def __init__(self):
        """
        Initialize the MapSum object with two dictionaries:
        - `pref`: Stores the prefix sums.
        - `check`: Stores the original values of the keys to track any updates.
        """
        self.pref = {}  # Stores the prefix sums
        self.check = {}  # Stores the original values of the keys

    def insert(self, key: str, val: int) -> None:
        """
        Inserts the key with the corresponding value. If the key already exists, update the value.
        
        :param key: str - The key to insert.
        :param val: int - The value associated with the key.
        """
        # Check if the key has been inserted before, and get the previous value
        if key in self.check:
            co = self.check[key]
        else:
            co = 0
        
        # Calculate the difference between the new value and the previous value
        delta = val - co
        self.check[key] = val  # Update the key's value in the check dictionary
        
        # Update the prefix sums with the difference
        p = ""
        for let in key:
            p += let
            if p not in self.pref:
                self.pref[p] = 0
            self.pref[p] += delta

    def sum(self, prefix: str) -> int:
        """
        Returns the sum of all values of keys that start with the given prefix.
        
        :param prefix: str - The prefix to calculate the sum for.
        :return: int - The sum of values for keys with the given prefix.
        """
        # Return the sum for the given prefix, or 0 if it doesn't exist
        return self.pref.get(prefix, 0)

# Time Complexity:
# - `insert`: O(m), where m is the length of the key. We update the prefix sums for each character in the key.
# - `sum`: O(1), as we are just querying the sum for a given prefix in the dictionary.
# 
# Space Complexity: O(n * m), where n is the number of keys inserted, and m is the average length of the keys. We store each prefix in the dictionary.
#
# Example Usage:
# obj = MapSum()
# obj.insert("apple", 3)
# print(obj.sum("ap"))  # Output: 3
# obj.insert("app", 2)
# print(obj.sum("ap"))  # Output: 5
