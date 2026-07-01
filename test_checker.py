import pytest
from checker import SimilarityChecker


def test_same_alphabet_set_gets_max_score():
    checker = SimilarityChecker("ASD, DSA")
    assert checker.get_alphabet_score() == 40


def test_completely_different_alphabets_gets_zero():
    checker = SimilarityChecker("A, BB")
    assert checker.get_alphabet_score() == 0


def test_same_alphabet_set_gets_max_score_with_repeats():
    checker = SimilarityChecker("AAABB, BAA")
    assert checker.get_alphabet_score() == 40


def test_partial_score_aa_aae():
    checker = SimilarityChecker("AA, AAE")
    assert checker.get_alphabet_score() == pytest.approx(20)


def test_order_does_not_matter():
    checker_first = SimilarityChecker("AA, AAE")
    checker_second = SimilarityChecker("AAE, AA")
    assert checker_first.get_alphabet_score() == checker_second.get_alphabet_score()


def test_lowercase_letters_are_ignored():
    checker = SimilarityChecker("aaa, bbb")
    assert checker.get_alphabet_score() == 0
