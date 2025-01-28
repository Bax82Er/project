from lsns.src.main import calculate_logarithm
import pytest


def test_calculate_logarithm_with_negative_number():
    assert calculate_logarithm(8, 2) == 3.0
    assert calculate_logarithm(8, 4) == 1.5


with pytest.raises(ValueError):
    assert calculate_logarithm(0, 2)
    # Проверяем, что сообщение об ошибке соответствует ожидаемому
    #assert str(exc_info.value) == "Логарифм можно вычислить только для положительных чисел"


