# mathspace_die_prob
Django project that calculates the probability of an n-sided die of rolling all n numbers if thrown n times

###Settings:
* Python 3.4.3
* Django 1.11.3

To solve the problem I made the following assumptions:
* All sides of the die are equally probable, therefore each side will have a probability of 1/n of being thrown
* A dice must have at least 2 sides (i.e a coin)
* The order of how I toss each of the numbers doesn't matters

### Solve strategy
As I have to roll all the numbers from 1 to n, the probability of tossing one of the numbers the first time is 1 (or n/n),  the second time the probability of tossing one of the remaining numbers will be (n-1)/n, the third time (n-2)/n and so on. So, in general, the probability of tossing all of the n numbers given that I toss the die n times is:

1 * (n-1)/n * (n-2)/n ... (n-i)/n ... 2/n * 1/n    for i=0...n

Another way of solving is by diving all the possible permutations of all the number from 1 to n (that would be n!) over all the possibilities of the n die rolls, as I roll the die n times and on each of one I have n different sides all the possible rolls will be n ^ n. Therefore the probability will be 
given by the expression:

n!/(n^n) 

Note: This expression can also be derived from the first one if we compute the numerators and divisors separately.
