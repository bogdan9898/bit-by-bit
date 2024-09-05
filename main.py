from curses import panel
from typing import List
import dearpygui.dearpygui as dpg

from consts import PADDING
from panels.panel_director import PanelDirector
from component import Component
from predefined_components.constant_signal import ConstantSignal



# todo: work on making the windows part of a layout in order to make them responsive
# TODO: add loading indicators


# def viewport_resized_cb():
# 	print("ABCD")
# 	dpg.set_item_width(LEVELS_TAG, )
# 	dpg.set_item_height(LEVELS_TAG, )

# 	dpg.set_item_width(EDITOR_TAG, )
# 	dpg.set_item_height(EDITOR_TAG, )



def load_components() -> List[Component]:
	res = []
	# todo: load components from json
	res.extend([ConstantSignal(0), ConstantSignal(1)])
	return res

def main():
	dpg.create_context()
	dpg.create_viewport(title='NAND Game', y_pos=500)

	dpg.setup_dearpygui()
	dpg.show_viewport(maximized=False)
	# dpg.set_viewport_resize_callback(viewport_resized_cb)

	panel_director = PanelDirector(loaded_components=load_components())

	dpg.set_item_pos(panel_director.level_selector_panel.TAG, pos=[PADDING, PADDING])
	dpg.set_item_pos(panel_director.toolkits_panel.TAG, pos=[PADDING, dpg.get_viewport_client_height() / 2 + PADDING / 2])
	dpg.set_item_pos(panel_director.editor_panel.TAG, pos=[PADDING * 2 + dpg.get_item_width(panel_director.level_selector_panel.TAG), PADDING])

	dpg.start_dearpygui()
	dpg.destroy_context()

if __name__ == "__main__":
	main()
