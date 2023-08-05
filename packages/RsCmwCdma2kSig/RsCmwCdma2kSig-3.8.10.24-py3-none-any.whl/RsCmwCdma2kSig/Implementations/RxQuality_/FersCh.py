from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FersCh:
	"""FersCh commands group definition. 4 total commands, 1 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("fersCh", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .FersCh_.State import State
			self._state = State(self._core, self._base)
		return self._state

	# noinspection PyTypeChecker
	class ReadStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Fers_Ch_0: float: Forward link frame error rate Queries the percentage of the frame error rate over the total number of received frames for SCH0. Range: 0 % to 100 %, Unit: %
			- Confidence_Level: float: Measured confidence level Queries the statistical probability that the true FER is within limits based on the current number of frame errors compared to the number of frames received. Range: 0 % to 100 %, Unit: %
			- Frame_Errors: int: Total number of detected frame errors. Range: 0 to 100E+3
			- Frames: int: Total number of frames. Range: 0 to 100E+3
			- Erased_Frames: int: Total number of erased frames (counted as errored frames) . Not all errored frames are erased. Some can be undetected by the MS. Range: 0 to 100E+3"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Fers_Ch_0'),
			ArgStruct.scalar_float('Confidence_Level'),
			ArgStruct.scalar_int('Frame_Errors'),
			ArgStruct.scalar_int('Frames'),
			ArgStruct.scalar_int('Erased_Frames')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Fers_Ch_0: float = None
			self.Confidence_Level: float = None
			self.Frame_Errors: int = None
			self.Frames: int = None
			self.Erased_Frames: int = None

	def read(self) -> ReadStruct:
		"""SCPI: READ:CDMA:SIGNaling<Instance>:RXQuality:FERSch \n
		Snippet: value: ReadStruct = driver.rxQuality.fersCh.read() \n
		Returns the results of the forward link FER measurement, see 'FER FCH / FER SCH0 View (Tab) '. The values described below
		are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result
		listed below. \n
			:return: structure: for return value, see the help for ReadStruct structure arguments."""
		return self._core.io.query_struct(f'READ:CDMA:SIGNaling<Instance>:RXQuality:FERSch?', self.__class__.ReadStruct())

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Fers_Ch: float: Forward link frame error rate Queries the percentage of the frame error rate over the total number of received frames for SCH0. Range: 0 % to 100 %, Unit: %
			- Confidence_Level: float: Measured confidence level Queries the statistical probability that the true FER is within limits based on the current number of frame errors compared to the number of frames received. Range: 0 % to 100 %, Unit: %
			- Frame_Errors: int: Total number of detected frame errors. Range: 0 to 100E+3
			- Frames: int: Total number of frames. Range: 0 to 100E+3
			- Erased_Frames: int: Total number of erased frames (counted as errored frames) . Not all errored frames are erased. Some can be undetected by the MS. Range: 0 to 100E+3"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Fers_Ch'),
			ArgStruct.scalar_float('Confidence_Level'),
			ArgStruct.scalar_int('Frame_Errors'),
			ArgStruct.scalar_int('Frames'),
			ArgStruct.scalar_int('Erased_Frames')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Fers_Ch: float = None
			self.Confidence_Level: float = None
			self.Frame_Errors: int = None
			self.Frames: int = None
			self.Erased_Frames: int = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:CDMA:SIGNaling<Instance>:RXQuality:FERSch \n
		Snippet: value: FetchStruct = driver.rxQuality.fersCh.fetch() \n
		Returns the results of the forward link FER measurement, see 'FER FCH / FER SCH0 View (Tab) '. The values described below
		are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result
		listed below. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:CDMA:SIGNaling<Instance>:RXQuality:FERSch?', self.__class__.FetchStruct())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Fers_Ch: float: Forward link frame error rate Queries the percentage of the frame error rate over the total number of received frames for SCH0. Range: 0 % to 100 %, Unit: %
			- Confidence_Level: float: Measured confidence level Queries the statistical probability that the true FER is within limits based on the current number of frame errors compared to the number of frames received. Range: 0 % to 100 %, Unit: %
			- Frame_Errors: float: Total number of detected frame errors. Range: 0 to 100E+3
			- Frames: float: Total number of frames. Range: 0 to 100E+3
			- Erased_Frames: int: Total number of erased frames (counted as errored frames) . Not all errored frames are erased. Some can be undetected by the MS. Range: 0 to 100E+3"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Fers_Ch'),
			ArgStruct.scalar_float('Confidence_Level'),
			ArgStruct.scalar_float('Frame_Errors'),
			ArgStruct.scalar_float('Frames'),
			ArgStruct.scalar_int('Erased_Frames')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Fers_Ch: float = None
			self.Confidence_Level: float = None
			self.Frame_Errors: float = None
			self.Frames: float = None
			self.Erased_Frames: int = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:CDMA:SIGNaling<Instance>:RXQuality:FERSch \n
		Snippet: value: CalculateStruct = driver.rxQuality.fersCh.calculate() \n
		Returns the results of the forward link FER measurement, see 'FER FCH / FER SCH0 View (Tab) '. The values described below
		are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result
		listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:CDMA:SIGNaling<Instance>:RXQuality:FERSch?', self.__class__.CalculateStruct())

	def clone(self) -> 'FersCh':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FersCh(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
