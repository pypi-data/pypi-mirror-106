from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Loop:
	"""Loop commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("loop", core, parent)

	# noinspection PyTypeChecker
	def get_frate(self) -> enums.FrameRate:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SCONfig:LOOP:FRATe \n
		Snippet: value: enums.FrameRate = driver.configure.sconfig.loop.get_frate() \n
		Sets the frame rate of the F-FCH to full, half, quarter, or eighth. \n
			:return: frame_rate: FULL | HALF | QUARter | EIGHth FULL: Frames at the full rate set. HALF: Frames at 1/2 of the rate set. QUARter: Frames at 1/4 of the rate set. EIGHth: Frames at 1/8 of the rate set.
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:SCONfig:LOOP:FRATe?')
		return Conversions.str_to_scalar_enum(response, enums.FrameRate)

	def set_frate(self, frame_rate: enums.FrameRate) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SCONfig:LOOP:FRATe \n
		Snippet: driver.configure.sconfig.loop.set_frate(frame_rate = enums.FrameRate.EIGHth) \n
		Sets the frame rate of the F-FCH to full, half, quarter, or eighth. \n
			:param frame_rate: FULL | HALF | QUARter | EIGHth FULL: Frames at the full rate set. HALF: Frames at 1/2 of the rate set. QUARter: Frames at 1/4 of the rate set. EIGHth: Frames at 1/8 of the rate set.
		"""
		param = Conversions.enum_scalar_to_str(frame_rate, enums.FrameRate)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:SCONfig:LOOP:FRATe {param}')

	# noinspection PyTypeChecker
	def get_pgeneration(self) -> enums.PatternGeneration:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SCONfig:LOOP:PGENeration \n
		Snippet: value: enums.PatternGeneration = driver.configure.sconfig.loop.get_pgeneration() \n
		Sets the type of pattern the R&S CMW generates and sends to the MS. \n
			:return: pgeneration: RAND | FIX RAND: Random: Sends a random pattern to the MS and is the preferred method to obtain the best measurement performance. FIX: Fixed: Sends the bit pattern defined with the pattern command (method RsCmwCdma2kSig.Configure.Sconfig.Loop.pattern) . The R&S CMW generates one fundamental data block to the MS. After a delay to allow for processing, the MS sends one reverse fundamental data block back to the R&S CMW. The R&S CMW can set the bits within a data block to a random pattern or any desired value (fixed) .
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:SCONfig:LOOP:PGENeration?')
		return Conversions.str_to_scalar_enum(response, enums.PatternGeneration)

	def set_pgeneration(self, pgeneration: enums.PatternGeneration) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SCONfig:LOOP:PGENeration \n
		Snippet: driver.configure.sconfig.loop.set_pgeneration(pgeneration = enums.PatternGeneration.FIX) \n
		Sets the type of pattern the R&S CMW generates and sends to the MS. \n
			:param pgeneration: RAND | FIX RAND: Random: Sends a random pattern to the MS and is the preferred method to obtain the best measurement performance. FIX: Fixed: Sends the bit pattern defined with the pattern command (method RsCmwCdma2kSig.Configure.Sconfig.Loop.pattern) . The R&S CMW generates one fundamental data block to the MS. After a delay to allow for processing, the MS sends one reverse fundamental data block back to the R&S CMW. The R&S CMW can set the bits within a data block to a random pattern or any desired value (fixed) .
		"""
		param = Conversions.enum_scalar_to_str(pgeneration, enums.PatternGeneration)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:SCONfig:LOOP:PGENeration {param}')

	def get_pattern(self) -> str:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SCONfig:LOOP:PATTern \n
		Snippet: value: str = driver.configure.sconfig.loop.get_pattern() \n
		Defines the bit pattern that the pattern generator uses to send to the MS for measurements. This pattern is used if
		'Pattern Generation' (method RsCmwCdma2kSig.Configure.Sconfig.Loop.pgeneration) is set to FIXED. \n
			:return: pattern: String to specify the pattern.
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:SCONfig:LOOP:PATTern?')
		return trim_str_response(response)

	def set_pattern(self, pattern: str) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SCONfig:LOOP:PATTern \n
		Snippet: driver.configure.sconfig.loop.set_pattern(pattern = '1') \n
		Defines the bit pattern that the pattern generator uses to send to the MS for measurements. This pattern is used if
		'Pattern Generation' (method RsCmwCdma2kSig.Configure.Sconfig.Loop.pgeneration) is set to FIXED. \n
			:param pattern: String to specify the pattern.
		"""
		param = Conversions.value_to_quoted_str(pattern)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:SCONfig:LOOP:PATTern {param}')
