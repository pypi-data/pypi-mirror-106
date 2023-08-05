from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MsInfo:
	"""MsInfo commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("msInfo", core, parent)

	def get_esn(self) -> float:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:TEST:MSINfo:ESN \n
		Snippet: value: float = driver.configure.test.msInfo.get_esn() \n
		Sets the hard-coded electronic serial number of the connected MS. \n
			:return: esn: Range: 0 to 4.294967296E+9
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:TEST:MSINfo:ESN?')
		return Conversions.str_to_float(response)

	def set_esn(self, esn: float) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:TEST:MSINfo:ESN \n
		Snippet: driver.configure.test.msInfo.set_esn(esn = 1.0) \n
		Sets the hard-coded electronic serial number of the connected MS. \n
			:param esn: Range: 0 to 4.294967296E+9
		"""
		param = Conversions.decimal_value_to_str(esn)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:TEST:MSINfo:ESN {param}')

	def get_meid(self) -> float:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:TEST:MSINfo:MEID \n
		Snippet: value: float = driver.configure.test.msInfo.get_meid() \n
		Sets the mobile equipment identifier of the connected MS. \n
			:return: meid: Range: 0 to 9.22337203685477E+18
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:TEST:MSINfo:MEID?')
		return Conversions.str_to_float(response)

	def set_meid(self, meid: float) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:TEST:MSINfo:MEID \n
		Snippet: driver.configure.test.msInfo.set_meid(meid = 1.0) \n
		Sets the mobile equipment identifier of the connected MS. \n
			:param meid: Range: 0 to 9.22337203685477E+18
		"""
		param = Conversions.decimal_value_to_str(meid)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:TEST:MSINfo:MEID {param}')
