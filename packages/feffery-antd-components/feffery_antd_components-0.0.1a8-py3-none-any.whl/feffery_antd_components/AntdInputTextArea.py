# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdInputTextArea(Component):
    """An AntdInputTextArea component.


Keyword arguments:
- children (a list of or a singular dash component, string or number; optional)
- id (string; optional)
- className (string; optional)
- style (dict; optional)
- defaultValue (string; default '')
- placeholder (string; optional)
- value (string; optional)
- maxLength (number; optional)
- showCount (boolean; default True)
- autoSize (dict; default {
    minRows: 5,
    maxRows: 10
}): autoSize has the following type: dict containing keys 'minRows', 'maxRows'.
Those keys have the following types:
  - minRows (number; optional)
  - maxRows (number; optional)
- allowClear (boolean; default True)"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, defaultValue=Component.UNDEFINED, placeholder=Component.UNDEFINED, value=Component.UNDEFINED, maxLength=Component.UNDEFINED, showCount=Component.UNDEFINED, autoSize=Component.UNDEFINED, allowClear=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'style', 'defaultValue', 'placeholder', 'value', 'maxLength', 'showCount', 'autoSize', 'allowClear']
        self._type = 'AntdInputTextArea'
        self._namespace = 'feffery_antd_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'style', 'defaultValue', 'placeholder', 'value', 'maxLength', 'showCount', 'autoSize', 'allowClear']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AntdInputTextArea, self).__init__(children=children, **args)
