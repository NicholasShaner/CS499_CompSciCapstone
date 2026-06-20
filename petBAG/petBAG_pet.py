# ############### #
# petBAG_pet.py
# Creator : Nicholas Shaner
# For : SNHU CS 499 - Computer Science Capstone
# Version : 1.0 (init)
# Intent :  This file contains the petBAG_pet class, which is a base class 
#           for all pets in the petBAG system. It defines common attributes and 
#           methods that all pets will have.
#
# ############### #

class pet:
    def __init__(self, ownerFirst, ownerLast, ownerPhone, ownerEmail, petName, petWeight, petAge):
        self.ownerFirst = ownerFirst.lower()
        self.ownerLast = ownerLast.lower()
        self.ownerPhone = int(ownerPhone)
        self.ownerEmail = ownerEmail.lower()
        self.name = petName.lower()
        self.weight = float(petWeight)
        self.age = int(petAge)
        self.status = "active"

    # Getter methods for pet/owner attributes
    def getOwnerFirst(self):
        return self.ownerFirst
    def getOwnerLast(self):
        return self.ownerLast
    def getOwnerPhone(self):
        return self.ownerPhone
    def getOwnerEmail(self):
        return self.ownerEmail
    def getPetName(self):
        return self.name
    def getPetWeight(self):
        return self.weight
    def getPetAge(self):
        return self.age
    def getStatus(self):
        return self.status
    
    
    # Test Method to display Owner Information
    # def displayOwnerInfo(self):
    #     print(f"{self.name}\'s Owner Information: ")
    #     print(f"Owner Name: {self.ownerFirst} {self.ownerLast}")
    #     print(f"Owner Phone: {self.ownerPhone}")
    #     print(f"Owner Email: {self.ownerEmail}")