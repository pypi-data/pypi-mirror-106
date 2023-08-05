from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Capabilities:
	"""Capabilities commands group definition. 22 total commands, 5 Sub-groups, 9 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("capabilities", core, parent)

	@property
	def soSupport(self):
		"""soSupport commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_soSupport'):
			from .Capabilities_.SoSupport import SoSupport
			self._soSupport = SoSupport(self._core, self._base)
		return self._soSupport

	@property
	def muxSupport(self):
		"""muxSupport commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_muxSupport'):
			from .Capabilities_.MuxSupport import MuxSupport
			self._muxSupport = MuxSupport(self._core, self._base)
		return self._muxSupport

	@property
	def roaming(self):
		"""roaming commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_roaming'):
			from .Capabilities_.Roaming import Roaming
			self._roaming = Roaming(self._core, self._base)
		return self._roaming

	@property
	def fdrSupport(self):
		"""fdrSupport commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_fdrSupport'):
			from .Capabilities_.FdrSupport import FdrSupport
			self._fdrSupport = FdrSupport(self._core, self._base)
		return self._fdrSupport

	@property
	def vrSupport(self):
		"""vrSupport commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_vrSupport'):
			from .Capabilities_.VrSupport import VrSupport
			self._vrSupport = VrSupport(self._core, self._base)
		return self._vrSupport

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:ENABle \n
		Snippet: value: bool = driver.configure.capabilities.get_enable() \n
		Enable or disable the MS capabilities report. \n
			:return: ms_report_enable: OFF | ON ON: Enable OFF: Disable
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, ms_report_enable: bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:ENABle \n
		Snippet: driver.configure.capabilities.set_enable(ms_report_enable = False) \n
		Enable or disable the MS capabilities report. \n
			:param ms_report_enable: OFF | ON ON: Enable OFF: Disable
		"""
		param = Conversions.bool_to_str(ms_report_enable)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:ENABle {param}')

	def get_bc_support(self) -> List[bool]:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:BCSupport \n
		Snippet: value: List[bool] = driver.configure.capabilities.get_bc_support() \n
		Queries the band class (BC) support from the MS. \n
			:return: bclass_support: OFF | ON 22 comma-separated values for BC 0 through BC 21
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:BCSupport?')
		return Conversions.str_to_bool_list(response)

	def get_sc_support(self) -> List[bool]:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:SCSupport \n
		Snippet: value: List[bool] = driver.configure.capabilities.get_sc_support() \n
		Queries which band subclasses are supported by the MS. \n
			:return: sclass_support: OFF | ON Returns the supported MS band subclass in the form: (OFF|ON) , (OFF|ON) , (OFF|ON) , (OFF|ON) , (OFF|ON) , (OFF|ON) , (OFF|ON) to indicate not supported (OFF) or supported (ON) for band subclasses 0 through 7.
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:SCSupport?')
		return Conversions.str_to_bool_list(response)

	# noinspection PyTypeChecker
	class TerminalStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Manufact_Code: int: MS manufacturer code number. Range: 0 to 999
			- Model_Number: int: MS model number. Range: 0 to 999
			- Fwa_Revision: int: MS firmware revision. Range: 0 to 32767
			- Local_Control: enums.Supported: NSUP | SUPP Local control. NSUP: Not supported SUPP: Supported
			- Rep_Serv_Options: int: Reported service options. Range: 0 to 999"""
		__meta_args_list = [
			ArgStruct.scalar_int('Manufact_Code'),
			ArgStruct.scalar_int('Model_Number'),
			ArgStruct.scalar_int('Fwa_Revision'),
			ArgStruct.scalar_enum('Local_Control', enums.Supported),
			ArgStruct.scalar_int('Rep_Serv_Options')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Manufact_Code: int = None
			self.Model_Number: int = None
			self.Fwa_Revision: int = None
			self.Local_Control: enums.Supported = None
			self.Rep_Serv_Options: int = None

	def get_terminal(self) -> TerminalStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:TERMinal \n
		Snippet: value: TerminalStruct = driver.configure.capabilities.get_terminal() \n
		Queries information about the MS terminal. \n
			:return: structure: for return value, see the help for TerminalStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:TERMinal?', self.__class__.TerminalStruct())

	# noinspection PyTypeChecker
	class GlocationStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Capabilities: enums.Supported: NSUP | SUPP Queries if the MS supports geo-location capabilities generally. NSUP: Not supported SUPP: Supported
			- Included: enums.Supported: NSUP | SUPP GEO_LOC_INCL. Geo-location included indicator. Specifies if the message on the R-SCH contains the GEO_LOC_TYPE field or not.
			- Type_Py: enums.GeoLocationType: NSUP | AFLT | AAG | GPS GEO_LOC_TYPE. Geo-location type. If parameter Included is set to SUPP, the supported geo-location type is shown with this parameter. NSUP: Not supported AFLT: Advanced forward link triangulation only. IS-801 capable. AAG: Advanced forward link triangulation and global positioning systems. IS-801 capable. GPS: Global positioning systems only."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Capabilities', enums.Supported),
			ArgStruct.scalar_enum('Included', enums.Supported),
			ArgStruct.scalar_enum('Type_Py', enums.GeoLocationType)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Capabilities: enums.Supported = None
			self.Included: enums.Supported = None
			self.Type_Py: enums.GeoLocationType = None

	# noinspection PyTypeChecker
	def get_glocation(self) -> GlocationStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:GLOCation \n
		Snippet: value: GlocationStruct = driver.configure.capabilities.get_glocation() \n
		Queries capabilities from the MS about geo-location. Refer to 3GPP2 C.S0005 for details. \n
			:return: structure: for return value, see the help for GlocationStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:GLOCation?', self.__class__.GlocationStruct())

	# noinspection PyTypeChecker
	class WllStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Info_Included: enums.Supported: NSUP | SUPP WLL information is included. NSUP: Not supported SUPP: Supported
			- Device_Type: enums.DeviceType: NO | LIMited | FULL NO: MS with no mobility. LIMited: MS with limited mobility. FULL: MS with full mobility.
			- Hook_Status: enums.HookStatus: ON | OFF | SOFF ON: MS is on-hook. OFF: MS is off-hook. SOFF: MS is stuck off-hook."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Info_Included', enums.Supported),
			ArgStruct.scalar_enum('Device_Type', enums.DeviceType),
			ArgStruct.scalar_enum('Hook_Status', enums.HookStatus)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Info_Included: enums.Supported = None
			self.Device_Type: enums.DeviceType = None
			self.Hook_Status: enums.HookStatus = None

	# noinspection PyTypeChecker
	def get_wll(self) -> WllStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:WLL \n
		Snippet: value: WllStruct = driver.configure.capabilities.get_wll() \n
		Queries the wireless local loop (WLL) capabilities of the MS. \n
			:return: structure: for return value, see the help for WllStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:WLL?', self.__class__.WllStruct())

	# noinspection PyTypeChecker
	class AuthenticStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Mode: enums.Supported: NSUP | SUPP Queries whether the authentication mode is support or not supported by the MS. NSUP: Not supported SUPP: Supported
			- Response: str: Queries the authentication response from the MS. It is used, for example, to validate MS registrations, originations and terminations. The 18-bit value is shown as hexadecimal number. Range: #H0 to #H7FFFFFFF
			- Randc: int: Queries the eight most-significant bits of the random challenge value used by the MS. The 8-bit value is shown as decimal number. Range: 0 to 255 (8 bits)
			- Call_History_Cnt: int: Queries the value of the call history parameter (COUNT) . It is a modulo-64 event counter maintained by the MS and authentication center that is used for clone detection. The 6-bit value is shown as decimal number. Range: 0 to 63 (6 bits)"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Mode', enums.Supported),
			ArgStruct.scalar_raw_str('Response'),
			ArgStruct.scalar_int('Randc'),
			ArgStruct.scalar_int('Call_History_Cnt')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Mode: enums.Supported = None
			self.Response: str = None
			self.Randc: int = None
			self.Call_History_Cnt: int = None

	# noinspection PyTypeChecker
	def get_authentic(self) -> AuthenticStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:AUTHentic \n
		Snippet: value: AuthenticStruct = driver.configure.capabilities.get_authentic() \n
		Queries MS authentication capabilities. Authentication is the process by which information is exchanged between an MS and
		BS to confirm the identity of the MS. \n
			:return: structure: for return value, see the help for AuthenticStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:AUTHentic?', self.__class__.AuthenticStruct())

	# noinspection PyTypeChecker
	class CommonStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Aentry_Handoff: enums.Supported: NSUP | SUPP ACCESS_ENTRY_HO. Access entry handoff support. Queries whether the MS supports the handoff via the paging channel, when the MS is transitioning from the MS idle state to the system access state. NSUP: Not supported SUPP: Supported
			- Aprobe_Handoff: enums.Supported: NSUP | SUPP ACCESS_PROBE_HO. Access probe handoff support. Queries whether the MS supports a handoff while the MS is performing an access attempt in the system access state.
			- Analog_Search: enums.Supported: NSUP | SUPP ANALOG_SEARCH. Analog search support. Queries whether the MS supports analog searching.
			- Analog_553_A: enums.Supported: NSUP | SUPP ANALOG_553A. Analog support. Queries whether the MS is compatibility with standard Core Analog Standard 800 MHz Mobile Station – Land Station Compatibility Specification with Authentication.
			- Hopping_Beacon: enums.Supported: NSUP | SUPP HOPPING_BEACON. Hopping beacon support. Queries whether the MS supports hopping pilot beacons.
			- Msa_Hard_Handoff: enums.Supported: NSUP | SUPP MAHHO. MS assisted hard handoff support. Queries whether the MS supports assisted hard handoff.
			- Power_Up_Function: enums.Supported: NSUP | SUPP PUF. Power up function support.
			- Slotted_Timer: enums.Supported: NSUP | SUPP SLOTTED_TIMER. Slotted timer support. Queries whether the MS supports the slotted timer.
			- Control_Hold_Mode: enums.Supported: NSUP | SUPP CHM_SUPPORTED. Control hold mode supported indicator.
			- Rev_Pilot_Gat_Rate: int: GATING_RATE_SET. Queries the set of MS supported reverse pilot gating rates. Only available if the MS supports ControlHoldMode. 0: Gating rate 1 1: Gating rates 1 and 1/2 2: Gating rates 1, 1/2 and 1/4 3: Reserved Range: 0 to 3
			- Ms_Assisted_Burst: enums.Supported: NSUP | SUPP MABO. Mobile assisted burst operation capability support.
			- Short_Data_Burst: enums.Supported: NSUP | SUPP SDB. Short data burst support.
			- Concur_Services: enums.Supported: NSUP | SUPP CS_SUPPORTED. Concurrent services support.
			- Reg_Type: enums.RegistrationType: TIMer | IMPLicit REG_TYPE. Queries the registration type which the MS supports. TIMer: Timer-based. The MS registers when a timer expires. IMPLicit: Implicit registration. When an MS successfully sends an origination message, reconnect message, or page response message, the BS can infer the MS location. It is considered an implicit registration.
			- Slot_Cycle_Index: int: SLOT_CYCLE_INDEX. Slot cycle index. Queries preferred slot cycle index of the MS. Only available if the MS is configured for slotted mode operation. Otherwise this value is set to 0. For details, refer to the GUI description 'Slot Cycle Index'. Range: 0 to 7 (3 bits)
			- St_Class_Mark: int: SCM. Station class Mark. Queries the station class mark of the MS. For the digital representation, refer to 3GPP2 C.S0005, table 2.3.3-1. Range: 0 to 255 (8 bits)
			- Mob_Term_Call: enums.Supported: NSUP | SUPP MOB_TERM. Mobile station termination indicator. Queries whether the MS accepts MS terminated calls in its current roaming status.
			- Qpch: enums.Supported: NSUP | SUPP QPCH. Quick paging channel. Queries whether the MS supports the quick paging channel.
			- Eradio_Config: enums.Supported: NSUP | SUPP ENHANCED_RC. Enhanced radio configuration support. Queries whether the MS supports any radio configuration (RC) in the RC class 2. That means RC 3 and RC 4 on the reverse channel, and RC 3, RC 4 and RC 5 on the forward channel.
			- User_Zone_Id_Incl: enums.Supported: NSUP | SUPP UZID_INCL. User zone identifier included. Queries whether the MS has a user zone identifier.
			- User_Zone_Ident: int: UZID. User zone identifier. Queries the MS UZID. Only applicable if parameter UserZoneIDIncl is set to SUPP. The 16-bit value is shown as decimal number. Range: 0 to 65535 (16 bits)
			- Orth_Tx_Diversity: enums.Supported: NSUP | SUPP OTD_SUPPORTED. Orthogonal transmission diversity support.
			- Sts_Tx_Diversity: enums.Supported: NSUP | SUPP STS_SUPPORTED. Space time spreading transmit diversity support.
			- Common_Channelx_3: enums.Supported: NSUP | SUPP 3X_CCH_SUPPORTED. 3X common channel supported. Queries whether the MS supports the spreading rate 3 common channels (3X BCCH, 3X F-CCCH, and 3X R-EACH) or not."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Aentry_Handoff', enums.Supported),
			ArgStruct.scalar_enum('Aprobe_Handoff', enums.Supported),
			ArgStruct.scalar_enum('Analog_Search', enums.Supported),
			ArgStruct.scalar_enum('Analog_553_A', enums.Supported),
			ArgStruct.scalar_enum('Hopping_Beacon', enums.Supported),
			ArgStruct.scalar_enum('Msa_Hard_Handoff', enums.Supported),
			ArgStruct.scalar_enum('Power_Up_Function', enums.Supported),
			ArgStruct.scalar_enum('Slotted_Timer', enums.Supported),
			ArgStruct.scalar_enum('Control_Hold_Mode', enums.Supported),
			ArgStruct.scalar_int('Rev_Pilot_Gat_Rate'),
			ArgStruct.scalar_enum('Ms_Assisted_Burst', enums.Supported),
			ArgStruct.scalar_enum('Short_Data_Burst', enums.Supported),
			ArgStruct.scalar_enum('Concur_Services', enums.Supported),
			ArgStruct.scalar_enum('Reg_Type', enums.RegistrationType),
			ArgStruct.scalar_int('Slot_Cycle_Index'),
			ArgStruct.scalar_int('St_Class_Mark'),
			ArgStruct.scalar_enum('Mob_Term_Call', enums.Supported),
			ArgStruct.scalar_enum('Qpch', enums.Supported),
			ArgStruct.scalar_enum('Eradio_Config', enums.Supported),
			ArgStruct.scalar_enum('User_Zone_Id_Incl', enums.Supported),
			ArgStruct.scalar_int('User_Zone_Ident'),
			ArgStruct.scalar_enum('Orth_Tx_Diversity', enums.Supported),
			ArgStruct.scalar_enum('Sts_Tx_Diversity', enums.Supported),
			ArgStruct.scalar_enum('Common_Channelx_3', enums.Supported)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Aentry_Handoff: enums.Supported = None
			self.Aprobe_Handoff: enums.Supported = None
			self.Analog_Search: enums.Supported = None
			self.Analog_553_A: enums.Supported = None
			self.Hopping_Beacon: enums.Supported = None
			self.Msa_Hard_Handoff: enums.Supported = None
			self.Power_Up_Function: enums.Supported = None
			self.Slotted_Timer: enums.Supported = None
			self.Control_Hold_Mode: enums.Supported = None
			self.Rev_Pilot_Gat_Rate: int = None
			self.Ms_Assisted_Burst: enums.Supported = None
			self.Short_Data_Burst: enums.Supported = None
			self.Concur_Services: enums.Supported = None
			self.Reg_Type: enums.RegistrationType = None
			self.Slot_Cycle_Index: int = None
			self.St_Class_Mark: int = None
			self.Mob_Term_Call: enums.Supported = None
			self.Qpch: enums.Supported = None
			self.Eradio_Config: enums.Supported = None
			self.User_Zone_Id_Incl: enums.Supported = None
			self.User_Zone_Ident: int = None
			self.Orth_Tx_Diversity: enums.Supported = None
			self.Sts_Tx_Diversity: enums.Supported = None
			self.Common_Channelx_3: enums.Supported = None

	# noinspection PyTypeChecker
	def get_common(self) -> CommonStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:COMMon \n
		Snippet: value: CommonStruct = driver.configure.capabilities.get_common() \n
		Queries capability information of the MS about supported features and channel configuration capabilities. Refer to 3GPP2
		C.S0005 for details. The number to the left of each result parameter is provided for easy identification of the parameter
		position within the result array. \n
			:return: structure: for return value, see the help for CommonStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:COMMon?', self.__class__.CommonStruct())

	# noinspection PyTypeChecker
	class RlpInfoStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Bitcount_Info: str: Information bit count. Range: #H0 to #HF423F
			- Protocol_Info: str: Protocol information."""
		__meta_args_list = [
			ArgStruct.scalar_raw_str('Bitcount_Info'),
			ArgStruct.scalar_str('Protocol_Info')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Bitcount_Info: str = None
			self.Protocol_Info: str = None

	def get_rlp_info(self) -> RlpInfoStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:RLPinfo \n
		Snippet: value: RlpInfoStruct = driver.configure.capabilities.get_rlp_info() \n
		Queries MS capabilities about the radio link protocol support. \n
			:return: structure: for return value, see the help for RlpInfoStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:CAPabilities:RLPinfo?', self.__class__.RlpInfoStruct())

	def clone(self) -> 'Capabilities':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Capabilities(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
