import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from calculos import promedio


def test_promedio_normal():
    assert promedio([2, 4, 6]) == 4


def test_promedio_lista_vacia():
    with pytest.raises(ZeroDivisionError):
        promedio([])


def test_promedio_negativos():
    assert promedio([-5, -10, -15]) == -10