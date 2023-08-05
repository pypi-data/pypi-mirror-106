from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FerfCh:
	"""FerfCh commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ferfCh", core, parent)

	def get_mfer(self) -> float:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RXQuality:LIMit:FERFch:MFER \n
		Snippet: value: float = driver.configure.rxQuality.limit.ferfCh.get_mfer() \n
		Defines the maximum FER allowed before indicating an error. \n
			:return: max_ferf_ch: No help available
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RXQuality:LIMit:FERFch:MFER?')
		return Conversions.str_to_float(response)

	def set_mfer(self, max_ferf_ch: float) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RXQuality:LIMit:FERFch:MFER \n
		Snippet: driver.configure.rxQuality.limit.ferfCh.set_mfer(max_ferf_ch = 1.0) \n
		Defines the maximum FER allowed before indicating an error. \n
			:param max_ferf_ch: Range: 0 % to 50 %, Unit: %
		"""
		param = Conversions.decimal_value_to_str(max_ferf_ch)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RXQuality:LIMit:FERFch:MFER {param}')

	def get_clevel(self) -> float:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RXQuality:LIMit:FERFch:CLEVel \n
		Snippet: value: float = driver.configure.rxQuality.limit.ferfCh.get_clevel() \n
		Defines the minimum confidence level of the FER that must be met without indicating an error. \n
			:return: min_confide_level: Range: 85 % to 99.99 %, Unit: %
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RXQuality:LIMit:FERFch:CLEVel?')
		return Conversions.str_to_float(response)

	def set_clevel(self, min_confide_level: float) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RXQuality:LIMit:FERFch:CLEVel \n
		Snippet: driver.configure.rxQuality.limit.ferfCh.set_clevel(min_confide_level = 1.0) \n
		Defines the minimum confidence level of the FER that must be met without indicating an error. \n
			:param min_confide_level: Range: 85 % to 99.99 %, Unit: %
		"""
		param = Conversions.decimal_value_to_str(min_confide_level)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RXQuality:LIMit:FERFch:CLEVel {param}')
