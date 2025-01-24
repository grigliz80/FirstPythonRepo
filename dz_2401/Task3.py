"""
Task 3
---------------------
TV controller

Create a simple prototype of a TV controller in Python.
It'll use the following commands:

first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel.
Pay attention that the channel numbers start from 1, not from 0.
next_channel() - turns on the next channel.
If the current channel is the last one, turns on the first channel.
previous_channel() - turns on the previous channel.
If the current channel is the first one, turns on the last channel.
current_channel() - returns the name of the current channel.
exists(N/'name') - gets 1 argument - the number N or the string 'name'
and returns "Yes", if the channel N or 'name' exists in the list,
or "No" - in the other case.

The default channel turned on before all commands is №1.

Your task is to create the TVController class and methods described above.
"""


class TVController:

    def __init__(self, channels):
        self.channels = channels
        self.current = 0

    def first_channel(self):
        self.current = 0
        return self.channels[self.current]

    def last_channel(self):
        self.current = len(self.channels) - 1
        return self.channels[self.current]

    def turn_channel(self, N):
        if 1 <= N <= len(self.channels):
            self.current = N - 1
            return self.channels[self.current]
        else:
            return "Channel does not exist"

    def next_channel(self):
        self.current = (self.current + 1) % len(self.channels)
        return self.channels[self.current]

    def previous_channel(self):
        self.current = (self.current - 1) % len(self.channels)
        return self.channels[self.current]

    def current_channel(self):
        return self.channels[self.current]

    def exists(self, query):
        if isinstance(query, int):
            return "Yes" if 1 <= query <= len(self.channels) else "No"
        elif isinstance(query, str):
            return "Yes" if query in self.channels else "No"
        else:
            return "No"


def main():

    CHANNELS = ['BBC', 'EUROSPORT', 'TV1000', 'N-channel']

    my_pult = TVController(CHANNELS)

    print(my_pult.first_channel())
    print(my_pult.last_channel())
    print(my_pult.turn_channel(3))
    print(my_pult.next_channel())
    print(my_pult.previous_channel())
    print(my_pult.current_channel())
    print(my_pult.exists(5))
    print(my_pult.exists("N-channel"))


if __name__ == "__main__":
    main()
