from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("state", core, parent)

	# noinspection PyTypeChecker
	def fetch(self) -> enums.CsState:
		"""SCPI: FETCh:CDMA:SIGNaling<Instance>:SOPTion<So>:STATe \n
		Snippet: value: enums.CsState = driver.soption.state.fetch() \n
		Returns the connection state of a CDMA2000 connection. Use method RsCmwCdma2kSig.Call.Soption.action to initiate a
		transition between different connection states. The state changes to ON when the signaling generator is started (method
		RsCmwCdma2kSig.Source.State.value ON) . To make sure that a CDMA2000 signal is available, query the state: method
		RsCmwCdma2kSig.Source.State.all must return ON, ADJ. \n
			:return: cs_state: OFF | ON | IDLE | REGistered | PAGing | ALERting | CONNected Connection state. For details, refer to 'Connection States'."""
		response = self._core.io.query_str(f'FETCh:CDMA:SIGNaling<Instance>:SOPTion1:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.CsState)
