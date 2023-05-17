class Main_class:
    def set_name(self,name):
        self.name=name
    def display(self):
        print("hello "+self.name)

class Subclass(Main_class):
    def show(self):
        print("welcome "+self.name)

x=Main_class()
name="sojan"
x.set_name(name)
x.display()

y=Subclass()
y.set_name("sachin")
y.display()
y.show()
