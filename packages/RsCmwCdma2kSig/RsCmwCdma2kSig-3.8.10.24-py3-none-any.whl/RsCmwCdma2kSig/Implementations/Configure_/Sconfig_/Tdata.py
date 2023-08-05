from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tdata:
	"""Tdata commands group definition. 10 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("tdata", core, parent)

	@property
	def fch(self):
		"""fch commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_fch'):
			from .Tdata_.Fch import Fch
			self._fch = Fch(self._core, self._base)
		return self._fch

	@property
	def sch(self):
		"""sch commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_sch'):
			from .Tdata_.Sch import Sch
			self._sch = Sch(self._core, self._base)
		return self._sch

	def clone(self) -> 'Tdata':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tdata(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
