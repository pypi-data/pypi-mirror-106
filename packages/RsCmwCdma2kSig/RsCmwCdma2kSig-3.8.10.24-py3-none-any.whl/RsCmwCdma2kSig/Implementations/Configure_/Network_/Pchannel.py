from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pchannel:
	"""Pchannel commands group definition. 5 total commands, 0 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pchannel", core, parent)

	# noinspection PyTypeChecker
	def get_rate(self) -> enums.PagingChannelRate:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:PCHannel:RATE \n
		Snippet: value: enums.PagingChannelRate = driver.configure.network.pchannel.get_rate() \n
		Sets the data rate of the forward paging channel. \n
			:return: paging_ch_rate: R4K8 | R9K6
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:PCHannel:RATE?')
		return Conversions.str_to_scalar_enum(response, enums.PagingChannelRate)

	def set_rate(self, paging_ch_rate: enums.PagingChannelRate) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:PCHannel:RATE \n
		Snippet: driver.configure.network.pchannel.set_rate(paging_ch_rate = enums.PagingChannelRate.R4K8) \n
		Sets the data rate of the forward paging channel. \n
			:param paging_ch_rate: R4K8 | R9K6
		"""
		param = Conversions.enum_scalar_to_str(paging_ch_rate, enums.PagingChannelRate)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:PCHannel:RATE {param}')

	def get_sc_index(self) -> int:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:PCHannel:SCINdex \n
		Snippet: value: int = driver.configure.network.pchannel.get_sc_index() \n
		Queries the current slot cycle index in use by both the MS and BS. See also: 'Slot Cycle Index' \n
			:return: slot_cycle_index: Range: 0 to 7
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:PCHannel:SCINdex?')
		return Conversions.str_to_int(response)

	def get_msc_index(self) -> int:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:PCHannel:MSCindex \n
		Snippet: value: int = driver.configure.network.pchannel.get_msc_index() \n
		Sets the paging channel max slot cycle index. It defines an upper limit on the slot cycle index allowed by the base
		station. The MS has an internally programmed preferred slot cycle index, which is sent in the mobile's registration
		message. See also: 'Slot Cycle Index' \n
			:return: max_slot_cyc_index: Range: 0 to 7
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:PCHannel:MSCindex?')
		return Conversions.str_to_int(response)

	def set_msc_index(self, max_slot_cyc_index: int) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:PCHannel:MSCindex \n
		Snippet: driver.configure.network.pchannel.set_msc_index(max_slot_cyc_index = 1) \n
		Sets the paging channel max slot cycle index. It defines an upper limit on the slot cycle index allowed by the base
		station. The MS has an internally programmed preferred slot cycle index, which is sent in the mobile's registration
		message. See also: 'Slot Cycle Index' \n
			:param max_slot_cyc_index: Range: 0 to 7
		"""
		param = Conversions.decimal_value_to_str(max_slot_cyc_index)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:PCHannel:MSCindex {param}')

	def get_bsc_index(self) -> int:
		"""SCPI: CONFigure:CDMA:SIGNaling<instance>:NETWork:PCHannel:BSCindex \n
		Snippet: value: int = driver.configure.network.pchannel.get_bsc_index() \n
		Specifies the interval of the periodical broadcast messaging. The value zero indicates that periodic paging is disabled. \n
			:return: broad_slot_ci_ndex: Range: 0 to 7
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:PCHannel:BSCindex?')
		return Conversions.str_to_int(response)

	def set_bsc_index(self, broad_slot_ci_ndex: int) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<instance>:NETWork:PCHannel:BSCindex \n
		Snippet: driver.configure.network.pchannel.set_bsc_index(broad_slot_ci_ndex = 1) \n
		Specifies the interval of the periodical broadcast messaging. The value zero indicates that periodic paging is disabled. \n
			:param broad_slot_ci_ndex: Range: 0 to 7
		"""
		param = Conversions.decimal_value_to_str(broad_slot_ci_ndex)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:PCHannel:BSCindex {param}')

	def get_prms(self) -> bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:PCHannel:PRMS \n
		Snippet: value: bool = driver.configure.network.pchannel.get_prms() \n
		Specifies if non-registered mobile stations have to be paged. \n
			:return: page_regsitered_ms: OFF | ON OFF: the paging is sent to the registered and unregistered mobile stations ON: the paging is sent only to the registered mobile stations
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:PCHannel:PRMS?')
		return Conversions.str_to_bool(response)

	def set_prms(self, page_regsitered_ms: bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:PCHannel:PRMS \n
		Snippet: driver.configure.network.pchannel.set_prms(page_regsitered_ms = False) \n
		Specifies if non-registered mobile stations have to be paged. \n
			:param page_regsitered_ms: OFF | ON OFF: the paging is sent to the registered and unregistered mobile stations ON: the paging is sent only to the registered mobile stations
		"""
		param = Conversions.bool_to_str(page_regsitered_ms)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:PCHannel:PRMS {param}')
