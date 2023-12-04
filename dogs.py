# Name: Mehria Faqirzai
# Prog Purpose: This program demonstrates how to manipulate a list, including:
# finding the number of items in the list, sorting the list, adding/removing items,
# copying a list of items into another list, and changing the data in the list.

# Example list of dog names
dogs = ["Sadie", "Molly", "Ella", "Gonzo", "Sweetie-Pie"]

def main():
    # Finding the number of dogs in the list
    num_dogs = len(dogs)
    print("\nNumber of dogs in the list: " + str(num_dogs))

    # Displaying the original list of dog names
    print("\nOriginal list of dog names:")
    print(dogs)

    # Reversing the list
    dogs.reverse()
    print("\nList from last to first:")
    print(dogs)

    # Sorting the list in alphabetical order
    dogs.sort()
    print("\nAlphabetized list:")
    print(dogs)

    # Sorting the list in reverse alphabetical order
    dogs.sort(reverse=True)
    print("\nList in reverse alphabetized order:")
    print(dogs)

    # Adding a dog to the end of the list
    dogs.append("Ranger")
    print("\nAdd a dog to the end of the list:")
    print(dogs)

    # Removing a dog from the front of the list
    removed_dog = dogs.pop(0)
    print("\nPop a dog off from the front of the list:")
    print(dogs)
    print(removed_dog + " was removed from the front of the list.")

    # Removing a dog from position 3 (which is the 4th dog in the list)
    another_dog = dogs.pop(3)
    print("\nPop a dog off from position 3:")
    print(dogs)
    print(another_dog + " was removed from position 3 of the list.")

    # Removing a dog by name rather than position in the list
    if 'Sweetie-Pie' in dogs:
        dogs.remove('Sweetie-Pie')
        print("\nRemove a dog by name rather than position in the list:")
        print(dogs)
    else:
        print("\n'Sweetie-Pie' not found in the list.")

    # Copying a list into another list
    dogs2 = dogs.copy()
    print("\nA list can be copied into another list by setting one equal to the other:")
    print(dogs)
    print(dogs2)

    # Using a FOR loop to modify each dog's name
    for i in range(len(dogs)):
        dogs[i] = dogs[i] + " Faqirzai"  # Change Stevens to YOUR last name
    print("\nUse a FOR loop to give each dog the same last name:")
    print(dogs)

if __name__ == "__main__":
    main()
