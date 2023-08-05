from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rwin:
	"""Rwin commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rwin", core, parent)

	def set(self, window_size: int) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:SYSTem:RWIN \n
		Snippet: driver.configure.network.system.rwin.set(window_size = 1) \n
			INTRO_CMD_HELP: Search window size (index) for \n
			- The active set and candidate set (SRCH_WIN_Asystem parameter → AWIN suffix)
			- The neighbor set (SRCH_WIN_N system parameter → NWIN suffix)
			- The remaining set (SRCH_WIN_R system parameter → RWIN suffix)
		The search window size is the number of PN chips specified in the following table:
			Table Header: SRCH_WIN_A SRCH_WIN_N SRCH_WIN_R / Window_size (PN chips) / SRCH_WIN_A SRCH_WIN_N SRCH_WIN_NGHB R SRCH_WIN_R CF_SRCH_WIN_N / Window_size (PN chips) \n
			- 0 / 4 / 8 / 60
			- 1 / 6 / 9 / 80
			- 2 / 8 / 10 / 100
			- 3 / 10 / 11 / 130
			- 4 / 14 / 12 / 160
			- 5 / 20 / 13 / 226
			- 6 / 28 / 14 / 320
			- 7 / 40 / 15 / 452 \n
			:param window_size: Window size index Range: 0 to 15
		"""
		param = Conversions.decimal_value_to_str(window_size)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:SYSTem:RWIN {param}')

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Window_Size: int: Window size index Range: 0 to 15
			- Pn_Chips: enums.PnChips: C4 | C6 | C8 | C10 | C14 | C20 | C28 | C40 | C60 | C80 | C100 | C130 | C160 | C226 | C320 | C452 Window size as number of PN chips"""
		__meta_args_list = [
			ArgStruct.scalar_int('Window_Size'),
			ArgStruct.scalar_enum('Pn_Chips', enums.PnChips)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Window_Size: int = None
			self.Pn_Chips: enums.PnChips = None

	def get(self) -> GetStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:SYSTem:RWIN \n
		Snippet: value: GetStruct = driver.configure.network.system.rwin.get() \n
			INTRO_CMD_HELP: Search window size (index) for \n
			- The active set and candidate set (SRCH_WIN_Asystem parameter → AWIN suffix)
			- The neighbor set (SRCH_WIN_N system parameter → NWIN suffix)
			- The remaining set (SRCH_WIN_R system parameter → RWIN suffix)
		The search window size is the number of PN chips specified in the following table:
			Table Header: SRCH_WIN_A SRCH_WIN_N SRCH_WIN_R / Window_size (PN chips) / SRCH_WIN_A SRCH_WIN_N SRCH_WIN_NGHB R SRCH_WIN_R CF_SRCH_WIN_N / Window_size (PN chips) \n
			- 0 / 4 / 8 / 60
			- 1 / 6 / 9 / 80
			- 2 / 8 / 10 / 100
			- 3 / 10 / 11 / 130
			- 4 / 14 / 12 / 160
			- 5 / 20 / 13 / 226
			- 6 / 28 / 14 / 320
			- 7 / 40 / 15 / 452 \n
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:SYSTem:RWIN?', self.__class__.GetStruct())
