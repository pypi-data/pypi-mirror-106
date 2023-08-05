from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RpControl:
	"""RpControl commands group definition. 6 total commands, 1 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rpControl", core, parent)

	@property
	def segment(self):
		"""segment commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_segment'):
			from .RpControl_.Segment import Segment
			self._segment = Segment(self._core, self._base)
		return self._segment

	# noinspection PyTypeChecker
	def get_pc_bits(self) -> enums.PowerCtrlBits:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RPControl:PCBits \n
		Snippet: value: enums.PowerCtrlBits = driver.configure.rpControl.get_pc_bits() \n
		Defines the power control bits within the generated CDMA signal. \n
			:return: power_ctrl_bits: AUTO | RTESt | AUP | ADOWn | HOLD | PATTern AUTO: Active closed loop power control: The R&S CMW sends the PCB needed to control the MS transmitter output power to the expected value. RTES: Range test: The R&S CMW sends a sequence of 128 up power bits (= 8 frames) followed by a sequence of 128 down power bits. AUP: All up: Sends only 0 as power control bits. ADOW: All down: Sends only 1 as power control bits. HOLD: Sends alternating 0/1 power control bits. Can be used to keep the current power level constant. PATT: Sends the user-specific segment bits executed by method RsCmwCdma2kSig.Configure.RpControl.run.
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RPControl:PCBits?')
		return Conversions.str_to_scalar_enum(response, enums.PowerCtrlBits)

	def set_pc_bits(self, power_ctrl_bits: enums.PowerCtrlBits) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RPControl:PCBits \n
		Snippet: driver.configure.rpControl.set_pc_bits(power_ctrl_bits = enums.PowerCtrlBits.ADOWn) \n
		Defines the power control bits within the generated CDMA signal. \n
			:param power_ctrl_bits: AUTO | RTESt | AUP | ADOWn | HOLD | PATTern AUTO: Active closed loop power control: The R&S CMW sends the PCB needed to control the MS transmitter output power to the expected value. RTES: Range test: The R&S CMW sends a sequence of 128 up power bits (= 8 frames) followed by a sequence of 128 down power bits. AUP: All up: Sends only 0 as power control bits. ADOW: All down: Sends only 1 as power control bits. HOLD: Sends alternating 0/1 power control bits. Can be used to keep the current power level constant. PATT: Sends the user-specific segment bits executed by method RsCmwCdma2kSig.Configure.RpControl.run.
		"""
		param = Conversions.enum_scalar_to_str(power_ctrl_bits, enums.PowerCtrlBits)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RPControl:PCBits {param}')

	def get_ssize(self) -> float:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RPControl:SSIZe \n
		Snippet: value: float = driver.configure.rpControl.get_ssize() \n
		Sets the power step size that the MS is to use for power control. The step size is the nominal change of the MS transmit
		power per single power control bit. \n
			:return: stepsize: Range: 0.25 dB | 0.5 dB | 1 dB , Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RPControl:SSIZe?')
		return Conversions.str_to_float(response)

	def set_ssize(self, stepsize: float) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RPControl:SSIZe \n
		Snippet: driver.configure.rpControl.set_ssize(stepsize = 1.0) \n
		Sets the power step size that the MS is to use for power control. The step size is the nominal change of the MS transmit
		power per single power control bit. \n
			:param stepsize: Range: 0.25 dB | 0.5 dB | 1 dB , Unit: dB
		"""
		param = Conversions.decimal_value_to_str(stepsize)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RPControl:SSIZe {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RPControl:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.rpControl.get_repetition() \n
		Specifies the repetition mode of the pattern execution. \n
			:return: repetition: SINGleshot | CONTinuous SINGleshot: the pattern execution is stopped after a single-shot CONTinuous: the pattern execution is repeated continuously and stopped by the method RsCmwCdma2kSig.Configure.RpControl.run
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RPControl:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RPControl:REPetition \n
		Snippet: driver.configure.rpControl.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		Specifies the repetition mode of the pattern execution. \n
			:param repetition: SINGleshot | CONTinuous SINGleshot: the pattern execution is stopped after a single-shot CONTinuous: the pattern execution is repeated continuously and stopped by the method RsCmwCdma2kSig.Configure.RpControl.run
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RPControl:REPetition {param}')

	def get_run(self) -> bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RPControl:RUN \n
		Snippet: value: bool = driver.configure.rpControl.get_run() \n
		Starts and in continuous mode also stops the execution of the user-specific pattern. \n
			:return: run_sequence_state: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RPControl:RUN?')
		return Conversions.str_to_bool(response)

	def set_run(self, run_sequence_state: bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RPControl:RUN \n
		Snippet: driver.configure.rpControl.set_run(run_sequence_state = False) \n
		Starts and in continuous mode also stops the execution of the user-specific pattern. \n
			:param run_sequence_state: OFF | ON
		"""
		param = Conversions.bool_to_str(run_sequence_state)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RPControl:RUN {param}')

	def clone(self) -> 'RpControl':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RpControl(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
