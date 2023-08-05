from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Send:
	"""Send commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("send", core, parent)

	def set_transmit(self, byte_array: bytes) -> None:
		"""SCPI: CALL:CDMA:SIGNaling<Instance>:OTASp:SEND:TRANsmit \n
		Snippet: driver.call.otasp.send.set_transmit(byte_array = b'ABCDEFGH') \n
		Sends binary data blocks to the MS. Data longer than the transport container are discarded and an error set. The data
		format corresponds to IEEE-488.2. \n
			:param byte_array: block
		"""
		self._core.io.write_bin_block('CALL:CDMA:SIGNaling<Instance>:OTASp:SEND:TRANsmit ', byte_array)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.OtaspSendMethodA:
		"""SCPI: CALL:CDMA:SIGNaling<Instance>:OTASp:SEND:MODE \n
		Snippet: value: enums.OtaspSendMethodA = driver.call.otasp.send.get_mode() \n
		Specifies the sending method for the OTASP messages. \n
			:return: send_method: NONE | SO18 | SO19 NONE: If a call does not exist, drop the message, do not establish a call. SOxx: If a call does not exist, establish a call using specified service option. The call will be released after the message is sent and acknowledged.
		"""
		response = self._core.io.query_str('CALL:CDMA:SIGNaling<Instance>:OTASp:SEND:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.OtaspSendMethodA)

	def set_mode(self, send_method: enums.OtaspSendMethodA) -> None:
		"""SCPI: CALL:CDMA:SIGNaling<Instance>:OTASp:SEND:MODE \n
		Snippet: driver.call.otasp.send.set_mode(send_method = enums.OtaspSendMethodA.NONE) \n
		Specifies the sending method for the OTASP messages. \n
			:param send_method: NONE | SO18 | SO19 NONE: If a call does not exist, drop the message, do not establish a call. SOxx: If a call does not exist, establish a call using specified service option. The call will be released after the message is sent and acknowledged.
		"""
		param = Conversions.enum_scalar_to_str(send_method, enums.OtaspSendMethodA)
		self._core.io.write(f'CALL:CDMA:SIGNaling<Instance>:OTASp:SEND:MODE {param}')

	# noinspection PyTypeChecker
	class StatusStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Delivery_Status: enums.DeliveryStatus: SUCCess | ACKTimeout | PENDing | CSTate | BADData SUCCess: successfully transmitted ACKTimeout: acknowledgment timeout appeared PENDing: message pending in the outgoing buffer CSTate: wrong call state (wrong service option or no registered device) BADData: wrong message length (zero or too long)
			- Timestamp: float: The message transmit time for the delivery status SUCC or ACKT with granularity of 20 ms Unit: s
			- Send_Method: enums.OtaspSendMethodB: NONE | TCH NONE: The message has not been sent yet. TCH: An existing call was used to send the message."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Delivery_Status', enums.DeliveryStatus),
			ArgStruct.scalar_float('Timestamp'),
			ArgStruct.scalar_enum('Send_Method', enums.OtaspSendMethodB)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Delivery_Status: enums.DeliveryStatus = None
			self.Timestamp: float = None
			self.Send_Method: enums.OtaspSendMethodB = None

	# noinspection PyTypeChecker
	def get_status(self) -> StatusStruct:
		"""SCPI: CALL:CDMA:SIGNaling<Instance>:OTASp:SEND:STATus \n
		Snippet: value: StatusStruct = driver.call.otasp.send.get_status() \n
		Returns the status, timestamp and transport of the last message sent. \n
			:return: structure: for return value, see the help for StatusStruct structure arguments.
		"""
		return self._core.io.query_struct('CALL:CDMA:SIGNaling<Instance>:OTASp:SEND:STATus?', self.__class__.StatusStruct())
