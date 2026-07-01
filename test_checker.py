import pytest
from checker import AlphabetChecker


def test_same_alphabet_set_gets_max_score():
    checker = AlphabetChecker("ASD", "DSA")
    assert checker.alphabet_score() == 40


def test_completely_different_alphabets_gets_zero():
    checker = AlphabetChecker("A", "BB")
    assert checker.alphabet_score() == 0


def test_same_alphabet_set_gets_max_score_with_repeats():
    checker = AlphabetChecker("AAABB", "BAA")
    assert checker.alphabet_score() == 40


def test_partial_score_aa_aae():
    checker = AlphabetChecker("AA", "AAE")
    assert checker.alphabet_score() == pytest.approx(20)


def test_order_does_not_matter():
    checker_first = AlphabetChecker("AA", "AAE")
    checker_second = AlphabetChecker("AAE", "AA")
    assert checker_first.alphabet_score() == checker_second.alphabet_score()


def test_lowercase_letters_are_ignored():
    checker = AlphabetChecker("aaa", "bbb")
    assert checker.alphabet_score() == 0


def test_empty_strings_get_zero():
    checker = AlphabetChecker("", "")
    assert checker.alphabet_score() == 0
