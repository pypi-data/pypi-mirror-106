from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Qpch:
	"""Qpch commands group definition. 4 total commands, 1 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("qpch", core, parent)

	@property
	def ibit(self):
		"""ibit commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ibit'):
			from .Qpch_.Ibit import Ibit
			self._ibit = Ibit(self._core, self._base)
		return self._ibit

	def get_channel(self) -> int:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:LAYer:QPCH:CHANnel \n
		Snippet: value: int = driver.configure.layer.qpch.get_channel() \n
		Queries the Walsh code of QPCH. \n
			:return: channel: Range: 1 to 128
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:LAYer:QPCH:CHANnel?')
		return Conversions.str_to_int(response)

	def get_level(self) -> float:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:LAYer:QPCH:LEVel \n
		Snippet: value: float = driver.configure.layer.qpch.get_level() \n
		Queries the level of quick paging channel (QPCH) relative to the 'CDMA Power'. \n
			:return: level: Range: -20 dB to -1 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:LAYer:QPCH:LEVel?')
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	def get_rate(self) -> enums.PagingChannelRate:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:LAYer:QPCH:RATE \n
		Snippet: value: enums.PagingChannelRate = driver.configure.layer.qpch.get_rate() \n
		Specifies the rate of quick paging channel (QPCH) . \n
			:return: rate: R4K8 | R9K6 4800 bit/s, 9600 bit/s Unit: bit/s
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:LAYer:QPCH:RATE?')
		return Conversions.str_to_scalar_enum(response, enums.PagingChannelRate)

	def set_rate(self, rate: enums.PagingChannelRate) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:LAYer:QPCH:RATE \n
		Snippet: driver.configure.layer.qpch.set_rate(rate = enums.PagingChannelRate.R4K8) \n
		Specifies the rate of quick paging channel (QPCH) . \n
			:param rate: R4K8 | R9K6 4800 bit/s, 9600 bit/s Unit: bit/s
		"""
		param = Conversions.enum_scalar_to_str(rate, enums.PagingChannelRate)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:LAYer:QPCH:RATE {param}')

	def clone(self) -> 'Qpch':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Qpch(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
