# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdRadioGroup(Component):
    """An AntdRadioGroup component.


Keyword arguments:
- children (a list of or a singular dash component, string or number; optional)
- id (string; optional)
- className (string; optional)
- style (dict; optional)
- options (dict; optional): options has the following type: list of dicts containing keys 'label', 'value'.
Those keys have the following types:
  - label (string; optional)
  - value (string; optional)
- value (number | string; optional)"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, options=Component.UNDEFINED, value=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'style', 'options', 'value']
        self._type = 'AntdRadioGroup'
        self._namespace = 'feffery_antd_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'style', 'options', 'value']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AntdRadioGroup, self).__init__(children=children, **args)
