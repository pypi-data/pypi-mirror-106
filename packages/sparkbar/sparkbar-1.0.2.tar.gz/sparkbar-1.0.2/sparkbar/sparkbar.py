#!/usr/bin/env python

import math

# FYI there are 8 of them
_BLOCKS = "▏▎▍▌▋▊▉█"
_MAX_WIDTH = 128

def sparkbarh(numbers=[], width=8, value_label=False, uniform_width=False):
    assert width > 0, "Requires non-negative width"
    assert width <= _MAX_WIDTH, "Max width is 128 characters."

    if len(numbers) == 0:
        return []

    # find max value
    max_value = _find_max_value(numbers)
    if max_value is None:
        return [""] * len(numbers)

    has_negative_numbers = _has_negative_numbers(numbers)
    assert has_negative_numbers == False, "There are negative numbers"

    # if uniform width, then determine needed padding
    if uniform_width and value_label:
        full_width = width + 1 + len(str(max_value))
    elif uniform_width:
        full_width = width
    else:
        full_width = 0

    return [sparkbarh_cell(x, max_value, width, value_label).ljust(full_width) for x in iter(numbers)]


def _find_max_value(numbers):
    not_none = [x for x in numbers if x is not None]
    if len(not_none) > 0:
        return max(not_none)
    else:
        return None

def _has_negative_numbers(numbers):
    for number in numbers:
        if number is not None and number < 0:
            return True
    return False

def sparkbarh_cell(value, max_value, width=8, value_label=False):
    assert width > 0, "Requires non-negative width"
    assert width <= _MAX_WIDTH, "Max width is 128 characters."

    if value is None:
        return ""
    assert value <= max_value, "Value to draw exceeds max value"

    bar_length = width * (value / max_value)
    full_bars = _BLOCKS[7] * math.floor(bar_length)
    remain_bar_length = bar_length % 1

    remain_bar_index = round(remain_bar_length * 8) - 1
    if remain_bar_length > 0 and remain_bar_index >= 0:
        partial_bars = _BLOCKS[remain_bar_index]
    else:
        partial_bars = ""

    if value_label:
        return "{}{} {}".format(full_bars, partial_bars, value)
    else:
        return "{}{}".format(full_bars, partial_bars)

