# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdBreadCrumb(Component):
    """An AntdBreadCrumb component.


Keyword arguments:
- id (string; optional)
- className (string; optional)
- style (dict; optional)
- render_home_icon (boolean; default True)
- urls (dict; optional): urls has the following type: list of dicts containing keys 'href', 'href_text', 'menu_item'.
Those keys have the following types:
  - href (string; required)
  - href_text (string; required)
  - menu_item (dict; optional): menu_item has the following type: list of dicts containing keys 'menu_item_href', 'menu_item_href_text'.
Those keys have the following types:
  - menu_item_href (string; optional)
  - menu_item_href_text (string; optional)
- separator (string; default '/')
- loading_state (dict; optional): Object that holds the loading state object coming from dash-renderer. loading_state has the following type: dict containing keys 'is_loading', 'prop_name', 'component_name'.
Those keys have the following types:
  - is_loading (boolean; optional): Determines if the component is loading or not
  - prop_name (string; optional): Holds which property is loading
  - component_name (string; optional): Holds the name of the component that is loading"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, render_home_icon=Component.UNDEFINED, urls=Component.UNDEFINED, separator=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'style', 'render_home_icon', 'urls', 'separator', 'loading_state']
        self._type = 'AntdBreadCrumb'
        self._namespace = 'feffery_antd_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'style', 'render_home_icon', 'urls', 'separator', 'loading_state']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AntdBreadCrumb, self).__init__(**args)
