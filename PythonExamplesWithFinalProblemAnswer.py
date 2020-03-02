from functools import wraps
import time
import os

def timeit(method):
	@wraps(method)
	def wrap(*args, **kwargs):
		os.system("cls")
		ts = time.time()
		result = method(*args, **kwargs)
		te =  time.time()
		print('function: {a} took {b:2.4f}s'.format(a=method.__name__.upper(), b=(te-ts)))
		return result
	return wrap

class Person:
	# test class
	def __init__(self, age: int, name: str, student: bool, major = None):
		self.age = age
		self.name = name
		self.studentTrue = student
		self.major = major
		return

	def __str__(self):
		print("Hi, I'm {name} and I'm {age} years old.".format(name=self.name, age=self.age))
		if self.studentTrue == True:
			return("I study {major} at UTS!".format(major=self.major))
		else:
			return("I'm not a student!".format(self.name))
		return

def conditionalEx(firstYear = True):
	# Conditional Examples
	if firstYear == True:
		print("I am a first year")
	else:
		print("I am not a first year")

	print("\n\tWorks the same as if elif else...\n")
	
	if firstYear == True:
		print("I am a first year")
	elif firstYear == False:
		print("I am not a first year")
	else:
		print("How did you get here??")
	return

def conditionalQuestions():
	# Question answers
	albert = Person(20, "Albert", True, "Data Engineering")
	jayden = Person(19, "Jayden", True, "Data Engineering")
	mature = Person(25, "Bob", True, "less than i work")
	not_student = Person(17, "Annabelle", False, "Gap year!!!")

	students = [albert, jayden, not_student, mature]
	for student in students:
		print('\n')
		if student.studentTrue is True:
			print("Student is True!")
			print(student)
		else:
			print("Student is False!")

		if student.age < 18:
			print("{name} is underage!".format(name=student.name))
		else:
			print("{name} is legal!".format(name=student.name))

		if student.studentTrue is True and student.age >= 25:
			print("{name} is a mature student!".format(name=student.name))
		else:
			print("{name} is immature!".format(name=student.name))
	return

def arrayEx():
	print("Arrays require two things, a type of each elem and a length!")
	print("If you're adding values later, you need a default placeholder val.")
	input()
	
	myArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	print(myArray)
	input()
	myOtherArray = list(range(1, 10))
	print(myOtherArray)
	input()
	
	myOtherOtherArray = list(range(0, 10, 2))
	if myArray == myOtherArray:
		print(True)

	print(myOtherOtherArray)
	print("Length: ", len(myOtherOtherArray))
	print("Sum: ", sum(myOtherOtherArray))
	print("Reverse: ", myOtherOtherArray.reverse())


	print("Strings are arrays too! Just for char's specifically")
	string = "Hello World"
	print(string)
	print('last elem: i = -1', string[-1])
	print('length: ', len(string))
	print("We can concatenate strings with more bits!")
	print("stringA + stringB prints stringAstringB")
	stringA = "Hello"
	stringB = "World"
	print("A", stringA)
	print("B", stringB)
	print(stringA, stringB)
	print(stringA + ' ' + stringB) # Python way
	print(stringA , ' ' , stringB) # more traditional way
	return

def usefulFuncs():
	print("Enter some input!!")
	var = input()
	print("The input: ", var)
	print("Length: ", len(var))
	a = 1
	string = "Hello"
	arr = [1,2,3]
	print('an int, ', a, ' a string, ', string, ' an array, ', arr)
	print("What are their lengths?")
	input() # program wait for any input to continue, useful for simple debugging
	try:
		print(len(a), len(string), len(arr))
	except TypeError:
		print("Ah ha! Int's dont have a length, not really")
		print(len(string), len(arr))

	# We already saw reverse, sum and len in arrayEx function above too!
	print("Enter some val's separated by single spaces")
	string_in = input()
	print("split a string by each space - creates an array!")
	print(string_in.split())
	return

@timeit # will clear screen and print time of funciton to run, fairly accurate.
def loops():
	print('\n', "*"*81)
	print("\tHuge area of CS if you ever study this you'll be a 10X programmer.")
	print("*"*81,'\n')

	arr = list(range(0, 100, 2)) # all even nums < 100
	print("\ntraditional in all langs, C style loops")
	for i in range(0, len(arr)):
		print(arr[i])
		if arr[i] == 34:
			break # stop at num == 34
			# how could we change this to stop at the 34th elem?
	print("\nShorthand for Python")
	# python shorthand
	for num in arr:
		print(num)
		if num == 34:
			break # stop at num == 34

	print("\nWhile loops can be made and often more elegant")
	i = 0
	s = 0
	while arr[i] != 34: # this is the Guard statement
		s = s + arr[i] # (advanced: the invariant), our sum to perform
		i = i + 1 # increment our counter
	return

def finalProject():
	"""Student Register
	Ask for the user to type a student’s first and last name, age, and degree
	Exit when there are 5 students, or early if the first name is ‘ZZZ’ (remember to use break keyword!)
	
	THEN
	Ask for a students first name, your array(s) for that name. If they exist, print their details, if they don’t return “User not found!” 
	Example output: “Albert Ferguson, 20. Major: Data Engineering”
	Note: You will need to store your data in an array(s). There are several ways to do this!
	"""

	# essentially making a simple class the long way!! Easy, let's do this!
	# The following is an answer that ignores some more advanced concepts, keywords, etc...
	names = ['', '', '', '', '']
	ages = [0, 0, 0, 0, 0]
	degrees = ['', '', '', '', '']
	QUIT_TERM = "ZZZ"
	MAX_STUDENTS = 5

	i = 0
	data_in = []
	while i < MAX_STUDENTS:
		print("Enter the full name, age and degree of the student to the register: ")
		data_in = input()
		if 'ZZZ' in data_in:
			break
		else:
			data_in = data_in.split()
			names[i] = data_in[0] + ' ' + data_in[1]
			ages[i] = int(data_in[2]) # cast is good habit, but not needed here
			degrees[i] = data_in[3]
		i = i + 1

	print("Enter a full name and I'll check the student register!")
	chck_name = input()
	while chck_name != QUIT_TERM:
		for i in range(len(names)):
			if chck_name == names[i]:
				print("Name: ", names[i])
				print("Age: ", ages[i])
				print("Degree: ", degrees[i])
				break
			elif i == len(names) - 1: # remember! Arrays are from 0 -> len()-1! Not 1 -> len()
				print("User not found!")
			else:
				continue
		chck_name = input()
	return