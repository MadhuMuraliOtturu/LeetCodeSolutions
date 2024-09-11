# Problem: Frequency Tracker
# Description: Implement a class `FrequencyTracker` that allows you to track the frequency of numbers
# and check if any number has a specific frequency. You can add or delete numbers and query the frequency.

class FrequencyTracker(object):
    def __init__(self):
        """
        Initializes the FrequencyTracker with two dictionaries:
        - `d` to map numbers to their frequencies.
        - `f` to map frequencies to the count of numbers with that frequency.
        """
        self.d = {}  # Number to frequency mapping
        self.f = {}  # Frequency to count of numbers with that frequency

    def add(self, number):
        """
        Adds a number to the tracker, updating its frequency and adjusting the frequency counts.

        :param number: Integer, the number to add.
        """
        if number not in self.d:
            old_freq = 0
            new_freq = 1
            self.d[number] = new_freq
        else:
            old_freq = self.d[number]
            new_freq = old_freq + 1
            self.d[number] = new_freq

        # Update frequency counts in `self.f`
        if old_freq in self.f and self.f[old_freq] > 0:
            self.f[old_freq] -= 1
            if self.f[old_freq] == 0:
                del self.f[old_freq]

        if new_freq in self.f:
            self.f[new_freq] += 1
        else:
            self.f[new_freq] = 1

    def deleteOne(self, number):
        """
        Deletes one occurrence of a number from the tracker, updating its frequency and adjusting the frequency counts.

        :param number: Integer, the number to delete.
        """
        if number in self.d and self.d[number] > 0:
            old_freq = self.d[number]
            new_freq = old_freq - 1
            self.d[number] = new_freq

            # Update frequency counts in `self.f`
            if old_freq in self.f and self.f[old_freq] > 0:
                self.f[old_freq] -= 1
                if self.f[old_freq] == 0:
                    del self.f[old_freq]

            if new_freq > 0:
                if new_freq in self.f:
                    self.f[new_freq] += 1
                else:
                    self.f[new_freq] = 1
            else:
                del self.d[number]  # Remove the number if frequency drops to 0

    def hasFrequency(self, frequency):
        """
        Checks if any number has a specific frequency.

        :param frequency: Integer, the frequency to check.
        :return: Boolean, True if any number has the specified frequency, False otherwise.
        """
        return self.f.get(frequency, 0) > 0

## Intuition:
# The `FrequencyTracker` class maintains two dictionaries: `d` for number-to-frequency mapping and `f` for frequency-to-count mapping.
# The `add` method updates the frequency of a number and adjusts the frequency counts. The `deleteOne` method reduces the frequency of a number or removes it if its frequency drops to zero.
# The `hasFrequency` method checks if there is any number with the specified frequency.
