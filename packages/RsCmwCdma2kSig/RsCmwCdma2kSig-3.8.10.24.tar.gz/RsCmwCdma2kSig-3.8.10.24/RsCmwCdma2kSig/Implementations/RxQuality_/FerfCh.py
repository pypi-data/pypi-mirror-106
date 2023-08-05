from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FerfCh:
	"""FerfCh commands group definition. 5 total commands, 2 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ferfCh", core, parent)

	@property
	def tdata(self):
		"""tdata commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_tdata'):
			from .FerfCh_.Tdata import Tdata
			self._tdata = Tdata(self._core, self._base)
		return self._tdata

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .FerfCh_.State import State
			self._state = State(self._core, self._base)
		return self._state

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Ferf_Ch: float: Forward link frame error rate Queries the percentage of the frame error rate over the total number of received frames for FCH. Range: 0 % to 100 %, Unit: %
			- Confidence_Level: float: Measured confidence level Queries the statistical probability that the true FER is within limits based on the current number of frame errors compared to the number of frames received. Range: 0 % to 100 %, Unit: %
			- Frame_Errors: int: Total number of detected frame errors. Range: 0 to 100E+3
			- Frames: int: Total number of test frames sent. Range: 0 to 100E+3
			- Erased_Frames: int: Total number of erased frames (counted as errored frames) . Not all errored frames are erased. Some can be undetected by the MS. Range: 0 to 100E+3"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Ferf_Ch'),
			ArgStruct.scalar_float('Confidence_Level'),
			ArgStruct.scalar_int('Frame_Errors'),
			ArgStruct.scalar_int('Frames'),
			ArgStruct.scalar_int('Erased_Frames')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Ferf_Ch: float = None
			self.Confidence_Level: float = None
			self.Frame_Errors: int = None
			self.Frames: int = None
			self.Erased_Frames: int = None

	def read(self) -> ResultData:
		"""SCPI: READ:CDMA:SIGNaling<Instance>:RXQuality:FERFch \n
		Snippet: value: ResultData = driver.rxQuality.ferfCh.read() \n
		Returns the results of the forward link FER measurement, see 'FER FCH / FER SCH0 View (Tab) '. The values described below
		are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result
		listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:CDMA:SIGNaling<Instance>:RXQuality:FERFch?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:CDMA:SIGNaling<Instance>:RXQuality:FERFch \n
		Snippet: value: ResultData = driver.rxQuality.ferfCh.fetch() \n
		Returns the results of the forward link FER measurement, see 'FER FCH / FER SCH0 View (Tab) '. The values described below
		are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result
		listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:CDMA:SIGNaling<Instance>:RXQuality:FERFch?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Ferf_Ch: float: Forward link frame error rate Queries the percentage of the frame error rate over the total number of received frames for FCH. Range: 0 % to 100 %, Unit: %
			- Confidence_Level: float: Measured confidence level Queries the statistical probability that the true FER is within limits based on the current number of frame errors compared to the number of frames received. Range: 0 % to 100 %, Unit: %
			- Frame_Errors: float: Total number of detected frame errors. Range: 0 to 100E+3
			- Frames: float: Total number of test frames sent. Range: 0 to 100E+3
			- Erased_Frames: int: Total number of erased frames (counted as errored frames) . Not all errored frames are erased. Some can be undetected by the MS. Range: 0 to 100E+3"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Ferf_Ch'),
			ArgStruct.scalar_float('Confidence_Level'),
			ArgStruct.scalar_float('Frame_Errors'),
			ArgStruct.scalar_float('Frames'),
			ArgStruct.scalar_int('Erased_Frames')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Ferf_Ch: float = None
			self.Confidence_Level: float = None
			self.Frame_Errors: float = None
			self.Frames: float = None
			self.Erased_Frames: int = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:CDMA:SIGNaling<Instance>:RXQuality:FERFch \n
		Snippet: value: CalculateStruct = driver.rxQuality.ferfCh.calculate() \n
		Returns the results of the forward link FER measurement, see 'FER FCH / FER SCH0 View (Tab) '. The values described below
		are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result
		listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:CDMA:SIGNaling<Instance>:RXQuality:FERFch?', self.__class__.CalculateStruct())

	def clone(self) -> 'FerfCh':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FerfCh(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
