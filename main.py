
def reverse_string(input_string):
    return input_string[::-1]



def count_words(input_string):
    words = input_string.split()
    return len(words)


def sort_list(input_list):
    sorted_list = sorted(input_list)
    return sorted_list

def is_palindrome(input_string):
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())
    return cleaned_string == cleaned_string[::-1]


def func(n):
    if n == 0:
        return 1
    else:
        return n * func(n-1)


def generator(n):
    primes = []
    for num in range(2, n+1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

