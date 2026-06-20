# ############### #
# petBAG_crud.py
# Creator : Nicholas Shaner
# For : SNHU CS 499 - Computer Science Capstone
# Version : 2.0 (module 4 enhancements)
# Intent :  This file contains the CRUD operations for managing pets in the petBAG system.
# ############### #

from petBAG_dict import petBAG_dict
import json

## CRUD Operations

# CREATE:

# Add a new dog pet to new client in petBAG system
@staticmethod
def create_newDog(dog):
    try:
        petBAG_dict.pet_dict[dog.getOwnerPhone()] = {dog.getPetName() : (dog.__dict__)}
        print(f"New dog {dog.getPetName()} added to petBAG system for owner account {dog.getOwnerPhone()}.")

    except Exception as e:
        print(f"Error: There was an issue adding new dog to owner account {dog.getOwnerPhone()}. Verify information and try again.")

# Add new dog to existing client in petBAG system
@staticmethod
def create_existingDog(dog):
    try:
        print(f"Adding new dog {dog.getPetName()} to owner account {dog.getOwnerPhone()}.")
        petBAG_dict.pet_dict[dog.getOwnerPhone()].update({dog.getPetName(): dog.__dict__})

    except KeyError:
        print(f"Error: There was an issue adding new pet to owner account {dog.getOwnerPhone()}. Verify information and try again.")

    print(f"New dog {dog.getPetName()} added to petBAG system successfully.")
    pass

# Add a new cat pet to new client in petBAG system
@staticmethod
def create_newCat(cat):
    try:
        petBAG_dict.pet_dict[cat.getOwnerPhone()] = {cat.getPetName() : (cat.__dict__)}
        print(f"New cat {cat.getPetName()} added to petBAG system for owner account {cat.getOwnerPhone()}.")

    except Exception as e:
        print(f"Error: There was an issue adding new cat to owner account {cat.getOwnerPhone()}. Verify information and try again.")
    pass

# Add new cat to existing client in petBAG system
@staticmethod
def create_existingCat(cat):
    try:
        print(f"Adding new cat {cat.getPetName()} to owner account {cat.getOwnerPhone()}.")
        
        petBAG_dict.pet_dict[cat.getOwnerPhone()].update({cat.getPetName(): cat.__dict__})
    except KeyError:
        print(f"Error: There was an issue adding new cat to owner account {cat.getOwnerPhone()}. Verify information and try again.")
    pass

# Add new BAG service to pet in petBAG system
@staticmethod
def create_newService(ownerPhone, petName, service):
    try:
        if ownerPhone in petBAG_dict.pet_dict:
            if petName in petBAG_dict.pet_dict[ownerPhone]:
                petBAG_dict.pet_dict[ownerPhone][petName]["Service"] = service
                print(f"New service successfully added to pet {petName} for owner account {ownerPhone} in petBAG system.")
            else:
                print(f"Error: No pet found with name {petName} for owner phone {ownerPhone}. Verify information and try again.")
        else:
            print(f"Error: No owner found with phone {ownerPhone}. Verify information and try again.")
    except KeyError:
        print(f"Error: There was an issue adding new service to pet {petName} for owner account {ownerPhone}. Verify information and try again.")
    pass

# READ:

# Retrieve ALL pet information from petBAG system
@staticmethod
def read_allPets():
    if petBAG_dict.pet_dict != {}:
        for ownerPhone in petBAG_dict.pet_dict.items():
            print(json.dumps(ownerPhone, indent = 2))
    else:
        print("No pets found in petBAG system.")    

# Retrieve SINGLE pet information from petBAG system
@staticmethod
def read_singlePet(ownerPhone, petName):
    try:
        if ownerPhone in petBAG_dict.pet_dict:
            if petName in petBAG_dict.pet_dict[ownerPhone]:
                print(json.dumps(petBAG_dict.pet_dict[ownerPhone][petName], indent = 2))
            else:
                print(f"Error: No pet found with name {petName} for owner phone {ownerPhone}.")
                pass
        else:
            print(f"Error: No owner found with phone {ownerPhone}.")
    except KeyError:
        print(f"Error: Something went wrong, check phone {ownerPhone} and pet name {petName} and try again.")
        pass

# Read current BAG service
@staticmethod
def read_currentService(ownerPhone, petName):
    try:
        # Drawn out nested if statements to provide more specific error checking to user when determining service for pet, for owner
        if ownerPhone in petBAG_dict.pet_dict:
            if petName in petBAG_dict.pet_dict[ownerPhone]:
                if "Service" in petBAG_dict.pet_dict[ownerPhone][petName]:
                    print(json.dumps(petBAG_dict.pet_dict[ownerPhone][petName]["Service"], indent = 2))
                else:
                    print(f"Error: No service found for pet {petName} for owner phone {ownerPhone}.")
                    pass
            else:
                print(f"Error: No pet found with name {petName} for owner phone {ownerPhone}.")
                pass
        else:
            print(f"Error: No owner found with phone {ownerPhone}.")
            pass
    except KeyError:
        print(f"Error: Something went wrong, check phone and pet name and try again.")
        pass

# Read Single Client Information
@staticmethod
def read_singleClient(ownerPhone):
    try:
        if ownerPhone in petBAG_dict.pet_dict:
            firstClient = next(iter(petBAG_dict.pet_dict[ownerPhone].values()))
            print("\n")
            print(f"Owner First Name: {firstClient['ownerFirst']}")
            print(f"Owner Last Name: {firstClient['ownerLast']}")
            print(f"Owner Phone: {firstClient['ownerPhone']}")
            print(f"Owner Email: {firstClient['ownerEmail']}")    
            print(f"\nNumber of Pets: {sum(1 for _ in petBAG_dict.pet_dict[ownerPhone].values())}")
        else:
            print(f"Error: No owner found with phone {ownerPhone}.")

    except KeyError:
        print(f"Error: Something went wrong, check information and try again.")
    pass

# Read All Client Information
@staticmethod
def read_allClients():
    if petBAG_dict.pet_dict != {}:
        for ownerPhone, pets_dict in petBAG_dict.pet_dict.items():
            firstClient = next(iter(petBAG_dict.pet_dict[ownerPhone].values()))
            print("\n")
            print(f"Owner First Name: {firstClient['ownerFirst']}")
            print(f"Owner Last Name: {firstClient['ownerLast']}")
            print(f"Owner Phone: {firstClient['ownerPhone']}")
            print(f"Owner Email: {firstClient['ownerEmail']}")
            print(f"Number of Pets: {sum(1 for _ in pets_dict.values())}")
        print(" ")
    else:
        print("No clients found in petBAG system.")
    pass

# UPDATE:

# Update owner information in petBAG system
@staticmethod
def update_ownerPhone(ownerPhone, newPhone):
    try:
        if ownerPhone in petBAG_dict.pet_dict:
            petBAG_dict.pet_dict[newPhone] = petBAG_dict.pet_dict.pop(ownerPhone)
            print(f"Owner phone updated from {ownerPhone} to {newPhone} in petBAG system.")
        else:
            print(f"Error: No owner found with phone {ownerPhone}. Cannot update phone.")
    except KeyError:
        print(f"Error: Something went wrong, check phone information and try again.")
    pass

# Update owner email in petBAG system
@staticmethod
def update_ownerEmail(ownerPhone, newEmail):
    try:
        if ownerPhone in petBAG_dict.pet_dict:
            for pet in petBAG_dict.pet_dict[ownerPhone].values():
                pet["ownerEmail"] = newEmail
            print(f"Owner email updated to {newEmail} for owner phone {ownerPhone} in petBAG system.")
        else:
            print(f"Error: No owner found with phone {ownerPhone}. Cannot update email.")
    except KeyError:
        print(f"Error: Something went wrong, check email information and try again.")
    pass

# Update owner first name in petBAG system
@staticmethod
def update_ownerFirstName(ownerPhone, newFirstName):
    try:
        if ownerPhone in petBAG_dict.pet_dict:
            for pet in petBAG_dict.pet_dict[ownerPhone].values():
                pet["ownerFirst"] = newFirstName
            print(f"Owner first name updated to {newFirstName} for owner phone {ownerPhone} in petBAG system.")
        else:
            print(f"Error: No owner found with phone {ownerPhone}. Cannot update first name.")
    except KeyError:
        print(f"Error: Something went wrong, check first name information and try again.")
    pass

# Update owner last name in petBAG system
@staticmethod
def update_ownerLastName(ownerPhone, newLastName):
    try:
        if ownerPhone in petBAG_dict.pet_dict:
            for pet in petBAG_dict.pet_dict[ownerPhone].values():
                pet["ownerLast"] = newLastName
            print(f"Owner last name updated to {newLastName} for owner phone {ownerPhone} in petBAG system.")
        else:
            print(f"Error: No owner found with phone {ownerPhone}. Cannot update last name.")
    except KeyError:
        print(f"Error: Something went wrong, check last name information and try again.")
    pass

# Update pet status in petBAG system Active to Inactive
@staticmethod
def update_petStatus(ownerPhone, petName, status):
    try:        
        if ownerPhone in petBAG_dict.pet_dict:
            if petName in petBAG_dict.pet_dict[ownerPhone]:
                petBAG_dict.pet_dict[ownerPhone][petName]["status"] = status
                print(f"Pet {petName} status updated to {status} for owner phone {ownerPhone} in petBAG system.")
            else:
                print(f"Error: No pet found with name {petName} for owner phone {ownerPhone}. Cannot update status.")
        else:
            print(f"Error: No owner found with phone {ownerPhone}. Cannot update status.")
    except KeyError:
        print(f"Error: Something went wrong, check status information and try again.")
    pass

# Update pet weight in petBAG system
@staticmethod
def update_petWeight(ownerPhone, petName, newWeight):
    try:
        if ownerPhone in petBAG_dict.pet_dict:
            if petName in petBAG_dict.pet_dict[ownerPhone]:
                petBAG_dict.pet_dict[ownerPhone][petName]["weight"] = newWeight
                print(f"Pet {petName} weight updated to {newWeight} for owner phone {ownerPhone} in petBAG system.")
            else:
                print(f"Error: No pet found with name {petName} for owner phone {ownerPhone}. Cannot update weight.")
        else:
            print(f"Error: No owner found with phone {ownerPhone}. Cannot update weight.")
    except KeyError:
        print(f"Error: Something went wrong, check weight information and try again.")
    pass

# Update pet age in petBAG system
@staticmethod
def update_petAge(ownerPhone, petName, newAge):
    try:
        if ownerPhone in petBAG_dict.pet_dict:
            if petName in petBAG_dict.pet_dict[ownerPhone]:
                petBAG_dict.pet_dict[ownerPhone][petName]["age"] = newAge
                print(f"Pet {petName} age updated to {newAge} for owner phone {ownerPhone} in petBAG system.")
            else:
                print(f"Error: No pet found with name {petName} for owner phone {ownerPhone}. Cannot update age.")
        else:
            print(f"Error: No owner found with phone {ownerPhone}. Cannot update age.")
    except KeyError:
        print(f"Error: Something went wrong, check age information and try again.")
    pass

    # Update pet 

# DELETE:

# Delete pet record from petBAG system
@staticmethod
def delete_pet(ownerPhone, petName):
    try:
        if ownerPhone in petBAG_dict.pet_dict:
            if petName in petBAG_dict.pet_dict[ownerPhone]:
                del petBAG_dict.pet_dict[ownerPhone][petName]
                print(f"Pet {petName} removed from petBAG system for owner phone {ownerPhone}.")
                if len(petBAG_dict.pet_dict[ownerPhone]) == 0:
                    del petBAG_dict.pet_dict[ownerPhone]
                    print(f"Owner account with phone {ownerPhone} removed from petBAG system as no more pets are associated with this owner.")
                else:
                    print(f"Owner account with phone {ownerPhone} still active with {len(petBAG_dict.pet_dict[ownerPhone])} remaining pet(s).")
        else:
            print(f"Error: No pet found with name {petName} for owner phone {ownerPhone}.")
    except KeyError:
        print(f"Error: Something went wrong, check pet information and try again.")
    pass

# Delete BAG service from petBAG system
@staticmethod
def delete_service(ownerPhone, petName):
    try:
        if ownerPhone in petBAG_dict.pet_dict:
            if petName in petBAG_dict.pet_dict[ownerPhone]:
                if "Service" in petBAG_dict.pet_dict[ownerPhone][petName]:
                    del petBAG_dict.pet_dict[ownerPhone][petName]["Service"]
                    print(f"Service removed from pet {petName} for owner phone {ownerPhone} in petBAG system.")
                else:
                    print(f"Error: No service found for pet {petName} for owner phone {ownerPhone}. Cannot delete service.")
            else:
                print(f"Error: No pet found with name {petName} for owner phone {ownerPhone}. Cannot delete service.")
        else:
            print(f"Error: No owner found with phone {ownerPhone}. Cannot delete service.")
    except KeyError:
        print(f"Error: Something went wrong, check service information and try again.")
    pass

# Delete owner record including all pets from petBAG system
@staticmethod
def delete_owner(ownerPhone):
    try:
        del petBAG_dict.pet_dict[ownerPhone]
        print(f"Owner with phone {ownerPhone} and all associated pets removed from petBAG system.")
    except KeyError:
        print(f"Error: Something went wrong, check owner information and try again.")
    pass