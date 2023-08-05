from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Network:
	"""Network commands group definition. 46 total commands, 8 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("network", core, parent)

	@property
	def system(self):
		"""system commands group. 3 Sub-classes, 4 commands."""
		if not hasattr(self, '_system'):
			from .Network_.System import System
			self._system = System(self._core, self._base)
		return self._system

	@property
	def propertyPy(self):
		"""propertyPy commands group. 0 Sub-classes, 7 commands."""
		if not hasattr(self, '_propertyPy'):
			from .Network_.PropertyPy import PropertyPy
			self._propertyPy = PropertyPy(self._core, self._base)
		return self._propertyPy

	@property
	def identity(self):
		"""identity commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_identity'):
			from .Network_.Identity import Identity
			self._identity = Identity(self._core, self._base)
		return self._identity

	@property
	def msettings(self):
		"""msettings commands group. 1 Sub-classes, 4 commands."""
		if not hasattr(self, '_msettings'):
			from .Network_.Msettings import Msettings
			self._msettings = Msettings(self._core, self._base)
		return self._msettings

	@property
	def cindicator(self):
		"""cindicator commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cindicator'):
			from .Network_.Cindicator import Cindicator
			self._cindicator = Cindicator(self._core, self._base)
		return self._cindicator

	@property
	def pchannel(self):
		"""pchannel commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_pchannel'):
			from .Network_.Pchannel import Pchannel
			self._pchannel = Pchannel(self._core, self._base)
		return self._pchannel

	@property
	def registration(self):
		"""registration commands group. 0 Sub-classes, 8 commands."""
		if not hasattr(self, '_registration'):
			from .Network_.Registration import Registration
			self._registration = Registration(self._core, self._base)
		return self._registration

	@property
	def aprobes(self):
		"""aprobes commands group. 1 Sub-classes, 5 commands."""
		if not hasattr(self, '_aprobes'):
			from .Network_.Aprobes import Aprobes
			self._aprobes = Aprobes(self._core, self._base)
		return self._aprobes

	def clone(self) -> 'Network':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Network(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
