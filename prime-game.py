import math

# def sieve_of_eratosthenes(n):
#     # Create a boolean array "prime[0..n]" and initialize all entries as True
#     # A value in prime[i] will finally be False if i is Not a prime, else True
#     prime = [True for i in range(n+1)]
#     p = 2
#     while (p * p <= n):
#         # If prime[p] is not changed, then it is a prime
#         if (prime[p] == True):
#             # Update all multiples of p
#             for i in range(p * p, n+1, p):
#                 prime[i] = False
#         p += 1
#     # Return all prime numbers
#     return [p for p in range(2, n) if prime[p]]


# def is_prime(n):
#     if n < 2:
#         return False
#     if n == 2 or n == 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True

def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    p = 2
    while p * p <= limit:
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1
    return [i for i in range(2, limit + 1) if primes[i]]

primes_up_to_10000 = sieve_of_eratosthenes(10000)

def isWinner(x, nums):
    pickers = {
        "Ben": 0,
        "Maria": 0
    }
    winner = None
    nround = 0
    if len(nums) == 0:
        pickers['Ben'] += 1
    while x > nround:
        next_picker = 'Ben'
        current_num = nums[nround]
        game_board = [i for i in range(1, current_num + 1)]
        picks = 1
        if len(game_board) == 0:
            pickers[next_picker] += 1
        while game_board:
            all_primes = sieve_of_eratosthenes(current_num)
			# [num for num in game_board if num in primes_up_to_10000]
            if not all_primes:
                pickers[next_picker] += 1
                break
            current_prime = all_primes[0]
            game_board = [num for num in game_board if num % current_prime != 0]
            next_picker = 'Ben' if picks % 2 == 0 else 'Maria'
            picks += 1
        nround += 1

    for key, val in pickers.items():
        if list(pickers.values())[0] == list(pickers.values())[1]:
            return None
        if val == max(list(pickers.values())):
            winner = key
            return key

# Test the function


# def isWinner(x, nums):
#     pickers = {
#         "Ben": 0,
#         "Maria": 0
#     }
#     winner = None
#     nround = 0
#     if len(nums) == 0:
#         pickers['Ben'] += 1
#     while x > nround:
#         next_picker = 'Ben'
#         current_num = nums[nround]
#         game_board = [i for i in range(1, current_num + 1)]
#         idx = len(game_board)
#         picks = 1
#         if len(game_board) == 0:
#             pickers[next_picker] += 1
#         while idx >= picks:
#             all_primes = [num for num in game_board if is_prime(num)]
#             if len(all_primes) == 0:
#                 pickers[next_picker] += 1
#                 break
#             current_prime = all_primes[0]
#             ans = list(filter(lambda x: x % current_prime != 0, game_board))
#             game_board = ans
#             if picks % 2 == 0:
#                 next_picker = 'Ben'
#             else:
#                 next_picker = 'Maria'
#             picks += 1
#         nround += 1

#     for key,val in pickers.items():
#         if list(pickers.values())[0] == list(pickers.values())[1]:
#             return None
#         if val == max(list(pickers.values())):
#             winner = key
#             return key

# print("-------")
# print("(10000, nums)")

# nums = [0] * 10000
# for i in range(10000):
#     nums[i] = i

# import time

# start_time = time.time()

# print("Winner: {}".format(isWinner(10000, nums)))



print("-------")
print("(10000, nums)")


nums = [0] * 10000
for i in range(10000):
    nums[i] = i

import time

start_time = time.time()

# print("Winner: {}".format(isWinner(10, nums)))

end_time = time.time()

print("Time taken: {} seconds".format(end_time - start_time))
print("-------")

import random

# random_numbers = [random.randint(1, 1000) for _ in range(100000)]

# board = [i for i in range(10000)]
# print('{} wins'.format(isWinner(10000, random_numbers)))

def isPrime(num):
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if  num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

for i in range(20):
	print('{} is {}'.format(i, isPrime(i)))
