from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sconfig:
	"""Sconfig commands group definition. 23 total commands, 4 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sconfig", core, parent)

	@property
	def loop(self):
		"""loop commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_loop'):
			from .Sconfig_.Loop import Loop
			self._loop = Loop(self._core, self._base)
		return self._loop

	@property
	def speech(self):
		"""speech commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_speech'):
			from .Sconfig_.Speech import Speech
			self._speech = Speech(self._core, self._base)
		return self._speech

	@property
	def tdata(self):
		"""tdata commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_tdata'):
			from .Sconfig_.Tdata import Tdata
			self._tdata = Tdata(self._core, self._base)
		return self._tdata

	@property
	def pdata(self):
		"""pdata commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_pdata'):
			from .Sconfig_.Pdata import Pdata
			self._pdata = Pdata(self._core, self._base)
		return self._pdata

	# noinspection PyTypeChecker
	def get_amoc(self) -> enums.MocCallsAcceptMode:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SCONfig:AMOC \n
		Snippet: value: enums.MocCallsAcceptMode = driver.configure.sconfig.get_amoc() \n
		Selects the types of mobile station originated calls (MOC) that the R&S CMW accepts and specifies how it responds to an
		accepted or rejected MOC. See also: 'Accept Speech Calls' \n
			:return: acc_ms_orig_call: ALL | SCL1 | FSC1 | ICAW | ICFW | ICOR | ROAW | ROFW | ROOR | BUAW | BUFW | IGNR | RERO ALL: Accept all calls SCL1: Accept only selected primary service FSC1: Force to selected primary service ICAW: Accept no calls – intercept (AWIM) ICFW: Accept no calls – intercept (FWIM) ICOR: Accept no calls – intercept (order) ROAW: Accept no calls – Reorder (AWIM) ROFW: Accept no calls – Reorder (FWIM) ROOR: Accept no calls – Reorder (order) BUAW: Accept no calls – busy (AWIM) BUFW: Accept no calls – busy (FWIM) IGNR: Accept no calls – ignore MS RERO: Accept no calls – release (RORJ)
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:SCONfig:AMOC?')
		return Conversions.str_to_scalar_enum(response, enums.MocCallsAcceptMode)

	def set_amoc(self, acc_ms_orig_call: enums.MocCallsAcceptMode) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SCONfig:AMOC \n
		Snippet: driver.configure.sconfig.set_amoc(acc_ms_orig_call = enums.MocCallsAcceptMode.ALL) \n
		Selects the types of mobile station originated calls (MOC) that the R&S CMW accepts and specifies how it responds to an
		accepted or rejected MOC. See also: 'Accept Speech Calls' \n
			:param acc_ms_orig_call: ALL | SCL1 | FSC1 | ICAW | ICFW | ICOR | ROAW | ROFW | ROOR | BUAW | BUFW | IGNR | RERO ALL: Accept all calls SCL1: Accept only selected primary service FSC1: Force to selected primary service ICAW: Accept no calls – intercept (AWIM) ICFW: Accept no calls – intercept (FWIM) ICOR: Accept no calls – intercept (order) ROAW: Accept no calls – Reorder (AWIM) ROFW: Accept no calls – Reorder (FWIM) ROOR: Accept no calls – Reorder (order) BUAW: Accept no calls – busy (AWIM) BUFW: Accept no calls – busy (FWIM) IGNR: Accept no calls – ignore MS RERO: Accept no calls – release (RORJ)
		"""
		param = Conversions.enum_scalar_to_str(acc_ms_orig_call, enums.MocCallsAcceptMode)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:SCONfig:AMOC {param}')

	# noinspection PyTypeChecker
	def get_ap_calls(self) -> enums.AcceptState:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SCONfig:APCalls \n
		Snippet: value: enums.AcceptState = driver.configure.sconfig.get_ap_calls() \n
		Defines the mobile originated packet calls handling. \n
			:return: acc_packet_calls: ACCept | REJect
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:SCONfig:APCalls?')
		return Conversions.str_to_scalar_enum(response, enums.AcceptState)

	def set_ap_calls(self, acc_packet_calls: enums.AcceptState) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SCONfig:APCalls \n
		Snippet: driver.configure.sconfig.set_ap_calls(acc_packet_calls = enums.AcceptState.ACCept) \n
		Defines the mobile originated packet calls handling. \n
			:param acc_packet_calls: ACCept | REJect
		"""
		param = Conversions.enum_scalar_to_str(acc_packet_calls, enums.AcceptState)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:SCONfig:APCalls {param}')

	def clone(self) -> 'Sconfig':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sconfig(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
