class ConstPinException(Exception):
	def __init__(self, *args, **kwargs) -> None:
		super().__init__("Constant pins are readonly")
