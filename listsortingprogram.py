import math

list = []

print("Welcome to the list sorting program!")

optionchoice = "0"

while optionchoice != "6":
    print("Please enter an option and choose what you'd like to do!")
    print("Would you like to...")
    print("   1) Add something to the list")
    print("   2) Remove something from the list")
    print("   3) Sort the list in ascending order")
    print("   4) Empty the list")
    print("   5) Find an item in the list") 
    print("   6) Quit out of the list sorting program")
    print()
    print("Current List: ")
    print(list)
    print()
    optionchoice = input("So, what would you like to do? ")
    print()
    print("----------------------------------------------------------------------------------------------")

    if optionchoice == "1":
        userinput = str(input("Alright! Please enter what you would like to add to the list: "))
        if userinput in list:
            print("Hey! Maybe add something thats not already in the list!")
        else:
            list.append(userinput)
            print("Got it! Your item has been added to the list.")
        print()

    elif optionchoice == "2":
        userinput = str(input("Enter the element that you want to remove, EXACTLY as it appears: "))
        if userinput in list:
            list.remove(userinput)
        else:
            print("Hey, that's not in the list!")
        print()

    elif optionchoice == "3":
        list.sort()
        print("List has been sorted!")

    elif optionchoice == "4":
        list = []
        print("The list is now empty!")
        print()
        
    elif optionchoice == "5":
        list.sort()
        if len(list) == 0:
            print("Nice try, but there's nothing in the list!")
        else:

            userinput = str(input("What would you like to search for in the list? "))
            
            currindex = int(round(len(list)/2,0)) # rounds a float value up, turns into an int
            stepsize = currindex
            for i in range (0,int( round( math.log( len( list ), 2 ),0 ) ) + 1):#range of 0 until the rounded up integer of the current list length, at log base 2, then add 1
                if userinput == list[currindex]:
                    break
                stepsize /= 2
                if userinput > list[currindex]:
                    currindex -= stepsize
                else:
                    currindex += stepsize
            print("Your search was found!")
            print("The item \"" + userinput + "\" was located at index " + str(currindex))

    elif optionchoice == "6":
        break

    else:
        print("Please pick a proper option!")

    print("----------------------------------------------------------------------------------------------")
    
print("The list is done")
print(list)
print()
print("Thank you for using the list sorting program.")