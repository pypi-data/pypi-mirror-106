from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Blanked:
	"""Blanked commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("blanked", core, parent)

	# noinspection PyTypeChecker
	class PercentStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Forward: int: Percentage of blanked frames in F-FCH Range: 0 to 100, Unit: %
			- Reverse: int: Percentage of blanked frames in R-FCH Range: 0 to 100, Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_int('Forward'),
			ArgStruct.scalar_int('Reverse')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Forward: int = None
			self.Reverse: int = None

	def get_percent(self) -> PercentStruct:
		"""SCPI: SENSe:CDMA:SIGNaling<Instance>:RXQuality:SPEech:BLANked:PERCent \n
		Snippet: value: PercentStruct = driver.sense.rxQuality.speech.blanked.get_percent() \n
		Displays the speech activity counters since the last reset statistics. \n
			:return: structure: for return value, see the help for PercentStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:CDMA:SIGNaling<Instance>:RXQuality:SPEech:BLANked:PERCent?', self.__class__.PercentStruct())

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Forward: int: Number of blanked frames in F-FCH Range: 0 to 2.112345678E+9, Unit: frames
			- Reverse: int: Number of blanked frames in R-FCH Range: 0 to 2.112345678E+9, Unit: frames"""
		__meta_args_list = [
			ArgStruct.scalar_int('Forward'),
			ArgStruct.scalar_int('Reverse')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Forward: int = None
			self.Reverse: int = None

	def get_value(self) -> ValueStruct:
		"""SCPI: SENSe:CDMA:SIGNaling<Instance>:RXQuality:SPEech:BLANked \n
		Snippet: value: ValueStruct = driver.sense.rxQuality.speech.blanked.get_value() \n
		Displays the speech activity counters since the last reset statistics. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:CDMA:SIGNaling<Instance>:RXQuality:SPEech:BLANked?', self.__class__.ValueStruct())
