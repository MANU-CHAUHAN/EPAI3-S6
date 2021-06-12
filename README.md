# S6 : First Class Functions

Default Values; Docstrings & Annotations; Lambda Expressions; Functional Introspection; Callables; Map, Filter & Zip; Reducing Functions; Partial Functions; The Operator Module

-------

Contents
    
1. Part 1 tasks
2. Part 2 tasks
3. Notes/experiments

--------------------

Part 1:
---------
1. Write a single expression that includes lambda, zip and map functions to select create 52 cards in a deck 
2. Write a normal function without using lambda, zip, and map function to create 52 cards in a deck 
3. Write a function that, when given 2 sets of 3 or 4 or 5 cards (1 game can only have 3 cards with each player or 4 cards or 5 cards per player) (1 deck of cards only), (2 players only), can identify who won the game of poker 

Given:
vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']

## Functions

### 1. create_deck_cards_lambda 

This function creates all 52 cards from vals and suits using lambda and map function in a single line

    def create_cards_lambda() -> list:
        """
        Creates 52 cards in a deck, with help of lambda, map, zip and list comprehension,
        all in a single expression
        :return: list of `tuples` containing card combinations
        """

### 2. create_deck_cards_normal_function

This function creates all 52 cards from vals and suits without using lambda and map function

    def create_deck_cards_normal_function() -> list:
        """
        Creates 52 cards in a deck via a simpler approach
        :return: list of tuples containing card combinations
        """

---------

## Rules for Poker:

#### Royal Flush : 

A, K, Q, J, 10, all the same suit for 5 cards.
A, K, Q, J, all the same suit for 4 cards.
A, K, Q, all the same suit for 3 cards.

#### Straight flush :

Cards in a sequence, all in the same suit.

#### Four of a kind :

Four cards of the same rank.
This is not applicable to set of 3 cards.

#### Full house :

Three of a kind with a pair.
This is not applicable to set of 3 or 4 cards.

#### Flush :

Any cards of the same suit, but not in a sequence.

#### Straight :

Cards in a sequence, but not of the same suit.

#### Three of a kind :

Three cards of the same rank.

#### Two pair :

Two different pairs.
This is not applicable to set of 3 cards.

#### One pair :

Two cards of the same rank.

#### High Card :

When you haven’t made any of the hands above, the highest card from both set is compared.

----

### **Test cases**

1. test_readme_exists : Checks whether readme exists

2. test_readme_contents : Checks if there are 500 words in readme

3. test_readme_proper_description :  test for appropriate documentation of readme including important functions and keywords

4. test_readme_file_for_formatting : checks for proper formatting (at leat 10 #s)

5. test_indentations : check for source file indentation

6. test_function_name_had_cap_letter :  checks if function has cap letters

7. test_all_functions_implemented : checks if all given functions were included in README

8. test_create_deck_cards_single_expression_docstring : check for docstring exists or not

9. test_create_deck_cards_single_expression_docstring_content : check for  docstring length

10. test_play_royal_flush : test for Royal Flush

11. test_play_straight_flush : checks for straight flush

12. test_play_4_Of_A_Kind : tests 4 of a kind

13. test_play_full_house : tests full house

14. test_play_flush : tests for a player having flush

15. test_play_straight : tests for a player having straight

16. test_play_3_kind : tests 3 of a kind for players

17. test_play_2_pair : tests for a pair formed for a player

18. test_play_1_pair : test for a single pair

19. test_play_high_card : tests for a player having a high card

20. test_create_deck_cards_single_expression_total_cards :  check for total no of cards

21. test_create_deck_cards_single_expression_compare_cards : compare the result with card combination

22. test_create_deck_cards_normal_function_docstring : check for docstring exists or not

23. test_create_deck_cards_normal_function_docstring_content : check for  docstring length

24. test_create_deck_cards_normal_function_total_cards : check for total no of cards

25. test_create_deck_cards_normal_function_compare_cards : compare the result with card combination

26. test_play_poker_game: checks if a given player wins or not
---------


Part 2:
-------
1. Write a function using only list filter lambda that can tell whether a number is a Fibonacci number or not. You can use a pre-calculated list/dict to store fab numbers till 10000

2. Using list comprehension (and zip/lambda/etc if required) write expressions that:
    a. add 2 iterables a and b such that a is even and b is odd
    b. strips every vowel from a string provided (tsai>>t s)
    c. acts like a sigmoid function for a 1D array
    d. takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn

3. A list comprehension expression that takes a ~200-word paragraph, and checks whether it has any of the swear words mentioned in https://github.com/RobertJGabriel/Google-profanity-words/blob/master/list.

4. Using reduce function:
    a. add only even numbers in a list
    b. find the biggest character in a string (printable ASCII characters)
    c. adds every 3rd number in a list

5. Using randint, random.choice and list comprehensions, write an expression that generates 15 random KADDAADDDD number plates, where KA is fixed, D stands for a digit, and A stands for Capital alphabets. 10<<DD<<99 & 1000<<DDDD<<9999

6. Write the above again from scratch where KA can be changed to DL, and 1000/9999 ranges can be provided. Now use a partial function such that 1000/9999 are hardcoded, but KA can be provided


## Part 3:

----------
### functools
The functools module is for higher-order functions: functions that act on or return other functions. In general, any callable object can be treated as a function for the purposes of this module.


### What are `partial functions` ?
A partial function is an in-built utility function that allows us to call another function with fixed values for certain arguments.

> from the official docs:

    functools.partial(func, /, *args, **keywords)
    Return a new partial object which when called will behave like func called with the positional arguments args and keyword arguments keywords. If more arguments are supplied to the call, they are appended to args. If additional keyword arguments are supplied, they extend and override keywords. Roughly equivalent to:
    
    def partial(func, /, *args, **keywords):
        def newfunc(*fargs, **fkeywords):
            newkeywords = {**keywords, **fkeywords}
            return func(*args, *fargs, **newkeywords)
        newfunc.func = func
        newfunc.args = args
        newfunc.keywords = keywords
        return newfunc
    The partial() is used for partial function application which “freezes” some portion of a function’s arguments and/or keywords resulting in a new object with a simplified signature. For example, partial() can be used to create a callable that behaves like the int() function where the base argument defaults to two:
    
    >>>
    >>> from functools import partial
    >>> basetwo = partial(int, base=2)
    >>> basetwo.__doc__ = 'Convert base 2 string to an int.'
    >>> basetwo('10010')
    18

--> Implementing a partial exponentiation function

    # original/base function
    def power(base, exponent):
      return base ** exponent

**we may want to implement a function that computes the squared value of a number**

Simple approach entails creating a separate function:

    def squared(base):
      return base ** 2

Not much of a hassle here as it is a small function but scenario could scale up quickly when developing say a Python pipeline.

-> Using same base function to solve our `square` needs:

    from functools import partial

    def power(base, exponent):
      return base ** exponent

    squared = partial(power, exponent=2)

we may call “squared()” as simply as follows:

    >>>squared(3)

    >>>squared(base=7)

-----------

## Why use `literal syntax` ?

example for list:

    >>>dis.dis('list()')

      1           0 LOAD_NAME                0 (list)
                  2 CALL_FUNCTION            0
                  4 RETURN_VALUE

    >>> dis.dis('[]')
      1           0 BUILD_LIST               0
                  2 RETURN_VALUE

As can be seen above with opcodes, `list()` has to resolve the name first by lookup in global and builtins,
call the function.

Whereas, `[]` resorts to directly building a list, thus avoiding name resolution and function call.


## Dictionaries in Python: Going deeper in the rabbit hole
> [How are Python's built-in Dictionaries Implemented?](https://stackoverflow.com/a/44509302/3903762)

1. They are hash tables
   
2. A new layout and algorithm, as of Python 3.6, makes them:
   
    a. ordered by key insertion, and
   
    b. take up less space,
   
    c. at virtually no cost in performance.

3. Another optimization saves space when dicts share keys (in special cases)

Note: This is implementation detail in 3.6 and NOT a language feature. This became a language feature since Python 3.7


> Python's Dictionaries are Hash Tables

For a long time, it worked exactly like this. Python would preallocate 8 empty rows and use the hash to determine where to stick the key-value pair. For example, if the hash for the key ended in 001, it would stick it in the 1 (i.e. 2nd) index (like the example below.)
    
       <hash>       <key>    <value>
         null        null    null
    ...010001    ffeb678c    633241c4 # addresses of the keys and values
         null        null    null
          ...         ...    ...
Each row takes up 24 bytes on a 64 bit architecture, 12 on a 32 bit. (Note that the column headers are just labels for our purposes here - they don't actually exist in memory.)

If the hash ended the same as a preexisting key's hash, this is a collision, and then it would stick the key-value pair in a different location.

After 5 key-values are stored, when adding another key-value pair, the probability of hash collisions is too large, so the dictionary is doubled in size. In a 64 bit process, before the resize, we have 72 bytes empty, and after, we are wasting 240 bytes due to the 10 empty rows.

This takes a lot of space, but the lookup time is fairly constant. The key comparison algorithm is to compute the hash, go to the expected location, compare the key's id - if they're the same object, they're equal. If not then compare the hash values, if they are not the same, they're not equal. Else, then we finally compare keys for equality, and if they are equal, return the value. The final comparison for equality can be quite slow, but the earlier checks usually shortcut the final comparison, making the lookups very quick.

Collisions slow things down, and an attacker could theoretically use hash collisions to perform a denial of service attack, so we randomized the initialization of the hash function such that it computes different hashes for each new Python process.

The wasted space described above has led us to modify the implementation of dictionaries, with an exciting new feature that dictionaries are now ordered by insertion.

>The New Compact Hash Tables

We start, instead, by preallocating an array for the index of the insertion.

Since our first key-value pair goes in the second slot, we index like this:
    
    [null, 0, null, null, null, null, null, null]
And our table just gets populated by insertion order:
    
       <hash>       <key>    <value>
    ...010001    ffeb678c    633241c4 
          ...         ...    ...
So when we do a lookup for a key, we use the hash to check the position we expect (in this case, we go straight to index 1 of the array), then go to that index in the hash-table (e.g. index 0), check that the keys are equal (using the same algorithm described earlier), and if so, return the value.

We retain constant lookup time, with minor speed losses in some cases and gains in others, with the upsides that we save quite a lot of space over the pre-existing implementation and we retain insertion order. The only space wasted are the null bytes in the index array.

**_Raymond Hettinger_** introduced this on python-dev in December of 2012. It finally got into CPython in Python 3.6. Ordering by insertion was considered an implementation detail for 3.6 to allow other implementations of Python a chance to catch up.

>Shared Keys

Another optimization to save space is an implementation that shares keys. Thus, instead of having redundant dictionaries that take up all of that space, we have dictionaries that reuse the shared keys and keys' hashes. You can think of it like this:

         hash         key    dict_0    dict_1    dict_2...
    ...010001    ffeb678c    633241c4  fffad420  ...
          ...         ...    ...       ...       ...
For a 64 bit machine, this could save up to 16 bytes per key per extra dictionary.
