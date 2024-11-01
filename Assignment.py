#assignment
#Print From patricia faith Phionah Anitah use slicing
#Add marsha At the 4th position 
#Update the name Phionah to Aladina
# Display the length of the student list
# Print all the student names using a for loop
# Calcuate the total marks for the student marks variable  
# Research about CRUD 
student_names = ['Sandra', 'Patricia', 'Faith', 'Phionah', 'Anitah', 'Michelle']

print(student_names[1:5])

student_names.insert(4, 'Marsha')
print(student_names)

student_names[3]= 'Phionah Aladinah'
print(student_names)

student_names = ['Sandra', 'Patricia', 'Faith', 'Phionah', 'Anitah', 'Michelle']
print(len(student_names))

student_names = ['Sandra', 'Patricia', 'Faith', 'Phionah', 'Anitah', 'Michelle']
for x in student_names:
    print (x)
    if x == 'Sandra':
          print(x) 
if x == "Patricia":
    print(x)
elif x == "Faith":
    print(x)
elif x == "Anitah":
    print(x)
else:
    print(x)

student_marks = [80, 56, 78, 90, 70, 67 ]
total_marks = sum(student_marks)
print(f"The total of the student Marks is {total_marks}")



