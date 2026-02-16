# Returnerar summan av alla tal i listan

def sum_list(list):
    return sum(list)


def test_empty_list():
    sum_list([])
    expected =  0
    actual = sum_list([])
    assert actual == expected


def test_number_list():
    # TODO: testa med listor som har ett, två respektive fem element.
    assert sum_list([1]) == 1
    assert sum_list([1, 2, 3, 4, 5]) == 15
    assert sum_list([1, 2]) == 3