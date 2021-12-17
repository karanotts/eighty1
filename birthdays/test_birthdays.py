import datetime
from birthdays import get_birthdays, get_match


def test_get_birthdays():
    assert len(get_birthdays(3)) == 3
    assert all(isinstance(x, datetime.date) for x in get_birthdays(3))


def test_get_match():
    no_match = [
        datetime.date(2000, 2, 27),
        datetime.date(2000, 9, 16),
        datetime.date(2000, 2, 21),
    ]
    one_match = [
        datetime.date(2000, 2, 27),
        datetime.date(2000, 5, 16),
        datetime.date(2000, 5, 16),
    ]
    assert get_match(no_match) == None
    assert get_match(one_match) == [datetime.date(2000, 5, 16)]
