from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sms:
	"""Sms commands group definition. 20 total commands, 4 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sms", core, parent)

	@property
	def incoming(self):
		"""incoming commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_incoming'):
			from .Sms_.Incoming import Incoming
			self._incoming = Incoming(self._core, self._base)
		return self._incoming

	@property
	def outgoing(self):
		"""outgoing commands group. 1 Sub-classes, 6 commands."""
		if not hasattr(self, '_outgoing'):
			from .Sms_.Outgoing import Outgoing
			self._outgoing = Outgoing(self._core, self._base)
		return self._outgoing

	@property
	def info(self):
		"""info commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_info'):
			from .Sms_.Info import Info
			self._info = Info(self._core, self._base)
		return self._info

	@property
	def broadcast(self):
		"""broadcast commands group. 1 Sub-classes, 5 commands."""
		if not hasattr(self, '_broadcast'):
			from .Sms_.Broadcast import Broadcast
			self._broadcast = Broadcast(self._core, self._base)
		return self._broadcast

	def clone(self) -> 'Sms':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sms(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
