from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cindicator:
	"""Cindicator commands group definition. 3 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cindicator", core, parent)

	@property
	def cid(self):
		"""cid commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_cid'):
			from .Cindicator_.Cid import Cid
			self._cid = Cid(self._core, self._base)
		return self._cid

	def clone(self) -> 'Cindicator':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cindicator(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
