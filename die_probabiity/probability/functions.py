from math import factorial as fact
from decimal import Decimal


def get_prob_div(n):
    """
    This functions computes the probability of rolling a n-sided die n times
    and getting all n numbers. It does it by dividing the possible
    permutations (without replacement) of all n numbers: n! over all the
    possible outcomes of the n die rolls: n ** n.
    To optimize a bit, both the numerator and the divisor are divided by n,
    therefore the final expression is: (n-1)!/(n ** (n-1))
    """
    return Decimal(fact(n-1)) / Decimal(n ** (n-1))


def get_prob_it(n):
    """
    This functions computes the probabilityfuby calculating the possibility of
    obtaining one of the n numbers on each die roll given the previous rolls.
    In the first roll the probability of getting one of the numbers is 1, in
    the second one, I have a (n-1)/n of rolling one of the remaining numbers,
    an so on for the rest of the n numbers (The las roll will have a
    probability of 1/n of rolling the remainig number). So, the probability
    is: 1 * (n-1)/n * ... (n-i)/n * ... 2/n * 1/n. for i = 1...n
    To optimize a bit, the loop is going to stop at n-1 to get rid of the
    n/n=1 factor.
    """
    div = Decimal(n)
    num = Decimal(n)
    prob = Decimal(1)

    for i in range(1, n):
        num -= 1
        prob *= num/div

    return prob


def wrapper(func, *args, **kwargs):
    """
    This function wrapper will be used by the timeit module to measure
    the funtions's execution time
    """
    def wrapped():
        return func(*args, **kwargs)
    return wrapped
