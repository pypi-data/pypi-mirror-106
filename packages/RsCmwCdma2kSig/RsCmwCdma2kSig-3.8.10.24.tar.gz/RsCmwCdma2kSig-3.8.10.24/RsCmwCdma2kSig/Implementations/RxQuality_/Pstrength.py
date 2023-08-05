from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ...Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pstrength:
	"""Pstrength commands group definition. 7 total commands, 1 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pstrength", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .Pstrength_.State import State
			self._state = State(self._core, self._base)
		return self._state

	def initiate(self) -> None:
		"""SCPI: INITiate:CDMA:SIGNaling<Instance>:RXQuality:PSTRength \n
		Snippet: driver.rxQuality.pstrength.initiate() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'INITiate:CDMA:SIGNaling<Instance>:RXQuality:PSTRength')

	def initiate_with_opc(self) -> None:
		"""SCPI: INITiate:CDMA:SIGNaling<Instance>:RXQuality:PSTRength \n
		Snippet: driver.rxQuality.pstrength.initiate_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCmwCdma2kSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'INITiate:CDMA:SIGNaling<Instance>:RXQuality:PSTRength')

	def stop(self) -> None:
		"""SCPI: STOP:CDMA:SIGNaling<Instance>:RXQuality:PSTRength \n
		Snippet: driver.rxQuality.pstrength.stop() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'STOP:CDMA:SIGNaling<Instance>:RXQuality:PSTRength')

	def stop_with_opc(self) -> None:
		"""SCPI: STOP:CDMA:SIGNaling<Instance>:RXQuality:PSTRength \n
		Snippet: driver.rxQuality.pstrength.stop_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCmwCdma2kSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'STOP:CDMA:SIGNaling<Instance>:RXQuality:PSTRength')

	def abort(self) -> None:
		"""SCPI: ABORt:CDMA:SIGNaling<Instance>:RXQuality:PSTRength \n
		Snippet: driver.rxQuality.pstrength.abort() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'ABORt:CDMA:SIGNaling<Instance>:RXQuality:PSTRength')

	def abort_with_opc(self) -> None:
		"""SCPI: ABORt:CDMA:SIGNaling<Instance>:RXQuality:PSTRength \n
		Snippet: driver.rxQuality.pstrength.abort_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCmwCdma2kSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'ABORt:CDMA:SIGNaling<Instance>:RXQuality:PSTRength')

	def read(self) -> float:
		"""SCPI: READ:CDMA:SIGNaling<Instance>:RXQuality:PSTRength \n
		Snippet: value: float = driver.rxQuality.pstrength.read() \n
		Returns the pilot strength at the MS antenna, as a result of the pilot strength measurement... \n
		Use RsCmwCdma2kSig.reliability.last_value to read the updated reliability indicator. \n
			:return: pilot_strength: The pilot power relative to the total power. Unit: dB"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'READ:CDMA:SIGNaling<Instance>:RXQuality:PSTRength?', suppressed)
		return Conversions.str_to_float(response)

	def fetch(self) -> float:
		"""SCPI: FETCh:CDMA:SIGNaling<Instance>:RXQuality:PSTRength \n
		Snippet: value: float = driver.rxQuality.pstrength.fetch() \n
		Returns the pilot strength at the MS antenna, as a result of the pilot strength measurement... \n
		Use RsCmwCdma2kSig.reliability.last_value to read the updated reliability indicator. \n
			:return: pilot_strength: The pilot power relative to the total power. Unit: dB"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:CDMA:SIGNaling<Instance>:RXQuality:PSTRength?', suppressed)
		return Conversions.str_to_float(response)

	def clone(self) -> 'Pstrength':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pstrength(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
