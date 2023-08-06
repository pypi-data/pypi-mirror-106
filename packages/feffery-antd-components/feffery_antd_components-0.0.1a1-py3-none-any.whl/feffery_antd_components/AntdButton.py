# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdButton(Component):
    """An AntdButton component.


Keyword arguments:
- children (a list of or a singular dash component, string or number; optional)
- id (string; optional)
- className (string; optional)
- style (dict; optional)
- type (string; default 'default')
- href (string; optional)
- target (string; optional)
- block (boolean; default False)
- danger (boolean; default False)
- disabled (boolean; default False)
- shape (string; optional)
- n_clicks (number; default 0)"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, type=Component.UNDEFINED, href=Component.UNDEFINED, target=Component.UNDEFINED, block=Component.UNDEFINED, danger=Component.UNDEFINED, disabled=Component.UNDEFINED, shape=Component.UNDEFINED, n_clicks=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'style', 'type', 'href', 'target', 'block', 'danger', 'disabled', 'shape', 'n_clicks']
        self._type = 'AntdButton'
        self._namespace = 'feffery_antd_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'style', 'type', 'href', 'target', 'block', 'danger', 'disabled', 'shape', 'n_clicks']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AntdButton, self).__init__(children=children, **args)
