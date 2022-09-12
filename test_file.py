import pytest
import math


class TestList:
    @pytest.mark.parametrize("x", [[], [1, "test"]])
    def test_list1(self, x):
        try:
            assert len(x) != 0
        except AssertionError:
            pass

    def test_list2(self):
        l = [1, 2, 3, 4]
        try:
            assert 4 in l
        except AssertionError:
            pass

    def test_list3(self):
        l = ["Tom", "Bob"]
        try:
            assert l.remove("Tim")
        except ValueError:
            pass


class TestInt:
    @pytest.mark.parametrize("x", [-1, 0, 1])
    def test_int1(self, x):
        try:
            assert x >= 0
        except AssertionError:
            pass

    def test_int2(self):
        a = 9937
        try:
            assert type(a) == int
        except AssertionError:
            pass

    def test_int3(self):
        a = -9937
        try:
            assert math.sqrt(a)
        except ValueError:
            pass
