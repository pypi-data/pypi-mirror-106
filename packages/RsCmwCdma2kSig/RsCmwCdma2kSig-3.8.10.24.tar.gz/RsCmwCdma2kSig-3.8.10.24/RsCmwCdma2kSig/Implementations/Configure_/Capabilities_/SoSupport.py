from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SoSupport:
	"""SoSupport commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("soSupport", core, parent)

	# noinspection PyTypeChecker
	class FfchStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Number: int: Service option number. Range: 0 to 99
			- Name: List[str]: Service option name.
			- State: List[bool]: OFF | ON"""
		__meta_args_list = [
			ArgStruct.scalar_int('Number'),
			ArgStruct('Name', DataType.StringList, None, False, True, 1),
			ArgStruct('State', DataType.BooleanList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Number: int = None
			self.Name: List[str] = None
			self.State: List[bool] = None

	def get_ffch(self) -> FfchStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:SOSupport:FFCH \n
		Snippet: value: FfchStruct = driver.configure.capabilities.soSupport.get_ffch() \n
		Queries which service options the MS supports on the forward fundamental channel. Returns the supported service option in
		the form <Number>{, <Name>, <State>}... for all supported service options (see 'Service Options ') . \n
			:return: structure: for return value, see the help for FfchStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:SOSupport:FFCH?', self.__class__.FfchStruct())

	# noinspection PyTypeChecker
	class RfchStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Number: int: Service option number. Range: 0 to 99
			- Name: List[str]: Service option name.
			- State: List[bool]: OFF | ON"""
		__meta_args_list = [
			ArgStruct.scalar_int('Number'),
			ArgStruct('Name', DataType.StringList, None, False, True, 1),
			ArgStruct('State', DataType.BooleanList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Number: int = None
			self.Name: List[str] = None
			self.State: List[bool] = None

	def get_rfch(self) -> RfchStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:SOSupport:RFCH \n
		Snippet: value: RfchStruct = driver.configure.capabilities.soSupport.get_rfch() \n
		Queries which service options the MS supports on the reverse fundamental channel. Returns the supported service option in
		the form <Number>{, <Name>, <State>}... for all supported service options (see 'Service Options ') . \n
			:return: structure: for return value, see the help for RfchStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:SOSupport:RFCH?', self.__class__.RfchStruct())
