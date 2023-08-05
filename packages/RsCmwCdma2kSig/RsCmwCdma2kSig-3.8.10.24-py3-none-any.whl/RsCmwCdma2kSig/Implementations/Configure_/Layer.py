from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Layer:
	"""Layer commands group definition. 23 total commands, 6 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("layer", core, parent)

	@property
	def soption(self):
		"""soption commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_soption'):
			from .Layer_.Soption import Soption
			self._soption = Soption(self._core, self._base)
		return self._soption

	@property
	def channel(self):
		"""channel commands group. 2 Sub-classes, 4 commands."""
		if not hasattr(self, '_channel'):
			from .Layer_.Channel import Channel
			self._channel = Channel(self._core, self._base)
		return self._channel

	@property
	def fch(self):
		"""fch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fch'):
			from .Layer_.Fch import Fch
			self._fch = Fch(self._core, self._base)
		return self._fch

	@property
	def sch(self):
		"""sch commands group. 0 Sub-classes, 6 commands."""
		if not hasattr(self, '_sch'):
			from .Layer_.Sch import Sch
			self._sch = Sch(self._core, self._base)
		return self._sch

	@property
	def pch(self):
		"""pch commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_pch'):
			from .Layer_.Pch import Pch
			self._pch = Pch(self._core, self._base)
		return self._pch

	@property
	def qpch(self):
		"""qpch commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_qpch'):
			from .Layer_.Qpch import Qpch
			self._qpch = Qpch(self._core, self._base)
		return self._qpch

	# noinspection PyTypeChecker
	def get_rconfig(self) -> enums.RadioConfig:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:LAYer:RCONfig \n
		Snippet: value: enums.RadioConfig = driver.configure.layer.get_rconfig() \n
		Queries the current radio configuration (RC) used during the connection to the mobile station. Setting this value has no
		effect because the radio configuration parameter is a result of the session negotiation. \n
			:return: radio_config: F1R1 | F2R2 | F3R3 | F4R3 | F5R4 The allowed values for the forward and reverse fundamental channel depends on the '1st Service Option'.
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:LAYer:RCONfig?')
		return Conversions.str_to_scalar_enum(response, enums.RadioConfig)

	def set_rconfig(self, radio_config: enums.RadioConfig) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:LAYer:RCONfig \n
		Snippet: driver.configure.layer.set_rconfig(radio_config = enums.RadioConfig.F1R1) \n
		Queries the current radio configuration (RC) used during the connection to the mobile station. Setting this value has no
		effect because the radio configuration parameter is a result of the session negotiation. \n
			:param radio_config: F1R1 | F2R2 | F3R3 | F4R3 | F5R4 The allowed values for the forward and reverse fundamental channel depends on the '1st Service Option'.
		"""
		param = Conversions.enum_scalar_to_str(radio_config, enums.RadioConfig)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:LAYer:RCONfig {param}')

	# noinspection PyTypeChecker
	def get_modulation(self) -> enums.Modulation:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:LAYer:MODulation \n
		Snippet: value: enums.Modulation = driver.configure.layer.get_modulation() \n
		Queries the preconfigured modulation scheme or in the connected status used for the active connection. It depends on the
		radio configuration. See also: 'Radio Configurations' \n
			:return: modulation: QPSK | HPSK
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:LAYer:MODulation?')
		return Conversions.str_to_scalar_enum(response, enums.Modulation)

	def clone(self) -> 'Layer':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Layer(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
