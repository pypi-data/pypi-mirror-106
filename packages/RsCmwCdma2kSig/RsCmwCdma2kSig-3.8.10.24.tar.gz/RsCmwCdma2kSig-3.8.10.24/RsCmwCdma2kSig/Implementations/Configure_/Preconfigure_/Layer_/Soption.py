from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Soption:
	"""Soption commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("soption", core, parent)

	# noinspection PyTypeChecker
	def get_first(self) -> enums.ServiceOption:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:PREConfigure:LAYer:SOPTion:FIRSt \n
		Snippet: value: enums.ServiceOption = driver.configure.preconfigure.layer.soption.get_first() \n
		Preconfigures the primary service option to be proposed to the MS during the next connection setup. \n
			:return: service_option: SO1 | SO2 | SO3 | SO9 | SO17 | SO32 | SO33 | SO55 | SO68 | SO8000 | SO70 | SO73 Speech services: SO1, SO3, SO17, SO68, SO70, SO73 and SO8000 used for a voice call to the MS Loopback services: SO2, SO9 and SO55 used for testing; e.g. for the CDMA2000 RX FER FCH tests. Test data service: SO32 used for testing of the high data rates using the supplemental channel SCH0; e.g. for the CDMA2000 RX FER SCH0 tests. Packet data service: SO33 used for PPP connection between the MS and DAU; see 'Packet Data Service'.
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:PREConfigure:LAYer:SOPTion:FIRSt?')
		return Conversions.str_to_scalar_enum(response, enums.ServiceOption)

	def set_first(self, service_option: enums.ServiceOption) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:PREConfigure:LAYer:SOPTion:FIRSt \n
		Snippet: driver.configure.preconfigure.layer.soption.set_first(service_option = enums.ServiceOption.SO1) \n
		Preconfigures the primary service option to be proposed to the MS during the next connection setup. \n
			:param service_option: SO1 | SO2 | SO3 | SO9 | SO17 | SO32 | SO33 | SO55 | SO68 | SO8000 | SO70 | SO73 Speech services: SO1, SO3, SO17, SO68, SO70, SO73 and SO8000 used for a voice call to the MS Loopback services: SO2, SO9 and SO55 used for testing; e.g. for the CDMA2000 RX FER FCH tests. Test data service: SO32 used for testing of the high data rates using the supplemental channel SCH0; e.g. for the CDMA2000 RX FER SCH0 tests. Packet data service: SO33 used for PPP connection between the MS and DAU; see 'Packet Data Service'.
		"""
		param = Conversions.enum_scalar_to_str(service_option, enums.ServiceOption)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:PREConfigure:LAYer:SOPTion:FIRSt {param}')
