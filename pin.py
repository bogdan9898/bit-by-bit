from __future__ import annotations
from typing import TYPE_CHECKING, List
from enum import Enum, auto

if TYPE_CHECKING:
	from component import Component

class PinType(Enum):
	INPUT = auto()
	OUTPUT = auto()

class Pin():
	def __init__(self, pin_type: PinType, value: bool=False) -> None:
		self._pin_type: PinType = pin_type
		self._value: bool = value
		self._next_components: List[Component] = list()

	def __str__(self) -> str:
		return f'Pin [{"IN" if self.is_input() else "OUT"}]'

	def __repr__(self) -> str:
		return f'Pin (pin_type={self._pin_type}, value={self._value}, next_component={self._next_component})'

	@property
	def pin_type(self) -> PinType:
		return self._pin_type
	
	@pin_type.setter
	def pin_type(self, pin_type: PinType) -> None:
		self._pin_type = pin_type

	@property
	def value(self) -> bool:
		return self._value

	@value.setter
	def value(self, value: bool) -> None:
		self._value = value

	@property
	def next_components(self) -> List[Component]:
		return self._next_components

	def is_input(self) -> bool:
		return self._pin_type == PinType.INPUT

	def is_output(self) -> bool:
		return not self.is_in()
