from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Reconfigure:
	"""Reconfigure commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("reconfigure", core, parent)

	def start(self) -> None:
		"""SCPI: CALL:CDMA:SIGNaling<Instance>:REConfigure:STARt \n
		Snippet: driver.call.reconfigure.start() \n
		Activates the settings for the first service option and radio configuration as selected via the following commands:
		method RsCmwCdma2kSig.Configure.Reconfigure.Layer.Soption.first method RsCmwCdma2kSig.Configure.Reconfigure.Layer.rconfig \n
		"""
		self._core.io.write(f'CALL:CDMA:SIGNaling<Instance>:REConfigure:STARt')

	def start_with_opc(self) -> None:
		"""SCPI: CALL:CDMA:SIGNaling<Instance>:REConfigure:STARt \n
		Snippet: driver.call.reconfigure.start_with_opc() \n
		Activates the settings for the first service option and radio configuration as selected via the following commands:
		method RsCmwCdma2kSig.Configure.Reconfigure.Layer.Soption.first method RsCmwCdma2kSig.Configure.Reconfigure.Layer.rconfig \n
		Same as start, but waits for the operation to complete before continuing further. Use the RsCmwCdma2kSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'CALL:CDMA:SIGNaling<Instance>:REConfigure:STARt')
