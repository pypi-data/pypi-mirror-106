from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Registration:
	"""Registration commands group definition. 8 total commands, 0 Sub-groups, 8 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("registration", core, parent)

	def get_dbased(self) -> float or bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:REGistration:DBASed \n
		Snippet: value: float or bool = driver.configure.network.registration.get_dbased() \n
		Gets/sets the distance threshold for distance-based registration. See 'Distance-based Registration' for details. Setting
		the value to 0 disables distance-based registration. \n
			:return: distance_based: Range: 0 to 2047 (#H7FF) Additional OFF/ON disables / enables the distance-based registration.
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:REGistration:DBASed?')
		return Conversions.str_to_float_or_bool(response)

	def set_dbased(self, distance_based: float or bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:REGistration:DBASed \n
		Snippet: driver.configure.network.registration.set_dbased(distance_based = 1.0) \n
		Gets/sets the distance threshold for distance-based registration. See 'Distance-based Registration' for details. Setting
		the value to 0 disables distance-based registration. \n
			:param distance_based: Range: 0 to 2047 (#H7FF) Additional OFF/ON disables / enables the distance-based registration.
		"""
		param = Conversions.decimal_or_bool_value_to_str(distance_based)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:REGistration:DBASed {param}')

	def get_tbased(self) -> float or bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:REGistration:TBASed \n
		Snippet: value: float or bool = driver.configure.network.registration.get_tbased() \n
		Turns timer-based registration OFF/ON and/or defines the registration interval in seconds. A numeric value must be
		between 12.16 and 199515.84, inclusive; it is rounded to the closest value in: See 'Timer-based Registration' for details. \n
			:return: timer_based: Range: OFF | ON | 12.16 | 14.48 | 17.20 | 20.48 | 24.32 | 28.96 | 34.40 | 40.96 | 48.64 | 57.92 | 68.88 | 81.92 | 97.36 | 115.84 | 137.76 | 163.84 | 194.80 | 231.68 | 275.52 | 327.68 | 389.60 | 463.36 | 551.04 | 655.36 | 779.28 | 926.80 | 1102.16 | 1310.72 | 1558.64 | 1853.60 | 2204.32 | 2621.44 | 3117.36 | 3707.20 | 4408.64 | 5242.88 | 6234.80 | 7414.48 | 8817.36 | 10485.76 | 12469.68 | 14829.04 | 17634.80 | 20971.52 | 24939.44 | 29658.16 | 35269.68 | 41943.04 | 49878.96 | 59316.40 | 70529.44 | 83886.08 | 99757.92 | 118632.80 | 141078.96 | 167772.16 | 199515.84 Additional OFF/ON disables / enables the timer-based registration.
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:REGistration:TBASed?')
		return Conversions.str_to_float_or_bool(response)

	def set_tbased(self, timer_based: float or bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:REGistration:TBASed \n
		Snippet: driver.configure.network.registration.set_tbased(timer_based = 1.0) \n
		Turns timer-based registration OFF/ON and/or defines the registration interval in seconds. A numeric value must be
		between 12.16 and 199515.84, inclusive; it is rounded to the closest value in: See 'Timer-based Registration' for details. \n
			:param timer_based: Range: OFF | ON | 12.16 | 14.48 | 17.20 | 20.48 | 24.32 | 28.96 | 34.40 | 40.96 | 48.64 | 57.92 | 68.88 | 81.92 | 97.36 | 115.84 | 137.76 | 163.84 | 194.80 | 231.68 | 275.52 | 327.68 | 389.60 | 463.36 | 551.04 | 655.36 | 779.28 | 926.80 | 1102.16 | 1310.72 | 1558.64 | 1853.60 | 2204.32 | 2621.44 | 3117.36 | 3707.20 | 4408.64 | 5242.88 | 6234.80 | 7414.48 | 8817.36 | 10485.76 | 12469.68 | 14829.04 | 17634.80 | 20971.52 | 24939.44 | 29658.16 | 35269.68 | 41943.04 | 49878.96 | 59316.40 | 70529.44 | 83886.08 | 99757.92 | 118632.80 | 141078.96 | 167772.16 | 199515.84 Additional OFF/ON disables / enables the timer-based registration.
		"""
		param = Conversions.decimal_or_bool_value_to_str(timer_based)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:REGistration:TBASed {param}')

	def get_home(self) -> bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:REGistration:HOME \n
		Snippet: value: bool = driver.configure.network.registration.get_home() \n
		Enables or disables autonomous registrations for home users, see 'Autonomous Registration (Home / Foreign SID / Foreign
		NID) '. Use method RsCmwCdma2kSig.Configure.Network.System.sid and method RsCmwCdma2kSig.Configure.Network.Identity.
		nid to set the system and network ID. \n
			:return: home: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:REGistration:HOME?')
		return Conversions.str_to_bool(response)

	def set_home(self, home: bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:REGistration:HOME \n
		Snippet: driver.configure.network.registration.set_home(home = False) \n
		Enables or disables autonomous registrations for home users, see 'Autonomous Registration (Home / Foreign SID / Foreign
		NID) '. Use method RsCmwCdma2kSig.Configure.Network.System.sid and method RsCmwCdma2kSig.Configure.Network.Identity.
		nid to set the system and network ID. \n
			:param home: OFF | ON
		"""
		param = Conversions.bool_to_str(home)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:REGistration:HOME {param}')

	def get_fsid(self) -> bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:REGistration:FSID \n
		Snippet: value: bool = driver.configure.network.registration.get_fsid() \n
		Enables or disables autonomous registrations for foreign SID roamers, see 'Autonomous Registration (Home / Foreign SID /
		Foreign NID) '. Use method RsCmwCdma2kSig.Configure.Network.System.sid to set the system ID. \n
			:return: foreign_sid: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:REGistration:FSID?')
		return Conversions.str_to_bool(response)

	def set_fsid(self, foreign_sid: bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:REGistration:FSID \n
		Snippet: driver.configure.network.registration.set_fsid(foreign_sid = False) \n
		Enables or disables autonomous registrations for foreign SID roamers, see 'Autonomous Registration (Home / Foreign SID /
		Foreign NID) '. Use method RsCmwCdma2kSig.Configure.Network.System.sid to set the system ID. \n
			:param foreign_sid: OFF | ON
		"""
		param = Conversions.bool_to_str(foreign_sid)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:REGistration:FSID {param}')

	def get_fnid(self) -> bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:REGistration:FNID \n
		Snippet: value: bool = driver.configure.network.registration.get_fnid() \n
		Enables or disables autonomous registrations for foreign SID roamers, see 'Autonomous Registration (Home / Foreign SID /
		Foreign NID) '. Use method RsCmwCdma2kSig.Configure.Network.System.sid and method RsCmwCdma2kSig.Configure.Network.
		Identity.nid to set the system and network ID. \n
			:return: foreign_nid: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:REGistration:FNID?')
		return Conversions.str_to_bool(response)

	def set_fnid(self, foreign_nid: bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:REGistration:FNID \n
		Snippet: driver.configure.network.registration.set_fnid(foreign_nid = False) \n
		Enables or disables autonomous registrations for foreign SID roamers, see 'Autonomous Registration (Home / Foreign SID /
		Foreign NID) '. Use method RsCmwCdma2kSig.Configure.Network.System.sid and method RsCmwCdma2kSig.Configure.Network.
		Identity.nid to set the system and network ID. \n
			:param foreign_nid: OFF | ON
		"""
		param = Conversions.bool_to_str(foreign_nid)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:REGistration:FNID {param}')

	def get_pup(self) -> bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:REGistration:PUP \n
		Snippet: value: bool = driver.configure.network.registration.get_pup() \n
		Enables or disables power-up registration, see 'Power-up Registration'. \n
			:return: power_up: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:REGistration:PUP?')
		return Conversions.str_to_bool(response)

	def set_pup(self, power_up: bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:REGistration:PUP \n
		Snippet: driver.configure.network.registration.set_pup(power_up = False) \n
		Enables or disables power-up registration, see 'Power-up Registration'. \n
			:param power_up: OFF | ON
		"""
		param = Conversions.bool_to_str(power_up)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:REGistration:PUP {param}')

	def get_pdown(self) -> bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:REGistration:PDOWn \n
		Snippet: value: bool = driver.configure.network.registration.get_pdown() \n
		Enables or disables power-down registration, see 'Power-down Registration'. \n
			:return: power_down: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:REGistration:PDOWn?')
		return Conversions.str_to_bool(response)

	def set_pdown(self, power_down: bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:REGistration:PDOWn \n
		Snippet: driver.configure.network.registration.set_pdown(power_down = False) \n
		Enables or disables power-down registration, see 'Power-down Registration'. \n
			:param power_down: OFF | ON
		"""
		param = Conversions.bool_to_str(power_down)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:REGistration:PDOWn {param}')

	def get_parameter(self) -> bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:REGistration:PARameter \n
		Snippet: value: bool = driver.configure.network.registration.get_parameter() \n
		Enables or disables parameter-change registration, see 'Parameter-change Registration'. \n
			:return: parameter_reg: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:REGistration:PARameter?')
		return Conversions.str_to_bool(response)

	def set_parameter(self, parameter_reg: bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:REGistration:PARameter \n
		Snippet: driver.configure.network.registration.set_parameter(parameter_reg = False) \n
		Enables or disables parameter-change registration, see 'Parameter-change Registration'. \n
			:param parameter_reg: OFF | ON
		"""
		param = Conversions.bool_to_str(parameter_reg)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:REGistration:PARameter {param}')
