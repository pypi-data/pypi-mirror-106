from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sch:
	"""Sch commands group definition. 5 total commands, 0 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sch", core, parent)

	# noinspection PyTypeChecker
	class PgenerationStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Fwd_Pgeneration: enums.PatternGeneration: RAND | FIX RAND: Random. FIX: Fixed: the bit pattern defined with the command [CMDLINK: CONFigure:CDMA:SIGNi:SCONfig:TDATa:SCH:PATTern CMDLINK].
			- Rev_Pgeneration: enums.PatternGeneration: RAND | FIX"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Fwd_Pgeneration', enums.PatternGeneration),
			ArgStruct.scalar_enum('Rev_Pgeneration', enums.PatternGeneration)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Fwd_Pgeneration: enums.PatternGeneration = None
			self.Rev_Pgeneration: enums.PatternGeneration = None

	# noinspection PyTypeChecker
	def get_pgeneration(self) -> PgenerationStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SCONfig:TDATa:SCH:PGENeration \n
		Snippet: value: PgenerationStruct = driver.configure.sconfig.tdata.sch.get_pgeneration() \n
		Sets the type of pattern the R&S CMW generates and sends to the MS for F-SCH0 and R-SCH0 test data. \n
			:return: structure: for return value, see the help for PgenerationStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:SCONfig:TDATa:SCH:PGENeration?', self.__class__.PgenerationStruct())

	def set_pgeneration(self, value: PgenerationStruct) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SCONfig:TDATa:SCH:PGENeration \n
		Snippet: driver.configure.sconfig.tdata.sch.set_pgeneration(value = PgenerationStruct()) \n
		Sets the type of pattern the R&S CMW generates and sends to the MS for F-SCH0 and R-SCH0 test data. \n
			:param value: see the help for PgenerationStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:CDMA:SIGNaling<Instance>:SCONfig:TDATa:SCH:PGENeration', value)

	# noinspection PyTypeChecker
	class PatternStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Fwd_Pattern: str: Range: #H00 to #HFF
			- Rev_Pattern: str: Range: #H00 to #HFF"""
		__meta_args_list = [
			ArgStruct.scalar_raw_str('Fwd_Pattern'),
			ArgStruct.scalar_raw_str('Rev_Pattern')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Fwd_Pattern: str = None
			self.Rev_Pattern: str = None

	def get_pattern(self) -> PatternStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SCONfig:TDATa:SCH:PATTern \n
		Snippet: value: PatternStruct = driver.configure.sconfig.tdata.sch.get_pattern() \n
		Defines the bit pattern for F-SCH0 and R-SCH0 that the pattern generator uses to send to the MS for measurements.
		This pattern is used if 'Pattern Generation' (method RsCmwCdma2kSig.Configure.Sconfig.Tdata.Sch.pgeneration) is set to
		FIXED. \n
			:return: structure: for return value, see the help for PatternStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:SCONfig:TDATa:SCH:PATTern?', self.__class__.PatternStruct())

	def set_pattern(self, value: PatternStruct) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SCONfig:TDATa:SCH:PATTern \n
		Snippet: driver.configure.sconfig.tdata.sch.set_pattern(value = PatternStruct()) \n
		Defines the bit pattern for F-SCH0 and R-SCH0 that the pattern generator uses to send to the MS for measurements.
		This pattern is used if 'Pattern Generation' (method RsCmwCdma2kSig.Configure.Sconfig.Tdata.Sch.pgeneration) is set to
		FIXED. \n
			:param value: see the help for PatternStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:CDMA:SIGNaling<Instance>:SCONfig:TDATa:SCH:PATTern', value)

	# noinspection PyTypeChecker
	class CbFramesStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Forward_Cb_Frames: int: Range: 1 to 255
			- Reverse_Cb_Frames: int: Range: 1 to 255"""
		__meta_args_list = [
			ArgStruct.scalar_int('Forward_Cb_Frames'),
			ArgStruct.scalar_int('Reverse_Cb_Frames')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Forward_Cb_Frames: int = None
			self.Reverse_Cb_Frames: int = None

	def get_cb_frames(self) -> CbFramesStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SCONfig:TDATa:SCH:CBFRames \n
		Snippet: value: CbFramesStruct = driver.configure.sconfig.tdata.sch.get_cb_frames() \n
		Sets the number of frames to use in the circular buffer of the F-SCH0 and R-SCH0 when the random pattern is selected. \n
			:return: structure: for return value, see the help for CbFramesStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:SCONfig:TDATa:SCH:CBFRames?', self.__class__.CbFramesStruct())

	def set_cb_frames(self, value: CbFramesStruct) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SCONfig:TDATa:SCH:CBFRames \n
		Snippet: driver.configure.sconfig.tdata.sch.set_cb_frames(value = CbFramesStruct()) \n
		Sets the number of frames to use in the circular buffer of the F-SCH0 and R-SCH0 when the random pattern is selected. \n
			:param value: see the help for CbFramesStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:CDMA:SIGNaling<Instance>:SCONfig:TDATa:SCH:CBFRames', value)

	# noinspection PyTypeChecker
	class TxonStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Fwd_Tx_On_Period: int: Range: 0 to 255, Unit: frames
			- Rev_Tx_On_Period: int: Range: 0 to 255, Unit: frames"""
		__meta_args_list = [
			ArgStruct.scalar_int('Fwd_Tx_On_Period'),
			ArgStruct.scalar_int('Rev_Tx_On_Period')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Fwd_Tx_On_Period: int = None
			self.Rev_Tx_On_Period: int = None

	def get_txon(self) -> TxonStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SCONfig:TDATa:SCH:TXON \n
		Snippet: value: TxonStruct = driver.configure.sconfig.tdata.sch.get_txon() \n
		Sets the transmission on period for the F-SCH0 and R-SCH0 when the frame activity is determined. \n
			:return: structure: for return value, see the help for TxonStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:SCONfig:TDATa:SCH:TXON?', self.__class__.TxonStruct())

	def set_txon(self, value: TxonStruct) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SCONfig:TDATa:SCH:TXON \n
		Snippet: driver.configure.sconfig.tdata.sch.set_txon(value = TxonStruct()) \n
		Sets the transmission on period for the F-SCH0 and R-SCH0 when the frame activity is determined. \n
			:param value: see the help for TxonStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:CDMA:SIGNaling<Instance>:SCONfig:TDATa:SCH:TXON', value)

	# noinspection PyTypeChecker
	class TxoffStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Fwd_Tx_Off_Period: int: Range: 0 to 255, Unit: frames
			- Rev_Tx_Off_Period: int: Range: 0 to 255, Unit: frames"""
		__meta_args_list = [
			ArgStruct.scalar_int('Fwd_Tx_Off_Period'),
			ArgStruct.scalar_int('Rev_Tx_Off_Period')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Fwd_Tx_Off_Period: int = None
			self.Rev_Tx_Off_Period: int = None

	def get_txoff(self) -> TxoffStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SCONfig:TDATa:SCH:TXOFf \n
		Snippet: value: TxoffStruct = driver.configure.sconfig.tdata.sch.get_txoff() \n
		Sets the transmission off period for the F-SCH0 and R-SCH0 when the frame activity is determined. \n
			:return: structure: for return value, see the help for TxoffStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:SCONfig:TDATa:SCH:TXOFf?', self.__class__.TxoffStruct())

	def set_txoff(self, value: TxoffStruct) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SCONfig:TDATa:SCH:TXOFf \n
		Snippet: driver.configure.sconfig.tdata.sch.set_txoff(value = TxoffStruct()) \n
		Sets the transmission off period for the F-SCH0 and R-SCH0 when the frame activity is determined. \n
			:param value: see the help for TxoffStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:CDMA:SIGNaling<Instance>:SCONfig:TDATa:SCH:TXOFf', value)
