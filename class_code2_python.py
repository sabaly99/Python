class Class1():
	
	def __init__(self):
		print("Class1 created")
	
	
	def method1(self):
		print("method1 created")

	def method2(self):
		print("method2 created")


class Class2(Class1):
	
	def __init__(self):
		Class1.__init__(self)
		print("Class2 created")



instance = Class2()