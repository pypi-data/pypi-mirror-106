from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pch:
	"""Pch commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pch", core, parent)

	def get_channel(self) -> int:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:LAYer:PCH:CHANnel \n
		Snippet: value: int = driver.configure.layer.pch.get_channel() \n
		Specifies the Walsh code of PCH. \n
			:return: channel: Range: 1 to 7
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:LAYer:PCH:CHANnel?')
		return Conversions.str_to_int(response)

	def set_channel(self, channel: int) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:LAYer:PCH:CHANnel \n
		Snippet: driver.configure.layer.pch.set_channel(channel = 1) \n
		Specifies the Walsh code of PCH. \n
			:param channel: Range: 1 to 7
		"""
		param = Conversions.decimal_value_to_str(channel)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:LAYer:PCH:CHANnel {param}')

	def get_level(self) -> float:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:LAYer:PCH:LEVel \n
		Snippet: value: float = driver.configure.layer.pch.get_level() \n
		Queries the level of paging channel (PCH) relative to the 'CDMA Power'. \n
			:return: level: Range: -20 dB to -1 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:LAYer:PCH:LEVel?')
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	def get_rate(self) -> enums.PagingChannelRate:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:LAYer:PCH:RATE \n
		Snippet: value: enums.PagingChannelRate = driver.configure.layer.pch.get_rate() \n
		Queries the rate of paging channel (PCH) . \n
			:return: rate: R4K8 | R9K6 4800 bit/s, 9600 bit/s Unit: bit/s
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:LAYer:PCH:RATE?')
		return Conversions.str_to_scalar_enum(response, enums.PagingChannelRate)
