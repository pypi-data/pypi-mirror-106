from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Msettings:
	"""Msettings commands group definition. 5 total commands, 1 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("msettings", core, parent)

	@property
	def imin(self):
		"""imin commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_imin'):
			from .Msettings_.Imin import Imin
			self._imin = Imin(self._core, self._base)
		return self._imin

	def get_mcc(self) -> int:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:MSETtings:MCC \n
		Snippet: value: int = driver.configure.network.msettings.get_mcc() \n
		Specifies the mobile country code (MCC) which is used to set up the connection to the MS. If an MS is registered, this
		parameter is updated automatically to the MCC of the registered MS. Afterwards when the MS is unregistered the R&S CMW
		keeps the last information. The parameter can be edit manually or can be updated automatically when an MS with another
		MCC is registered. The MCC consists of 3 numerical characters (0-9) . It is a part of the IMSI for identifying a mobile
		subscriber. \n
			:return: mob_country_code: Range: 0000 to 9999
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:MSETtings:MCC?')
		return Conversions.str_to_int(response)

	def set_mcc(self, mob_country_code: int) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:MSETtings:MCC \n
		Snippet: driver.configure.network.msettings.set_mcc(mob_country_code = 1) \n
		Specifies the mobile country code (MCC) which is used to set up the connection to the MS. If an MS is registered, this
		parameter is updated automatically to the MCC of the registered MS. Afterwards when the MS is unregistered the R&S CMW
		keeps the last information. The parameter can be edit manually or can be updated automatically when an MS with another
		MCC is registered. The MCC consists of 3 numerical characters (0-9) . It is a part of the IMSI for identifying a mobile
		subscriber. \n
			:param mob_country_code: Range: 0000 to 9999
		"""
		param = Conversions.decimal_value_to_str(mob_country_code)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:MSETtings:MCC {param}')

	# noinspection PyTypeChecker
	def get_plcm(self) -> enums.PlcmDerivation:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:MSETtings:PLCM \n
		Snippet: value: enums.PlcmDerivation = driver.configure.network.msettings.get_plcm() \n
		Defines how the MS generates its public long code mask (PLCM) . \n
			:return: plcm_derivation: ESN | MEID ESN: The electronic serial number (ESN) is used to generate the public long code mask. MEID: The mobile equipment identifier (MEID) is used for the public long code mask.
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:MSETtings:PLCM?')
		return Conversions.str_to_scalar_enum(response, enums.PlcmDerivation)

	def set_plcm(self, plcm_derivation: enums.PlcmDerivation) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:MSETtings:PLCM \n
		Snippet: driver.configure.network.msettings.set_plcm(plcm_derivation = enums.PlcmDerivation.ESN) \n
		Defines how the MS generates its public long code mask (PLCM) . \n
			:param plcm_derivation: ESN | MEID ESN: The electronic serial number (ESN) is used to generate the public long code mask. MEID: The mobile equipment identifier (MEID) is used for the public long code mask.
		"""
		param = Conversions.enum_scalar_to_str(plcm_derivation, enums.PlcmDerivation)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:MSETtings:PLCM {param}')

	def get_nmsi(self) -> str:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:MSETtings:NMSI \n
		Snippet: value: str = driver.configure.network.msettings.get_nmsi() \n
		Specifies the mobile ID of the MS which is used to set up the connection to the MS. For some protocol revisions, it is
		possible to choose either a mobile identification number (MIN) or national mobile subscriber identity (NMSI) as mobile ID.
		For other protocol revisions, a choice of the mobile ID is not available. To enter a mobile ID is optional. However,
		together with the MCC (method RsCmwCdma2kSig.Configure.Network.Msettings.mcc) these parameters provide for the R&S CMW
		the necessary information so that the 'Connect 1st SO' softkey (see chapter 'Connection Control Hotkeys') can be used
		without waiting for registration. If an MS is registered, this parameter is updated automatically to the mobile ID of the
		registered MS. Afterwards when the MS is unregistered the R&S CMW keeps the last information. The parameter can be edit
		manually or can be updated automatically when another MS is registered. \n
			:return: nmsi: Up to 12-digit decimal number Range: 000000000000 to 999999999999 (12 digits)
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:MSETtings:NMSI?')
		return trim_str_response(response)

	def set_nmsi(self, nmsi: str) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:MSETtings:NMSI \n
		Snippet: driver.configure.network.msettings.set_nmsi(nmsi = '1') \n
		Specifies the mobile ID of the MS which is used to set up the connection to the MS. For some protocol revisions, it is
		possible to choose either a mobile identification number (MIN) or national mobile subscriber identity (NMSI) as mobile ID.
		For other protocol revisions, a choice of the mobile ID is not available. To enter a mobile ID is optional. However,
		together with the MCC (method RsCmwCdma2kSig.Configure.Network.Msettings.mcc) these parameters provide for the R&S CMW
		the necessary information so that the 'Connect 1st SO' softkey (see chapter 'Connection Control Hotkeys') can be used
		without waiting for registration. If an MS is registered, this parameter is updated automatically to the mobile ID of the
		registered MS. Afterwards when the MS is unregistered the R&S CMW keeps the last information. The parameter can be edit
		manually or can be updated automatically when another MS is registered. \n
			:param nmsi: Up to 12-digit decimal number Range: 000000000000 to 999999999999 (12 digits)
		"""
		param = Conversions.value_to_quoted_str(nmsi)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:MSETtings:NMSI {param}')

	def get_umr_data(self) -> bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:MSETtings:UMRData \n
		Snippet: value: bool = driver.configure.network.msettings.get_umr_data() \n
		No command help available \n
			:return: umr_data: No help available
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:MSETtings:UMRData?')
		return Conversions.str_to_bool(response)

	def set_umr_data(self, umr_data: bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:MSETtings:UMRData \n
		Snippet: driver.configure.network.msettings.set_umr_data(umr_data = False) \n
		No command help available \n
			:param umr_data: No help available
		"""
		param = Conversions.bool_to_str(umr_data)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:MSETtings:UMRData {param}')

	def clone(self) -> 'Msettings':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Msettings(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
