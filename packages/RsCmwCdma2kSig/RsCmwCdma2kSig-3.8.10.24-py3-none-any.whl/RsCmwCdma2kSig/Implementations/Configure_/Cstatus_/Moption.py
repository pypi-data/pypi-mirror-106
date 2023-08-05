from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Moption:
	"""Moption commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("moption", core, parent)

	# noinspection PyTypeChecker
	class FchStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Forward_Fch: str: Forward fundamental channel Range: #H0 to #HFFFF
			- Reverse_Fch: str: Reverse fundamental channel Range: #H0 to #HFFFF"""
		__meta_args_list = [
			ArgStruct.scalar_raw_str('Forward_Fch'),
			ArgStruct.scalar_raw_str('Reverse_Fch')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Forward_Fch: str = None
			self.Reverse_Fch: str = None

	def get_fch(self) -> FchStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:CSTatus:MOPTion:FCH \n
		Snippet: value: FchStruct = driver.configure.cstatus.moption.get_fch() \n
		Queries the connected forward and reverse multiplied options for the fundamental channel. \n
			:return: structure: for return value, see the help for FchStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:CSTatus:MOPTion:FCH?', self.__class__.FchStruct())

	# noinspection PyTypeChecker
	class SchStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Forward_Sch: str: Range: #H0 to #HFFFF
			- Reverse_Sch: str: Range: #H0 to #HFFFF"""
		__meta_args_list = [
			ArgStruct.scalar_raw_str('Forward_Sch'),
			ArgStruct.scalar_raw_str('Reverse_Sch')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Forward_Sch: str = None
			self.Reverse_Sch: str = None

	def get_sch(self) -> SchStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:CSTatus:MOPTion:SCH \n
		Snippet: value: SchStruct = driver.configure.cstatus.moption.get_sch() \n
		Queries MS multiplex option on the forward and reverse SCH0. Refer to 3GPP2 C.S0003. \n
			:return: structure: for return value, see the help for SchStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:CSTatus:MOPTion:SCH?', self.__class__.SchStruct())
