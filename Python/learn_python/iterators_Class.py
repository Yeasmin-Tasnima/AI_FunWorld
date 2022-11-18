class RemoteControl:
    def __init__(self):
        self.channels = ['HBO', 'CNN', 'Discovery', 'BBC']
        self.index = -1  # current index of the channel list

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration
        return self.channels[self.index]


r = RemoteControl()
itr = iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
