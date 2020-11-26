import math

user_input = input("Please give a number: ")


def sieve(number):
    number_to_count_towards = int(number)
    array_of_primes = [1]
    array_of_multiples = []
    for i in range(2, math.ceil(math.sqrt(number_to_count_towards))):

        if i not in array_of_primes:
            if i not in array_of_multiples:

                for j in range(i + 1, number_to_count_towards):
                    if j not in array_of_multiples:
                        if j % i == 0:
                            array_of_multiples.append(j)
                array_of_primes.append(i)

    for i in range(1, number_to_count_towards):
        if i not in array_of_primes:
            if i not in array_of_multiples:
                array_of_primes.append(i)

    return array_of_primes


print(sieve(user_input))