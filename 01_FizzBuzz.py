# write a program that prints numbers from 1 to n, with a twist – for numbers divisible by 3, print 'Fizz';
# for numbers divisible by 5, print 'Buzz'; and for numbers divisible by both, print 'FizzBuzz'.

def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizzbuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizz_buzz(15)