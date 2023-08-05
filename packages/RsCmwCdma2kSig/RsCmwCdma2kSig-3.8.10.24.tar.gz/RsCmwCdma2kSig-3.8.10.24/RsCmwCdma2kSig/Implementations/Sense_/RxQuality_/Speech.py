from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Speech:
	"""Speech commands group definition. 12 total commands, 5 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("speech", core, parent)

	@property
	def blanked(self):
		"""blanked commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_blanked'):
			from .Speech_.Blanked import Blanked
			self._blanked = Blanked(self._core, self._base)
		return self._blanked

	@property
	def eight(self):
		"""eight commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_eight'):
			from .Speech_.Eight import Eight
			self._eight = Eight(self._core, self._base)
		return self._eight

	@property
	def quarter(self):
		"""quarter commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_quarter'):
			from .Speech_.Quarter import Quarter
			self._quarter = Quarter(self._core, self._base)
		return self._quarter

	@property
	def half(self):
		"""half commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_half'):
			from .Speech_.Half import Half
			self._half = Half(self._core, self._base)
		return self._half

	@property
	def full(self):
		"""full commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_full'):
			from .Speech_.Full import Full
			self._full = Full(self._core, self._base)
		return self._full

	# noinspection PyTypeChecker
	class ThroughputStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Forward: int: Throughput in F-FCH Range: 0 to 2.112345678E+9, Unit: bit/s
			- Reverse: float: Throughput in R-FCH Range: 0 to 2.112345678E+9, Unit: bit/s"""
		__meta_args_list = [
			ArgStruct.scalar_int('Forward'),
			ArgStruct.scalar_float('Reverse')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Forward: int = None
			self.Reverse: float = None

	def get_throughput(self) -> ThroughputStruct:
		"""SCPI: SENSe:CDMA:SIGNaling<Instance>:RXQuality:SPEech:THRoughput \n
		Snippet: value: ThroughputStruct = driver.sense.rxQuality.speech.get_throughput() \n
		Displays the speech activity throughput since the last reset statistics. \n
			:return: structure: for return value, see the help for ThroughputStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:CDMA:SIGNaling<Instance>:RXQuality:SPEech:THRoughput?', self.__class__.ThroughputStruct())

	def get_state(self) -> str:
		"""SCPI: SENSe:CDMA:SIGNaling<Instance>:RXQuality:SPEech:STATe \n
		Snippet: value: str = driver.sense.rxQuality.speech.get_state() \n
		Returns a string containing status information about the measurement. \n
			:return: status: See table below.
		"""
		response = self._core.io.query_str('SENSe:CDMA:SIGNaling<Instance>:RXQuality:SPEech:STATe?')
		return trim_str_response(response)

	def clone(self) -> 'Speech':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Speech(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
