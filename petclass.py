class Pet:
    def __init__(self):
        self.__name= "Name"
        self.__animal_type= "Animal Type"
        self.__age= "Age"

    def set_name(self,name):
        self.__name= name

    def set_animal_type(self, an_type):
        self.__animal_type=an_type

    def set_age(self, age):
        self.__age= age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

def main():
    name= input("Enter the name of your pet:")
    animal_type= input("Enter the animal type of your pet:")
    age= int(input("Enter the age of your pet:"))

    my_pet= Pet()
    my_pet.set_name(name)
    print(my_pet.get_name())
    my_pet.set_animal_type(animal_type)
    print(my_pet.get_animal_type())
    my_pet.set_age(age)
    print(my_pet.get_age())

main()
