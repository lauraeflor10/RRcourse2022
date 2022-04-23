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
