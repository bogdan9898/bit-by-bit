from __future__ import annotations
from typing import List

from pin import Pin, PinType	

class Component():
	def __init__(self, name: str, in_pins_count: int, out_pins_counts: int) -> None:
		self._name: str = name
		self._inputs: List[Pin] = [Pin(pin_type=PinType.INPUT) for _ in range(in_pins_count)]
		self._outputs: List[Pin] = [Pin(pin_type=PinType.OUTPUT) for _ in range(out_pins_counts)]
		self._next_components: List[Component] = list()

	def __str__(self) -> str:
		return f'{self.name}'

	def __repr__(self) -> str:
		return f'Component(name={self._name}, in={self._inputs}, out={self._outputs}, next_component={self._next_component})'

	@property
	def inputs(self) -> List[Pin]:
		return self._inputs

	@property
	def outputs(self) -> List[Pin]:
		return self._outputs

	@property
	def name(self) -> str:
		return self._name

	@name.setter
	def name(self, name: str) -> None:
		self._name = name

	@property
	def next_components(self) -> List[Component]:
		return self._next_components

	def compute(self) -> None:
		# TODO: execution needs to happen in a breadth first way
		pass

	def render(self) -> None:
		pass
