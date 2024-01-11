#class peron

class person:
    def __init__(self, name, age, gender, birth_date, town):
        self.name = name
        self.age = age
        self.gender = gender
        self.birth_date = birth_date
        self.town = town
    def greet(self):
        return f"Hello, my name is {self.name}, i'm {self.age} years old, gender {self.gender} i was born in {self.town}"
    
person1 = person("Eng.ziroh",37,"Male",1986-9-25,"Kilifi")
print(person1.greet())