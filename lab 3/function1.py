# 1. A recipe you are reading states how many grams you need for the ingredient.
# Unfortunately, your store only sells items in ounces. Create a function to convert grams to ounces. ounces = 28.3495231 * grams
def grams_to_ounces(grams):
    return 28.3495231 * grams
grams = int(input())
print(grams_to_ounces(grams))

# 2. Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. 
# The following formula is used for the conversion: C = (5 / 9) * (F – 32)
def fahrenheit_to_centigrade(fahrenheit):
    return (5/9)*(fahrenheit-32)
fahrenheit = int(input())
print(fahrenheit_to_centigrade(fahrenheit))

# 3. Write a program to solve a classic puzzle:
# We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):
def solve(numheads,numlegs):
    rabbits = 0.5 * numlegs - numheads
    chickens = 2 * numheads - 0.5 * numlegs
    return(rabbits,chickens)
numheads = int(input())
numlegs = int(input())
print(solve(numheads,numlegs))

# 4. You are given list of numbers separated by spaces.
# Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.
from math import sqrt
def is_prime(nums):
    primes = []
    isPrime = True
    for num in nums:
        for i in range(2, int(sqrt(num))):
            if num % i == 0:
                isPrime = False
                break
        if isPrime is True:
            primes.append(num)
        isPrime = True
    return primes
nums = list(map(int, input().split()))
print(is_prime(nums))

# 5. Write a function that accepts string from user and print all permutations of that string.
from itertools import permutations
def find_permutations(s):
    char_list = [s[i] for i in range(0, len(s))]
    char_list.sort()
    prms = permutations(char_list)
    for permutation in prms:
        print(permutation)
find_permutations("abc")

# 6.Write a function that accepts string from user, return a sentence with the words reversed.
# We are ready -> ready are We
def reverse_words(s):
    s = s.split()
    s.reverse()
    return ' '.join(s)
s = input()
print(reverse_words(s))

# 7. Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(nums):
    isTrue = False
    for i in range(1, len(nums)):
        num = nums[i] * 10 + nums[i-1]
        if num == 33:
            isTrue = True
            break
    return isTrue
nums = list(map(int, input().split()))
print(has_33(nums))

# 8. Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(nums):
    is007 = False
    for i in range(2, len(nums)):
        agent = nums[i-2] * 100 + nums[i-1] * 10 + nums[i]
        if agent == 7:
            is007 = True
            break
    return is007
nums = list(map(int, input().split()))
print(spy_game(nums))

# 9. Write a function that computes the volume of a sphere given its radius.
def volume(radius):
    from math import pi
    return 4/3 * pi * radius**3
radius = int(input())
print(volume(radius))

# 10. Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.
def uniques(elements):
    uniques = dict(())
    for i in elements:
        if(i not in uniques.keys()):
            uniques[i] = 0
    return uniques.keys()
elements = list(map(int, input().split()))
print(uniques(elements))

# 11. Write a Python function that checks whether a word or phrase is palindrome or not. 
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam
def is_palindrome(s):
    char_list = [s[i] for i in range(len(s))]
    char_list.reverse()
    s1 = ''.join(char_list)
    return s == s1
s = str(input())
print(is_palindrome(s))

# 12. Define a function histogram() that takes a list of integers and prints a histogram to the screen. 
# For example, histogram([4, 9, 7]) should print the following:
def histogram(values):
    char = '*'
    for i in values:
        if i != 0:
            char = char * i
        else:
            char = ''
        print(char)
        char = '*'
histogram([4, 9, 7])

# 13. Write a program able to play the "Guess the number" 
import random
print("Hello! What is your name?")
name = str(input())
print("Well,", name,", I am thinking of a number between 1 and 20.")
guessed_num = random.randint(1, 20)
guess = 0
num_guesses = 0
while guess != guessed_num:
    print("Take a guess")
    guess = int(input())
    num_guesses += 1
    if guess < guessed_num:
        print('Your guess is too low.')
    elif guess > guessed_num:
        print('Your guess is too high')
    else:
        print(f"Good job, {name}! You guessed my number in {num_guesses} guesses!")
        break


