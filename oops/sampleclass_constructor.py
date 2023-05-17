class MySampleClass:
    year=2023
    def __init__(self, peru, vayass, stalam):
        self.name=peru
        self.age=vayass
        self.place=stalam
    def name_para(self):                                          #init(construtor) call cheytillelum work cheyyum
        print("hai " + self.name)
    def vayass_para(self):
        print("you are ",self.age," years old")
    def stalam_para(self):
        print("you are from " + self.place)
    def full_details(self):
        print("name: " + self.name)
        print("age: " , self.age)
        print("place: " + self.place)                #user inte kayyinnu input medikkandadathokke
        print("year : " , MySampleClass.year)         # def fuction _name(self,input kodukkanam
    def add_age(self):
        self.age = self.age + 1
    def relocate(self,place):
        self.place=place
    @classmethod
    def add_year(cls):
        cls.year=cls.year+1

x=MySampleClass("sojan",23,"kottayam")
x.name_para()
x.vayass_para()
x.full_details()
print("_____________________________________________")
y=MySampleClass("sachin",20,"kottayam")
y.name_para()
y.stalam_para()
y.relocate("pala")
y.full_details()
print("_____________________________________________")
MySampleClass.year=MySampleClass.year+1
"-----------or-------------"
MySampleClass.add_year()
x.add_age()
x.full_details()
print("_____________________________________________")
y.add_age()
y.full_details()