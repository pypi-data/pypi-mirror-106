from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class VrSupport:
	"""VrSupport commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("vrSupport", core, parent)

	# noinspection PyTypeChecker
	class SchStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Forward_Sch: bool: OFF | ON
			- Reverse_Sch: bool: OFF | ON"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Forward_Sch'),
			ArgStruct.scalar_bool('Reverse_Sch')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Forward_Sch: bool = None
			self.Reverse_Sch: bool = None

	def get_sch(self) -> SchStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:VRSupport:SCH \n
		Snippet: value: SchStruct = driver.configure.capabilities.vrSupport.get_sch() \n
		Queries MS information whether the MS supports a variable rate set on the forward and reverse supplemental channel (F-SCH,
		R-SCH) . \n
			:return: structure: for return value, see the help for SchStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:VRSupport:SCH?', self.__class__.SchStruct())

	# noinspection PyTypeChecker
	class MsbitsStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Convol_Rates: int: Range: 0 to 65535 (16 bits)
			- Turbo_Code_Rates: int: Range: 0 to 65535 (16 bits)"""
		__meta_args_list = [
			ArgStruct.scalar_int('Convol_Rates'),
			ArgStruct.scalar_int('Turbo_Code_Rates')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Convol_Rates: int = None
			self.Turbo_Code_Rates: int = None

	def get_msbits(self) -> MsbitsStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:VRSupport:MSBits \n
		Snippet: value: MsbitsStruct = driver.configure.capabilities.vrSupport.get_msbits() \n
		Queries MS information about the maximum sum of number of bits corresponding to convolutional and turbo code rates in the
		variable rate set. Refer to 3GPP2 C.S0005 for details. \n
			:return: structure: for return value, see the help for MsbitsStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:VRSupport:MSBits?', self.__class__.MsbitsStruct())
