from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Drate:
	"""Drate commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("drate", core, parent)

	# noinspection PyTypeChecker
	class SchStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Forward_Sch: float: Range: 0 kbit/s to 999 kbit/s
			- Reverse_Sch: float: Range: 0 kbit/s to 999 kbit/s"""
		__meta_args_list = [
			ArgStruct.scalar_float('Forward_Sch'),
			ArgStruct.scalar_float('Reverse_Sch')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Forward_Sch: float = None
			self.Reverse_Sch: float = None

	def get_sch(self) -> SchStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:CSTatus:DRATe:SCH \n
		Snippet: value: SchStruct = driver.configure.cstatus.drate.get_sch() \n
		Displays data rate on SCH0. See Table 'SCH maximum data rate (kbit/s) dependencies on MuxPDUs per physical layer SDU, RC
		and frame type for frame size 20 ms' \n
			:return: structure: for return value, see the help for SchStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:CSTatus:DRATe:SCH?', self.__class__.SchStruct())
