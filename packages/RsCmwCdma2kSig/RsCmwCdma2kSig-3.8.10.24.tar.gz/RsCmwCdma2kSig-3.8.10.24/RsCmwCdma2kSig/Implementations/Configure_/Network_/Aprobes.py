from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Aprobes:
	"""Aprobes commands group definition. 7 total commands, 1 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("aprobes", core, parent)

	@property
	def spAttempt(self):
		"""spAttempt commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_spAttempt'):
			from .Aprobes_.SpAttempt import SpAttempt
			self._spAttempt = SpAttempt(self._core, self._base)
		return self._spAttempt

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.AccessProbeMode:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:APRobes:MODE \n
		Snippet: value: enums.AccessProbeMode = driver.configure.network.aprobes.get_mode() \n
		Specifies whether the tester acknowledges or ignores access probes from the MS. \n
			:return: mode: IGN | ACK
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:APRobes:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.AccessProbeMode)

	def set_mode(self, mode: enums.AccessProbeMode) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:APRobes:MODE \n
		Snippet: driver.configure.network.aprobes.set_mode(mode = enums.AccessProbeMode.ACK) \n
		Specifies whether the tester acknowledges or ignores access probes from the MS. \n
			:param mode: IGN | ACK
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.AccessProbeMode)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:APRobes:MODE {param}')

	def get_noffset(self) -> int:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:APRobes:NOFFset \n
		Snippet: value: int = driver.configure.network.aprobes.get_noffset() \n
		Specifies the nominal power offset for access probes (NOM_PWR) . The offset range depends on the network settings. \n
			:return: nominal_offset: Range: -8 dB to 7 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:APRobes:NOFFset?')
		return Conversions.str_to_int(response)

	def set_noffset(self, nominal_offset: int) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:APRobes:NOFFset \n
		Snippet: driver.configure.network.aprobes.set_noffset(nominal_offset = 1) \n
		Specifies the nominal power offset for access probes (NOM_PWR) . The offset range depends on the network settings. \n
			:param nominal_offset: Range: -8 dB to 7 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(nominal_offset)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:APRobes:NOFFset {param}')

	def get_ioffset(self) -> int:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:APRobes:IOFFset \n
		Snippet: value: int = driver.configure.network.aprobes.get_ioffset() \n
		Specifies the initial power offset for access probes (INIT_PWR) parameter in the access parameters message. \n
			:return: initial_offset: Range: -16 dB to 15 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:APRobes:IOFFset?')
		return Conversions.str_to_int(response)

	def set_ioffset(self, initial_offset: int) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:APRobes:IOFFset \n
		Snippet: driver.configure.network.aprobes.set_ioffset(initial_offset = 1) \n
		Specifies the initial power offset for access probes (INIT_PWR) parameter in the access parameters message. \n
			:param initial_offset: Range: -16 dB to 15 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(initial_offset)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:APRobes:IOFFset {param}')

	def get_pincrement(self) -> int:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:APRobes:PINCrement \n
		Snippet: value: int = driver.configure.network.aprobes.get_pincrement() \n
		Defines the step size of power increases (PWR_STEP) between consecutive access probes. \n
			:return: probe_increment: Range: 0 dB to 7 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:APRobes:PINCrement?')
		return Conversions.str_to_int(response)

	def set_pincrement(self, probe_increment: int) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:APRobes:PINCrement \n
		Snippet: driver.configure.network.aprobes.set_pincrement(probe_increment = 1) \n
		Defines the step size of power increases (PWR_STEP) between consecutive access probes. \n
			:param probe_increment: Range: 0 dB to 7 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(probe_increment)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:APRobes:PINCrement {param}')

	def get_pp_sequence(self) -> int:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:APRobes:PPSequence \n
		Snippet: value: int = driver.configure.network.aprobes.get_pp_sequence() \n
		Defines the maximum number of access probes (NUM_STEP) contained in a single access probe sequence. \n
			:return: prob_per_sequence: Range: 1 to 16
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:APRobes:PPSequence?')
		return Conversions.str_to_int(response)

	def set_pp_sequence(self, prob_per_sequence: int) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:APRobes:PPSequence \n
		Snippet: driver.configure.network.aprobes.set_pp_sequence(prob_per_sequence = 1) \n
		Defines the maximum number of access probes (NUM_STEP) contained in a single access probe sequence. \n
			:param prob_per_sequence: Range: 1 to 16
		"""
		param = Conversions.decimal_value_to_str(prob_per_sequence)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:APRobes:PPSequence {param}')

	def clone(self) -> 'Aprobes':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Aprobes(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
