import dearpygui.dearpygui as dpg

from component import Component
from windows.editor_window import EditorWindow

class ConstantSignal(Component):
	def __init__(self, value: bool=False) -> None:
		super().__init__(name='Const Signal', in_pins_count=0, out_pins_counts=1)
		self.outputs[0].value = value

	def __str__(self) -> str:
		return f'{self.name} [{self.outputs[0].value}]'

	@property
	def value(self) -> bool:
		return self.outputs[0].value

	def compute(self) -> None:
		pass

	def render(self) -> None:
		with dpg.node(label=self.name, parent=EditorWindow.NODE_EDITOR_TAG):
			with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_TriangleFilled):
				dpg.add_text(self.value)
