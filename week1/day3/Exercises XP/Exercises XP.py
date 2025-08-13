#exercice1:
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
cat1 = Cat("lolo",4)
cat2 = Cat("caty", 5)
cat3 = Cat("oso", 6)

def find_oldest_cat(*cats):
    return max(cats, key=lambda cat: cat.age)

oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest  is {oldest_cat.name}, and is {oldest_cat.age} years old.")
#exercice2:
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    def bark(self):
        print(f"{self.name} goes woof!")
    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")
davids_dog = Dog("Rex", 50)
print(f"David's dog name: {davids_dog.name}")
print(f"David's dog height: {davids_dog.height} cm")
davids_dog.bark()
davids_dog.jump()
sarahs_dog = Dog("Teacup", 20)
print(f"Sarah's dog name: {sarahs_dog.name}") 
print(f"Sarah's dog height: {sarahs_dog.height} cm")
sarahs_dog.bark() 
sarahs_dog.jump() 
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is taller than {sarahs_dog.name}.")  
else:
    print(f"{sarahs_dog.name} is taller than {davids_dog.name}.")
# exercice3
class song:
    def __init__(self,lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
stairway = song([
    "There’s a lady who's sure",
    "all that glitters is gold",
    "and she’s buying a stairway to heaven"
])
stairway.sing_me_a_song()
# exercice4
class Zoo:
    def __init__(self, zoo_name):       
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        self.animals.append(animal)
        print(f"{animal} has been added to the zoo.")
    def get_animals(self):
        print("Animals in the zoo:", self.animals)
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold.")
        else:
            print(f"{animal_sold} is not in the zoo.")
    def sort_animals(self):
        self.animals.sort()
        print("Animals sorted alphabetically:", self.animals)   
    def get_groups(self):
        for letter, group in self.animal_groups.items():
            if len(group) == 1:
                print(f"{letter}: {group[0]}")
            else:
                print(f"{letter}: {group}")  