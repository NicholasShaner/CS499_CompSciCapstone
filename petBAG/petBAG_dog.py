# ############### #
# petBAG_dog.py
# Creator : Nicholas Shaner
# For : SNHU CS 499 - Computer Science Capstone
# Version : 1.0 (init)
# Intent :  This file contains the petBAG_dog class, which 
#           is a subclass of petBAG_pet class. It represents 
#           a dog pet in the petBAG system.
#
# ############### #

# Import pet class from petBAG_pet module for inheritance
from petBAG_pet import pet

# Define dog class as a subclass of pet class
class dog(pet):
    def __init__(self, ownerFirst, ownerLast, ownerPhone, ownerEmail, petName, petWeight, petAge, dogBreed):
        super().__init__(ownerFirst, ownerLast, ownerPhone, ownerEmail, petName, petWeight, petAge)

        self.breed = dogBreed.lower()

    # Getter method for dog breed
    def getBreed(self):
        return self.breed
    
    # Method to display Dog Information
    def displayDogInfo(self):
        print(f"{self.petName}\'s Information: ")
        print(f"Breed: {self.breed}")
        print(f"Weight: {self.weight} lbs")
        print(f"Age: {self.age} years")
        print(f"Status: {self.status}")