import pytest

from configura.plugins.filter_by_field import FilterByField


def test_filter_by_field_filters_numeric_values():
    plugin = FilterByField(key_name="value", operator=">=", value=20)

    data = [
        {"id": 1, "value": 10},
        {"id": 2, "value": 20},
        {"id": 3, "value": 25},
    ]

    assert plugin.process(data) == [
        {"id": 2, "value": 20},
        {"id": 3, "value": 25},
    ]


def test_filter_by_field_handles_nested_keys_and_type_errors():
    plugin = FilterByField(
        key_name="payload.temp_c",
        operator=">",
        value=18,
        fail_on_type_error=False,
    )

    data = [
        {"payload": {"temp_c": 17}},
        {"payload": {"temp_c": 19}},
        {"payload": {"temp_c": "cold"}},
        {},
    ]

    assert plugin.process(data) == [{"payload": {"temp_c": 19}}]

    plugin_fail = FilterByField(
        key_name="payload.temp_c",
        operator=">",
        value=18,
        fail_on_type_error=True,
    )

    with pytest.raises(TypeError):
        plugin_fail.process(data)