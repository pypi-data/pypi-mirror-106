from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FersCh:
	"""FersCh commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("fersCh", core, parent)

	def get_mfer(self) -> float:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RXQuality:LIMit:FERSch:MFER \n
		Snippet: value: float = driver.configure.rxQuality.limit.fersCh.get_mfer() \n
		Defines the maximum FER allowed before indicating an error. \n
			:return: max_fersh_0: Range: 0 % to 50 %, Unit: %
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RXQuality:LIMit:FERSch:MFER?')
		return Conversions.str_to_float(response)

	def set_mfer(self, max_fersh_0: float) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RXQuality:LIMit:FERSch:MFER \n
		Snippet: driver.configure.rxQuality.limit.fersCh.set_mfer(max_fersh_0 = 1.0) \n
		Defines the maximum FER allowed before indicating an error. \n
			:param max_fersh_0: Range: 0 % to 50 %, Unit: %
		"""
		param = Conversions.decimal_value_to_str(max_fersh_0)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RXQuality:LIMit:FERSch:MFER {param}')

	def get_clevel(self) -> float:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RXQuality:LIMit:FERSch:CLEVel \n
		Snippet: value: float = driver.configure.rxQuality.limit.fersCh.get_clevel() \n
		Defines the minimum confidence level of the FER that must be met without indicating an error. \n
			:return: min_confide_level: Range: 85 % to 99.99 %, Unit: %
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RXQuality:LIMit:FERSch:CLEVel?')
		return Conversions.str_to_float(response)

	def set_clevel(self, min_confide_level: float) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RXQuality:LIMit:FERSch:CLEVel \n
		Snippet: driver.configure.rxQuality.limit.fersCh.set_clevel(min_confide_level = 1.0) \n
		Defines the minimum confidence level of the FER that must be met without indicating an error. \n
			:param min_confide_level: Range: 85 % to 99.99 %, Unit: %
		"""
		param = Conversions.decimal_value_to_str(min_confide_level)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RXQuality:LIMit:FERSch:CLEVel {param}')
