from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ebnt:
	"""Ebnt commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ebnt", core, parent)

	def get_fch(self) -> float or bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFPower:EBNT:FCH \n
		Snippet: value: float or bool = driver.configure.rfPower.ebnt.get_fch() \n
		Queries the calculated signal to noise ratio of the F-FCH (FCH Eb/Nt) . The value is displayed while the AWGN is turned
		on (see method RsCmwCdma2kSig.Configure.RfPower.Level.awgn) . Otherwise Eb/Nt is undefined as the noise level Nt tends to
		zero. \n
			:return: fch_eb_nt: Range: -100 dB to 100 dB, Unit: dB Additional parameters: OFF | ON disables / enables the calculation of Eb/Nt
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RFPower:EBNT:FCH?')
		return Conversions.str_to_float_or_bool(response)

	def get_sch(self) -> float or bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFPower:EBNT:SCH \n
		Snippet: value: float or bool = driver.configure.rfPower.ebnt.get_sch() \n
		Queries the calculated signal to noise ratio of the F-SCH (SCH Eb/Nt) . The value is displayed while the AWGN is turned
		on (see method RsCmwCdma2kSig.Configure.RfPower.Level.awgn) . Otherwise Eb/Nt is undefined as the noise level Nt tends to
		zero. \n
			:return: sch_0_eb_nt: Range: -100 dB to 100 dB, Unit: dB Additional parameters: OFF | ON disables / enables the calculation of Eb/Nt
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RFPower:EBNT:SCH?')
		return Conversions.str_to_float_or_bool(response)
