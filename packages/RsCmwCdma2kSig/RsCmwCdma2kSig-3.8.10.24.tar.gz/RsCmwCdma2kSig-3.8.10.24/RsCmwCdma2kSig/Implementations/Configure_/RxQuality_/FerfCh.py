from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FerfCh:
	"""FerfCh commands group definition. 4 total commands, 0 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ferfCh", core, parent)

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RXQuality:FERFch:TOUT \n
		Snippet: value: float = driver.configure.rxQuality.ferfCh.get_timeout() \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually ([ON | OFF] key or [RESTART | STOP] key) .
		When the measurement has completed the first measurement cycle (first single shot) , the statistical depth is reached and
		the timer is reset. If the first measurement cycle has not been completed when the timer expires, the measurement is
		stopped. The measurement state changes to RDY. The reliability indicator is set to 1, indicating that a measurement
		timeout occurred. Still running READ, FETCh or CALCulate commands are completed, returning the available results.
		At least for some results, there are no values at all or the statistical depth has not been reached. A timeout of 0 s
		corresponds to an infinite measurement timeout. \n
			:return: timeout: Unit: s
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RXQuality:FERFch:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, timeout: float) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RXQuality:FERFch:TOUT \n
		Snippet: driver.configure.rxQuality.ferfCh.set_timeout(timeout = 1.0) \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually ([ON | OFF] key or [RESTART | STOP] key) .
		When the measurement has completed the first measurement cycle (first single shot) , the statistical depth is reached and
		the timer is reset. If the first measurement cycle has not been completed when the timer expires, the measurement is
		stopped. The measurement state changes to RDY. The reliability indicator is set to 1, indicating that a measurement
		timeout occurred. Still running READ, FETCh or CALCulate commands are completed, returning the available results.
		At least for some results, there are no values at all or the statistical depth has not been reached. A timeout of 0 s
		corresponds to an infinite measurement timeout. \n
			:param timeout: Unit: s
		"""
		param = Conversions.decimal_value_to_str(timeout)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RXQuality:FERFch:TOUT {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RXQuality:FERFch:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.rxQuality.ferfCh.get_repetition() \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single-shot or repeated continuously. Use method RsCmwCdma2kSig.Configure.RxQuality.FersCh.frames to determine the
		number of test frames per single shot. \n
			:return: repetition: SINGleshot | CONTinuous SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RXQuality:FERFch:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RXQuality:FERFch:REPetition \n
		Snippet: driver.configure.rxQuality.ferfCh.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		Specifies the repetition mode of the measurement. The repetition mode specifies whether the measurement is stopped after
		a single-shot or repeated continuously. Use method RsCmwCdma2kSig.Configure.RxQuality.FersCh.frames to determine the
		number of test frames per single shot. \n
			:param repetition: SINGleshot | CONTinuous SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RXQuality:FERFch:REPetition {param}')

	# noinspection PyTypeChecker
	def get_scondition(self) -> enums.StopConditionB:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RXQuality:FERFch:SCONdition \n
		Snippet: value: enums.StopConditionB = driver.configure.rxQuality.ferfCh.get_scondition() \n
		Qualifies whether the measurement is stopped after a failed limit check or continued. SLFail means that the measurement
		is stopped and reaches the RDY state when one of the results exceeds the limits. \n
			:return: stop_condition: NONE | ALEXeeded | MCLexceeded | MFER NONE: Continue measurement irrespective of the limit check ALEXceeded: Stop if any limit is exceeded MCLexceeded: Stop if minimum confidence level is exceeded MFERexceeded: Stop if maximum FER is exceeded
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RXQuality:FERFch:SCONdition?')
		return Conversions.str_to_scalar_enum(response, enums.StopConditionB)

	def set_scondition(self, stop_condition: enums.StopConditionB) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RXQuality:FERFch:SCONdition \n
		Snippet: driver.configure.rxQuality.ferfCh.set_scondition(stop_condition = enums.StopConditionB.ALEXeeded) \n
		Qualifies whether the measurement is stopped after a failed limit check or continued. SLFail means that the measurement
		is stopped and reaches the RDY state when one of the results exceeds the limits. \n
			:param stop_condition: NONE | ALEXeeded | MCLexceeded | MFER NONE: Continue measurement irrespective of the limit check ALEXceeded: Stop if any limit is exceeded MCLexceeded: Stop if minimum confidence level is exceeded MFERexceeded: Stop if maximum FER is exceeded
		"""
		param = Conversions.enum_scalar_to_str(stop_condition, enums.StopConditionB)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RXQuality:FERFch:SCONdition {param}')

	def get_frames(self) -> int:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RXQuality:FERFch:FRAMes \n
		Snippet: value: int = driver.configure.rxQuality.ferfCh.get_frames() \n
		Defines the number of frames used to calculate FER. Hence it defines the length of a single shot FER measurement. \n
			:return: ferf_ch_frames: No help available
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RXQuality:FERFch:FRAMes?')
		return Conversions.str_to_int(response)

	def set_frames(self, ferf_ch_frames: int) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RXQuality:FERFch:FRAMes \n
		Snippet: driver.configure.rxQuality.ferfCh.set_frames(ferf_ch_frames = 1) \n
		Defines the number of frames used to calculate FER. Hence it defines the length of a single shot FER measurement. \n
			:param ferf_ch_frames: Range: 1 to 100E+3
		"""
		param = Conversions.decimal_value_to_str(ferf_ch_frames)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RXQuality:FERFch:FRAMes {param}')
