from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Imin:
	"""Imin commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("imin", core, parent)

	def get_user(self) -> str:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:MSETtings:IMIN:USER \n
		Snippet: value: str = driver.configure.network.msettings.imin.get_user() \n
		No command help available \n
			:return: min_imsi_user: No help available
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:MSETtings:IMIN:USER?')
		return trim_str_response(response)

	def set_user(self, min_imsi_user: str) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:MSETtings:IMIN:USER \n
		Snippet: driver.configure.network.msettings.imin.set_user(min_imsi_user = '1') \n
		No command help available \n
			:param min_imsi_user: No help available
		"""
		param = Conversions.value_to_quoted_str(min_imsi_user)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:MSETtings:IMIN:USER {param}')
