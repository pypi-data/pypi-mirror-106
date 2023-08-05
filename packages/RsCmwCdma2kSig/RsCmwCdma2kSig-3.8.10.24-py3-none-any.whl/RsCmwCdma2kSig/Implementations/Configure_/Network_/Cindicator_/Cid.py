from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cid:
	"""Cid commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cid", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:CINDicator:CID:ENABle \n
		Snippet: value: bool = driver.configure.network.cindicator.cid.get_enable() \n
		Enables or disables the caller ID insertion. If enabled, the 'Caller ID' (method RsCmwCdma2kSig.Configure.Network.
		Cindicator.Cid.value) is transferred immediately after the 'Alerting' message. In addition, it can be sent during an
		established call using the call waiting indicator parameter. \n
			:return: caller_id_enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:CINDicator:CID:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, caller_id_enable: bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:CINDicator:CID:ENABle \n
		Snippet: driver.configure.network.cindicator.cid.set_enable(caller_id_enable = False) \n
		Enables or disables the caller ID insertion. If enabled, the 'Caller ID' (method RsCmwCdma2kSig.Configure.Network.
		Cindicator.Cid.value) is transferred immediately after the 'Alerting' message. In addition, it can be sent during an
		established call using the call waiting indicator parameter. \n
			:param caller_id_enable: OFF | ON
		"""
		param = Conversions.bool_to_str(caller_id_enable)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:CINDicator:CID:ENABle {param}')

	# noinspection PyTypeChecker
	def get_pindicator(self) -> enums.CallerIdPresentation:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:CINDicator:CID:PINDicator \n
		Snippet: value: enums.CallerIdPresentation = driver.configure.network.cindicator.cid.get_pindicator() \n
		Sets/gets the presentation indicator for the caller ID (calling party number) , i.e. specifies how the MS under test
		displays the caller ID received from the R&S CMW: \n
			:return: caller_id_pres_ind: PAL | PRES | NNAV PAL: Presentation allowed PRES: Presentation restricted NNAV: Number not available
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:CINDicator:CID:PINDicator?')
		return Conversions.str_to_scalar_enum(response, enums.CallerIdPresentation)

	def set_pindicator(self, caller_id_pres_ind: enums.CallerIdPresentation) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:CINDicator:CID:PINDicator \n
		Snippet: driver.configure.network.cindicator.cid.set_pindicator(caller_id_pres_ind = enums.CallerIdPresentation.NNAV) \n
		Sets/gets the presentation indicator for the caller ID (calling party number) , i.e. specifies how the MS under test
		displays the caller ID received from the R&S CMW: \n
			:param caller_id_pres_ind: PAL | PRES | NNAV PAL: Presentation allowed PRES: Presentation restricted NNAV: Number not available
		"""
		param = Conversions.enum_scalar_to_str(caller_id_pres_ind, enums.CallerIdPresentation)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:CINDicator:CID:PINDicator {param}')

	def get_value(self) -> str:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:CINDicator:CID \n
		Snippet: value: str = driver.configure.network.cindicator.cid.get_value() \n
		Sets/gets the caller ID also known as calling party number (CPN) . It is the number of a (virtual) calling party that the
		R&S CMW sends to the MS to test whether it is properly displayed. \n
			:return: caller_id: A string consisting of decimal digits Range: max. 32 characters
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:CINDicator:CID?')
		return trim_str_response(response)

	def set_value(self, caller_id: str) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:CINDicator:CID \n
		Snippet: driver.configure.network.cindicator.cid.set_value(caller_id = '1') \n
		Sets/gets the caller ID also known as calling party number (CPN) . It is the number of a (virtual) calling party that the
		R&S CMW sends to the MS to test whether it is properly displayed. \n
			:param caller_id: A string consisting of decimal digits Range: max. 32 characters
		"""
		param = Conversions.value_to_quoted_str(caller_id)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:CINDicator:CID {param}')
