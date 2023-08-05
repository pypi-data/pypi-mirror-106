from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ...Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SfPower:
	"""SfPower commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sfPower", core, parent)

	def read(self) -> float:
		"""SCPI: READ:CDMA:SIGNaling<Instance>:RXQuality:SFPower \n
		Snippet: value: float = driver.rxQuality.sfPower.read() \n
		Returns the serving frequency power at the MS antenna as a result of the pilot strength measurement. \n
		Use RsCmwCdma2kSig.reliability.last_value to read the updated reliability indicator. \n
			:return: serving_frequency_power: Total received power. Range: -100 dBm to 100 dBm , Unit: dBm"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:CDMA:SIGNaling<Instance>:RXQuality:SFPower?', suppressed)
		return Conversions.str_to_float(response)

	def fetch(self) -> float:
		"""SCPI: FETCh:CDMA:SIGNaling<Instance>:RXQuality:SFPower \n
		Snippet: value: float = driver.rxQuality.sfPower.fetch() \n
		Returns the serving frequency power at the MS antenna as a result of the pilot strength measurement. \n
		Use RsCmwCdma2kSig.reliability.last_value to read the updated reliability indicator. \n
			:return: serving_frequency_power: Total received power. Range: -100 dBm to 100 dBm , Unit: dBm"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:CDMA:SIGNaling<Instance>:RXQuality:SFPower?', suppressed)
		return Conversions.str_to_float(response)
