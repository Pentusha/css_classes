import pytest

from css_classes import css_classes


@pytest.mark.parametrize('args, kwargs, expected', (
    (('btn',), {}, 'btn'),
    (('btn btn',), {}, 'btn'),
    (('btn', 'btn'), {}, 'btn'),
    (('btn btn-success',), {}, 'btn btn-success'),
    (('btn', 'btn-success'), {}, 'btn btn-success'),
    (('btn',), {'btn-success': True, 'btn-warning': False}, 'btn btn-success'),
    (({'btn': True}, {'btn-success': False}), {}, 'btn'),
    (({('btn', 'btn-success'): True}, {'btn-success': False}), {}, 'btn btn-success'),
    (('btn', ('btn-success', 'disabled')), {}, 'btn btn-success disabled'),
))
def test_positive(args, kwargs, expected):
    assert css_classes(*args, **kwargs) == expected


def test_negative():
    with pytest.raises(ValueError) as e:
        css_classes(7)
    assert str(e.value) == 'CSS class "7" should be a string'


def test_underscore_kwarg():
    assert css_classes(btn_success=True) == 'btn-success'
    assert css_classes(btn_success=True, underscore_as_dash=True) == 'btn-success'
