from bagels import get_secret_num, get_clues


def test_get_secret_num():
    '''Test if get_secret_num() returns a string of 3 digits'''
    secret_num = get_secret_num(3)
    assert all(isinstance(x, str) for x in secret_num)
    assert len(secret_num) == 3
    assert isinstance(secret_num, str)


def test_get_clues():
    '''Test if get_clues returns correct hints'''
    guess = '123'
    assert get_clues(guess, '123') == 'You got it!'
    assert get_clues(guess, '145') == 'Fermi'
    assert get_clues(guess, '124') == 'Fermi Fermi'
    assert get_clues(guess, '134') == 'Fermi Pico'
    assert get_clues(guess, '132') == 'Fermi Pico Pico'
    assert get_clues(guess, '541') == 'Pico'
    assert get_clues(guess, '531') == 'Pico Pico'
    assert get_clues(guess, '312') == 'Pico Pico Pico'
    assert get_clues(guess, '456') == 'Bagels'