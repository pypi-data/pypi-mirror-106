import pytest

from pymultirole_plugins.formatter import FormatterBase, FormatterParameters


def test_formatter():
    with pytest.raises(TypeError) as err:
        parser = FormatterBase()
        assert parser is None
    assert "Can't instantiate abstract class FormatterBase with abstract methods format" in str(err.value)


def test_default_options():
    options = FormatterParameters()
    assert options is not None
