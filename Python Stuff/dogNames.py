'''
Name: Christina
Program Purpose:
    This program demonstrates how to manipulate a list, including:
    -- finding the number of items in the list
    -- sorting the list
    -- adding/removing items
    -- copying a list of items into another list
    -- changing the data in the list
'''

    ### define varibles ###
dogs = ["Sadie", "Molly", "Ella", "Milo", "Buddy", "Rocky", "AnnaBelle", "Gonzo",
        "Sweetie-Pie", "Diego", "Trash Compactor"]
dogs2 = []

    ### define functions ###
def main():
    global dogs, dogs2
    
    how_many = len(dogs)
    str_dogs = str(dogs)
    print("\nNumber of dogs in the list: " + str(how_many))
    print("\nOriginal list of dog names:\n" + str_dogs)

    dogs.reverse()
    print_dogs("\nList from last to first:")

    dogs.sort()
    print_dogs("\nAlphabetized list:")

    dogs.sort(reverse = True)
    print_dogs("\nList in reverse alphabetized order:")
    
    dogs.append("Ranger")
    print_dogs("\nAdd a dog to the end of a list:")

    doggy = dogs.pop(0)
    print_dogs("\nPop a dog off (remove) from the front of the list:")
    print(doggy + " was removed from the list (position 0)")

    another_dog = dogs.pop(3)
    print("\nNote: Position numbers in a list begin with 0, not with 1")
    print_dogs("Pop a dog off from position 3 (which is the 4th dog) in the list:" + str_dogs)
    print(another_dog + " was removed from the list (position 3)")

    dogs.remove('AnnaBelle')
    print_dogs("\n Remove a dog by name rather than position in the list:")

    dogs2 = dogs
    print_dogs("\nA list can be copied into another list by setting one equal to the other:")
    print(dogs2)

    print("\nUse a FOR loop to give each dog in the list the same last name:")
    for i in range(len(dogs)):
        dogs[i] = dogs[i] + " Creegan"
    print(dogs)

    pass

def print_dogs(text):
    print(text)
    print(dogs)
    
    ### run functions ###
main()
