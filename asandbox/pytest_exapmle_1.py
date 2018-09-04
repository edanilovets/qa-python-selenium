import pytest
import random


@pytest.fixture
def rnd_gen():
    return random.Random(12345)


@pytest.fixture
def rnd(rnd_gen):
    return rnd_gen.random()


def test_1(rnd):
    print("Random: %s" % rnd)
