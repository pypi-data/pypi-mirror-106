from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FerfCh:
	"""FerfCh commands group definition. 4 total commands, 1 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ferfCh", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .FerfCh_.State import State
			self._state = State(self._core, self._base)
		return self._state

	def initiate(self) -> None:
		"""SCPI: INITiate:CDMA:SIGNaling<Instance>:RXQuality:TDATa:FERFch \n
		Snippet: driver.rxQuality.tdata.ferfCh.initiate() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'INITiate:CDMA:SIGNaling<Instance>:RXQuality:TDATa:FERFch')

	def initiate_with_opc(self) -> None:
		"""SCPI: INITiate:CDMA:SIGNaling<Instance>:RXQuality:TDATa:FERFch \n
		Snippet: driver.rxQuality.tdata.ferfCh.initiate_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCmwCdma2kSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'INITiate:CDMA:SIGNaling<Instance>:RXQuality:TDATa:FERFch')

	def stop(self) -> None:
		"""SCPI: STOP:CDMA:SIGNaling<Instance>:RXQuality:TDATa:FERFch \n
		Snippet: driver.rxQuality.tdata.ferfCh.stop() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'STOP:CDMA:SIGNaling<Instance>:RXQuality:TDATa:FERFch')

	def stop_with_opc(self) -> None:
		"""SCPI: STOP:CDMA:SIGNaling<Instance>:RXQuality:TDATa:FERFch \n
		Snippet: driver.rxQuality.tdata.ferfCh.stop_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCmwCdma2kSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'STOP:CDMA:SIGNaling<Instance>:RXQuality:TDATa:FERFch')

	def abort(self) -> None:
		"""SCPI: ABORt:CDMA:SIGNaling<Instance>:RXQuality:TDATa:FERFch \n
		Snippet: driver.rxQuality.tdata.ferfCh.abort() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'ABORt:CDMA:SIGNaling<Instance>:RXQuality:TDATa:FERFch')

	def abort_with_opc(self) -> None:
		"""SCPI: ABORt:CDMA:SIGNaling<Instance>:RXQuality:TDATa:FERFch \n
		Snippet: driver.rxQuality.tdata.ferfCh.abort_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCmwCdma2kSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'ABORt:CDMA:SIGNaling<Instance>:RXQuality:TDATa:FERFch')

	def clone(self) -> 'FerfCh':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FerfCh(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
