import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test with an empty list, expecting 0."""
    assert longest_positive_streak([]) == 0

def test_multiple_streaks_longest_wins():
    """Test with multiple streaks to ensure the longest one is returned."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_with_zeros():
    """Test with zeros breaking the streak."""
    assert longest_positive_streak([1, 2, 0, 3, 4, 5]) == 3

def test_with_negatives():
    """Test with negative numbers breaking the streak."""
    assert longest_positive_streak([1, 2, -3, 4, 5]) == 2

def test_all_positive_numbers():
    """Test a list with only positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_all_non_positive_numbers():
    """Test a list with no positive numbers."""
    assert longest_positive_streak([-1, -2, 0, -3]) == 0

def test_single_positive_number():
    """Test a list with a single positive number."""
    assert longest_positive_streak([5]) == 1

def test_single_non_positive_number():
    """Test a list with a single non-positive number."""
    assert longest_positive_streak([-5]) == 0

def test_streak_at_the_end():
    """Test when the longest streak is at the end of the list."""
    assert longest_positive_streak([-1, 0, 1, 2, 3, 4]) == 4

def test_identical_positive_values():
    """Test with a streak of identical positive values."""
    assert longest_positive_streak([1, 1, 1]) == 3