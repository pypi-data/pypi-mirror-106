# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdInput(Component):
    """An AntdInput component.


Keyword arguments:
- children (a list of or a singular dash component, string or number; optional)
- id (string; optional)
- className (string; optional)
- style (dict; optional)
- addonBefore (string; default '')
- addonAfter (string; default '')
- defaultValue (string; default '')
- placeholder (string; optional)
- value (string; optional)
- n_commits (number; default 0)
- maxLength (number; optional)"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, addonBefore=Component.UNDEFINED, addonAfter=Component.UNDEFINED, defaultValue=Component.UNDEFINED, placeholder=Component.UNDEFINED, value=Component.UNDEFINED, n_commits=Component.UNDEFINED, maxLength=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'style', 'addonBefore', 'addonAfter', 'defaultValue', 'placeholder', 'value', 'n_commits', 'maxLength']
        self._type = 'AntdInput'
        self._namespace = 'feffery_antd_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'style', 'addonBefore', 'addonAfter', 'defaultValue', 'placeholder', 'value', 'n_commits', 'maxLength']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AntdInput, self).__init__(children=children, **args)
