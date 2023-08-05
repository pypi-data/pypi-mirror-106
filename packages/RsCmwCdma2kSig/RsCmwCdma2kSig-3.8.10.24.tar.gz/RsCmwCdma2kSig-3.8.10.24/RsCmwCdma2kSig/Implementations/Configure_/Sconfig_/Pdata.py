from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pdata:
	"""Pdata commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pdata", core, parent)

	def get_itimer(self) -> int or bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SCONfig:PDATa:ITIMer \n
		Snippet: value: int or bool = driver.configure.sconfig.pdata.get_itimer() \n
		Sets the inactive timer of PPP connection. If the inactive timer expires, R&S CMW terminates the PPP session and releases
		the dormant timer of the MS (see method RsCmwCdma2kSig.Configure.Sconfig.Pdata.dtimer) . \n
			:return: inactive_timer: Range: 5 s to 60 s, Unit: s Additional OFF/ON disables / enables the timer
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:SCONfig:PDATa:ITIMer?')
		return Conversions.str_to_int_or_bool(response)

	def set_itimer(self, inactive_timer: int or bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SCONfig:PDATa:ITIMer \n
		Snippet: driver.configure.sconfig.pdata.set_itimer(inactive_timer = 1) \n
		Sets the inactive timer of PPP connection. If the inactive timer expires, R&S CMW terminates the PPP session and releases
		the dormant timer of the MS (see method RsCmwCdma2kSig.Configure.Sconfig.Pdata.dtimer) . \n
			:param inactive_timer: Range: 5 s to 60 s, Unit: s Additional OFF/ON disables / enables the timer
		"""
		param = Conversions.decimal_or_bool_value_to_str(inactive_timer)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:SCONfig:PDATa:ITIMer {param}')

	def get_dtimer(self) -> float or bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SCONfig:PDATa:DTIMer \n
		Snippet: value: float or bool = driver.configure.sconfig.pdata.get_dtimer() \n
		Sets packet data dormant timer of the MS. If dormant timer expires, IP connection is released. \n
			:return: dormant_timer: Range: 0 s to 25.5 s, Unit: s Additional OFF/ON disables / enables the timer
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:SCONfig:PDATa:DTIMer?')
		return Conversions.str_to_float_or_bool(response)

	def set_dtimer(self, dormant_timer: float or bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SCONfig:PDATa:DTIMer \n
		Snippet: driver.configure.sconfig.pdata.set_dtimer(dormant_timer = 1.0) \n
		Sets packet data dormant timer of the MS. If dormant timer expires, IP connection is released. \n
			:param dormant_timer: Range: 0 s to 25.5 s, Unit: s Additional OFF/ON disables / enables the timer
		"""
		param = Conversions.decimal_or_bool_value_to_str(dormant_timer)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:SCONfig:PDATa:DTIMer {param}')
