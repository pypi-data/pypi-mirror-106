from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cstatus:
	"""Cstatus commands group definition. 5 total commands, 2 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cstatus", core, parent)

	@property
	def moption(self):
		"""moption commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_moption'):
			from .Cstatus_.Moption import Moption
			self._moption = Moption(self._core, self._base)
		return self._moption

	@property
	def drate(self):
		"""drate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_drate'):
			from .Cstatus_.Drate import Drate
			self._drate = Drate(self._core, self._base)
		return self._drate

	def get_log(self) -> str:
		"""SCPI: CONFigure:CDMA:SIGNaling<instance>:CSTatus:LOG \n
		Snippet: value: str = driver.configure.cstatus.get_log() \n
		Reports events and errors like connection state changes, RRC connection establishment/release and authentication failure. \n
			:return: con_status_log: Report as a string
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:CSTatus:LOG?')
		return trim_str_response(response)

	def get_vcoder(self) -> str:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:CSTatus:VCODer \n
		Snippet: value: str = driver.configure.cstatus.get_vcoder() \n
		Returns the voice coder used for the speech connection (speech service option) . \n
			:return: voice_coder: 'Echo' if 'Voice Coder' = echo or for the service option 0x8000 If 'Voice Coder' = codec: '8k QCELP' for SO1 '8k EVRC' for SO3 '13k QCELP' for S17 'EVRC-B' for SO68 'EVRC-WB' for SO70 'EVRC-NW' for SO73
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:CSTatus:VCODer?')
		return trim_str_response(response)

	def clone(self) -> 'Cstatus':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cstatus(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
