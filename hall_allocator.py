
#This is the main function for assigning student to their respective halls
def hall_allocator():
    
    #The global here is to allow us to call the name variable outside the function
    global name

    #The inputs functions are used here to allow the user to type his own name , making the code more interactive
    name = input("What is your name Mortal ?: ")
    course = input("Input your course Mortal: ")
    age = int(input("How long have you been on this earth Mortal: "))

