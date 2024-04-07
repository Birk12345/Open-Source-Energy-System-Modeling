from Calculator import add
from Calculator import subtract
from Calculator import multiply
from Calculator import divide


class TestCalculator:
    def test_add(self):
        assert add(4, 5) == 9
        assert add(5, 2) == 7
        assert add(24, 1) == 25

    def test_subtract(self):
        assert subtract(3, 1) == 2
        assert subtract(2, 1) == 1
        assert subtract(20, 10) == 10

    def test_multiply(self):
        assert multiply(6, 2) == 12
        assert multiply(1, 5) == 5
        assert multiply(3, 6) == 18

    def test_divide(self):
        assert divide(4, 2) == 2
        assert divide(10, 5) == 2
        assert divide(50, 2) == 25
