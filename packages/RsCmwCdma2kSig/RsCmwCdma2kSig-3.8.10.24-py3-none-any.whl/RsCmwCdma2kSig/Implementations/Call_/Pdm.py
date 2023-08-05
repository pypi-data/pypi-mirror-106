from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pdm:
	"""Pdm commands group definition. 5 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pdm", core, parent)

	@property
	def send(self):
		"""send commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_send'):
			from .Pdm_.Send import Send
			self._send = Send(self._core, self._base)
		return self._send

	@property
	def receive(self):
		"""receive commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_receive'):
			from .Pdm_.Receive import Receive
			self._receive = Receive(self._core, self._base)
		return self._receive

	def clone(self) -> 'Pdm':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pdm(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
