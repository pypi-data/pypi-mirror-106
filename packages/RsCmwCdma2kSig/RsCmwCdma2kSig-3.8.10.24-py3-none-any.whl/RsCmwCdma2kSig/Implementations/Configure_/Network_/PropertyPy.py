from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PropertyPy:
	"""PropertyPy commands group definition. 7 total commands, 0 Sub-groups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("propertyPy", core, parent)

	def get_pn_offset(self) -> int:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:PROPerty:PNOFfset \n
		Snippet: value: int = driver.configure.network.propertyPy.get_pn_offset() \n
		Sets the offset of the PN sequence. Changing the PN offset changes the timing of the pilot channel, the timing and
		contents of the sync channel message, and the long code mask of the paging channel. \n
			:return: pn_offset: Range: 0 to 511
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:PROPerty:PNOFfset?')
		return Conversions.str_to_int(response)

	def set_pn_offset(self, pn_offset: int) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:PROPerty:PNOFfset \n
		Snippet: driver.configure.network.propertyPy.set_pn_offset(pn_offset = 1) \n
		Sets the offset of the PN sequence. Changing the PN offset changes the timing of the pilot channel, the timing and
		contents of the sync channel message, and the long code mask of the paging channel. \n
			:param pn_offset: Range: 0 to 511
		"""
		param = Conversions.decimal_value_to_str(pn_offset)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:PROPerty:PNOFfset {param}')

	def get_cld_time(self) -> int or bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:PROPerty:CLDTime \n
		Snippet: value: int or bool = driver.configure.network.propertyPy.get_cld_time() \n
		Sets the value of the fade timer to detect when a call is lost or dropped. \n
			:return: cld_time: Range: 1 s to 5 s, Unit: s Additional parameters: OFF | ON (disables | enables the timer)
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:PROPerty:CLDTime?')
		return Conversions.str_to_int_or_bool(response)

	def set_cld_time(self, cld_time: int or bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:PROPerty:CLDTime \n
		Snippet: driver.configure.network.propertyPy.set_cld_time(cld_time = 1) \n
		Sets the value of the fade timer to detect when a call is lost or dropped. \n
			:param cld_time: Range: 1 s to 5 s, Unit: s Additional parameters: OFF | ON (disables | enables the timer)
		"""
		param = Conversions.decimal_or_bool_value_to_str(cld_time)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:PROPerty:CLDTime {param}')

	def get_pr_timeout(self) -> int:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:PROPerty:PRTimeout \n
		Snippet: value: int = driver.configure.network.propertyPy.get_pr_timeout() \n
		Sets the timeout value of the page timer to define the maximum time the R&S CMW attempts to page the MS. \n
			:return: pr_timeout: Range: 5 to 15 , Unit: seconds
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:PROPerty:PRTimeout?')
		return Conversions.str_to_int(response)

	def set_pr_timeout(self, pr_timeout: int) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:PROPerty:PRTimeout \n
		Snippet: driver.configure.network.propertyPy.set_pr_timeout(pr_timeout = 1) \n
		Sets the timeout value of the page timer to define the maximum time the R&S CMW attempts to page the MS. \n
			:param pr_timeout: Range: 5 to 15 , Unit: seconds
		"""
		param = Conversions.decimal_value_to_str(pr_timeout)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:PROPerty:PRTimeout {param}')

	def get_lt_offset(self) -> int:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:PROPerty:LTOFfset \n
		Snippet: value: int = driver.configure.network.propertyPy.get_lt_offset() \n
		Specifies the local time offset from CDMA system time. It ranged from 0 to +63, which represents a range from –16:00 ...
		+15:30 hours in 30 minute increments. See also GUI description, 'Local Time Offset'. \n
			:return: local_time_offset: Range: 0 to 63
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:PROPerty:LTOFfset?')
		return Conversions.str_to_int(response)

	def set_lt_offset(self, local_time_offset: int) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:PROPerty:LTOFfset \n
		Snippet: driver.configure.network.propertyPy.set_lt_offset(local_time_offset = 1) \n
		Specifies the local time offset from CDMA system time. It ranged from 0 to +63, which represents a range from –16:00 ...
		+15:30 hours in 30 minute increments. See also GUI description, 'Local Time Offset'. \n
			:param local_time_offset: Range: 0 to 63
		"""
		param = Conversions.decimal_value_to_str(local_time_offset)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:PROPerty:LTOFfset {param}')

	def get_dl_savings(self) -> bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:PROPerty:DLSavings \n
		Snippet: value: bool = driver.configure.network.propertyPy.get_dl_savings() \n
		No command help available \n
			:return: daylight_savings: No help available
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:PROPerty:DLSavings?')
		return Conversions.str_to_bool(response)

	def set_dl_savings(self, daylight_savings: bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:PROPerty:DLSavings \n
		Snippet: driver.configure.network.propertyPy.set_dl_savings(daylight_savings = False) \n
		No command help available \n
			:param daylight_savings: No help available
		"""
		param = Conversions.bool_to_str(daylight_savings)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:PROPerty:DLSavings {param}')

	# noinspection PyTypeChecker
	class LatitudeStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Direction: enums.DirectionVertical: NORTh | SOUTh
			- Degrees: float: Range: 0 to 90
			- Minutes: float: Range: 0 to 59
			- Seconds: float: Range: 0 to 59.75"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Direction', enums.DirectionVertical),
			ArgStruct.scalar_float('Degrees'),
			ArgStruct.scalar_float('Minutes'),
			ArgStruct.scalar_float('Seconds')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Direction: enums.DirectionVertical = None
			self.Degrees: float = None
			self.Minutes: float = None
			self.Seconds: float = None

	# noinspection PyTypeChecker
	def get_latitude(self) -> LatitudeStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:PROPerty:LATitude \n
		Snippet: value: LatitudeStruct = driver.configure.network.propertyPy.get_latitude() \n
		Gets/sets the latitude (BASE_LATS parameter) of the base station, specified by its direction (north or south) and an
		angle between 0 degrees and 90 degrees with 0.25 seconds granularity. \n
			:return: structure: for return value, see the help for LatitudeStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:NETWork:PROPerty:LATitude?', self.__class__.LatitudeStruct())

	def set_latitude(self, value: LatitudeStruct) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:PROPerty:LATitude \n
		Snippet: driver.configure.network.propertyPy.set_latitude(value = LatitudeStruct()) \n
		Gets/sets the latitude (BASE_LATS parameter) of the base station, specified by its direction (north or south) and an
		angle between 0 degrees and 90 degrees with 0.25 seconds granularity. \n
			:param value: see the help for LatitudeStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:CDMA:SIGNaling<Instance>:NETWork:PROPerty:LATitude', value)

	# noinspection PyTypeChecker
	class LongitudeStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Direction: enums.DirectionHorizontal: EAST | WEST
			- Degrees: float: Range: 0 to 90
			- Minutes: float: Range: 0 to 59
			- Seconds: float: Range: 0 to 59.75"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Direction', enums.DirectionHorizontal),
			ArgStruct.scalar_float('Degrees'),
			ArgStruct.scalar_float('Minutes'),
			ArgStruct.scalar_float('Seconds')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Direction: enums.DirectionHorizontal = None
			self.Degrees: float = None
			self.Minutes: float = None
			self.Seconds: float = None

	# noinspection PyTypeChecker
	def get_longitude(self) -> LongitudeStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:PROPerty:LONGitude \n
		Snippet: value: LongitudeStruct = driver.configure.network.propertyPy.get_longitude() \n
		Gets/sets the longitude (BASE_LONGS parameter) of the base station, specified by its direction (west or east) and an
		angle between 0 degrees and 180 degrees with 0.25 seconds granularity. \n
			:return: structure: for return value, see the help for LongitudeStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:NETWork:PROPerty:LONGitude?', self.__class__.LongitudeStruct())

	def set_longitude(self, value: LongitudeStruct) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:PROPerty:LONGitude \n
		Snippet: driver.configure.network.propertyPy.set_longitude(value = LongitudeStruct()) \n
		Gets/sets the longitude (BASE_LONGS parameter) of the base station, specified by its direction (west or east) and an
		angle between 0 degrees and 180 degrees with 0.25 seconds granularity. \n
			:param value: see the help for LongitudeStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:CDMA:SIGNaling<Instance>:NETWork:PROPerty:LONGitude', value)
