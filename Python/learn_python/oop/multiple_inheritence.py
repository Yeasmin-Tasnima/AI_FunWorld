class Father:
    def gardening(self):
        print('Father hobby: I love Gardening.')

    def skills(self):
        print('Father skills: Programming.')


class Mother:
    def cooking(self):
        print('Mother hobby: I love Gardening.')

    def skills(self):
        print('Mother skills: Painting.')


class Child(Father, Mother):
    def sporting(self):
        self.gardening()
        self.cooking()
        print('Child hobby: I love Sports.')

    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print('Child skills: Playing.')


c = Child()
c.sporting()
c.skills()
