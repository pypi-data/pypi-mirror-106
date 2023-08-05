#!/usr/bin/env python

import pytest

from sparkbar import sparkbarh

def test_empty_list():
    "Test passing in an empty list"
    assert sparkbarh([]) == []

def test_list_with_negative_numbers():
    "Raises on negative numbers"
    with pytest.raises(Exception) as e_info:
        sparkbarh([1, -1, 1])

def test_list_of_none():
    "List full of nones returns blank strings"
    assert sparkbarh([None, None, None]) == ["", "", ""]

def test_mult_number_list():
    "Basic number list is correctly visualized"
    in_list = [40, 30, 10]
    assert sparkbarh(in_list, width=4) == ["████", "███", "█"]

def test_single_number_list():
    "Single number list is correctly visualized"
    in_list = [30]
    assert sparkbarh(in_list, width=5) == ["█████"]

def test_default_width():
    "Not passing a width works"
    in_list = [30, 15]
    assert sparkbarh(in_list) == ["████████", "████"]

def test_list_with_none():
    "List with None values is correctly visualized"
    in_list = [40, None, 10]
    assert sparkbarh(in_list, width=4) == ["████", "", "█"]

def test_value_label():
    "value_label option displays correctly"
    in_list = [40, 30, 10]
    assert sparkbarh(in_list, width=4, value_label=True) == ["████ 40", "███ 30", "█ 10"]

def test_uniform_width():
    "uniform_width option displays correctly"
    in_list = [40, 30, 10]
    assert sparkbarh(in_list, width=4, uniform_width=True) == [
        "████",
        "███ ",
        "█   "
    ]

def test_uniform_width_and_value_label():
    "uniform_width with value_label option displays correctly"
    in_list = [40, 30, 10]
    assert sparkbarh(in_list, width=4, value_label=True, uniform_width=True) == [
        "████ 40",
        "███ 30 ",
        "█ 10   "
    ]

def test_negative_width():
    "Raises on negative widths"
    with pytest.raises(Exception) as e_info:
        sparkbarh([1, 2, 3], width=-1)

def test_excessive_width():
    "Raises on large widths"
    with pytest.raises(Exception) as e_info:
        sparkbarh([1, 2, 3], width=150)
