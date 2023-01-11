def test_passing():
    assert (1, 2, 3) == (1, 2, 3)


def test_fail_in():
    assert 1 in [2, 3, 4]


def test_passing_two():
    a = 50
    b = 60
    assert a < b


def test_passing_not_in():
    assert 'flzz' not in 'fizzbuzz'