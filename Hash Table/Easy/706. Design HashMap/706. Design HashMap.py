class MyHashMap:

    def __init__(self):
        """
        Initializes the MyHashMap object.
        """
        self.d = {}  # Initialize an empty dictionary to store key-value pairs

    def put(self, key: int, value: int) -> None:
        """
        Inserts or updates the value associated with the key.

        :param key: Integer key to be inserted or updated.
        :param value: Integer value to be associated with the key.
        """
        self.d[key] = value

    def get(self, key: int) -> int:
        """
        Retrieves the value associated with the key.

        :param key: Integer key whose associated value is to be retrieved.
        :return: Integer value associated with the key. Returns -1 if the key does not exist.
        """
        if key not in self.d:
            return -1  # Key does not exist
        return self.d[key]

    def remove(self, key: int) -> None:
        """
        Removes the key and its associated value if the key exists.

        :param key: Integer key to be removed.
        """
        if key in self.d:
            self.d.pop(key)  # Remove the key-value pair from the dictionary

# Example usage:
# obj = MyHashMap()
# obj.put(key, value)
# param_2 = obj.get(key)  # Retrieves the value associated with the key
# obj.remove(key)  # Removes the key and its associated value
