from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Call:
	"""Call commands group definition. 13 total commands, 5 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("call", core, parent)

	@property
	def soption(self):
		"""soption commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_soption'):
			from .Call_.Soption import Soption
			self._soption = Soption(self._core, self._base)
		return self._soption

	@property
	def handoff(self):
		"""handoff commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_handoff'):
			from .Call_.Handoff import Handoff
			self._handoff = Handoff(self._core, self._base)
		return self._handoff

	@property
	def reconfigure(self):
		"""reconfigure commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_reconfigure'):
			from .Call_.Reconfigure import Reconfigure
			self._reconfigure = Reconfigure(self._core, self._base)
		return self._reconfigure

	@property
	def otasp(self):
		"""otasp commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_otasp'):
			from .Call_.Otasp import Otasp
			self._otasp = Otasp(self._core, self._base)
		return self._otasp

	@property
	def pdm(self):
		"""pdm commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdm'):
			from .Call_.Pdm import Pdm
			self._pdm = Pdm(self._core, self._base)
		return self._pdm

	def clone(self) -> 'Call':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Call(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
