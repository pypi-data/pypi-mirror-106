from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ibit:
	"""Ibit commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: Indicator, default value after init: Indicator.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ibit", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_indicator_get', 'repcap_indicator_set', repcap.Indicator.Nr1)

	def repcap_indicator_set(self, enum_value: repcap.Indicator) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Indicator.Default
		Default value after init: Indicator.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_indicator_get(self) -> repcap.Indicator:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	def set(self, indicator_bit: bool, indicator=repcap.Indicator.Default) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:LAYer:QPCH:IBIT<n> \n
		Snippet: driver.configure.layer.qpch.ibit.set(indicator_bit = False, indicator = repcap.Indicator.Default) \n
		Enables up to two indicators that trigger the MS to decode the PCH. \n
			:param indicator_bit: OFF | ON
			:param indicator: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ibit')"""
		param = Conversions.bool_to_str(indicator_bit)
		indicator_cmd_val = self._base.get_repcap_cmd_value(indicator, repcap.Indicator)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:LAYer:QPCH:IBIT{indicator_cmd_val} {param}')

	def get(self, indicator=repcap.Indicator.Default) -> bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:LAYer:QPCH:IBIT<n> \n
		Snippet: value: bool = driver.configure.layer.qpch.ibit.get(indicator = repcap.Indicator.Default) \n
		Enables up to two indicators that trigger the MS to decode the PCH. \n
			:param indicator: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ibit')
			:return: indicator_bit: OFF | ON"""
		indicator_cmd_val = self._base.get_repcap_cmd_value(indicator, repcap.Indicator)
		response = self._core.io.query_str(f'CONFigure:CDMA:SIGNaling<Instance>:LAYer:QPCH:IBIT{indicator_cmd_val}?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'Ibit':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ibit(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
