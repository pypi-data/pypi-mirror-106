from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MsInfo:
	"""MsInfo commands group definition. 9 total commands, 0 Sub-groups, 9 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("msInfo", core, parent)

	def get_dnumber(self) -> str:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:MSINfo:DNUMber \n
		Snippet: value: str = driver.configure.msInfo.get_dnumber() \n
		Queries the number dialed at the MS. \n
			:return: dialed_number: Dialed number as string.
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:MSINfo:DNUMber?')
		return trim_str_response(response)

	# noinspection PyTypeChecker
	def get_gecall(self) -> enums.YesNoStatus:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:MSINfo:GECall \n
		Snippet: value: enums.YesNoStatus = driver.configure.msInfo.get_gecall() \n
		Queries information from the MS. The value indicates if the current call is a global emergency call. \n
			:return: global_emerg_call: NO | YES
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:MSINfo:GECall?')
		return Conversions.str_to_scalar_enum(response, enums.YesNoStatus)

	def get_prevision(self) -> int:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:MSINfo:PREVision \n
		Snippet: value: int = driver.configure.msInfo.get_prevision() \n
		Queries the protocol revision supported by the MS. \n
			:return: protocol_rev: Range: 1 to 100
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:MSINfo:PREVision?')
		return Conversions.str_to_int(response)

	def get_mcc(self) -> int:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:MSINfo:MCC \n
		Snippet: value: int = driver.configure.msInfo.get_mcc() \n
		No command help available \n
			:return: mcc: No help available
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:MSINfo:MCC?')
		return Conversions.str_to_int(response)

	def get_nmsi(self) -> str:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:MSINfo:NMSI \n
		Snippet: value: str = driver.configure.msInfo.get_nmsi() \n
		No command help available \n
			:return: nmsi: No help available
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:MSINfo:NMSI?')
		return trim_str_response(response)

	def get_msupport(self) -> bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:MSINfo:MSUPport \n
		Snippet: value: bool = driver.configure.msInfo.get_msupport() \n
		Queries information from the MS. The value indicates whether the MEID support bit 4 is set or not. \n
			:return: meid_support: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:MSINfo:MSUPport?')
		return Conversions.str_to_bool(response)

	def get_esn(self) -> str:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:MSINfo:ESN \n
		Snippet: value: str = driver.configure.msInfo.get_esn() \n
		Queries the electronic serial number (ESN) of the MS. It is 32-bit number which is shown in 8-digit hex string format. \n
			:return: esn: Range: #H0 to #HFFFFFFFF
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:MSINfo:ESN?')
		return trim_str_response(response)

	def get_meid(self) -> str:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:MSINfo:MEID \n
		Snippet: value: str = driver.configure.msInfo.get_meid() \n
		Queries information from the MS. The value shows the mobile equipment identifier of the MS. It is 56-bit number assigned
		by the MS manufacturer, uniquely identifying the MS equipment. \n
			:return: meid: 14-digit hexadecimal number Range: #H0 to #HFFFFFFFFFFFFFF (14 digits)
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:MSINfo:MEID?')
		return trim_str_response(response)

	def get_eirp(self) -> int:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:MSINfo:EIRP \n
		Snippet: value: int = driver.configure.msInfo.get_eirp() \n
		Queries the information from the MS about the maximum effective isotropic radiated power (EIRP) . \n
			:return: max_eirp: Range: 0 to 999
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:MSINfo:EIRP?')
		return Conversions.str_to_int(response)
