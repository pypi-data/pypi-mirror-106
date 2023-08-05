from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rstatistics:
	"""Rstatistics commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rstatistics", core, parent)

	def set(self) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RXQuality:RSTatistics \n
		Snippet: driver.configure.rxQuality.rstatistics.set() \n
		Sets all counters of the RX measurements to zero. \n
		"""
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RXQuality:RSTatistics')

	def set_with_opc(self) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RXQuality:RSTatistics \n
		Snippet: driver.configure.rxQuality.rstatistics.set_with_opc() \n
		Sets all counters of the RX measurements to zero. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwCdma2kSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'CONFigure:CDMA:SIGNaling<Instance>:RXQuality:RSTatistics')
