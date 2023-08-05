from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Service:
	"""Service commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("service", core, parent)

	def get_category(self) -> str:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SMS:BROadcast:SERVice:CATegory \n
		Snippet: value: str = driver.configure.sms.broadcast.service.get_category() \n
		Defined in 3GPP2 C.R1001, section 9.3. \n
			:return: category: Standard service category for the whole range except #H1000 to #H10FF: WEA messages and #H8001 to #H803F, #HC001 to #HC03F: proprietary service category Range: #H0 to #HFFFF
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:SMS:BROadcast:SERVice:CATegory?')
		return trim_str_response(response)

	def set_category(self, category: str) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SMS:BROadcast:SERVice:CATegory \n
		Snippet: driver.configure.sms.broadcast.service.set_category(category = r1) \n
		Defined in 3GPP2 C.R1001, section 9.3. \n
			:param category: Standard service category for the whole range except #H1000 to #H10FF: WEA messages and #H8001 to #H803F, #HC001 to #HC03F: proprietary service category Range: #H0 to #HFFFF
		"""
		param = Conversions.value_to_str(category)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:SMS:BROadcast:SERVice:CATegory {param}')
