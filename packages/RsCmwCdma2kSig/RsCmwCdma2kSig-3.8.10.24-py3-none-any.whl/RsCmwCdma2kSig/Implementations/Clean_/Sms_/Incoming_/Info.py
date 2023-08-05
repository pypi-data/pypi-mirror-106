from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Info:
	"""Info commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("info", core, parent)

	def set(self) -> None:
		"""SCPI: CLEan:CDMA:SIGNaling<Instance>:SMS:INComing:INFO \n
		Snippet: driver.clean.sms.incoming.info.set() \n
		Deletes the last received SMS. \n
		"""
		self._core.io.write(f'CLEan:CDMA:SIGNaling<Instance>:SMS:INComing:INFO')

	def set_with_opc(self) -> None:
		"""SCPI: CLEan:CDMA:SIGNaling<Instance>:SMS:INComing:INFO \n
		Snippet: driver.clean.sms.incoming.info.set_with_opc() \n
		Deletes the last received SMS. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwCdma2kSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'CLEan:CDMA:SIGNaling<Instance>:SMS:INComing:INFO')
