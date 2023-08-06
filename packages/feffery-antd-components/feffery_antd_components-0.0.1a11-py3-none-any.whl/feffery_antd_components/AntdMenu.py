# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdMenu(Component):
    """An AntdMenu component.


Keyword arguments:
- id (string; optional)
- className (string; optional)
- style (dict; optional)
- menu_tree_structure (list; optional)
- current_key (string; optional)
- default_selected_keys (list of strings; optional)
- mode (string; default 'inline')"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, menu_tree_structure=Component.UNDEFINED, current_key=Component.UNDEFINED, default_selected_keys=Component.UNDEFINED, mode=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'style', 'menu_tree_structure', 'current_key', 'default_selected_keys', 'mode']
        self._type = 'AntdMenu'
        self._namespace = 'feffery_antd_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'style', 'menu_tree_structure', 'current_key', 'default_selected_keys', 'mode']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AntdMenu, self).__init__(**args)
