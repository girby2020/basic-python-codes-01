'''
Coding Quiz: Check for Prime Numbers
Prime numbers are whole numbers that have only two factors: 1 and the number itself. The first few prime numbers are 2, 3, 5, 7.
For instance, 6 has four factors: 1, 2, 3, 6.
1 X 6 = 6,     2 X 3 = 6
So we know 6 is not a prime number.
In the following coding environment, write code to check if the numbers provided in the list check_prime are prime numbers.
'''
# my try 01
check_prime = [26, 39, 51, 53, 57, 79, 85]

for num in check_prime:
    

    n= num//2
    while n>1:
        if (num%n == 0) or (num % 2 == 0):
            print("{} is NOT a prime number, because {} is a factor".format(num,n))
            break
        else:
            n-=1
            continue
    else:
        print("{} IS a prime number".format(num))