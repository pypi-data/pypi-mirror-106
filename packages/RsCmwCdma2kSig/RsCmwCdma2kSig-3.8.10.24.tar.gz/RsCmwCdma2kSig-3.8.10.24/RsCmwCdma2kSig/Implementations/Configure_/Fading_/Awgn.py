from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Awgn:
	"""Awgn commands group definition. 4 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("awgn", core, parent)

	@property
	def bandwidth(self):
		"""bandwidth commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Awgn_.Bandwidth import Bandwidth
			self._bandwidth = Bandwidth(self._core, self._base)
		return self._bandwidth

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:FADing:AWGN:ENABle \n
		Snippet: value: bool = driver.configure.fading.awgn.get_enable() \n
		Enables or disables AWGN insertion via the fading module. For dual carrier, the same settings are applied to both
		carriers. Thus it is sufficient to configure one carrier. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:FADing:AWGN:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:FADing:AWGN:ENABle \n
		Snippet: driver.configure.fading.awgn.set_enable(enable = False) \n
		Enables or disables AWGN insertion via the fading module. For dual carrier, the same settings are applied to both
		carriers. Thus it is sufficient to configure one carrier. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:FADing:AWGN:ENABle {param}')

	def get_sn_ratio(self) -> float:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:FADing:AWGN:SNRatio \n
		Snippet: value: float = driver.configure.fading.awgn.get_sn_ratio() \n
		Queries the signal to noise ratio for the AWGN inserted via the internal fading module. \n
			:return: ratio: Range: -50 dB to 30 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:FADing:AWGN:SNRatio?')
		return Conversions.str_to_float(response)

	def set_sn_ratio(self, ratio: float) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:FADing:AWGN:SNRatio \n
		Snippet: driver.configure.fading.awgn.set_sn_ratio(ratio = 1.0) \n
		Queries the signal to noise ratio for the AWGN inserted via the internal fading module. \n
			:param ratio: Range: -50 dB to 30 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(ratio)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:FADing:AWGN:SNRatio {param}')

	def clone(self) -> 'Awgn':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Awgn(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
