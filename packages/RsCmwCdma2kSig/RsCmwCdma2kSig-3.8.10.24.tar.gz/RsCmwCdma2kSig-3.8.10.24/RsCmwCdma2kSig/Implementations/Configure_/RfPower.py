from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfPower:
	"""RfPower commands group definition. 16 total commands, 3 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rfPower", core, parent)

	@property
	def level(self):
		"""level commands group. 1 Sub-classes, 7 commands."""
		if not hasattr(self, '_level'):
			from .RfPower_.Level import Level
			self._level = Level(self._core, self._base)
		return self._level

	@property
	def ebnt(self):
		"""ebnt commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ebnt'):
			from .RfPower_.Ebnt import Ebnt
			self._ebnt = Ebnt(self._core, self._base)
		return self._ebnt

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .RfPower_.Mode import Mode
			self._mode = Mode(self._core, self._base)
		return self._mode

	def get_expected(self) -> float:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFPower:EXPected \n
		Snippet: value: float = driver.configure.rfPower.get_expected() \n
		Queries the calculated value of the expected input power from the MS. The input power range is stated in the data sheet. \n
			:return: exp_nom_power: Unit: dBm
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RFPower:EXPected?')
		return Conversions.str_to_float(response)

	def get_cdma(self) -> float:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFPower:CDMA \n
		Snippet: value: float = driver.configure.rfPower.get_cdma() \n
		Sets the total CDMA output power. The value range depends on the RF output used and the external attenuation set.
		The 'CDMA Power' level does not include the AWGN power level. The allowed value range can be calculated as follows: Range
		(CDMAPower) = Range (Output Power) - External Attenuation - AWGNPower Range (Output Power) = -130 dBm to 0 dBm (RFx COM)
		or -120 dBm to 13 dBm (RFx OUT) ; please also notice the ranges quoted in the data sheet. \n
			:return: cdma_power: Range: see above , Unit: dBm
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RFPower:CDMA?')
		return Conversions.str_to_float(response)

	def set_cdma(self, cdma_power: float) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFPower:CDMA \n
		Snippet: driver.configure.rfPower.set_cdma(cdma_power = 1.0) \n
		Sets the total CDMA output power. The value range depends on the RF output used and the external attenuation set.
		The 'CDMA Power' level does not include the AWGN power level. The allowed value range can be calculated as follows: Range
		(CDMAPower) = Range (Output Power) - External Attenuation - AWGNPower Range (Output Power) = -130 dBm to 0 dBm (RFx COM)
		or -120 dBm to 13 dBm (RFx OUT) ; please also notice the ranges quoted in the data sheet. \n
			:param cdma_power: Range: see above , Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(cdma_power)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RFPower:CDMA {param}')

	def get_output(self) -> float:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFPower:OUTPut \n
		Snippet: value: float = driver.configure.rfPower.get_output() \n
		Queries the total output power. The total output power includes the AWGN power level. The allowed value: Range (Output
		Power) = -130 dBm to 0 dBm (RFx COM) or -120 dBm to 13 dBm (RFx OUT) ; please also notice the ranges quoted in the data
		sheet. \n
			:return: output_power: Range: see above , Unit: dBm
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RFPower:OUTPut?')
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	def get_epmode(self) -> enums.ExpectedPowerMode:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFPower:EPMode \n
		Snippet: value: enums.ExpectedPowerMode = driver.configure.rfPower.get_epmode() \n
		Configures the input path of the RF analyzer according to the expected output power of the MS under test. The R&S CMW
		assumes a 9 dB peak-to-average ratio (crest factor) of the received CDMA2000 signal and allows for an additional reserve.
		See also: 'Expected Power Mode' \n
			:return: exp_power_mode: MANual | OLRule | MAX | MIN MANual: Assume that the MS transmits at the fixed 'Manual Expected Power' value and configure the R&S CMW input path accordingly. OLRule: Open loop rule: Assume that the MS transmits according to the open loop power rule: The sum of the mean input power at the MS receiver plus the mean output power at the MS transmitter is maintained at a constant 'power offset' value: input power + output power = power offset. The power offset depends on the band class; see 3GPP2 C.S0057-D. MAX: Maximum: Assume that MS transmits at its maximum output power (RMS value ≤+23 dBm) . MIN: Minimum: Assume that MS transmits at its minimum output power (RMS value ≤–47 dBm) .
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RFPower:EPMode?')
		return Conversions.str_to_scalar_enum(response, enums.ExpectedPowerMode)

	def set_epmode(self, exp_power_mode: enums.ExpectedPowerMode) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFPower:EPMode \n
		Snippet: driver.configure.rfPower.set_epmode(exp_power_mode = enums.ExpectedPowerMode.MANual) \n
		Configures the input path of the RF analyzer according to the expected output power of the MS under test. The R&S CMW
		assumes a 9 dB peak-to-average ratio (crest factor) of the received CDMA2000 signal and allows for an additional reserve.
		See also: 'Expected Power Mode' \n
			:param exp_power_mode: MANual | OLRule | MAX | MIN MANual: Assume that the MS transmits at the fixed 'Manual Expected Power' value and configure the R&S CMW input path accordingly. OLRule: Open loop rule: Assume that the MS transmits according to the open loop power rule: The sum of the mean input power at the MS receiver plus the mean output power at the MS transmitter is maintained at a constant 'power offset' value: input power + output power = power offset. The power offset depends on the band class; see 3GPP2 C.S0057-D. MAX: Maximum: Assume that MS transmits at its maximum output power (RMS value ≤+23 dBm) . MIN: Minimum: Assume that MS transmits at its minimum output power (RMS value ≤–47 dBm) .
		"""
		param = Conversions.enum_scalar_to_str(exp_power_mode, enums.ExpectedPowerMode)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RFPower:EPMode {param}')

	def get_manual(self) -> float:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFPower:MANual \n
		Snippet: value: float = driver.configure.rfPower.get_manual() \n
		Set the value of expected power of the MS to transmit. Only applicable if for parameter 'Expected Power Mode' (method
		RsCmwCdma2kSig.Configure.RfPower.epmode) Manual is selected. \n
			:return: manual_exp_power: Range: -47 dBm to 55 dBm, Unit: dBm
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RFPower:MANual?')
		return Conversions.str_to_float(response)

	def set_manual(self, manual_exp_power: float) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFPower:MANual \n
		Snippet: driver.configure.rfPower.set_manual(manual_exp_power = 1.0) \n
		Set the value of expected power of the MS to transmit. Only applicable if for parameter 'Expected Power Mode' (method
		RsCmwCdma2kSig.Configure.RfPower.epmode) Manual is selected. \n
			:param manual_exp_power: Range: -47 dBm to 55 dBm, Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(manual_exp_power)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RFPower:MANual {param}')

	def clone(self) -> 'RfPower':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RfPower(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
