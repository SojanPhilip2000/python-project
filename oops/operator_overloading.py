class SampleClass:
    def set_name(self,name):
        self.name=name
    def __add__(self,other):
        name=self.name+" "+ other.name
        return name
first=SampleClass( )
second=SampleClass()
first.set_name("sojan")
second.set_name("philip")
fullname=first+second
print(fullname)
