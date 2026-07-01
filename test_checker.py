import pytest
from checker import SimilarityChecker


def test_same_length_gets_max_score():
    checker = SimilarityChecker("ASD, DSA")
    assert checker.get_length_score() == 60


def test_double_length_gets_zero():
    checker = SimilarityChecker("A, BB")
    assert checker.get_length_score() == 0


def test_more_than_double_length_gets_zero():
    checker = SimilarityChecker("A, BBBBB")
    assert checker.get_length_score() == 0


def test_partial_score_aaabb_baa():
    checker = SimilarityChecker("AAABB, BAA")
    assert checker.get_length_score() == pytest.approx(20)


def test_partial_score_aa_aae():
    checker = SimilarityChecker("AA, AAE")
    assert checker.get_length_score() == pytest.approx(30)


def test_order_does_not_matter():
    checker_first = SimilarityChecker("AAABB, BAA")
    checker_second = SimilarityChecker("BAA, AAABB")
    assert checker_first.get_length_score() == checker_second.get_length_score()
