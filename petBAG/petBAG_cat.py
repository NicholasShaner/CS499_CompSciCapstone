# ############### #
# petBAG_cat.py
# Creator : Nicholas Shaner
# For : SNHU CS 499 - Computer Science Capstone
# Version : 1.0 (init)
# Intent :  This file contains the petBAG_cat class, which 
#           is a subclass of petBAG_pet class. It represents 
#           a cat pet in the petBAG system.
#
# ############### #
# Import pet class from petBAG_pet module for inheritance
from petBAG_pet import pet

# Define cat class as a subclass of pet class
class cat(pet):
    def __init__(self, ownerFirst, ownerLast, ownerPhone, ownerEmail, petName, petWeight, petAge, catBreed):
        super().__init__(ownerFirst, ownerLast, ownerPhone, ownerEmail, petName, petWeight, petAge)
        
        self.breed = catBreed.lower()

    # Getter method for cat breed
    def getBreed(self):
        return self.breed
    
    # Method to display Cat Information
    def displayCatInfo(self):
        print(f"{self.petName}\'s Information: ")
        print(f"Breed: {self.breed}")
        print(f"Weight: {self.weight} lbs")
        print(f"Age: {self.age} years")
        print(f"Status: {self.status}")