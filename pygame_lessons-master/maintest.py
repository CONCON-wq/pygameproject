#test_main.py
#импортируем pytest

import pytest

#пишем функция сложения
def add(a,b):
    return a + b

def test_add():
    result = add(2,3)
    assert result


@pytest.fixture

def sample_list():
    return[1,2,3,4,5]

def test_sum(sample_list):
    assert sum(sample_list) == 15

@pytest.mark.support
def test_heavy_computation():
    write = sum(range(1_000_000))
    assert write>0

@pytest.mark.makes
def test_login():
    assert "admin" in ["user","admin","guest","easy"]
