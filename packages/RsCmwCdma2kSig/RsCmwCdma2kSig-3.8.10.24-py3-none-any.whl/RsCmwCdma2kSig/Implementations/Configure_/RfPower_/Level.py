from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 8 total commands, 1 Sub-groups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("level", core, parent)

	@property
	def ocns(self):
		"""ocns commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ocns'):
			from .Level_.Ocns import Ocns
			self._ocns = Ocns(self._core, self._base)
		return self._ocns

	def get_pich(self) -> float or bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFPower:LEVel:PICH \n
		Snippet: value: float or bool = driver.configure.rfPower.level.get_pich() \n
		Activates or deactivates the pilot channel (PICH) and defines its level relative to the 'CDMA Power' (method
		RsCmwCdma2kSig.Configure.RfPower.cdma) . \n
			:return: pich_level: Range: -20 dB to -1 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the PICH)
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RFPower:LEVel:PICH?')
		return Conversions.str_to_float_or_bool(response)

	def set_pich(self, pich_level: float or bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFPower:LEVel:PICH \n
		Snippet: driver.configure.rfPower.level.set_pich(pich_level = 1.0) \n
		Activates or deactivates the pilot channel (PICH) and defines its level relative to the 'CDMA Power' (method
		RsCmwCdma2kSig.Configure.RfPower.cdma) . \n
			:param pich_level: Range: -20 dB to -1 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the PICH)
		"""
		param = Conversions.decimal_or_bool_value_to_str(pich_level)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RFPower:LEVel:PICH {param}')

	def get_sync(self) -> float or bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFPower:LEVel:SYNC \n
		Snippet: value: float or bool = driver.configure.rfPower.level.get_sync() \n
		Activates or deactivates the synchronization channel and defines its level relative to the 'CDMA Power' (method
		RsCmwCdma2kSig.Configure.RfPower.cdma) . \n
			:return: sync_level: Range: -20 dB to -1 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the sync channel)
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RFPower:LEVel:SYNC?')
		return Conversions.str_to_float_or_bool(response)

	def set_sync(self, sync_level: float or bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFPower:LEVel:SYNC \n
		Snippet: driver.configure.rfPower.level.set_sync(sync_level = 1.0) \n
		Activates or deactivates the synchronization channel and defines its level relative to the 'CDMA Power' (method
		RsCmwCdma2kSig.Configure.RfPower.cdma) . \n
			:param sync_level: Range: -20 dB to -1 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the sync channel)
		"""
		param = Conversions.decimal_or_bool_value_to_str(sync_level)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RFPower:LEVel:SYNC {param}')

	def get_pch(self) -> float or bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFPower:LEVel:PCH \n
		Snippet: value: float or bool = driver.configure.rfPower.level.get_pch() \n
		Activates or deactivates the paging channel (PCH) and defines its level relative to the 'CDMA Power' (method
		RsCmwCdma2kSig.Configure.RfPower.cdma) . \n
			:return: pch_level: Range: -20 dB to -1 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the PCH)
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RFPower:LEVel:PCH?')
		return Conversions.str_to_float_or_bool(response)

	def set_pch(self, pch_level: float or bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFPower:LEVel:PCH \n
		Snippet: driver.configure.rfPower.level.set_pch(pch_level = 1.0) \n
		Activates or deactivates the paging channel (PCH) and defines its level relative to the 'CDMA Power' (method
		RsCmwCdma2kSig.Configure.RfPower.cdma) . \n
			:param pch_level: Range: -20 dB to -1 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the PCH)
		"""
		param = Conversions.decimal_or_bool_value_to_str(pch_level)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RFPower:LEVel:PCH {param}')

	def get_fch(self) -> float or bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFPower:LEVel:FCH \n
		Snippet: value: float or bool = driver.configure.rfPower.level.get_fch() \n
		Activates or deactivates the forward fundamental channel and defines its level relative to the 'CDMA Power' (method
		RsCmwCdma2kSig.Configure.RfPower.cdma) . \n
			:return: fch_level: Range: -20 dB to -1 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the F-FCH)
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RFPower:LEVel:FCH?')
		return Conversions.str_to_float_or_bool(response)

	def set_fch(self, fch_level: float or bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFPower:LEVel:FCH \n
		Snippet: driver.configure.rfPower.level.set_fch(fch_level = 1.0) \n
		Activates or deactivates the forward fundamental channel and defines its level relative to the 'CDMA Power' (method
		RsCmwCdma2kSig.Configure.RfPower.cdma) . \n
			:param fch_level: Range: -20 dB to -1 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the F-FCH)
		"""
		param = Conversions.decimal_or_bool_value_to_str(fch_level)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RFPower:LEVel:FCH {param}')

	def get_sch(self) -> float or bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFPower:LEVel:SCH \n
		Snippet: value: float or bool = driver.configure.rfPower.level.get_sch() \n
		For the F-SCH defines the level relative to the 'CDMA Power' (method RsCmwCdma2kSig.Configure.RfPower.cdma) . \n
			:return: sch_0_level: Range: -20 dB to -1 dB, Unit: dB Additional OFF/ON disables / enables F-SCH
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RFPower:LEVel:SCH?')
		return Conversions.str_to_float_or_bool(response)

	def set_sch(self, sch_0_level: float or bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFPower:LEVel:SCH \n
		Snippet: driver.configure.rfPower.level.set_sch(sch_0_level = 1.0) \n
		For the F-SCH defines the level relative to the 'CDMA Power' (method RsCmwCdma2kSig.Configure.RfPower.cdma) . \n
			:param sch_0_level: Range: -20 dB to -1 dB, Unit: dB Additional OFF/ON disables / enables F-SCH
		"""
		param = Conversions.decimal_or_bool_value_to_str(sch_0_level)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RFPower:LEVel:SCH {param}')

	def get_qpch(self) -> int or bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFPower:LEVel:QPCH \n
		Snippet: value: int or bool = driver.configure.rfPower.level.get_qpch() \n
		Activates or deactivates the quick paging channel (QPCH) and defines its level relative to the 'CDMA Power'. \n
			:return: qpch_level: Range: -5 dB to 2 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the QPCH)
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RFPower:LEVel:QPCH?')
		return Conversions.str_to_int_or_bool(response)

	def set_qpch(self, qpch_level: int or bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFPower:LEVel:QPCH \n
		Snippet: driver.configure.rfPower.level.set_qpch(qpch_level = 1) \n
		Activates or deactivates the quick paging channel (QPCH) and defines its level relative to the 'CDMA Power'. \n
			:param qpch_level: Range: -5 dB to 2 dB, Unit: dB Additional parameters: OFF | ON (disables | enables the QPCH)
		"""
		param = Conversions.decimal_or_bool_value_to_str(qpch_level)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RFPower:LEVel:QPCH {param}')

	def get_awgn(self) -> float or bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFPower:LEVel:AWGN \n
		Snippet: value: float or bool = driver.configure.rfPower.level.get_awgn() \n
		Sets the total level of the additional white Gaussian noise (AWGN) interfere. The value is relative to the 'CDMA Power'
		(method RsCmwCdma2kSig.Configure.RfPower.cdma) . The AWGN level range depends on the operating mode of the AWGN generator
		(method RsCmwCdma2kSig.Configure.RfPower.Mode.awgn) . \n
			:return: awgn_level: Range: -25 dB to +4 dB (normal mode) , -12 dB to 11.70 dB (high-power mode) , Unit: dB Additional OFF/ON disables / enables AWGN signal
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RFPower:LEVel:AWGN?')
		return Conversions.str_to_float_or_bool(response)

	def set_awgn(self, awgn_level: float or bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFPower:LEVel:AWGN \n
		Snippet: driver.configure.rfPower.level.set_awgn(awgn_level = 1.0) \n
		Sets the total level of the additional white Gaussian noise (AWGN) interfere. The value is relative to the 'CDMA Power'
		(method RsCmwCdma2kSig.Configure.RfPower.cdma) . The AWGN level range depends on the operating mode of the AWGN generator
		(method RsCmwCdma2kSig.Configure.RfPower.Mode.awgn) . \n
			:param awgn_level: Range: -25 dB to +4 dB (normal mode) , -12 dB to 11.70 dB (high-power mode) , Unit: dB Additional OFF/ON disables / enables AWGN signal
		"""
		param = Conversions.decimal_or_bool_value_to_str(awgn_level)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RFPower:LEVel:AWGN {param}')

	def clone(self) -> 'Level':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Level(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
