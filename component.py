from abc import ABCMeta, abstractmethod

from pin import Pin, PinType	

class Component(metaclass=ABCMeta):
	def __init__(self, name: str, in_pins_count: int, out_pins_counts: int) -> None:
		self._name: str = name
		self._inputs: list[Pin] = [Pin(pin_type=PinType.INPUT) for _ in range(in_pins_count)]
		self._outputs: list[Pin] = [Pin(pin_type=PinType.OUTPUT) for _ in range(out_pins_counts)]
		# TODO: add a list of components

	def __str__(self) -> str:
		return f'{self.name}'

	def __repr__(self) -> str:
		return f'Component(name={self._name}, in={self._inputs}, out={self._outputs})'

	@property
	def inputs(self) -> list[Pin]:
		return self._inputs

	@property
	def outputs(self) -> list[Pin]:
		return self._outputs

	@property
	def name(self) -> str:
		return self._name

	@name.setter
	def name(self, name: str) -> None:
		self._name = name

	# @property
	# def generic_name(self) -> str:
	# 	return self._generic_name

	@abstractmethod
	def compute(self) -> None:
		pass

	@abstractmethod
	def render(self) -> None:
		pass
