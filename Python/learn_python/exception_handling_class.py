class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg

    def printing_exception(self):
        print('User defined exception: {}'.format(self.msg))

    def handling_exception(self):
        print('Accident occurred. Take Detour')


try:
    raise Accident('Collision of two cars.')
except Accident as e:
    e.printing_exception()
    e.handling_exception()
