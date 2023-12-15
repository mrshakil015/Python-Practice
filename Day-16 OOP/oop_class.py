class Cat:

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    
    def catinfo(self):
        print(f"{self.name} is {self.age} year(s) old. Color is {self.color}" )
    
    def setBuddy(self, buddy):
        self.buddy = buddy
        buddy.buddy = self

pappu = Cat("Pappu",2,"White")
mimi = Cat("Mimi",4,"White & Golden")
pisi = Cat("Pisi",4,"Black & White")



pappu.catinfo()
mimi.catinfo()
pisi.catinfo()
pappu.setBuddy(pisi)
print(f"Buddy: {pappu.buddy.name}")
pappu.buddy.catinfo()
