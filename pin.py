from enum import Enum, auto

class PinType(Enum):
	INPUT = auto()
	OUTPUT = auto()

class Pin():
	def __init__(self, pin_type: PinType, value: bool=False) -> None:
		self._pin_type = pin_type
		self._value = value

	def __str__(self) -> str:
		return f'Pin'

	def __repr__(self) -> str:
		return f'Pin [{"IN" if self.is_input() else "OUT"}]'

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

	def is_input(self) -> bool:
		return self._pin_type == PinType.INPUT

	def is_output(self) -> bool:
		return not self.is_in()
