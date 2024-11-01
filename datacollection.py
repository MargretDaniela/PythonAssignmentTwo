#store multiple data
#LISTS
#use angle brackets[] must be of the same type like names, numbers,
# can be changed
students_names = ["Daniela", "Margret", "Aisha", "Imelda"]#strings
students_marks = [ 50, 56, 78, 45]#intergers
data = [ 'Daniela' , 49, 'Ntinda']#mixed types
#Access the whole list 
print(students_names, type(students_names))

#use indexing(Positive)
#accessing list items
print(students_names[0])#first student and indexing starts from 0 to the last.
print(students_names[1])#second student
print(students_names[2])#third student
print(students_names[3])#fourth/last student

#use indexing(negative)
#accessing list items
print(students_names[-4])#first student
print(students_names[-3])#second student
print(students_names[-2])#third student
print(students_names[-1])#fourth/last student
students_names.append('Michelle') #Adding new items in the list
print(students_names)

#Add at  particular position
students_names.insert(2,'Faith')
print(students_names)


