from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Preconfigure:
	"""Preconfigure commands group definition. 2 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("preconfigure", core, parent)

	@property
	def layer(self):
		"""layer commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_layer'):
			from .Preconfigure_.Layer import Layer
			self._layer = Layer(self._core, self._base)
		return self._layer

	def clone(self) -> 'Preconfigure':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Preconfigure(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
