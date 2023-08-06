# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdTree(Component):
    """An AntdTree component.


Keyword arguments:
- id (string; optional)
- className (string; optional)
- style (dict; optional)
- treeData (list; required)
- showIcon (boolean; default True)
- checkable (boolean; default False)
- defaultCheckedKeys (list; optional)
- defaultExpandAll (boolean; default False)
- defaultExpandedKeys (list; optional)
- defaultExpandParent (boolean; default False)
- defaultSelectedKeys (list; optional)
- multiple (boolean; default False)
- selectable (boolean; default True)
- showLine (a value equal to: PropTypes.bool, PropTypes.exact({ showLeafIcon: PropTypes.bool }); default { showLeafIcon: false })
- selectedKeys (list; optional)
- checkedKeys (list; optional)
- height (number; optional)"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, treeData=Component.REQUIRED, showIcon=Component.UNDEFINED, checkable=Component.UNDEFINED, defaultCheckedKeys=Component.UNDEFINED, defaultExpandAll=Component.UNDEFINED, defaultExpandedKeys=Component.UNDEFINED, defaultExpandParent=Component.UNDEFINED, defaultSelectedKeys=Component.UNDEFINED, multiple=Component.UNDEFINED, selectable=Component.UNDEFINED, showLine=Component.UNDEFINED, selectedKeys=Component.UNDEFINED, checkedKeys=Component.UNDEFINED, height=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'style', 'treeData', 'showIcon', 'checkable', 'defaultCheckedKeys', 'defaultExpandAll', 'defaultExpandedKeys', 'defaultExpandParent', 'defaultSelectedKeys', 'multiple', 'selectable', 'showLine', 'selectedKeys', 'checkedKeys', 'height']
        self._type = 'AntdTree'
        self._namespace = 'feffery_antd_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'style', 'treeData', 'showIcon', 'checkable', 'defaultCheckedKeys', 'defaultExpandAll', 'defaultExpandedKeys', 'defaultExpandParent', 'defaultSelectedKeys', 'multiple', 'selectable', 'showLine', 'selectedKeys', 'checkedKeys', 'height']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['treeData']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AntdTree, self).__init__(**args)
