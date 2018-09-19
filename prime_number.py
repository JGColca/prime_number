number = int(input('Please enter a number: '))

def is_prime(number):
    if number < 2:
        return f'{number} is not a prime number'
    else:
        for index in range(2, number-1):
            if number % index == 0:
                return f'{number} is not a prime number'
        return f'{number} is a prime number'


print(is_prime(number))
