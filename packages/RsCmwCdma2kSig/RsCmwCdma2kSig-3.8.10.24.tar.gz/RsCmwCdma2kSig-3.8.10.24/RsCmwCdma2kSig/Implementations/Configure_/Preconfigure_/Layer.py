from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Layer:
	"""Layer commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

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

	# noinspection PyTypeChecker
	def get_rconfig(self) -> enums.RadioConfig:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:PREConfigure:LAYer:RCONfig \n
		Snippet: value: enums.RadioConfig = driver.configure.preconfigure.layer.get_rconfig() \n
		Preconfigures the radio configuration to be proposed to the MS during the next connection setup. \n
			:return: radio_config: F1R1 | F2R2 | F3R3 | F4R3 | F5R4 The allowed values for the forward and reverse fundamental channel depends on the '1st Service Option'.
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:PREConfigure:LAYer:RCONfig?')
		return Conversions.str_to_scalar_enum(response, enums.RadioConfig)

	def set_rconfig(self, radio_config: enums.RadioConfig) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:PREConfigure:LAYer:RCONfig \n
		Snippet: driver.configure.preconfigure.layer.set_rconfig(radio_config = enums.RadioConfig.F1R1) \n
		Preconfigures the radio configuration to be proposed to the MS during the next connection setup. \n
			:param radio_config: F1R1 | F2R2 | F3R3 | F4R3 | F5R4 The allowed values for the forward and reverse fundamental channel depends on the '1st Service Option'.
		"""
		param = Conversions.enum_scalar_to_str(radio_config, enums.RadioConfig)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:PREConfigure:LAYer:RCONfig {param}')

	def clone(self) -> 'Layer':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Layer(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
