# ############### #
# petBAG_launcher.py
# Creator : Nicholas Shaner
# For : SNHU CS 499 - Computer Science Capstone
# Version : 2.0 (module 4 enhancements)
# Intent :  This file contains the driver code for the petBAG system.
#           It controls the runtime flow of the program, including creating pet objects,
#           adding them to the petBAG_dict, and performing necessary CRUD operations.
#
# ############### #

import os
import time
import signal
import json
from urllib import response

from petBAG_dog import dog
from petBAG_cat import cat
from petBAG_crud import *
from petBAG_dict import petBAG_dict


## Menu Functions for User Interaction
# Reusable function to display the petBAG page header
def pageHeader():
    print("\033[47m" + "\033[31m" + "\033[1m" + "#############################################" + "\033[0m")
    print("\033[47m" + "\033[31m" + "\033[1m" + "               Welcome to...                 " + "\033[0m")
    print("\033[47m" + "\033[92m" + "\033[1m" + "    ***   ****  *****  ***     **    **      " + "\033[0m")
    print("\033[47m" + "\033[92m" + "\033[1m" + "    *  *  *       *    *  *   *  *  *  *     " + "\033[0m")
    print("\033[47m" + "\033[92m" + "\033[1m" + "    ***   ***     *    * *    ****  *        " + "\033[0m")
    print("\033[47m" + "\033[92m" + "\033[1m" + "    *     *       *    *  *   *  *  *  **    " + "\033[0m")
    print("\033[47m" + "\033[92m" + "\033[1m" + "    *     ****    *    ***    *  *   ***     " + "\033[0m")
    print("\033[47m" + "\033[31m" + "\033[1m" + "#############################################" + "\033[0m")

# petBAG Menu function to display options for user interaction
def petBAGMenuMain():
    print("\033[4m" + "\033[1m" + "Please select an option from the menu below:" + "\033[0m")
    print("\033[94m" + "1." + "\033[0m" + " Manage Pets")
    print("\033[94m" + "2." + "\033[0m" + " Manage Services")
    print("\033[94m" + "3." + "\033[0m" + " Manage Clients")
    print("\033[94m" + "0." + "\033[0m" + "\033[31m" + "\033[1m" + " Exit" + "\033[0m")
    menuOption = int(input("Enter menu option number: "))
    return menuOption

# petBAG Manage Pets Menu
def petBAGMenuPets():
    print("\033[4m" + "Please select an option from the menu below:" + "\033[0m")
    print("\033[94m" + "1." + "\033[0m" + " Add New Dog")
    print("\033[94m" + "2." + "\033[0m" + " Add New Cat")
    print("\033[94m" + "3." + "\033[0m" + " View Single Pet")
    print("\033[94m" + "4." + "\033[0m" + " View All Pets")
    print("\033[94m" + "5." + "\033[0m" + " Update Pet Information")
    print("\033[94m" + "6." + "\033[0m" + " Delete Pet")
    print("\033[94m" + "0. Return to Main Menu" + "\033[0m")
    menuOption = int(input("Enter menu option number: "))
    return menuOption

# petBAG Update Pet Information Menu
def petBAGMenuUpdatePetInfo():
    print("\033[4m" + "Please select an option from the menu below:" + "\033[0m")
    print("\033[94m" + "1." + "\033[0m" + " Update Pet Weight")
    print("\033[94m" + "2." + "\033[0m" + " Update Pet Age")
    print("\033[94m" + "3." + "\033[0m" + " Update Pet Status")
    print("\033[94m" + "0. Return to Pet Menu" + "\033[0m")
    menuOption = int(input("Enter menu option number: "))
    return menuOption

# petBAG Manage Services Menu
def petBAGMenuServices():
    print("\033[4m" + "Please select an option from the menu below:" + "\033[0m")
    print("\033[94m" + "1." + "\033[0m" + " Add New Service")
    print("\033[94m" + "2." + "\033[0m" + " View Current Service")
    print("\033[94m" + "3." + "\033[0m" + " Delete Service")
    print("\033[94m" + "0. Return to Main Menu" + "\033[0m")
    menuOption = int(input("Enter menu option number: "))
    return menuOption

# petBAG Manage Clients Menu
def petBAGMenuClients():
    print("\033[4m" + "Please select an option from the menu below:" + "\033[0m")
    print("\033[94m" + "1." + "\033[0m" + " View Single Client")
    print("\033[94m" + "2." + "\033[0m" + " View All Clients")
    print("\033[94m" + "3." + "\033[0m" + " Update Client Information")
    print("\033[94m" + "4." + "\033[0m" + " Delete Client")
    print("\033[94m" + "0. Return to Main Menu" + "\033[0m")
    menuOption = int(input("Enter menu option number: "))
    return menuOption

# petBAG Update Client Information Menu
def petBAGMenuUpdateClientInfo():
    print("\033[4m" + "Please select an option from the menu below:" + "\033[0m")
    print("\033[94m" + "1." + "\033[0m" + " Update Owner First Name")
    print("\033[94m" + "2." + "\033[0m" + " Update Owner Last Name")
    print("\033[94m" + "3." + "\033[0m" + " Update Owner Phone Number")
    print("\033[94m" + "4." + "\033[0m" + " Update Owner Email Address")
    print("\033[94m" + "0. Return to Client Menu" + "\033[0m")
    menuOption = int(input("Enter menu option number: "))
    return menuOption


## Misc. Program Function for Style and Functionality
# check and load petBAG_dict data from JSON file, if file does not exist, return empty dictionary
def load_petBAG_dict():
    try:
        if os.path.exists("petBAG_dict.json") and os.path.getsize("petBAG_dict.json") > 0:
            with open("petBAG_dict.json", "r") as petBAG_JSON:
                petBAG_dict.pet_dict = json.load(petBAG_JSON)
                return petBAG_dict.pet_dict
        else:
            print("No existing database found. Empty petBAG dictionary initialized.")
            petBAG_dict.pet_dict = {}
            return petBAG_dict.pet_dict
    except FileNotFoundError or json.JSONDecodeError:
        pass

# Save petBAG_dict data to JSON file for data persistence
def save_petBAG_dict(pet_dict):
    with open('petBAG_dict.json', 'w') as petBAG_JSON:
        json.dump(pet_dict, petBAG_JSON, indent=2)

# Clear console screen for better readability and user experience
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Graceful exit handler for program termination using Ctrl+C
def graceful_shutdown(signal, frame):
    clearScreen()
    pageHeader()

    print("\n" + "\033[31m" + "Graceful shutdown initiated." + "\033[0m" + " Saving database and exiting...")
    time.sleep(0.75)
    save_petBAG_dict(petBAG_dict.pet_dict)
    print("\033[32m" + "Database saved. Goodbye!" + "\033[0m")
    time.sleep(1.5)
    clearScreen()

    exit(0)

# Set up signal handlers for graceful shutdown on Ctrl+C or termination signal
signal.signal(signal.SIGINT, graceful_shutdown)  # Ctrl+C
signal.signal(signal.SIGTERM, graceful_shutdown)  # Termination signal from OS


## Main function to run the petBAG system
def main():
    running = True

    # Initialize petBAG dictionary with data from JSON file, or empty dictionary if file doesn't exist
    petBAG_dict.pet_dict = load_petBAG_dict() 

    # Program while loop to keep the petBAG system running until user chooses to exit
    while running:
        clearScreen()
        pageHeader()

        # Display main menu and get user selection
        menuOption = petBAGMenuMain()

        # End program loop and exit petBAG system
        if menuOption == 0:
            
            clearScreen()
            pageHeader()
            print("\033[32m" + "Thank you for using petBAG!" + "\033[0m")
            time.sleep(0.75)
            print("\033[32m" + "Saving Database..." + "\033[0m")
            time.sleep(0.75)

            save_petBAG_dict(petBAG_dict.pet_dict)

            print("\033[32m" + "\033[1m" + "Done!" + "\033[0m")
            time.sleep(0.75)
            clearScreen()
            running = False  # Exit program loop and end petBAG system

        # Display pet management menu and get user selection
        elif menuOption == 1:
            clearScreen()
            pageHeader()

            # Display pet management menu
            petMenuOption = petBAGMenuPets()

            ## Return to Main Menu
            if petMenuOption == 0:
                continue
            
            # Handle adding new dog
            elif petMenuOption == 1:
                
                ownerFirst = input("\033[1m" + "Enter owner's first name: " + "\033[0m")
                ownerLast = input("\033[1m" + "Enter owner's last name: " + "\033[0m")
                ownerPhone = input("\033[1m" + "Enter owner's phone number: " + "\033[0m")
                ownerEmail = input("\033[1m" + "Enter owner's email address: " + "\033[0m")
                petName = input("\033[1m" + "Enter dog's name: " + "\033[0m")
                petWeight = float(input("\033[1m" + "Enter dog's weight in pounds: " + "\033[0m"))
                petAge = int(input("\033[1m" + "Enter dog's age in years: " + "\033[0m"))
                dogBreed = input("\033[1m" + "Enter dog's breed: " + "\033[0m")

                # Create new dog object using user input and add to petBAG_dict using crud class method
                newDog = dog(ownerFirst, ownerLast, ownerPhone, ownerEmail, petName, petWeight, petAge, dogBreed)
                if ownerPhone in petBAG_dict.pet_dict:
                    create_existingDog(newDog)
                else:
                    create_newDog(newDog)

                save_petBAG_dict(petBAG_dict.pet_dict)

                time.sleep(1.0)
                clearScreen()
                pageHeader()
                petBAGMenuPets()
            
            # Handle adding new cat
            elif petMenuOption == 2:

                ownerFirst = input("\033[1m" + "Enter owner's first name: " + "\033[0m")
                ownerLast = input("\033[1m" + "Enter owner's last name: " + "\033[0m")
                ownerPhone = input("\033[1m" + "Enter owner's phone number: " + "\033[0m")
                ownerEmail = input("\033[1m" + "Enter owner's email address: " + "\033[0m")
                petName = input("\033[1m" + "Enter cat's name: " + "\033[0m")
                petWeight = float(input("\033[1m" + "Enter cat's weight in pounds: " + "\033[0m"))
                petAge = int(input("\033[1m" + "Enter cat's age in years: " + "\033[0m"))
                catBreed = input("\033[1m" + "Enter cat's breed: " + "\033[0m")

                # Create new cat object using user input and add to petBAG_dict using crud class method
                newCat = cat(ownerFirst, ownerLast, ownerPhone, ownerEmail, petName, petWeight, petAge, catBreed)
                if ownerPhone in petBAG_dict.pet_dict:
                    create_existingCat(newCat)
                else:
                    create_newCat(newCat)

                save_petBAG_dict(petBAG_dict.pet_dict)

                time.sleep(1.0)
                clearScreen()
                pageHeader()
                petBAGMenuPets()

            # Handle viewing single pet           
            elif petMenuOption == 3:
                
                clearScreen()
                pageHeader()

                ownerPhone = input("\033[1m" + "Enter owner's phone number: " + "\033[0m")
                petName = input("\033[1m" + "Enter pet's name: " + "\033[0m").lower()

                read_singlePet(ownerPhone, petName)

                input("\033[36m" + "Press Enter to return to pet menu..." + "\033[0m")
                clearScreen()
                pageHeader()
                petBAGMenuPets()

            # Handle viewing all pets         
            elif petMenuOption == 4:
                
                clearScreen()
                pageHeader()
                read_allPets()

                input("\033[36m" + "Press Enter to return to pet menu..." + "\033[0m")
                clearScreen()
                pageHeader()
                petBAGMenuPets()

            # Handle updating pet information           
            elif petMenuOption == 5:
                
                petMenuOption = petBAGMenuUpdatePetInfo()
                
                if petMenuOption == 0:
                    clearScreen()
                    pageHeader()
                    petBAGMenuPets()

                # Handle updating pet weight
                elif petMenuOption == 1:
                    
                    ownerPhone = input("\033[1m" + "Enter owner's phone number: " + "\033[0m")
                    petName = input("\033[1m" + "Enter pet's name: " + "\033[0m").lower()
                    newWeight = float(input("\033[1m" + "Enter pet's new weight in pounds: " + "\033[0m"))

                    update_petWeight(ownerPhone, petName, newWeight)

                    save_petBAG_dict(petBAG_dict.pet_dict)
                    
                    input("\033[36m" + "Press Enter to return to pet menu..." + "\033[0m")
                    clearScreen()
                    pageHeader()
                    petBAGMenuPets()

                # Handle updating pet age
                elif petMenuOption == 2:
                    
                    ownerPhone = input("\033[1m" + "Enter owner's phone number: " + "\033[0m")
                    petName = input("\033[1m" + "Enter pet's name: " + "\033[0m").lower()
                    newAge = int(input("\033[1m" + "Enter pet's new age in years: " + "\033[0m"))

                    update_petAge(ownerPhone, petName, newAge)

                    save_petBAG_dict(petBAG_dict.pet_dict)

                    
                    input("\033[36m" + "Press Enter to return to pet menu..." + "\033[0m")
                    clearScreen()
                    pageHeader()
                    petBAGMenuPets()
                    
                # Handle updating pet status
                elif petMenuOption == 3:
                    
                    ownerPhone = input("\033[1m" + "Enter owner's phone number: " + "\033[0m")
                    petName = input("\033[1m" + "Enter pet's name: " + "\033[0m").lower()
                    newStatus = input("\033[1m" + "Enter pet's new status (active/inactive): " + "\033[0m").lower()

                    update_petStatus(ownerPhone, petName, newStatus)

                    save_petBAG_dict(petBAG_dict.pet_dict)

                    input("\033[36m" + "Press Enter to return to pet menu..." + "\033[0m")
                    clearScreen()
                    pageHeader()
                    petBAGMenuPets()

                # Handle invalid update pet information menu option selection
                else:
                    print("\033[31m" + "Invalid menu option. Please try again." + "\033[0m")
                    time.sleep(1.5)
                    clearScreen()
                    pageHeader()
                    petMenuOption = petBAGMenuUpdatePetInfo()

            # Handle deleting pet
            elif petMenuOption == 6:
                
                ownerPhone = input("\033[1m" + "Enter owner's phone number: " + "\033[0m")
                petName = input("\033[1m" + "Enter pet's name: " + "\033[0m").lower()

                delete_pet(ownerPhone, petName)

                save_petBAG_dict(petBAG_dict.pet_dict)

                input("\033[36m" + "Press Enter to return to pet menu..." + "\033[0m")
                clearScreen()
                pageHeader()
                petBAGMenuPets()

            # Handle invalid pet menu option selection
            else:
                
                print("\033[31m" + "Invalid menu option. Please try again." + "\033[0m")
                time.sleep(1.5)
                clearScreen()
                pageHeader()
                petMenuOption = petBAGMenuPets()

        # Display service management menu and get user selection      
        elif menuOption == 2:
            clearScreen()
            pageHeader()

            # Display service management menu
            serviceMenuOption = petBAGMenuServices()

            # Return to Main Menu
            if serviceMenuOption == 0:
                continue
            
            # Handle adding new service
            elif serviceMenuOption == 1:
                
                ownerPhone = input("\033[1m" + "Enter owner's phone number: " + "\033[0m")
                petName = input("\033[1m" + "Enter pet's name: " + "\033[0m").lower()
                services = []
                while True:
                    service = input("\033[1m" + "Enter a service to add then type 'done' to finish: " + "\033[0m").lower()
                    if service.lower() == 'done':
                        break
                    services.append(service)

                create_newService(ownerPhone, petName, services)

                save_petBAG_dict(petBAG_dict.pet_dict)

                input("\033[36m" + "Press Enter to return to services menu..." + "\033[0m")
                clearScreen()
                pageHeader()
                petBAGMenuServices()
            
            # Handle viewing current service
            elif serviceMenuOption == 2:
                
                ownerPhone = input("\033[1m" + "Enter owner's phone number: " + "\033[0m")
                petName = input("\033[1m" + "Enter pet's name: " + "\033[0m").lower()

                read_currentService(ownerPhone, petName)
                
                input("\033[36m" + "Press Enter to return to services menu..." + "\033[0m")
                clearScreen()
                pageHeader()
                petBAGMenuServices()
            
            # Handle deleting service
            elif serviceMenuOption == 3:
                
                ownerPhone = input("\033[1m" + "Enter owner's phone number: " + "\033[0m")
                petName = input("\033[1m" + "Enter pet's name: " + "\033[0m").lower()

                delete_service(ownerPhone, petName)

                save_petBAG_dict(petBAG_dict.pet_dict)

                input("\033[36m" + "Press Enter to return to services menu..." + "\033[0m")
                clearScreen()
                pageHeader()
                petBAGMenuServices()

            # Handle invalid services menu option selection
            else:
                print("\033[31m" + "Invalid menu option. Please try again." + "\033[0m")
                time.sleep(1.5)
                clearScreen()
                pageHeader()
                serviceMenuOption = petBAGMenuServices()
        
        # Display client management menu and get user selection
        elif menuOption == 3:
            clearScreen()
            pageHeader()

            # Display client management menu
            clientMenuOption = petBAGMenuClients()
            
            # Return to Main Menu
            if clientMenuOption == 0:
                continue
            
            # Handle viewing single client
            elif clientMenuOption == 1:
                
                ownerPhone = str(input("\033[1m" + "Enter owner's phone number: " + "\033[0m"))
                read_singleClient(ownerPhone)

                input("\033[36m" + "Press Enter to return to client menu..." + "\033[0m")
                clearScreen()
                pageHeader()
                petBAGMenuClients()
            
            # Handle viewing all clients
            elif clientMenuOption == 2:
                
                read_allClients()

                input("\033[36m" + "Press Enter to return to client menu..." + "\033[0m")
                clearScreen()
                pageHeader()
                clientMenuOption = petBAGMenuClients()
            
            # Handle updating client information
            elif clientMenuOption == 3:
                
                clientMenuOption = petBAGMenuUpdateClientInfo()
                
                # Return to Client Menu
                if clientMenuOption == 0:
                    clearScreen()
                    pageHeader()
                    clientMenuOption = petBAGMenuClients()

                # Handle updating owner first name
                elif clientMenuOption == 1: 
                    
                    ownerPhone = input("\033[1m" + "Enter owner's phone number: " + "\033[0m")
                    newFirstName = input("\033[1m" + "Enter owner's new first name: " + "\033[0m").lower()

                    update_ownerFirstName(ownerPhone, newFirstName)

                    save_petBAG_dict(petBAG_dict.pet_dict)

                    input("\033[36m" + "Press Enter to return to client menu..." + "\033[0m")
                    clearScreen()
                    pageHeader()
                    clientMenuOption = petBAGMenuClients()

                # Handle updating owner last name
                elif clientMenuOption == 2:
                    
                    ownerPhone = input("\033[1m" + "Enter owner's phone number: " + "\033[0m")
                    newLastName = input("\033[1m" + "Enter owner's new last name: " + "\033[0m").lower()

                    update_ownerLastName(ownerPhone, newLastName)

                    save_petBAG_dict(petBAG_dict.pet_dict)
                    
                    input("\033[36m" + "Press Enter to return to client menu..." + "\033[0m")
                    clearScreen()
                    pageHeader()
                    clientMenuOption = petBAGMenuClients()

                # Handle updating owner phone number
                elif clientMenuOption == 3:
                    
                    ownerPhone = input("\033[1m" + "Enter owner's current phone number: " + "\033[0m")
                    newPhone = input("\033[1m" + "Enter owner's new phone number: " + "\033[0m")

                    update_ownerPhone(ownerPhone, newPhone)

                    save_petBAG_dict(petBAG_dict.pet_dict)
                    
                    input("\033[36m" + "Press Enter to return to client menu..." + "\033[0m")
                    clearScreen()
                    pageHeader()
                    clientMenuOption = petBAGMenuClients()

                # Handle updating owner email address
                elif clientMenuOption == 4:
                    
                    ownerPhone = input("\033[1m" + "Enter owner's phone number: " + "\033[0m")
                    newEmail = input("\033[1m" + "Enter owner's new email address: " + "\033[0m").lower()

                    update_ownerEmail(ownerPhone, newEmail)

                    save_petBAG_dict(petBAG_dict.pet_dict)
                    
                    input("\033[36m" + "Press Enter to return to client menu..." + "\033[0m")
                    clearScreen()
                    pageHeader()
                    clientMenuOption = petBAGMenuClients()

            # Handle deleting client
            elif clientMenuOption == 4:
                
                ownerPhone = input("\033[1m" + "Enter owner's phone number: " + "\033[0m")
                delete_owner(ownerPhone)

                save_petBAG_dict(petBAG_dict.pet_dict)
                    
                input("\033[36m" + "Press Enter to return to client menu..." + "\033[0m")
                clearScreen()
                pageHeader()
                clientMenuOption = petBAGMenuClients()

            # Handle invalid menu option selection
            else:
                print("\033[31m" + "Invalid menu option. Please try again." + "\033[0m")
                time.sleep(1.5)
                clearScreen()
                pageHeader()
                clientMenuOption = petBAGMenuClients()
        
        # Handle invalid main menu option selection
        else:
            print("\033[31m" + "Invalid menu option. Please try again." + "\033[0m")
            time.sleep(1.5)
            clearScreen()
            continue


if __name__ == "__main__":
    main()








