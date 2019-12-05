import pytest


def func(x):
    return x + 1


def setup_module():
    print("setup_module")


def test_answer():
    assert func(3) == 4


class TestFunc:
    @classmethod
    def setup_class(cls):
        print("setup_class")

    def setup(self):
        print("setup")

    @pytest.mark.fail
    def test_answer1(self):
        print("test_answer")
        assert func(3) == 4

    @pytest.mark.success
    @pytest.mark.parametrize("input, expect", [
        (5, 6),
        (7, 8),
        (0, 1),
        (2, 3)
    ])
    def test_answer2(self, input, expect):
        print("test_answer2")
        assert func(input) == expect

    def test_answer3(self):
        print("test_answer2")
        assert func(7) == 8
