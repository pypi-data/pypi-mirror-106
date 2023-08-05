from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("mode", core, parent)

	def get_awgn(self) -> float:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFPower:MODE:AWGN \n
		Snippet: value: float = driver.configure.rfPower.mode.get_awgn() \n
		Selects the operating mode of the AWGN generator. The AWGN level range (method RsCmwCdma2kSig.Configure.RfPower.Level.
		awgn) depends on the operating mode. \n
			:return: awgn_mode: NORMal | HPOWer Normal, high-power mode
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RFPower:MODE:AWGN?')
		return Conversions.str_to_float(response)

	def set_awgn(self, awgn_mode: float) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFPower:MODE:AWGN \n
		Snippet: driver.configure.rfPower.mode.set_awgn(awgn_mode = 1.0) \n
		Selects the operating mode of the AWGN generator. The AWGN level range (method RsCmwCdma2kSig.Configure.RfPower.Level.
		awgn) depends on the operating mode. \n
			:param awgn_mode: NORMal | HPOWer Normal, high-power mode
		"""
		param = Conversions.decimal_value_to_str(awgn_mode)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RFPower:MODE:AWGN {param}')
