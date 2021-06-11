# S6

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
