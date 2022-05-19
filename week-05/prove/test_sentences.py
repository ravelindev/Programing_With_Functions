# This is my test file for the sentences.py file.
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["two", "some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


# Writing the get_noun test
def test_get_noun():
        # 1. Test the single determiners.
    single_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    
    for _ in range(4):
        word = get_determiner(1)
        assert word in single_determiners
    # 2. Test the plural determiners.

    plural_determiners = ["two", "some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


def test_get_verb():
    # 1. Test the present tense.

    present_tense = ["ate", "fought", "gave", "went", "took", "made", "wrote", "read", "broke", "kept"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_verb function which
        # should return a present tense verb.
        word = get_verb(1, "present")

        # Verify that the word returned from get_verb
        # is one of the words in the present_tense list.
        assert word in present_tense

    # 2. Test the past tense.

    past_tense = ["ate", "fought", "gave", "went", "took", "made", "wrote", "read", "broke", "kept"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_verb function which
        # should return a past tense verb.
        word = get_verb(1, "past")

        # Verify that the word returned from get_verb
        # is one of the words in the past_tense list.
        assert word in past_tense

    # 3. Test the future tense.

    future_tense = ["ate", "fought", "gave", "went", "took", "made", "wrote", "read", "broke", "kept"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_verb function which
        # should return a future tense verb.
        word = get_verb(1, "future")

        # Verify that the word returned from get_verb
        # is one of the words in the future_tense list.
        assert word in future_tense


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])