from assertpy import assert_that

from coding_exercise.application.splitter import Splitter
from coding_exercise.domain.model.cable import Cable


def test_should_not_return_none_when_splitting_cable():
    assert_that(Splitter().split(Cable(10, "coconuts"), 1)).is_not_none()

def test_should_raise_error_if_cuts_greater_than_cable():
    cable = Cable(10, "coconuts")
    assert_that(Splitter().split).raises(ValueError).when_called_with(cable, 11)

def test_should_raise_error_if_cuts_less_than_min():
    cable = Cable(10, "coconuts")
    assert_that(Splitter().split).raises(ValueError).when_called_with(cable, -1)

def test_should_raise_error_if_cuts_greater_than_max():
    cable = Cable(10, "coconuts")
    assert_that(Splitter().split).raises(ValueError).when_called_with(cable, 65)

def test_should_raise_error_if_cable_length_less_than_min():
    cable = Cable(1, "coconuts")
    assert_that(Splitter().split).raises(ValueError).when_called_with(cable, 2)

def test_should_raise_error_if_cable_length_greater_than_max():
    cable = Cable(1025, "coconuts")
    assert_that(Splitter().split).raises(ValueError).when_called_with(cable, 2)

def test_should_raise_error_if_nan():
    assert_that(Splitter().plus_one).raises(ValueError).when_called_with('one')

def test_should_equal_no_remainder():
    given_cable = Cable(10, "coconuts")
    assert_that(Splitter().get_new_cable_lengths(given_cable, 1)).is_equal_to([5, 5])

def test_should_equal_with_remainder():
    given_cable = Cable(5, "coconuts")
    assert_that(Splitter().get_new_cable_lengths(given_cable, 2)).is_equal_to([1, 1, 1, 1, 1])

def test_should_equal_plus_one():
    assert_that(Splitter().plus_one(1)).is_equal_to(2)

def test_should_equal_zfill_1():
    assert_that(Splitter().get_zfill(9)).is_equal_to(1)

def test_should_equal_zfill_2():
    assert_that(Splitter().get_zfill(99)).is_equal_to(2)

def test_should_equal_zfill_3():
    assert_that(Splitter().get_zfill(999)).is_equal_to(3)

def test_should_have_correct_names_under_ten_cables():
    given_cable = Cable(5, "coconuts")
    split_results = Splitter().split(given_cable, 2)
    split_names = [cable.name for cable in split_results]
    expected_results = ['coconuts-0', 'coconuts-1', 'coconuts-2', 'coconuts-3', 'coconuts-4']
    assert_that(split_names).is_equal_to(expected_results)
    
def test_should_have_correct_names_over_ten_cables():
    given_cable = Cable(20, "coconuts")
    split_results = Splitter().split(given_cable, 9)
    split_names = [cable.name for cable in split_results]
    expected_results = [
        'coconuts-00',
        'coconuts-01',
        'coconuts-02',
        'coconuts-03',
        'coconuts-04',
        'coconuts-05',
        'coconuts-06',
        'coconuts-07',
        'coconuts-08',
        'coconuts-09'
    ]
    assert_that(split_names).is_equal_to(expected_results)
    