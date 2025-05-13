import Lab3

print("Lab 3 - Software Unit Testing with PyTest")

def test_bubble_sort_ascending_less_than_10():
    input_arr = [64, 34, 25, 12, 22]
    expected_result = [12, 22, 25, 34, 64]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert result == expected_result

def test_bubble_sort_descending_less_than_10():
    input_arr = [64, 34, 25, 12, 22]
    expected_result = [64, 34, 25, 22, 12]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)
    assert result == expected_result

def test_bubble_sort_more_than_or_equal_10_numbers():
    input_arr = [64, 34, 25, 12, 22, 11, 90, 55, 43, 88]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert result == 1

def test_bubble_sort_no_numbers():
    input_arr = []
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert result == 0

def test_bubble_sort_non_integer_values():
    input_arr = [64, 34, 'a', 12, 22]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert result == 2
