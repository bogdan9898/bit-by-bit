from __future__ import annotations
from typing import TYPE_CHECKING
import dearpygui.dearpygui as dpg

from consts import PADDING

if TYPE_CHECKING:
	from panels.panel_director import PanelDirector

class LevelSelectorPanel:
	TAG = "levels"

	def __init__(self, panel_director: PanelDirector) -> None:
		self._panel_director: PanelDirector = panel_director
		with dpg.window(label="Levels", tag=self.TAG, width=200, height=dpg.get_viewport_client_height() / 2 - PADDING * 1.5, no_move=True, no_resize=True, no_close=True):
			dpg.add_text("Select level")
			items = (dpg.add_selectable(label=x) for x in ['Level 1', 'Level 2', 'W.I.P.', '...'])
			for item in items:
				dpg.configure_item(item, callback=self._on_click, user_data=items)

	def _on_click(self, sender, app_data, user_data):
		print(f'{sender=} {app_data=} {user_data=}')
		# for item in user_data:
			# if item != sender:
				# dpg.set_value(item, False)
			# dpg.add_button(label="Save")
			# dpg.add_input_text(label="string", default_value="Quick brown fox")
			# dpg.add_slider_float(label="float", default_value=0.273, max_value=1)
