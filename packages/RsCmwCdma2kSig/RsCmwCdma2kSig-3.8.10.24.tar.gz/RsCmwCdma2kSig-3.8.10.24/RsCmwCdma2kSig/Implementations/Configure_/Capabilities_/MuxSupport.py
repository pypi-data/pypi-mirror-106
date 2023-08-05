from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MuxSupport:
	"""MuxSupport commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("muxSupport", core, parent)

	# noinspection PyTypeChecker
	class FwdStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Number: int: Number of the used multiplex option. Range: 0 to 99
			- Name: List[str]: Name of the forward channel (I.e. FCH)
			- State_Full: List[bool]: OFF | ON
			- State_Half: List[bool]: OFF | ON
			- State_Quarter: List[bool]: OFF | ON
			- State_Eighth: List[bool]: OFF | ON"""
		__meta_args_list = [
			ArgStruct.scalar_int('Number'),
			ArgStruct('Name', DataType.StringList, None, False, True, 1),
			ArgStruct('State_Full', DataType.BooleanList, None, False, True, 1),
			ArgStruct('State_Half', DataType.BooleanList, None, False, True, 1),
			ArgStruct('State_Quarter', DataType.BooleanList, None, False, True, 1),
			ArgStruct('State_Eighth', DataType.BooleanList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Number: int = None
			self.Name: List[str] = None
			self.State_Full: List[bool] = None
			self.State_Half: List[bool] = None
			self.State_Quarter: List[bool] = None
			self.State_Eighth: List[bool] = None

	def get_fwd(self) -> FwdStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:MUXSupport:FWD \n
		Snippet: value: FwdStruct = driver.configure.capabilities.muxSupport.get_fwd() \n
		Queries MS capabilities about MUX support on the forward channel. Refer to 3GPP2 C.S0003-C. <Number>{, <Name>,
		<StateFull>, <StateHalf>, <StateQuarter>, <StateEighth>}.. \n
			:return: structure: for return value, see the help for FwdStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:MUXSupport:FWD?', self.__class__.FwdStruct())

	# noinspection PyTypeChecker
	class RevStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Number: int: Number of the used multiplex option. Range: 0 to 99
			- Name: List[str]: Name of the reverse channel (I.e. FCH)
			- State_Full: List[bool]: OFF | ON
			- State_Half: List[bool]: OFF | ON
			- State_Quarter: List[bool]: OFF | ON
			- State_Eighth: List[bool]: OFF | ON"""
		__meta_args_list = [
			ArgStruct.scalar_int('Number'),
			ArgStruct('Name', DataType.StringList, None, False, True, 1),
			ArgStruct('State_Full', DataType.BooleanList, None, False, True, 1),
			ArgStruct('State_Half', DataType.BooleanList, None, False, True, 1),
			ArgStruct('State_Quarter', DataType.BooleanList, None, False, True, 1),
			ArgStruct('State_Eighth', DataType.BooleanList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Number: int = None
			self.Name: List[str] = None
			self.State_Full: List[bool] = None
			self.State_Half: List[bool] = None
			self.State_Quarter: List[bool] = None
			self.State_Eighth: List[bool] = None

	def get_rev(self) -> RevStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:MUXSupport:REV \n
		Snippet: value: RevStruct = driver.configure.capabilities.muxSupport.get_rev() \n
		Queries MS capabilities about MUX support on the reverse channel. Refer to 3GPP2 C.S0003-C. <Number>{, <Name>,
		<StateFull>, <StateHalf>, <StateQuarter>, <StateEighth>}.. \n
			:return: structure: for return value, see the help for RevStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:MUXSupport:REV?', self.__class__.RevStruct())
