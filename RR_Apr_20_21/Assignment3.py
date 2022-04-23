## Exercise 1

"""Consider a [FizzBuzz problem](https://codegolf.stackexchange.com/questions/58615/1-2-fizz-4-buzz).
The program should write numbers from 1 to 100, separated by a newline,
but multiples of 3 and of 5 should be replaced with "Fizz" and "Buzz" respectively.
For numbers which are multiples of both 3 and 5 print "FizzBuzz". Here are some solutions, which are not readable:

Python: `for i in range(100):print(int(i%3/2)*'Fizz'+int(i%5/4)*'Buzz'or-~i)`
R: `x=y=1:100;y[3*x]='Fizz';y[5*x]='Buzz';y[15*x]='FizzBuzz';write(y[x],1)`

Write a readable and working solution in your preferred language.
"""

for fizzbuzz in range(101):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)

## Exercise 2

"""
1. Write a function which takes *n* (float or integer) as a parameter and returns the largest Fibonacci number smaller than *n*. 
The function should be documented, with type hints, and appropriate comments.
2. Write a function which reverses digits in an integer number (for example 7245 -> 5427). 
The function should be documented, with type hints, and appropriate comments.
"""

## Exercise 2 - 1
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


N = 45  # random number
result = []
smallest = 1
for i in range(1, N + 1):
    term = fibonacci(i)
    if term < N:
        result.append(fibonacci(i))
    else:
        smallest = term
        break

print(*result)
print('smallest value greater than N:', smallest)

## Exercise 2 - 2

digit = 85723
reversed_digit = 0

while digit != 0:
    digitrev = digit % 10
    reversed_digit = reversed_digit * 10 + digitrev
    digit //= 10

print("Reversed Number: " + str(reversed_digit))

## Exercise 3

"""Write names of all US states in UPPERCASE and lowercase to a file. 
Write how to do this without typing all 50 names manually. Separate code from input and from output.
"""
# Exercise 3 - Uppercase
import pandas as pd

df = pd.read_excel(r'C:\Users\Laura Eflor\OneDrive\Documents\GitHub\RRcourse2022\RR_Apr_20_21\USState.xlsx')
df['State'] = df['State'].str.upper()

print(df)

# Exercise 3 - lowercase
import pandas as pd

df = pd.read_excel(r'C:\Users\Laura Eflor\OneDrive\Documents\GitHub\RRcourse2022\RR_Apr_20_21\USState.xlsx')
df['State'] = df['State'].str.lower()

print(df)

## Exercise 4

"""
The code below is of poor quality. Improve it (you may rewrite it to R, if you find it more convenient). 
[Data (StudentsPerfomance.csv) is available on Kaggle.](https://www.kaggle.com/spscientist/students-performance-in-exams)
"""

import pandas as pd
import matplotlib.pyplot as plt

# read the file with data
studPerformance = pd.read_csv(r'C:\Users\Laura Eflor\OneDrive\Documents\GitHub\RRcourse2022\RR_Apr_20_21\StudentsPerformance.csv')

# the dataframe contains data about 5 groups
stud_a = studPerformance.loc[studPerformance['race/ethnicity'] == 'group A']
stud_b = studPerformance.loc[studPerformance['race/ethnicity'] == 'group B']
stud_c = studPerformance.loc[studPerformance['race/ethnicity'] == 'group C']
stud_d = studPerformance.loc[studPerformance['race/ethnicity'] == 'group D']
stud_e = studPerformance.loc[studPerformance['race/ethnicity'] == 'group E']

# print mean math score for each group
groupa = stud_a['math score'].mean()
print(groupa)
groupb = stud_b['math score'].mean()
print(groupb)
groupc = stud_c['math score'].mean()
print(groupc)
groupd = stud_d['math score'].mean()
print(groupd)
groupe = stud_e['math score'].mean()
print(groupe)

# print mean math, reading, and writing scores for students who completed the test preparation course
# and their parent obtained a degree
degree_test = studPerformance.loc[(studPerformance['test preparation course'] == 'completed') &
                                  (studPerformance['parental level of education'].isin(["associate's degree", "bachelor's degree", "master's degree"]))]
print('math', degree_test['math score'].mean())
print('reading', degree_test['reading score'].mean())
print('writing', degree_test['writing score'].mean())

# plot the histogram of math scores divided by reading scores for each student
plt.hist(studPerformance['math score'] / studPerformance['reading score'])
plt.title('ratio')
plt.show()
plt.close()