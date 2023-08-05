from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Handoff:
	"""Handoff commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("handoff", core, parent)

	def start(self) -> None:
		"""SCPI: CALL:CDMA:SIGNaling<Instance>:HANDoff:STARt \n
		Snippet: driver.call.handoff.start() \n
		Initiates a handoff to a band class selected via method RsCmwCdma2kSig.Configure.Handoff.bclass. \n
		"""
		self._core.io.write(f'CALL:CDMA:SIGNaling<Instance>:HANDoff:STARt')

	def start_with_opc(self) -> None:
		"""SCPI: CALL:CDMA:SIGNaling<Instance>:HANDoff:STARt \n
		Snippet: driver.call.handoff.start_with_opc() \n
		Initiates a handoff to a band class selected via method RsCmwCdma2kSig.Configure.Handoff.bclass. \n
		Same as start, but waits for the operation to complete before continuing further. Use the RsCmwCdma2kSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'CALL:CDMA:SIGNaling<Instance>:HANDoff:STARt')
