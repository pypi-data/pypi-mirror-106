import pytest

from pymultirole_plugins.converter import ConverterBase, ConverterParameters


def test_converter():
    with pytest.raises(TypeError) as err:
        parser = ConverterBase()
        assert parser is None
    assert "Can't instantiate abstract class ConverterBase with abstract methods convert" in str(err.value)


def test_default_options():
    options = ConverterParameters()
    assert options is not None
