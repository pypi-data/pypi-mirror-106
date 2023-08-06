# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdSelect(Component):
    """An AntdSelect component.


Keyword arguments:
- children (a list of or a singular dash component, string or number; optional)
- id (string; optional)
- className (string; optional)
- style (dict; optional)
- options (list; required)
- allowClear (boolean; default True)
- mode (string; default '')
- placeholder (string; optional)
- values (string | list of strings; optional)
- defaultValue (string | list of strings; optional)
- showSearch (boolean; default True)
- maxTagCount (number; default 5)
- listHeight (number; default 256)"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, options=Component.REQUIRED, allowClear=Component.UNDEFINED, mode=Component.UNDEFINED, placeholder=Component.UNDEFINED, values=Component.UNDEFINED, defaultValue=Component.UNDEFINED, showSearch=Component.UNDEFINED, maxTagCount=Component.UNDEFINED, listHeight=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'style', 'options', 'allowClear', 'mode', 'placeholder', 'values', 'defaultValue', 'showSearch', 'maxTagCount', 'listHeight']
        self._type = 'AntdSelect'
        self._namespace = 'feffery_antd_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'style', 'options', 'allowClear', 'mode', 'placeholder', 'values', 'defaultValue', 'showSearch', 'maxTagCount', 'listHeight']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['options']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AntdSelect, self).__init__(children=children, **args)
