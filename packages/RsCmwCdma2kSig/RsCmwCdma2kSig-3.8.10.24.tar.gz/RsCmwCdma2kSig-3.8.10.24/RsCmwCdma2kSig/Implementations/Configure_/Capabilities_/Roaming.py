from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Roaming:
	"""Roaming commands group definition. 4 total commands, 0 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("roaming", core, parent)

	def get_oclass(self) -> int:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:ROAMing:OCLass \n
		Snippet: value: int = driver.configure.capabilities.roaming.get_oclass() \n
		Queries MS overload class. \n
			:return: overloaded_class: Range: 0 to 15
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:ROAMing:OCLass?')
		return Conversions.str_to_int(response)

	# noinspection PyTypeChecker
	def get_home(self) -> enums.Supported:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:ROAMing:HOME \n
		Snippet: value: enums.Supported = driver.configure.capabilities.roaming.get_home() \n
		Queries MS capability about the home registration functionality. \n
			:return: enable: NSUP | SUPP NSUP: Not supported SUPP: Supported
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:ROAMing:HOME?')
		return Conversions.str_to_scalar_enum(response, enums.Supported)

	# noinspection PyTypeChecker
	class SidStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: bool: OFF | ON
			- Sid: List[int]: 16-bit system identity code. Range: 0 to 65535"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct('Sid', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Sid: List[int] = None

	def get_sid(self) -> SidStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:ROAMing:SID \n
		Snippet: value: SidStruct = driver.configure.capabilities.roaming.get_sid() \n
		Queries information about the MS foreign roaming registration SID. \n
			:return: structure: for return value, see the help for SidStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:ROAMing:SID?', self.__class__.SidStruct())

	# noinspection PyTypeChecker
	class NidStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: bool: OFF | ON
			- Nid: List[int]: 16-bit network identity code. Range: 0 to 65535"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct('Nid', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Nid: List[int] = None

	def get_nid(self) -> NidStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:ROAMing:NID \n
		Snippet: value: NidStruct = driver.configure.capabilities.roaming.get_nid() \n
		Queries MS information whether the foreign roaming registration is enabled or not and the current network identity (NID)
		code. Parameter result list: <Enable>, <NID>... \n
			:return: structure: for return value, see the help for NidStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:ROAMing:NID?', self.__class__.NidStruct())
