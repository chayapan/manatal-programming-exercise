"""Exercise 2: Randomness Test
In a lottery game, there is a container that contains 50 balls numbered from 1 to 50.
The lottery game consists in picking 10 balls out of the container and ordering them in ascending order.
Write a Python function that generates the output of a lottery game (it should return a list).
Also, describe which unit tests you could implement to test the output of your function.

Time: 10 minutes plus 5 minutes for test development.

Use an array as container class.
Whether or not to build a Ball class to support the game element. Nope. Too complex.
This program first generate original pool of 50 balls.
Then the program pick 10 balls from this pool.
For picking the 10 balls outcome, use random.choices().

Two unit tests are included:
1. check that the return list has correct length
2. check that the values in the return list are within specified parameter

Run unit tests:

$ python3 -m pytest ex2_randballs.py
======================================== test session starts ========================================
platform darwin -- Python 3.7.6, pytest-7.0.1, pluggy-1.0.0
rootdir: /Users/chayapan/Desktop/Sr.Python Developer (Manatal)
collected 2 items

ex2_randballs.py ..                                                                           [100%]

========================================= 2 passed in 0.01s =========================================


Run demo:

$ python3 ex2_randballs.py
Game 1:
[50, 45, 5, 42, 27, 29, 24, 46, 39, 45]
Game 2:
[39, 30, 42, 11, 14, 16, 16, 11, 50, 17]
Game 3:
Pool: [46, 38, 16, 9, 48, 29, 16, 3, 25, 13, 21, 44, 1, 10, 23, 41, 18, 20, 38, 29, 5, 39, 5, 2, 18, 45, 49, 10, 32, 1, 42, 27, 7, 45, 36, 46, 8, 18, 38, 23, 8, 6, 2, 9, 44, 13, 43, 40, 40, 18]
[48, 9, 43, 38, 38, 2, 36, 6, 13, 16]
Game 4:
Pool: [42, 5, 37, 31, 34, 32, 48, 27, 8, 13, 6, 31, 5, 18, 15, 6, 41, 17, 2, 10, 17, 28, 23, 43, 7, 27, 31, 21, 3, 32, 40, 50, 42, 24, 9, 39, 48, 2, 47, 34, 8, 45, 23, 37, 24, 23, 18, 27, 41, 5]
[45, 37, 42, 17, 8, 24, 48, 50, 5, 10]


In current implementation, the function operates as black box and doesn't allow
    examining the method that is used to generate the numbers and randomness.
For testing the true randomness, regression technique might be performed over several
    calls to the function to obtain the output as samples and then use analysis of
    mathematical property to determine randomness quality.

"""
from random import randint, choices

def lottery_game_output(show_original_pool=False):
    """ Returns a list.
        This list contains 10 balls picked from the original pool of 50 balls.
        When  show_original_pool  flag is True, print the original 50 balls.
    """
    # Make original pool of balls. 50 balls in total.
    original_list = [randint(1,50) for i in range(50)]
    if show_original_pool==True:
        print("Pool:", original_list)
    # Pick 10 balls at random. Equally probable chance for each ball.
    pick_list = choices(original_list, k=10)
    return pick_list

def test_output_length():
    """The function returns correct number of output."""
    assert len(lottery_game_output()) == 10

def test_output_values_within_range():
    """Values in the output list are within specification."""
    outcome = lottery_game_output()
    for v in outcome:
        assert v >= 1
        assert v <=50

if __name__ == '__main__':
    print("Game 1:")
    print(lottery_game_output())
    print("Game 2:")
    print(lottery_game_output())
    print("Game 3:")
    print(lottery_game_output(show_original_pool=True))
    print("Game 4:")
    print(lottery_game_output(show_original_pool=True))
