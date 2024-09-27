# Problem: MyCalendar Two - Event Booking with Double Booking Detection
# Description: Implement a class `MyCalendarTwo` that allows booking events such that no more than two events overlap.
# The `book` method should return True if the event can be booked without creating a triple booking, and False otherwise.

class MyCalendarTwo:
    def __init__(self):
        """
        Initializes two lists: 
        - `events` to store the single bookings.
        - `second` to store the double bookings.
        """
        self.events = []  # List of single booked events
        self.second = []  # List of double booked events
    
    def book(self, start: int, end: int) -> bool:
        """
        Books an event if it does not result in a triple booking.

        :param start: int, the start time of the event.
        :param end: int, the end time of the event (non-inclusive).
        :return: bool, True if the event can be booked, False otherwise.
        """
        # Check if this event would create a triple booking
        for s, e in self.second:
            if start < e and end > s:  # Overlap condition with double bookings
                return False
        
        # Check for overlaps with single bookings and add to second bookings if necessary
        for s, e in self.events:
            if start < e and end > s:  # Overlap with single bookings
                self.second.append((max(start, s), min(end, e)))  # Add overlap to second bookings
        
        # Add this event to single bookings
        self.events.append((start, end))
        return True

## Time Complexity: O(N), where N is the number of previously booked events.
## Space Complexity: O(N), for storing all events and double-booked intervals.

# Example usage:
# my_calendar = MyCalendarTwo()
# print(my_calendar.book(10, 20))  # Expected output: True, first booking
# print(my_calendar.book(50, 60))  # Expected output: True, no overlap with any booking
# print(my_calendar.book(10, 40))  # Expected output: True, creates a double booking but no triple booking
# print(my_calendar.book(5, 15))   # Expected output: False, creates a triple booking with [10, 20] and [10, 40]
