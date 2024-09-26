# Problem: Implement a Calendar Booking System
# Description: You are required to implement a class `MyCalendar` that allows booking events. Each event has a 
# start time and an end time. A booking is valid if it does not overlap with any previously booked event.
# The `book` method should return True if the booking can be made and False otherwise.

class MyCalendar:
    def __init__(self):
        """
        Initializes an empty list to store booked events.
        """
        self.event = []
        
    def book(self, start: int, end: int) -> bool:
        """
        Books an event if it does not overlap with any existing event.

        :param start: int, the start time of the event.
        :param end: int, the end time of the event (non-inclusive).
        :return: bool, True if the event can be booked, False otherwise.
        """
        # Sort events to ensure they are checked in order.
        self.event.sort()
        # Check for overlap with existing events.
        for s, e in self.event:
            if e > start and end > s:
                return False
        # If no overlap, book the event.
        self.event.append([start, end])
        return True

## Time Complexity: O(N log N), where N is the number of booked events due to sorting.
## Space Complexity: O(N), where N is the number of booked events stored in the list.

# Example usage:
# my_calendar = MyCalendar()
# print(my_calendar.book(10, 20))  # Expected output: True, since it is the first booking.
# print(my_calendar.book(15, 25))  # Expected output: False, as it overlaps with the previous booking.
# print(my_calendar.book(20, 30))  # Expected output: True, as it does not overlap with any existing booking.
