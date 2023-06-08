# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest

def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.usefixtures('start_end_time')
class Test:
    def test_division_positive(self, duration):
        assert all_division(2, 2) == 1


    def test_division_3_args(self):
        assert all_division(12, 2, 3) == 2
