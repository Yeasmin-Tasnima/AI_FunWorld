class Human:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def do_work(self):
        if self.occupation == 'doctor':
            print('{} is a {}'.format(self.name, self.occupation))
        elif self.occupation == 'engineer':
            print('{} is an {}'.format(self.name, self.occupation))
        else:
            print('{} is from an unknown occupation'.format(self.name))


obj1 = Human('tasnim', 'engineer')
obj2 = Human('moonmoon', 'doctor')
obj3 = Human('Mr.X', 'unknown')

obj1.do_work()
obj2.do_work()
obj3.do_work()