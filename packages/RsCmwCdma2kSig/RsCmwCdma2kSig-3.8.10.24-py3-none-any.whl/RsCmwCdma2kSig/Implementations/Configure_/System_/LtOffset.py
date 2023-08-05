from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LtOffset:
	"""LtOffset commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ltOffset", core, parent)

	def get_hex(self) -> str:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SYSTem:LTOFfset:HEX \n
		Snippet: value: str = driver.configure.system.ltOffset.get_hex() \n
		Displays time offset from UTC in hexadecimal format according to the local time zone. Local time offset = (sign(h)
		*(abs(h) *60+m) /30) AND ((1UL<<6) -1) \n
			:return: local_time_off_hex: Range: #H00 to #HFF
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:SYSTem:LTOFfset:HEX?')
		return trim_str_response(response)

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Sign: float: MINU | PLUS
			- Hour: int: Range: 0 to 16
			- Minute: int: Range: 0 | 30"""
		__meta_args_list = [
			ArgStruct.scalar_float('Sign'),
			ArgStruct.scalar_int('Hour'),
			ArgStruct.scalar_int('Minute')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Sign: float = None
			self.Hour: int = None
			self.Minute: int = None

	def get_value(self) -> ValueStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SYSTem:LTOFfset \n
		Snippet: value: ValueStruct = driver.configure.system.ltOffset.get_value() \n
		Defines the time offset from UTC according to the local time zone. Possible range is from -16:00 to +15:30 \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:SYSTem:LTOFfset?', self.__class__.ValueStruct())

	def set_value(self, value: ValueStruct) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SYSTem:LTOFfset \n
		Snippet: driver.configure.system.ltOffset.set_value(value = ValueStruct()) \n
		Defines the time offset from UTC according to the local time zone. Possible range is from -16:00 to +15:30 \n
			:param value: see the help for ValueStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:CDMA:SIGNaling<Instance>:SYSTem:LTOFfset', value)
