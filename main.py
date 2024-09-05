import dearpygui.dearpygui as dpg

from consts import PADDING
from windows.levels_window import LevelsWindow
from windows.editor_window import EditorWindow
from windows.components_window import ComponentsWindow
from pin import Pin, PinType
from component import Component
from constant_signal import ConstantSignal



# todo: work on making the windows part of a layout in order to make them responsive
# TODO: add loading indicators


# def viewport_resized_cb():
# 	print("ABCD")
# 	dpg.set_item_width(LEVELS_TAG, )
# 	dpg.set_item_height(LEVELS_TAG, )

# 	dpg.set_item_width(EDITOR_TAG, )
# 	dpg.set_item_height(EDITOR_TAG, )



def load_generic_components() -> list[type[Component]]:
	res = []
	# todo: load components from json
	res.extend([ConstantSignal(0), ConstantSignal(1)])
	return res

def main():
	generic_components = load_generic_components()

	dpg.create_context()
	dpg.create_viewport(title='NAND Game', y_pos=500)

	levels_w_instance = LevelsWindow()
	components_w_instance = ComponentsWindow(generic_components)
	editor_w_instance = EditorWindow()

	# dependency injection
	levels_w_instance.inject_components_w_instance(components_w_instance)
	levels_w_instance.inject_editor_w_instance(editor_w_instance)
	components_w_instance.inject_levels_w_instance(levels_w_instance)
	components_w_instance.inject_editor_w_instance(editor_w_instance)
	editor_w_instance.inject_levels_w_instance(levels_w_instance)
	editor_w_instance.inject_components_w_instance(components_w_instance)

	dpg.setup_dearpygui()
	dpg.show_viewport(maximized=False)
	# dpg.set_viewport_resize_callback(viewport_resized_cb)

	dpg.set_item_pos(levels_w_instance.TAG, pos=[PADDING, PADDING])
	dpg.set_item_pos(components_w_instance.TAG, pos=[PADDING, dpg.get_viewport_client_height() / 2 + PADDING / 2])
	dpg.set_item_pos(editor_w_instance.TAG, pos=[PADDING * 2 + dpg.get_item_width(levels_w_instance.TAG), PADDING])

	dpg.start_dearpygui()
	dpg.destroy_context()

if __name__ == "__main__":
	main()
