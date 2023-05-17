class Main_class:
    def __init__(self):
        print("base init")
    def set_name(self,name):
        self.name=name
    def display(self):
        print("hello "+self.name)

class Subclass(Main_class):
    def __init__(self):
        super(Subclass, self).__init__()
        print("sub class init")
    def show(self):
        print("welcome "+self.name)

y=Subclass()
y.set_name("sojan")
y.display()
y.show()