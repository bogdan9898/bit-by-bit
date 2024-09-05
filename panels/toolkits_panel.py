from __future__ import annotations
from typing import TYPE_CHECKING, List
import dearpygui.dearpygui as dpg

from consts import PADDING

if TYPE_CHECKING:
	from panels.panel_director import PanelDirector
	from component import Component

class ToolkitsPanel:
	TAG = "components"

	def __init__(self, panel_director: PanelDirector, components_list: List[Component]) -> None:
		self._panel_director: PanelDirector = panel_director
		self._components_list: List[Component] = components_list
		with dpg.window(label="Components", tag=self.TAG, width=200, height=dpg.get_viewport_client_height() / 2 - PADDING * 1.5, no_move=True, no_resize=True, no_close=True):
			# dpg.add_listbox([str(x) for x in components_list], callback=self._on_click, user_data=[1,2])
			for el in components_list:
				with dpg.group(horizontal=True):
					dpg.add_button(label="+", user_data=el, callback=self._on_click)
					dpg.add_text(str(el))

	def _on_click(self, _sender, _app_data, user_data):
		self._panel_director.editor_panel.create_new_node(user_data)
