# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdTab(Component):
    """An AntdTab component.


Keyword arguments:
- children (a list of or a singular dash component, string or number; optional)
- id (string; optional)
- tab (string; optional)
- key (string; optional)
- disabled (string; optional)
- className (string; optional)
- style (dict; optional)"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, tab=Component.UNDEFINED, key=Component.UNDEFINED, disabled=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'tab', 'key', 'disabled', 'className', 'style']
        self._type = 'AntdTab'
        self._namespace = 'feffery_antd_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'tab', 'key', 'disabled', 'className', 'style']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AntdTab, self).__init__(children=children, **args)
