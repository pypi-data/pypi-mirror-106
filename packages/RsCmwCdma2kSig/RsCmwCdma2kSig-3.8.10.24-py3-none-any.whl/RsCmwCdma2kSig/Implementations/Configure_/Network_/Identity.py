from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Identity:
	"""Identity commands group definition. 4 total commands, 0 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("identity", core, parent)

	def get_nid(self) -> int:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:IDENtity:NID \n
		Snippet: value: int = driver.configure.network.identity.get_nid() \n
		Specifies the network identification number. \n
			:return: network_id_number: Range: 0 to 65535 (16 bits)
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:IDENtity:NID?')
		return Conversions.str_to_int(response)

	def set_nid(self, network_id_number: int) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:IDENtity:NID \n
		Snippet: driver.configure.network.identity.set_nid(network_id_number = 1) \n
		Specifies the network identification number. \n
			:param network_id_number: Range: 0 to 65535 (16 bits)
		"""
		param = Conversions.decimal_value_to_str(network_id_number)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:IDENtity:NID {param}')

	def get_mcc(self) -> int:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:IDENtity:MCC \n
		Snippet: value: int = driver.configure.network.identity.get_mcc() \n
		Specifies the 3-digit mobile country code (MCC) . Leading zeros can be omitted. See method RsCmwCdma2kSig.Configure.
		Network.Identity.uwcard on how to broadcast the wildcard MCC (andIMSI_11_12) . \n
			:return: mob_country_code: Range: 000 to 999
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:IDENtity:MCC?')
		return Conversions.str_to_int(response)

	def set_mcc(self, mob_country_code: int) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:IDENtity:MCC \n
		Snippet: driver.configure.network.identity.set_mcc(mob_country_code = 1) \n
		Specifies the 3-digit mobile country code (MCC) . Leading zeros can be omitted. See method RsCmwCdma2kSig.Configure.
		Network.Identity.uwcard on how to broadcast the wildcard MCC (andIMSI_11_12) . \n
			:param mob_country_code: Range: 000 to 999
		"""
		param = Conversions.decimal_value_to_str(mob_country_code)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:IDENtity:MCC {param}')

	def get_imsi(self) -> int:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:IDENtity:IMSI \n
		Snippet: value: int = driver.configure.network.identity.get_imsi() \n
		11th and 12th digits of the IMSI (IMSI_11_12) See method RsCmwCdma2kSig.Configure.Network.Identity.uwcard on how to
		broadcast the wildcard IMSI_11_12 (and MCC) . \n
			:return: imsi_1112: Range: 00 to 99
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:IDENtity:IMSI?')
		return Conversions.str_to_int(response)

	def set_imsi(self, imsi_1112: int) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:IDENtity:IMSI \n
		Snippet: driver.configure.network.identity.set_imsi(imsi_1112 = 1) \n
		11th and 12th digits of the IMSI (IMSI_11_12) See method RsCmwCdma2kSig.Configure.Network.Identity.uwcard on how to
		broadcast the wildcard IMSI_11_12 (and MCC) . \n
			:param imsi_1112: Range: 00 to 99
		"""
		param = Conversions.decimal_value_to_str(imsi_1112)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:IDENtity:IMSI {param}')

	def get_uwcard(self) -> bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:IDENtity:UWCard \n
		Snippet: value: bool = driver.configure.network.identity.get_uwcard() \n
		If enabled, the R&S CMW broadcasts the wildcard values binary 1111111111 (decimal 1023) for MNC and binary 1111111
		(decimal 127) for IMSI_11_12. See method RsCmwCdma2kSig.Configure.Network.Identity.mcc and method RsCmwCdma2kSig.
		Configure.Network.Identity.imsi on how to set non/wildcard values for MCC and IMSI_11_12) . \n
			:return: use_wildcard: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:IDENtity:UWCard?')
		return Conversions.str_to_bool(response)

	def set_uwcard(self, use_wildcard: bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:IDENtity:UWCard \n
		Snippet: driver.configure.network.identity.set_uwcard(use_wildcard = False) \n
		If enabled, the R&S CMW broadcasts the wildcard values binary 1111111111 (decimal 1023) for MNC and binary 1111111
		(decimal 127) for IMSI_11_12. See method RsCmwCdma2kSig.Configure.Network.Identity.mcc and method RsCmwCdma2kSig.
		Configure.Network.Identity.imsi on how to set non/wildcard values for MCC and IMSI_11_12) . \n
			:param use_wildcard: OFF | ON
		"""
		param = Conversions.bool_to_str(use_wildcard)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:IDENtity:UWCard {param}')
