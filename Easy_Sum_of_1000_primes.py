def sieve_of_eratosthenes(Upper_bound):
    primes_list = [i for i in range(2, Upper_bound)]
    i = 0
    while(i != len(primes_list) - 1):
        primes_list[:] = [val for val in primes_list if val %
                          primes_list[i] != 0 or val == primes_list[i]]
        i += 1
    # print(primes_list)
    for i in range(len(primes_list) - 1, -1, -1):
        if(is_palindrome(primes_list[i])):
            print(primes_list[i])
            return


def is_palindrome(val):
    return (str(val) == str(val)[::-1])

sieve_of_eratosthenes(1000)
