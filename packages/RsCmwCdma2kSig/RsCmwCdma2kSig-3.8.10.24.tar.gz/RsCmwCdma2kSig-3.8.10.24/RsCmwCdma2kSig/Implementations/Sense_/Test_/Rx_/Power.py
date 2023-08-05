from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("power", core, parent)

	def get_state(self) -> float:
		"""SCPI: SENSe:CDMA:SIGNaling<Instance>:TEST:RX:POWer:STATe \n
		Snippet: value: float = driver.sense.test.rx.power.get_state() \n
		Queries the quality of the RX signal from the connected MS. \n
			:return: state: NAV | LOW | OK | HIGH NAV: no signal from MS detected LOW: the MS power is below the expected range OK: the MS power is in the expected range HIGH: the MS power is above the expected range
		"""
		response = self._core.io.query_str('SENSe:CDMA:SIGNaling<Instance>:TEST:RX:POWer:STATe?')
		return Conversions.str_to_float(response)
