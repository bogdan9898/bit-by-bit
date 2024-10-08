from __future__ import annotations
from typing import TYPE_CHECKING, List
import dearpygui.dearpygui as dpg

from consts import PADDING

if TYPE_CHECKING:
	from panels.panel_director import PanelDirector
	from component import Component

class EditorPanel:
	TAG = "editor"
	NODE_EDITOR_TAG = "node_editor"

	def __init__(self, panel_director: PanelDirector) -> None:
		self._panel_director: PanelDirector = panel_director
		self._links: List[tuple] = []
		with dpg.window(label="Editor", tag=self.TAG, width=dpg.get_viewport_client_width() - PADDING * 3 - dpg.get_item_width(panel_director.level_selector_panel.TAG), height=dpg.get_viewport_client_height() - PADDING * 2, no_move=True, no_resize=True, no_close=True):
			with dpg.node_editor(tag=self.NODE_EDITOR_TAG, callback=self._link_callback, delink_callback=self._delink_callback):
				with dpg.node(label="Node 1"):
					with dpg.node_attribute(label="Node A1", shape=dpg.mvNode_PinShape_TriangleFilled):
						dpg.add_input_float(label="F1", width=150)

					with dpg.node_attribute(label="Node A2", attribute_type=dpg.mvNode_Attr_Output,):
						dpg.add_input_float(label="F2", width=150)

				with dpg.node(label="Node 2"):
					with dpg.node_attribute(label="Node A3"):
						dpg.add_input_float(label="F3", width=200)

					with dpg.node_attribute(label="Node A4", attribute_type=dpg.mvNode_Attr_Output):
						dpg.add_input_float(label="F4", width=200)

	# callback runs when user attempts to connect attributes
	def _link_callback(self, sender, app_data):
		# app_data -> (link_id1, link_id2)
		print(app_data)
		dpg.add_node_link(app_data[0], app_data[1], parent=sender)

	# callback runs when user attempts to disconnect attributes
	def _delink_callback(self, sender, app_data):
		# app_data -> link_id
		print(f'{sender=} {app_data=}')
		dpg.delete_item(app_data)

	def create_new_node(self, component: Component) -> None:
		component.render()
