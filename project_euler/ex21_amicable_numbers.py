"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from collections import Counter
from itertools import count


def get_sum_of_divs(number):
    return sum(d for d in range(1, number) if number % d == 0)


def get_list_of_sums(number):
    list_ = []
    for n in range(number):
        r = get_sum_of_divs(n)
        if r > 1:
            list_.append(r)
    return list_


def main(number):
    values = get_list_of_sums(number)
    c_values = Counter(values)
    c_occurence = count(1)
    for k, v in c_values.items():
        if v > 1:
            next(c_occurence)
    return c_occurence


res = main(10000)
print(res)