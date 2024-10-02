'''TASK 1
Review the following codes,find and fix errors and explain the error.'''

#CODE SNIPPET 1: Variable Name Typo

#ERROR
number_of_apples = 5
print(number_of_apple)

#CORRECT CODE
number_of_apples = 5
print(number_of_apples)

#output:5

#explanation of error

'''
defined a variable named number_of_apples and assigned it the value 5.
When you print(number_of_apple), Python is looking for a variable named number_of_apple, which does not exist.
It would show something be like NameError: name 'number_of_apple' is not defined.
'''


#CODE SNIPPET 2: Acessing List Elements Out of Range

#ERROR
fruits = ["apple","banana","cherry"]
print(fruits[3])

#CORRECT CODE
fruits = ["apple","banana","cherry"]
print(fruits[2])

#output:cherry

#explanation of error
'''
In Python, list indices start at 0. So, for the list fruits, the indices are:
fruits[0] → "apple"
fruits[1] → "banana"
fruits[2] → "cherry"

It would show something be like IndexError: list index out of range.
'''


#CODE SNIPPET 3:Function Not Behaving as Expected

#ERROR
def find_average(numbers):
    sum = 0
    for number in numbers:
        sum += number
    average = sum / len(numbers)
    return average

numbers = [1,2,3,4,5,"6"]
average = find_average(numbers)
print(f"the average is: {average}")

#CORRECT CODE
def find_average(numbers):
    sum = 0
    for number in numbers:
        sum += number
    average = sum / len(numbers)
    return average

# Convert the string "6" to an integer
numbers = [1, 2, 3, 4, 5, int("6")]
average = find_average(numbers)
print(f"The average is: {average}")

#output: average is 3.5

#explanation of error
'''
TypeError: unsupported operand type(s) for +=: 'int' and 'str'

It would show something be like TypeError.
'''


#CODE SNIPPET 4:Incorrect Dictionary Usage

#ERROR
def update_record(records, name, score):
    if name in records:
        records[name].append(score)
    else:
        records[name] = [score]

student_records = {"Alice": [88, 92], "Bob": [70, 85]}
update_record(student_records, "Charlie", 91)
update_record(student_records, "Alice", 95)

print(student_records)

#CORRECT CODE

def update_record(records, name, score):
    if name in records:
        records[name].append(score)
    else:
        records[name] = [score]
        
student_records = {"Alice": [88, 92], "Bob": [70, 85]}
update_record(student_records, "Charlie", 91)
update_record(student_records, "Alice", 95)

print(student_records)

#output:{'Alice': [88, 92, 95], 'Bob': [70, 85], 'Charlie': [91]}


#explanation of error

'''It does not show any error and showing output without showing any error.'''

