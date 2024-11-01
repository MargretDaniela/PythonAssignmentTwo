#FUNCTIONS
#are used to perform a particular task
#def functionName():
#parameters acta as the data /information passed in the functions like def functionName(radius):
#Argument()are the values given to the funtion like radius = 3cm
#Function call is functionName() and it should align with def functionName use the naming convention

#Create a function that returns the main components of the fuction
# def functionBasis():
#     print(f"The main components of the function are the function Name, arguments, function call ")
# functionBasis()

#Create  a function that returns you student name , student number and student age.
# def studentData():#local variable
#     studentName = 'Daniela'
#     studentNumber = '2024/DSC/0078/SS'
#     studentAge = 20

#     print(f"My name is {studentName} with a number of {studentNumber} and an age of {studentAge} years old")

# studentData()

#Global variables
# marks = 69
# print(marks)

#Parameters
#Create a function that returns your student name , reg number and age as parameters.
#you dont rewrite the variables like studentName = 'Daniela'
# def student_details(student_name, student_reg_no, student_age):
#     print(f"My name is {student_name} and {student_reg_no} with an age of {student_age} years")
# student_details('student_name', 'student_reg_no', 'student_age')#other approach when calling
#student_details('Margret', '204/ddd/67/hh', 28)# calling the function in the paramters we 
#put the arguments and details
 
#Return values
#return function is to return  aspecific variable (instead of print we can use return)
def myName():
    return "Daniela"
myName()
#view the output
name = myName()
print(name)
#other approach
def myNameParamter ():
    name = 'Margret'
    return name
myNameParamter()

def myAge ():
    age = 12
    return age
myAge()
print(f"name is {myNameParamter()} age {myAge()} ")

# #Approach two
# def myNameApproachTwo():
#     name = "Danie"
#     return name
# myNameApproachTwo()

#create a function that calcualtes area of the triangle the base and the height must be function parameters
def area_of_the_triangle(base, height):
    area = 1/2 * base *height
    print(f"The area the triangle of base {base} and height {height} is {area} square units ")
area_of_the_triangle(6,8)
#local variables no parameters
def area_of_the_triangle():
    base = 6
    height = 10
    area = 1/2 * base *height
    print(f"The area the triangle of base {base} and height {height} is {area} square units ")
area_of_the_triangle()
# using the input function
def area_of_the_triangle():
    base = int(input('Enter the base:'))
    height =  int(input('Enter the base:'))
    area = 1/2 * base *height
    print(f"The area the triangle of base {base} and height {height} is {area} square units ")
area_of_the_triangle()





    
