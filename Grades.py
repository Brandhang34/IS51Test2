


"""
STRUCTURED ENGLISH

In this program, we will create a program that will show
the number grades, the average grade, and the percentage of 
grades that are above the average grade. Using the Final.txt
file, that will be utilized as a source of inputs in order to 
perform the following program.
"""

"""
Pseudo-code

Create a main function
    open Final.txt file in read mode and set it to a variable name "file"
    create a list named "grades"
    for loop i in file
        append the obtained number as an int and store into grades
    
    create a variable sum to sum the grades in the list
    create a varaible leng  and setting it to the length of the list
    create a variable avg to caclulate the average grade (sum / leng)

    print "Number of grades: " , the length of the grades list

    print "Average grade: " , the average of the grades list

    Call calculate_percent_above_average() function and pass the grades list the average and the list length

Create a calculate_percent_above_average function
    Create a list called "grades_above_avg_list"

    for loop i in grades list
        if(i is greater than avg)
            append i into grades_above_avg list

    Create a variable grades_above_avg_sum and set it to sum of grades_above_avg list
    Create a variable grades_above_avg and set it the the average (grades_above_avg_sum / leng)

    print the grades_above_avg
"""

#Code

def main():
    file = open("Final.txt", "r")
    grades = []

    for i in file:
        grades.append(int(i))
    
    grades_sum = sum(grades)
    grades_leng = len(grades)
    grades_avg = (grades_sum/grades_leng)

    print("Number of grades:", grades_leng)
    print("Average grade:", grades_avg)

    calculate_percent_above_average(grades, grades_avg, grades_leng)

def calculate_percent_above_average(list, avg, leng):
    grades_above_avg_list = []

    for i in list:
        if(i > avg):
            grades_above_avg_list.append(i)
    
    grades_above_avg_leng = len(grades_above_avg_list)
    grades_above_avg = ((grades_above_avg_leng / leng) * 100)

    print("Percentage of grades above average:", round(grades_above_avg, 2) ,"%") 

main()