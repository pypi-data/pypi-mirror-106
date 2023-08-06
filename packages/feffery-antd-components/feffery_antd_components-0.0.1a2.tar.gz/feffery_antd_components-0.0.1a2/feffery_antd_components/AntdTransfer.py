# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdTransfer(Component):
    """An AntdTransfer component.


Keyword arguments:
- children (a list of or a singular dash component, string or number; optional)
- id (string; optional)
- className (string; optional)
- style (dict; optional)
- targetKeys (list; optional)
- moveDirection (string; optional)
- moveKeys (list; optional)
- pagination (dict; default False): pagination has the following type: boolean | dict containing keys 'pageSize'.
Those keys have the following types:
  - pageSize (number; optional)
- operations (list; optional)
- showSearch (boolean; default False)
- showSelectAll (boolean; default True)
- titles (list; default ['Source', 'Target'])
- listStyle (dict; optional)"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, targetKeys=Component.UNDEFINED, moveDirection=Component.UNDEFINED, moveKeys=Component.UNDEFINED, pagination=Component.UNDEFINED, operations=Component.UNDEFINED, showSearch=Component.UNDEFINED, showSelectAll=Component.UNDEFINED, titles=Component.UNDEFINED, listStyle=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'style', 'targetKeys', 'moveDirection', 'moveKeys', 'pagination', 'operations', 'showSearch', 'showSelectAll', 'titles', 'listStyle']
        self._type = 'AntdTransfer'
        self._namespace = 'feffery_antd_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'style', 'targetKeys', 'moveDirection', 'moveKeys', 'pagination', 'operations', 'showSearch', 'showSelectAll', 'titles', 'listStyle']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AntdTransfer, self).__init__(children=children, **args)
