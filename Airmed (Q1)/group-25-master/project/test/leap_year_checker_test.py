from project.leap_year_checker import is_leap_year


def test_is_leap_year_positive():
    result = is_leap_year(2020)
    assert result


def test_is_leap_year_negative():
    result = is_leap_year(2019)
    assert not result


def test_is_leap_year_hundred():
    result = is_leap_year(2100)
    assert not result


def test_is_leap_year_four_hundred():
    result = is_leap_year(2400)
    assert result
