from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Receive:
	"""Receive commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("receive", core, parent)

	# noinspection PyTypeChecker
	class WatermarkStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Queue_Depth: int: Number of messages waiting in the queue
			- Queue_State: enums.QueueState: OK | OVERflow Overflow indication flag"""
		__meta_args_list = [
			ArgStruct.scalar_int('Queue_Depth'),
			ArgStruct.scalar_enum('Queue_State', enums.QueueState)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Queue_Depth: int = None
			self.Queue_State: enums.QueueState = None

	def get_watermark(self) -> WatermarkStruct:
		"""SCPI: CALL:CDMA:SIGNaling<Instance>:PDM:RECeive:WATermark \n
		Snippet: value: WatermarkStruct = driver.call.pdm.receive.get_watermark() \n
		Returns the current depth and overflow status of the receive queue. If the queue overflows, new messages are lost until
		the queue is reset. After the overflow, the existing messages in the queue still can be read. \n
			:return: structure: for return value, see the help for WatermarkStruct structure arguments.
		"""
		return self._core.io.query_struct('CALL:CDMA:SIGNaling<Instance>:PDM:RECeive:WATermark?', self.__class__.WatermarkStruct())

	def reset(self) -> None:
		"""SCPI: CALL:CDMA:SIGNaling<Instance>:PDM:RECeive:RESet \n
		Snippet: driver.call.pdm.receive.reset() \n
		Resets the incoming message queue and overflow flag. All messages in the queue are discarded. \n
		"""
		self._core.io.write(f'CALL:CDMA:SIGNaling<Instance>:PDM:RECeive:RESet')

	def reset_with_opc(self) -> None:
		"""SCPI: CALL:CDMA:SIGNaling<Instance>:PDM:RECeive:RESet \n
		Snippet: driver.call.pdm.receive.reset_with_opc() \n
		Resets the incoming message queue and overflow flag. All messages in the queue are discarded. \n
		Same as reset, but waits for the operation to complete before continuing further. Use the RsCmwCdma2kSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'CALL:CDMA:SIGNaling<Instance>:PDM:RECeive:RESet')
