from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FdrSupport:
	"""FdrSupport commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("fdrSupport", core, parent)

	# noinspection PyTypeChecker
	class FchStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Forward_Fch: bool: No parameter help available
			- Reverse_Fch: bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Forward_Fch'),
			ArgStruct.scalar_bool('Reverse_Fch')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Forward_Fch: bool = None
			self.Reverse_Fch: bool = None

	def get_fch(self) -> FchStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:FDRSupport:FCH \n
		Snippet: value: FchStruct = driver.configure.capabilities.fdrSupport.get_fch() \n
		Queries whether the MS supports the flexible data rate (FDR) for the corresponding forward and the reverse channel. This
		command is available for the fundamental channel (FCH) , dedicated control channel (DCCH) and supplemental channel (SCH) . \n
			:return: structure: for return value, see the help for FchStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:FDRSupport:FCH?', self.__class__.FchStruct())

	# noinspection PyTypeChecker
	class DcchStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Forward_Dcch: bool: OFF | ON FDR support for the forward channel.
			- Reverse_Dcch: bool: OFF | ON FDR support for the reverse channel."""
		__meta_args_list = [
			ArgStruct.scalar_bool('Forward_Dcch'),
			ArgStruct.scalar_bool('Reverse_Dcch')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Forward_Dcch: bool = None
			self.Reverse_Dcch: bool = None

	def get_dcch(self) -> DcchStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:FDRSupport:DCCH \n
		Snippet: value: DcchStruct = driver.configure.capabilities.fdrSupport.get_dcch() \n
		Queries whether the MS supports the flexible data rate (FDR) for the corresponding forward and the reverse channel. This
		command is available for the fundamental channel (FCH) , dedicated control channel (DCCH) and supplemental channel (SCH) . \n
			:return: structure: for return value, see the help for DcchStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:FDRSupport:DCCH?', self.__class__.DcchStruct())

	# noinspection PyTypeChecker
	class SchStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Forward_Sch: bool: No parameter help available
			- Reverse_Sch: bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Forward_Sch'),
			ArgStruct.scalar_bool('Reverse_Sch')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Forward_Sch: bool = None
			self.Reverse_Sch: bool = None

	def get_sch(self) -> SchStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:FDRSupport:SCH \n
		Snippet: value: SchStruct = driver.configure.capabilities.fdrSupport.get_sch() \n
		Queries whether the MS supports the flexible data rate (FDR) for the corresponding forward and the reverse channel. This
		command is available for the fundamental channel (FCH) , dedicated control channel (DCCH) and supplemental channel (SCH) . \n
			:return: structure: for return value, see the help for SchStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:FDRSupport:SCH?', self.__class__.SchStruct())
