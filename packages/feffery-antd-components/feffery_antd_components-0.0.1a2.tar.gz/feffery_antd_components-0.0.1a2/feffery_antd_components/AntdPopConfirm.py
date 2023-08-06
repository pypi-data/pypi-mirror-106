# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdPopConfirm(Component):
    """An AntdPopConfirm component.


Keyword arguments:
- children (a list of or a singular dash component, string or number; optional)
- id (string; optional)
- className (string; optional)
- style (dict; optional)
- last_confirm_datetime (string; optional)
- last_cancel_datetime (string; optional)
- placement (string; default 'top')"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, last_confirm_datetime=Component.UNDEFINED, last_cancel_datetime=Component.UNDEFINED, placement=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'style', 'last_confirm_datetime', 'last_cancel_datetime', 'placement']
        self._type = 'AntdPopConfirm'
        self._namespace = 'feffery_antd_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'style', 'last_confirm_datetime', 'last_cancel_datetime', 'placement']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AntdPopConfirm, self).__init__(children=children, **args)
