from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bits:
	"""Bits commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("bits", core, parent)

	def set(self, segment_bits: enums.SegmentBits, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<instance>:RPControl:SEGMent<nr>:BITS \n
		Snippet: driver.configure.rpControl.segment.bits.set(segment_bits = enums.SegmentBits.ALTernating, segment = repcap.Segment.Default) \n
		Sets the user-specific power control bits. \n
			:param segment_bits: DOWN | UP | ALTernating All 0, all 1 or alternating
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')"""
		param = Conversions.enum_scalar_to_str(segment_bits, enums.SegmentBits)
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RPControl:SEGMent{segment_cmd_val}:BITS {param}')

	# noinspection PyTypeChecker
	def get(self, segment=repcap.Segment.Default) -> enums.SegmentBits:
		"""SCPI: CONFigure:CDMA:SIGNaling<instance>:RPControl:SEGMent<nr>:BITS \n
		Snippet: value: enums.SegmentBits = driver.configure.rpControl.segment.bits.get(segment = repcap.Segment.Default) \n
		Sets the user-specific power control bits. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: segment_bits: DOWN | UP | ALTernating All 0, all 1 or alternating"""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		response = self._core.io.query_str(f'CONFigure:CDMA:SIGNaling<Instance>:RPControl:SEGMent{segment_cmd_val}:BITS?')
		return Conversions.str_to_scalar_enum(response, enums.SegmentBits)
