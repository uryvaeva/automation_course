# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('a, b, result',
[pytest.param(2, 2, 1, marks=pytest.mark.smoke('basic test')),
 pytest.param(2, 4, 0.5, marks=pytest.mark.skip('bad test')),
 (12, 2, 6),
 (1, -1, -1),
 (10, 5, 2)])


def test_division_test(a, b, result):
    assert all_division(a, b) == result
