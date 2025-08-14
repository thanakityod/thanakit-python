
"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""

# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("borbank",20, "bangkok", "thailand")  # name, age, city, country
    hobbies = []
    
    
    # Your code here
    while True:

    print("1 Display into , 2 Add hobby , 3 Remove hobby , 4 Edit age , 5 Exit")
    choice = input("what do you want to do? : ")

    if choice == "1":
        print("Name : ",person[0])
        print("Age : ",person[1])
        print("City : ",person[2])
        print("Country : ",person[3])
        print("Hobbies : ",person[4])

    elif choice =="2":
        hobby = input("Insert new hobby : ")
        hobbies.append(hobby)

    elif choice =="3":
        del hobbies[0]

    elif choice =="4":
        age = int(input("Insert new age"))
        person_list = list(person)
        person_list[1] = age
        person = turple(person_list)
    
    elif choice =="5":
        break 

if __name__ == "__main__":
    personal_info_manager()

