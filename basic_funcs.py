def greetings():
#This function is meant to greet the user by first asking the mortal(user) to type in his name
    name = input("what is your name dear mortal: ")
    return f"Hello dear {name},Welcome to our new pyhton code"


def room_allocation():
#This Function takes the mortal's course,Age and qualification points and assign them a residence
    course = input("Input the course you offer mortal !: ")
    Age = input("Mortal , how many years have you been in this accursed world: ")
    qualification_point = float(input("Type here your Qualification Points: "))
    if course == "Engineering":
        print("YOU've been assigned to Katanga Hall ")
    elif course == "Social Science":
        print('''you've been assigned to Queen's Hall''')
    elif course == "Sciences":
        print("You've assigned to Independence Hall")
    else :
        print("You've been assigned to Continental Hall")

#This line simply calls the function and executes the code in the function
message = greetings()
print(message)

#This line simply calls the function and executes the code in the function
room = room_allocation()
print(room)


