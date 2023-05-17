class MySampleClass:
    def hello(self,n):
        self.name=n
    def prnt(self):
        print("hai " + self.name)
x=MySampleClass( )
name="sojan philip"
x.hello(name)
x.prnt()

y=MySampleClass()
y.hello("sachin philip")
y.prnt()