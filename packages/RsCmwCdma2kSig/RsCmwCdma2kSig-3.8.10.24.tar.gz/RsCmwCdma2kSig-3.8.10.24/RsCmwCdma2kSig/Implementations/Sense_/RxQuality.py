from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RxQuality:
	"""RxQuality commands group definition. 30 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rxQuality", core, parent)

	@property
	def rlp(self):
		"""rlp commands group. 0 Sub-classes, 18 commands."""
		if not hasattr(self, '_rlp'):
			from .RxQuality_.Rlp import Rlp
			self._rlp = Rlp(self._core, self._base)
		return self._rlp

	@property
	def speech(self):
		"""speech commands group. 5 Sub-classes, 2 commands."""
		if not hasattr(self, '_speech'):
			from .RxQuality_.Speech import Speech
			self._speech = Speech(self._core, self._base)
		return self._speech

	def clone(self) -> 'RxQuality':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RxQuality(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
