from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ocns:
	"""Ocns commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ocns", core, parent)

	def set(self, ocns_enable: bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFPower:LEVel:OCNS \n
		Snippet: driver.configure.rfPower.level.ocns.set(ocns_enable = False) \n
		Activates or deactivates the orthogonal channel noise simulator (OCNS) channels and queries the total OCNS channel power
		relative to the value of 'CDMA Power' (method RsCmwCdma2kSig.Configure.RfPower.cdma) . OCNS channels are generated if the
		total power of all active channels is smaller than the value of 'CDMA Power'. The remaining power is assigned to the OCNS
		channels so that the value of 'CDMA Power' is reached. \n
			:param ocns_enable: OFF | ON ON: enables OCNS channels OFF: disables OCNS channels
		"""
		param = Conversions.bool_to_str(ocns_enable)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RFPower:LEVel:OCNS {param}')

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Ocns_Enable: bool: OFF | ON ON: enables OCNS channels OFF: disables OCNS channels
			- Ocns_Level: float: Queries the total OCNS channel power relative to CDMA power ([CMDLINK: CONFigure:CDMA:SIGNi:RFPower:CDMA CMDLINK]) . Range: - 150 dB to 0 dB , Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Ocns_Enable'),
			ArgStruct.scalar_float('Ocns_Level')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ocns_Enable: bool = None
			self.Ocns_Level: float = None

	def get(self) -> GetStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFPower:LEVel:OCNS \n
		Snippet: value: GetStruct = driver.configure.rfPower.level.ocns.get() \n
		Activates or deactivates the orthogonal channel noise simulator (OCNS) channels and queries the total OCNS channel power
		relative to the value of 'CDMA Power' (method RsCmwCdma2kSig.Configure.RfPower.cdma) . OCNS channels are generated if the
		total power of all active channels is smaller than the value of 'CDMA Power'. The remaining power is assigned to the OCNS
		channels so that the value of 'CDMA Power' is reached. \n
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:CDMA:SIGNaling<Instance>:RFPower:LEVel:OCNS?', self.__class__.GetStruct())
