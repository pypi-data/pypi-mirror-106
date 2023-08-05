from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pstrength:
	"""Pstrength commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pstrength", core, parent)

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RXQuality:PSTRength:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.rxQuality.pstrength.get_repetition() \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single-shot or repeated continuously. Use method RsCmwCdma2kSig.Configure.RxQuality.Pstrength.urate to specify the
		period of MS reporting in continuous mode. \n
			:return: repetition: SINGleshot | CONTinuous SINGleshot: single-shot measurement CONTinuous: continuous measurement
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RXQuality:PSTRength:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RXQuality:PSTRength:REPetition \n
		Snippet: driver.configure.rxQuality.pstrength.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single-shot or repeated continuously. Use method RsCmwCdma2kSig.Configure.RxQuality.Pstrength.urate to specify the
		period of MS reporting in continuous mode. \n
			:param repetition: SINGleshot | CONTinuous SINGleshot: single-shot measurement CONTinuous: continuous measurement
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RXQuality:PSTRength:REPetition {param}')

	def get_urate(self) -> float:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RXQuality:PSTRength:URATe \n
		Snippet: value: float = driver.configure.rxQuality.pstrength.get_urate() \n
		Defines a period for pilot strength reporting. \n
			:return: update_rate: Range: 0.25 s to 2 s
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RXQuality:PSTRength:URATe?')
		return Conversions.str_to_float(response)

	def set_urate(self, update_rate: float) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RXQuality:PSTRength:URATe \n
		Snippet: driver.configure.rxQuality.pstrength.set_urate(update_rate = 1.0) \n
		Defines a period for pilot strength reporting. \n
			:param update_rate: Range: 0.25 s to 2 s
		"""
		param = Conversions.decimal_value_to_str(update_rate)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RXQuality:PSTRength:URATe {param}')
