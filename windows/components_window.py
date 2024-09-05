from typing import List
import dearpygui.dearpygui as dpg

from consts import PADDING
from component import Component

class ComponentsWindow:
	TAG = "components"

	def __init__(self, components_list: List[Component]) -> None:
		with dpg.window(label="Components", tag=self.TAG, width=200, height=dpg.get_viewport_client_height() / 2 - PADDING * 1.5, no_move=True, no_resize=True, no_close=True):
			# dpg.add_listbox([str(x) for x in components_list], callback=self._on_click, user_data=[1,2])
			for el in components_list:
				with dpg.group(horizontal=True):
					dpg.add_button(label="+", user_data=el, callback=self._on_click)
					dpg.add_text(str(el))

	def _on_click(self, _sender, _app_data, user_data):
		self._editor_w_instance.create_new_node(user_data)

	def inject_levels_w_instance(self, levels_w_instance) -> None:
		self._levels_w_instance = levels_w_instance

	def inject_editor_w_instance(self, editor_w_instance) -> None:
		self._editor_w_instance = editor_w_instance
