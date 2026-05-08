from app.calculator import add, subtract


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-2, -3) == -5


def test_add_positive_and_negative_number():
    assert add(10, -4) == 6


def test_subtract_positive_numbers():
    assert subtract(10, 3) == 7


def test_subtract_negative_numbers():
    assert subtract(-10, -3) == -7


def test_subtract_result_can_be_negative():
    assert subtract(3, 10) == -7