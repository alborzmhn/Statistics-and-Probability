import random
import sympy
import math
import numpy

def monte_carlo(n, k):
    days_taken = 0
    for i in range(k):
        cards_own = []
        while True:
            new_card = random.randint(1, n)
            days_taken += 1
            if new_card not in cards_own : cards_own.append(new_card)
            if len(cards_own) >= n:
                break 
    average = days_taken / k
    return average


print(monte_carlo(10, 10))
print(monte_carlo(10, 100))
print(monte_carlo(10, 1000))

s = sympy.symbols('s')

def calculate_mgf(n):
    answer = []
    for i in range(1, n + 1):
        answer.append(pow(math.e, s) * (1 - (i - 1) / n) / (1 - (pow(math.e, s) * ((i - 1) / n))))
    return numpy.prod(answer)

mgf_X = calculate_mgf(10)

deriv = sympy.diff(mgf_X, s)
print(deriv.subs({s:0}))