import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_no_positive_numbers():
    """Test a list with no positive numbers, including zeros and negatives."""
    assert longest_positive_streak([0, -1, -5, 0, -10]) == 0

def test_all_positive_numbers():
    """Test a list with all positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_single_streak():
    """Test a single streak of positive numbers."""
    assert longest_positive_streak([0, 1, 2, 3, 0]) == 3

def test_multiple_streaks():
    """Test multiple streaks and ensure the longest is returned."""
    assert longest_positive_streak([1, 2, 0, 1, 2, 3, 0, 1]) == 3
    assert longest_positive_streak([1, 0, 1, 2, 3, 4, 0, 1, 2]) == 4

def test_streak_at_beginning():
    """Test a streak at the beginning of the list."""
    assert longest_positive_streak([1, 2, 3, 0, -5]) == 3

def test_streak_at_end():
    """Test a streak at the end of the list."""
    assert longest_positive_streak([-1, 0, 1, 2, 3, 4]) == 4

def test_mixed_numbers():
    """Test a mixed list of positive, negative and zero values."""
    assert longest_positive_streak([1, -2, 3, 4, 0, 5, 6, 7, -8, 9]) == 3