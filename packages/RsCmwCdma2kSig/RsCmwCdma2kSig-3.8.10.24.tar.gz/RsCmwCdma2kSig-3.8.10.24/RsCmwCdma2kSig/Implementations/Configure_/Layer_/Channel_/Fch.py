from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fch:
	"""Fch commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("fch", core, parent)

	def set(self, walsh_code: int, qof: int) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:LAYer:CHANnel:FCH \n
		Snippet: driver.configure.layer.channel.fch.set(walsh_code = 1, qof = 1) \n
		Defines the Walsh code, quasi-orthogonal function and shows the used spreading factor. See also:
			- 'Channel Overview'
			- 'Channelization Codes' \n
			:param walsh_code: Sets the channelization code of the physical forward channel. Range: 2 to 63
			:param qof: The quasi-orthogonal function (QOF) is only available for a forward radio configurations (F-RC) 3 to 5. Range: 0 to 3
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('walsh_code', walsh_code, DataType.Integer), ArgSingle('qof', qof, DataType.Integer))
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:LAYer:CHANnel:FCH {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Spreading_Factor: int: Queries the spreading factor of the physical forward channel (fixed for FCH) . Range: 64
			- Walsh_Code: int: Sets the channelization code of the physical forward channel. Range: 2 to 63
			- Qof: int: The quasi-orthogonal function (QOF) is only available for a forward radio configurations (F-RC) 3 to 5. Range: 0 to 3"""
		__meta_args_list = [
			ArgStruct.scalar_int('Spreading_Factor'),
			ArgStruct.scalar_int('Walsh_Code'),
			ArgStruct.scalar_int('Qof')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Spreading_Factor: int = None
			self.Walsh_Code: int = None
			self.Qof: int = None

	def get(self) -> GetStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:LAYer:CHANnel:FCH \n
		Snippet: value: GetStruct = driver.configure.layer.channel.fch.get() \n
		Defines the Walsh code, quasi-orthogonal function and shows the used spreading factor. See also:
			- 'Channel Overview'
			- 'Channelization Codes' \n
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:CDMA:SIGNaling<Instance>:LAYer:CHANnel:FCH?', self.__class__.GetStruct())
