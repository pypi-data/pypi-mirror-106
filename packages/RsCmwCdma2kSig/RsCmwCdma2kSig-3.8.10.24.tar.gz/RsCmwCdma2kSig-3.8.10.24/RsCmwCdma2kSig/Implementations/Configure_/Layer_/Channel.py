from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Channel:
	"""Channel commands group definition. 6 total commands, 2 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("channel", core, parent)

	@property
	def fch(self):
		"""fch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fch'):
			from .Channel_.Fch import Fch
			self._fch = Fch(self._core, self._base)
		return self._fch

	@property
	def sch(self):
		"""sch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sch'):
			from .Channel_.Sch import Sch
			self._sch = Sch(self._core, self._base)
		return self._sch

	# noinspection PyTypeChecker
	class PichStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Spreading_Factor: int: Queries the spreading factor of the physical forward channel. The spreading factor corresponds to the length of the employed Walsh code. The Walsh code to be used is specified by the standard and cannot be chosen. Range: 1 to 128
			- Walsh_Code: int: Defines the channelization code of the physical forward channel. For PCH, PICH and sync it is fixed. Range: 1 to 128"""
		__meta_args_list = [
			ArgStruct.scalar_int('Spreading_Factor'),
			ArgStruct.scalar_int('Walsh_Code')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Spreading_Factor: int = None
			self.Walsh_Code: int = None

	def get_pich(self) -> PichStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:LAYer:CHANnel:PICH \n
		Snippet: value: PichStruct = driver.configure.layer.channel.get_pich() \n
		Queries the spreading factor (SF) and the Walsh code. For PCH, PICH, QPCH and sync the Walsh code to be used is specified
		by the standard and therefore it cannot be chosen. See also: 'Channelization Codes' \n
			:return: structure: for return value, see the help for PichStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:LAYer:CHANnel:PICH?', self.__class__.PichStruct())

	# noinspection PyTypeChecker
	class PchStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Spreading_Factor: int: Queries the spreading factor of the physical forward channel. The spreading factor corresponds to the length of the employed Walsh code. The Walsh code to be used is specified by the standard and cannot be chosen. Range: 1 to 128
			- Walsh_Code: int: Defines the channelization code of the physical forward channel. For PCH, PICH and sync it is fixed. Range: 1 to 128"""
		__meta_args_list = [
			ArgStruct.scalar_int('Spreading_Factor'),
			ArgStruct.scalar_int('Walsh_Code')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Spreading_Factor: int = None
			self.Walsh_Code: int = None

	def get_pch(self) -> PchStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:LAYer:CHANnel:PCH \n
		Snippet: value: PchStruct = driver.configure.layer.channel.get_pch() \n
		Queries the spreading factor (SF) and the Walsh code. For PCH, PICH, QPCH and sync the Walsh code to be used is specified
		by the standard and therefore it cannot be chosen. See also: 'Channelization Codes' \n
			:return: structure: for return value, see the help for PchStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:LAYer:CHANnel:PCH?', self.__class__.PchStruct())

	# noinspection PyTypeChecker
	class QpchStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Spreading_Factor: int: Queries the spreading factor of the physical forward channel. The spreading factor corresponds to the length of the employed Walsh code. The Walsh code to be used is specified by the standard and cannot be chosen. Range: 1 to 128
			- Walsh_Code: int: Defines the channelization code of the physical forward channel. For PCH, PICH and sync it is fixed. Range: 1 to 128"""
		__meta_args_list = [
			ArgStruct.scalar_int('Spreading_Factor'),
			ArgStruct.scalar_int('Walsh_Code')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Spreading_Factor: int = None
			self.Walsh_Code: int = None

	def get_qpch(self) -> QpchStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:LAYer:CHANnel:QPCH \n
		Snippet: value: QpchStruct = driver.configure.layer.channel.get_qpch() \n
		Queries the spreading factor (SF) and the Walsh code. For PCH, PICH, QPCH and sync the Walsh code to be used is specified
		by the standard and therefore it cannot be chosen. See also: 'Channelization Codes' \n
			:return: structure: for return value, see the help for QpchStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:LAYer:CHANnel:QPCH?', self.__class__.QpchStruct())

	# noinspection PyTypeChecker
	class SyncStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Spreading_Factor: int: Queries the spreading factor of the physical forward channel. The spreading factor corresponds to the length of the employed Walsh code. The Walsh code to be used is specified by the standard and cannot be chosen. Range: 1 to 128
			- Walsh_Code: int: Defines the channelization code of the physical forward channel. For PCH, PICH and sync it is fixed. Range: 1 to 128"""
		__meta_args_list = [
			ArgStruct.scalar_int('Spreading_Factor'),
			ArgStruct.scalar_int('Walsh_Code')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Spreading_Factor: int = None
			self.Walsh_Code: int = None

	def get_sync(self) -> SyncStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:LAYer:CHANnel:SYNC \n
		Snippet: value: SyncStruct = driver.configure.layer.channel.get_sync() \n
		Queries the spreading factor (SF) and the Walsh code. For PCH, PICH, QPCH and sync the Walsh code to be used is specified
		by the standard and therefore it cannot be chosen. See also: 'Channelization Codes' \n
			:return: structure: for return value, see the help for SyncStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:LAYer:CHANnel:SYNC?', self.__class__.SyncStruct())

	def clone(self) -> 'Channel':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Channel(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
