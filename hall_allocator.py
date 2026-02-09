
#This is the main function for assigning student to their respective halls
def hall_allocator():
    
    #The global here is to allow us to call the name variable outside the function
    global name

    #The inputs functions are used here to allow the user to type his own name , making the code more interactive
    name = input("What is your name Mortal ?: ")
    course = input("Input your course Mortal: ")
    age = int(input("How long have you been on this earth Mortal: "))

    #Float used here cus the individual's points might  be decimal digit
    points = float(input(" Tell me your total credit points: "))
	
	
	#These are the conditions for assigning the students to their respective halls
	if course.lower() == "engineering" and age >= 25 and points >= 85:
		return "Assigned to KATANGA HALL"
		
		elif course.lower() == "Science" and points >=70:
		return "Assigned to UNITY HALL"
		
		elif course.lower() == "Arts" and age <= 19 :
		return "Assigned to INDEPENDENCE  HAll"
		
		else :
			return "Assigned to QUEENS HALL"
			
			#Now we create a variable that calls our 'hall_allocator' function and uses it 
			Assigned = hall_allocator()
			
			# we now print out 
			print("Name: " ,name)
			print("Assigned to : " ,Assigned)