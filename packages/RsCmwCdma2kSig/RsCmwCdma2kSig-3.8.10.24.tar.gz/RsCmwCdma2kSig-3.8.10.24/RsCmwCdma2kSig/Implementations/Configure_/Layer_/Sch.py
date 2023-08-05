from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sch:
	"""Sch commands group definition. 6 total commands, 0 Sub-groups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sch", core, parent)

	def get_foffset(self) -> float:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:LAYer:SCH:FOFFset \n
		Snippet: value: float = driver.configure.layer.sch.get_foffset() \n
		No command help available \n
			:return: frame_offset: No help available
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:LAYer:SCH:FOFFset?')
		return Conversions.str_to_float(response)

	def set_foffset(self, frame_offset: float) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:LAYer:SCH:FOFFset \n
		Snippet: driver.configure.layer.sch.set_foffset(frame_offset = 1.0) \n
		No command help available \n
			:param frame_offset: No help available
		"""
		param = Conversions.decimal_value_to_str(frame_offset)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:LAYer:SCH:FOFFset {param}')

	# noinspection PyTypeChecker
	class MpplStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Forward_Mux_Pdus: int: Range: 1 | 2 | 4 | 8
			- Rev_Mux_Pdus: int: Range: 1 | 2 | 4 | 8"""
		__meta_args_list = [
			ArgStruct.scalar_int('Forward_Mux_Pdus'),
			ArgStruct.scalar_int('Rev_Mux_Pdus')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Forward_Mux_Pdus: int = None
			self.Rev_Mux_Pdus: int = None

	def get_mppl(self) -> MpplStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:LAYer:SCH:MPPL \n
		Snippet: value: MpplStruct = driver.configure.layer.sch.get_mppl() \n
		Sets the number of multiplex PDUs per physical layer SDU for the F-SCH0 and R-SCH0 for segmentation. Together with the
		'Frame Type', this parameter determines the data rate of SCH0. See Table 'SCH maximum data rate (kbit/s) dependencies on
		MuxPDUs per physical layer SDU, RC and frame type for frame size 20 ms' \n
			:return: structure: for return value, see the help for MpplStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:LAYer:SCH:MPPL?', self.__class__.MpplStruct())

	def set_mppl(self, value: MpplStruct) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:LAYer:SCH:MPPL \n
		Snippet: driver.configure.layer.sch.set_mppl(value = MpplStruct()) \n
		Sets the number of multiplex PDUs per physical layer SDU for the F-SCH0 and R-SCH0 for segmentation. Together with the
		'Frame Type', this parameter determines the data rate of SCH0. See Table 'SCH maximum data rate (kbit/s) dependencies on
		MuxPDUs per physical layer SDU, RC and frame type for frame size 20 ms' \n
			:param value: see the help for MpplStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:CDMA:SIGNaling<Instance>:LAYer:SCH:MPPL', value)

	# noinspection PyTypeChecker
	class FtypeStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Fwd_Frame_Type: enums.ForwardFrameType: R1 | R2
			- Rev_Frame_Type: enums.ForwardFrameType: R1 | R2"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Fwd_Frame_Type', enums.ForwardFrameType),
			ArgStruct.scalar_enum('Rev_Frame_Type', enums.ForwardFrameType)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Fwd_Frame_Type: enums.ForwardFrameType = None
			self.Rev_Frame_Type: enums.ForwardFrameType = None

	# noinspection PyTypeChecker
	def get_ftype(self) -> FtypeStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:LAYer:SCH:FTYPe \n
		Snippet: value: FtypeStruct = driver.configure.layer.sch.get_ftype() \n
		Sets the Rate value for F-SCH0 and R-SCH0. Together with the 'MuxPDUs / Layer', this parameter determines the data rate
		of SCH0. See also Table 'SCH maximum data rate (kbit/s) dependencies on MuxPDUs per physical layer SDU, RC and frame type
		for frame size 20 ms'. \n
			:return: structure: for return value, see the help for FtypeStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:LAYer:SCH:FTYPe?', self.__class__.FtypeStruct())

	def set_ftype(self, value: FtypeStruct) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:LAYer:SCH:FTYPe \n
		Snippet: driver.configure.layer.sch.set_ftype(value = FtypeStruct()) \n
		Sets the Rate value for F-SCH0 and R-SCH0. Together with the 'MuxPDUs / Layer', this parameter determines the data rate
		of SCH0. See also Table 'SCH maximum data rate (kbit/s) dependencies on MuxPDUs per physical layer SDU, RC and frame type
		for frame size 20 ms'. \n
			:param value: see the help for FtypeStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:CDMA:SIGNaling<Instance>:LAYer:SCH:FTYPe', value)

	# noinspection PyTypeChecker
	class DrateStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Fwd_Data_Rate: enums.ForwardDataRate: R9K | R14K | R19K | R28K | R38K | R57K | R76K | R115k | R153k | R230k
			- Rev_Data_Rate: enums.ForwardDataRate: R9K | R14K | R19K | R28K | R38K | R57K | R76K | R115k | R153k | R230k"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Fwd_Data_Rate', enums.ForwardDataRate),
			ArgStruct.scalar_enum('Rev_Data_Rate', enums.ForwardDataRate)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Fwd_Data_Rate: enums.ForwardDataRate = None
			self.Rev_Data_Rate: enums.ForwardDataRate = None

	# noinspection PyTypeChecker
	def get_drate(self) -> DrateStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:LAYer:SCH:DRATe \n
		Snippet: value: DrateStruct = driver.configure.layer.sch.get_drate() \n
		Queries data rate in F-SCH and R-SCH. See also Table 'SCH maximum data rate (kbit/s) dependencies on MuxPDUs per physical
		layer SDU, RC and frame type for frame size 20 ms'. \n
			:return: structure: for return value, see the help for DrateStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:LAYer:SCH:DRATe?', self.__class__.DrateStruct())

	# noinspection PyTypeChecker
	class FsizeStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Fwd_Frame_Size: int: Range: 20 ms | 40 ms | 80 ms
			- Rev_Frame_Size: int: Range: 20 ms | 40 ms | 80 ms"""
		__meta_args_list = [
			ArgStruct.scalar_int('Fwd_Frame_Size'),
			ArgStruct.scalar_int('Rev_Frame_Size')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Fwd_Frame_Size: int = None
			self.Rev_Frame_Size: int = None

	def get_fsize(self) -> FsizeStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:LAYer:SCH:FSIZe \n
		Snippet: value: FsizeStruct = driver.configure.layer.sch.get_fsize() \n
		Queries frame size of F-SCH and R-SCH. See Table 'F-SCH Walsh codes dependencies on MuxPDUs per physical layer SDU, RC
		and frame type for frame size 20 ms' \n
			:return: structure: for return value, see the help for FsizeStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:LAYer:SCH:FSIZe?', self.__class__.FsizeStruct())

	# noinspection PyTypeChecker
	class CodingStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Fwd_Coding: enums.ForwardCoding: CONV | TURB
			- Rev_Coding: enums.ForwardCoding: CONV | TURB"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Fwd_Coding', enums.ForwardCoding),
			ArgStruct.scalar_enum('Rev_Coding', enums.ForwardCoding)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Fwd_Coding: enums.ForwardCoding = None
			self.Rev_Coding: enums.ForwardCoding = None

	# noinspection PyTypeChecker
	def get_coding(self) -> CodingStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:LAYer:SCH:CODing \n
		Snippet: value: CodingStruct = driver.configure.layer.sch.get_coding() \n
		Sets a type of error-correcting code for F-SCH and R-SCH. For details, see 3GPP2 C.S0005. \n
			:return: structure: for return value, see the help for CodingStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:LAYer:SCH:CODing?', self.__class__.CodingStruct())

	def set_coding(self, value: CodingStruct) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:LAYer:SCH:CODing \n
		Snippet: driver.configure.layer.sch.set_coding(value = CodingStruct()) \n
		Sets a type of error-correcting code for F-SCH and R-SCH. For details, see 3GPP2 C.S0005. \n
			:param value: see the help for CodingStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:CDMA:SIGNaling<Instance>:LAYer:SCH:CODing', value)
