class First:
    def display_first(self,name):
        self.name=name
        print("hello "+self.name)
class Second:
    def display_second(self):
        print("welcome ")
class Third(First,Second):
    def display_third(self):
        print("hai "+self.name)

x=Third()
x.display_first("sojan")
x.display_second()
x.display_third()