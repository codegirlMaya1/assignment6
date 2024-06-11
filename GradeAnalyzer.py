#The aim of this assignment is to analyze a set of grades and provide statistics.
Grades=[60, 89, 75, 98]
Classmates=["Greg", "Sherry", "Melissa", "Peter"]
highest_grade=max(Grades)
lowest_grade=min(Grades)
highest_grade__index__=Grades.index(highest_grade)
lowest_grade__index__=Grades.index(lowest_grade)
letter_grade=["D", "B", "C", "A"]
combined_average=sum(Grades)
grader=4

#Task 1: Code a function to calculate the average grade.
print( "The total average grade amongst the four students =", combined_average / (grader))
#Task 2: Implement a function to find the highest and lowest grade.
print("Please show  the highest vs lowest grades:",highest_grade__index__, lowest_grade__index__)
print ("Who had the highest score:",Classmates[highest_grade__index__])
print ("Who had the lowest score:", Classmates[lowest_grade__index__])
#Task 3: Create a feature that categorizes grades into letter grades 
print ("What was Peter's letter grade?:",letter_grade[highest_grade__index__])
print ("What was Greg's letter grade?:", letter_grade[lowest_grade__index__])