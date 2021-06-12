"""
Part 2: uses map, filter, reduce, lambda, list comprehensions, with various use cases
"""
import os
import re
import math
import random
import string
from functools import reduce, partial

letters = string.ascii_letters
upper_letters = string.ascii_uppercase
cache = {0: 0, 1: 1}


def generate_fibonacci(limit: int) -> dict:
    """
    Uses Memoization approach to generate Fibonacci numbers, with a given limit
    :param limit: the limit for fibonacci numbers
    """
    global cache

    def fib(num, cache):
        if num not in cache:
            cache[num] = fib(num - 1, cache) + fib(num - 2, cache)
        return cache[num]

    for i in range(limit):
        fib(i, cache)
    return cache


fib_numbers = generate_fibonacci(limit=10001)


def check_for_fibonacci(number: int) -> bool:
    """
    Checks whether a provided number is a valid Fibonacci number
    :param number: the number to be checked
    :return: bool value indicating the check result
    """
    if not isinstance(number, int):
        raise TypeError("Check the type of number given")
    return bool(list(filter(lambda x: x in fib_numbers.values(), [number])))


def list_comprehension(*, a: list, b: list, string_: str, array: list) -> tuple:
    """
    Performs the following:
    1) to add only even and odd numbers respectively from two lists
    2) to remove vowels from a string
    3) Sigmoid
    4) shifted string

    :param a: first list
    :param b: second list
    :param string_: the string given by used for processing
    :param array: 1D array for Sigmoid
    :return: tuple of all outputs
    """
    if not (isinstance(a, list) and isinstance(b, list) and isinstance(string_, str) and
            isinstance(array, list) and len(string_) > 0):
        raise ValueError(
            "\nYou should check what type of arguments you are passing for function `all_hail_list_comprehension`")

    # to add only even and odd numbers respectively from two lists
    first = [x + y for x, y in zip(a, b) if x % 2 == 0 and y % 2 != 0]

    # strip down every vowel from the given string 🤫
    vowel_nazi = re.sub(r'[aeiou]', '', string_, flags=re.IGNORECASE)

    sigmoid = list(map(lambda x: 1 / (1 + math.exp(-1 * x)), array))

    # converts string to lower case, 97 is the ASCII value for `a`, `ord` returns the ASCII value ✌🏻
    shifted_string = ' '.join(
        map(lambda char_list: ''.join(chr((ord(x) - 97 + 5) % 26 + 97) if x in letters else x for x in char_list),
            string_.lower().split()))

    return first, vowel_nazi, sigmoid, shifted_string


def check_for_profanity(text: str) -> bool:
    """
    Check for the profanity for user text against a well curated list of swear words.
    """
    if not os.path.isfile("profanity.txt"):
        raise FileNotFoundError("`profanity.txt` not found")
    if not (text and isinstance(text, str) and len(text.strip().split()) >= 200):
        raise ValueError("Make sure you provide text as string"
                                  " and/or"
                                  " the provided text contains at least 200 words")
    with open("profanity.txt", 'r') as f:
        profane_words = set([x.strip() for x in f.readlines()])
    words = set(text.strip().split())
    return any(x in words for x in profane_words)


def use_reduce(data_list: list, user_string: str) -> tuple:
    """
    1) to add only even numbers in a list
    2) to find the biggest character in a string (printable ascii characters)
    3) to add every 3rd number in the given list

    :param data_list: list of elements
    :param user_string:the user defined string
    :return: tuple of all results

    """
    all_evens = reduce(lambda a, b: a + b, filter(lambda x: x % 2 == 0, data_list))
    biggest_char = reduce(lambda x, y: x if ord(x) > ord(y) else y, user_string)
    add_3rd_element = reduce(lambda x, y: x + y, [e for i, e in enumerate(data_list) if (i + 1) % 3 == 0])

    return all_evens, biggest_char, add_3rd_element


def generate_random_number_for_vehicles():
    """
    Using randint, random.choice and list comprehensions,
    write an expression that generates 15 random KADDAADDDD number plates,
    where KA is fixed, D stands for a digit, and A stands for Capital alphabets. 10<<DD<<99 & 1000<<DDDD<<9999
    :return: list of 15 random vehicle licence plate numbers
    """
    return ["KA" + str(d1) + l1 + l2 + str(d2) for _ in range(15) for d1 in [random.randint(10, 99)] for l1, l2 in
            zip(*random.sample(population=upper_letters, k=2)) for d2 in [random.randint(1000, 9999)]]


def generate_random_number_for_vehicles_again(start_range=1000, end_range=9999, state="KA"):
    """Write the above again from scratch where KA can be changed to DL,
    and 1000/9999 ranges can be provided. Now use a partial function such that 1000/9999 are hardcoded, but KA can be provided
    :return: list of 15 random vehicle licence plate numbers and a partial function
    """

    if not (state and isinstance(state, str) and state.isalpha()):
        raise ValueError("😑 `state` must be a string containing only letters from English alphabet")
    if not (start_range and end_range and isinstance(start_range, int) and isinstance(end_range, int)
            and str(start_range).isdigit() and str(end_range).isdigit()):
        raise ValueError("👊 `start_range` and `end_range` must be valid positive int ranges")

    return [state + str(d1) + l1 + l2 + str(d2) for _ in range(15) for d1 in [random.randint(10, 99)] for l1, l2 in
            zip(*random.sample(population=upper_letters, k=2)) for d2 in
            [random.randint(start_range, end_range)]], partial(generate_random_number_for_vehicles_again, start_range=1000, end_range=9999)


def generate_random_number_for_vehicles_again_using_partial(state):
    """Calls previous function to utilize it's second return value which is a Partial function
    with fixed start end end range values but `state` can be provided"""
    if not (state and isinstance(state, str) and state.isalpha()):
        raise ValueError("`state` must be a valid string containing only letters from English alphabet")

    _, f = generate_random_number_for_vehicles_again(state=state)
    return f(state=state)[0]
