import pytest
from checker import SimilarityChecker


def test_same_length_gets_max_score():
    checker = SimilarityChecker("ASD", "DSA")
    assert checker.length_score() == 60


def test_double_length_gets_zero():
    checker = SimilarityChecker("A", "BB")
    assert checker.length_score() == 0


def test_more_than_double_length_gets_zero():
    checker = SimilarityChecker("A", "BBBBB")
    assert checker.length_score() == 0


def test_partial_score_aaabb_baa():
    checker = SimilarityChecker("AAABB", "BAA")
    assert checker.length_score() == pytest.approx(20)


def test_partial_score_aa_aae():
    checker = SimilarityChecker("AA", "AAE")
    assert checker.length_score() == pytest.approx(30)


def test_order_does_not_matter():
    checker_long_first = SimilarityChecker("AAABB", "BAA")
    checker_short_first = SimilarityChecker("BAA", "AAABB")
    assert checker_long_first.length_score() == checker_short_first.length_score()


def test_empty_string_gets_zero():
    checker = SimilarityChecker("", "ABC")
    assert checker.length_score() == 0
