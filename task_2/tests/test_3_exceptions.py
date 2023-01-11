"""Проверка на ожидаемые исключения"""

import pytest


def test_add_raises():
    with pytest.raises(ZeroDivisionError):
        1/0


def f():
    raise SystemExit(1)


def test_system_exit():
    with pytest.raises(SystemExit):
        f()
