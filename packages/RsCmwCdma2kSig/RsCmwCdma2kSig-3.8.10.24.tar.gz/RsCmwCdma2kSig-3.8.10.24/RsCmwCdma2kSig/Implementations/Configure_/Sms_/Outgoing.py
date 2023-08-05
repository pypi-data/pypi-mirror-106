from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Outgoing:
	"""Outgoing commands group definition. 8 total commands, 1 Sub-groups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("outgoing", core, parent)

	@property
	def file(self):
		"""file commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_file'):
			from .Outgoing_.File import File
			self._file = File(self._core, self._base)
		return self._file

	# noinspection PyTypeChecker
	def get_smethod(self) -> enums.SmsSendMethod:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SMS:OUTGoing:SMEThod \n
		Snippet: value: enums.SmsSendMethod = driver.configure.sms.outgoing.get_smethod() \n
		Specifies the send method for the message file when the MS is in 'Registered' state. \n
			:return: send_method: PCH | SO6 | SO14 Send method PCH: Paging channel SO6: Service option 6 SO14: Service option 14 Range: PCH
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:SMS:OUTGoing:SMEThod?')
		return Conversions.str_to_scalar_enum(response, enums.SmsSendMethod)

	def set_smethod(self, send_method: enums.SmsSendMethod) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SMS:OUTGoing:SMEThod \n
		Snippet: driver.configure.sms.outgoing.set_smethod(send_method = enums.SmsSendMethod.ACH) \n
		Specifies the send method for the message file when the MS is in 'Registered' state. \n
			:param send_method: PCH | SO6 | SO14 Send method PCH: Paging channel SO6: Service option 6 SO14: Service option 14 Range: PCH
		"""
		param = Conversions.enum_scalar_to_str(send_method, enums.SmsSendMethod)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:SMS:OUTGoing:SMEThod {param}')

	def get_acknowledge(self) -> bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SMS:OUTGoing:ACKNowledge \n
		Snippet: value: bool = driver.configure.sms.outgoing.get_acknowledge() \n
		If checked, the R&S CMW requests the MS to return an SMS acknowledge message after receiving the message. \n
			:return: acknowledgement: OFF | ON OFF: No request for acknowledgment ON: R&S CMW requests MS for acknowledgment
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:SMS:OUTGoing:ACKNowledge?')
		return Conversions.str_to_bool(response)

	def set_acknowledge(self, acknowledgement: bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SMS:OUTGoing:ACKNowledge \n
		Snippet: driver.configure.sms.outgoing.set_acknowledge(acknowledgement = False) \n
		If checked, the R&S CMW requests the MS to return an SMS acknowledge message after receiving the message. \n
			:param acknowledgement: OFF | ON OFF: No request for acknowledgment ON: R&S CMW requests MS for acknowledgment
		"""
		param = Conversions.bool_to_str(acknowledgement)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:SMS:OUTGoing:ACKNowledge {param}')

	def get_atstamp(self) -> bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SMS:OUTGoing:ATSTamp \n
		Snippet: value: bool = driver.configure.sms.outgoing.get_atstamp() \n
		Specifies whether the R&S CMW adds a time stamp when the message is sent to the MS. \n
			:return: add_time_stamp: OFF | ON OFF: Omit time stamp. ON: Add time stamp with the current send time.
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:SMS:OUTGoing:ATSTamp?')
		return Conversions.str_to_bool(response)

	def set_atstamp(self, add_time_stamp: bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SMS:OUTGoing:ATSTamp \n
		Snippet: driver.configure.sms.outgoing.set_atstamp(add_time_stamp = False) \n
		Specifies whether the R&S CMW adds a time stamp when the message is sent to the MS. \n
			:param add_time_stamp: OFF | ON OFF: Omit time stamp. ON: Add time stamp with the current send time.
		"""
		param = Conversions.bool_to_str(add_time_stamp)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:SMS:OUTGoing:ATSTamp {param}')

	# noinspection PyTypeChecker
	def get_lhandling(self) -> enums.LongSmsHandling:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SMS:OUTGoing:LHANdling \n
		Snippet: value: enums.LongSmsHandling = driver.configure.sms.outgoing.get_lhandling() \n
		Manage SMS messages, which exceed the maximum physical size of an SMS message. According to the transmit method (PCH, SO6,
		SO14, traffic channel) and data encoding (ASCII, binary or Unicode) the maximum physical size of one SMS varies. \n
			:return: lsms_handling: TRUNcate | MSMS TRUNcate: Truncate the outgoing SMS message text to the length of exactly one SMS message. MSMS: Multiple SMS. If the SMS message exceeds the maximum physical size of one SMS, the R&S CMW cuts the entire message into multiple messages and sends the multiple messages consecutively.
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:SMS:OUTGoing:LHANdling?')
		return Conversions.str_to_scalar_enum(response, enums.LongSmsHandling)

	def set_lhandling(self, lsms_handling: enums.LongSmsHandling) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SMS:OUTGoing:LHANdling \n
		Snippet: driver.configure.sms.outgoing.set_lhandling(lsms_handling = enums.LongSmsHandling.MSMS) \n
		Manage SMS messages, which exceed the maximum physical size of an SMS message. According to the transmit method (PCH, SO6,
		SO14, traffic channel) and data encoding (ASCII, binary or Unicode) the maximum physical size of one SMS varies. \n
			:param lsms_handling: TRUNcate | MSMS TRUNcate: Truncate the outgoing SMS message text to the length of exactly one SMS message. MSMS: Multiple SMS. If the SMS message exceeds the maximum physical size of one SMS, the R&S CMW cuts the entire message into multiple messages and sends the multiple messages consecutively.
		"""
		param = Conversions.enum_scalar_to_str(lsms_handling, enums.LongSmsHandling)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:SMS:OUTGoing:LHANdling {param}')

	# noinspection PyTypeChecker
	def get_mes_handling(self) -> enums.MessageHandling:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SMS:OUTGoing:MESHandling \n
		Snippet: value: enums.MessageHandling = driver.configure.sms.outgoing.get_mes_handling() \n
		Specifies whether the outgoing message text is entered manually (method RsCmwCdma2kSig.Configure.Sms.Outgoing.internal)
		or an existing SMS file is taken, which is selected via method RsCmwCdma2kSig.Configure.Sms.Outgoing.File.value. \n
			:return: message_handling: INTernal | FILE INTernal: Content is entered manually FILE: Use an existing *.sms file.
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:SMS:OUTGoing:MESHandling?')
		return Conversions.str_to_scalar_enum(response, enums.MessageHandling)

	def set_mes_handling(self, message_handling: enums.MessageHandling) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SMS:OUTGoing:MESHandling \n
		Snippet: driver.configure.sms.outgoing.set_mes_handling(message_handling = enums.MessageHandling.FILE) \n
		Specifies whether the outgoing message text is entered manually (method RsCmwCdma2kSig.Configure.Sms.Outgoing.internal)
		or an existing SMS file is taken, which is selected via method RsCmwCdma2kSig.Configure.Sms.Outgoing.File.value. \n
			:param message_handling: INTernal | FILE INTernal: Content is entered manually FILE: Use an existing *.sms file.
		"""
		param = Conversions.enum_scalar_to_str(message_handling, enums.MessageHandling)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:SMS:OUTGoing:MESHandling {param}')

	def get_internal(self) -> str:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SMS:OUTGoing:INTernal \n
		Snippet: value: str = driver.configure.sms.outgoing.get_internal() \n
		Specifies the text of the short message to send to the MS for method RsCmwCdma2kSig.Configure.Sms.Outgoing.internal =
		'Use Internal'. The message is always encoded as 7-bit ASCII text and has the teleservice ID 'CMT-95'. For other formats,
		create an SMS message file and select it via method RsCmwCdma2kSig.Configure.Sms.Outgoing.File.value. \n
			:return: sms_internal: String parameter to specify the message text.
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:SMS:OUTGoing:INTernal?')
		return trim_str_response(response)

	def set_internal(self, sms_internal: str) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SMS:OUTGoing:INTernal \n
		Snippet: driver.configure.sms.outgoing.set_internal(sms_internal = '1') \n
		Specifies the text of the short message to send to the MS for method RsCmwCdma2kSig.Configure.Sms.Outgoing.internal =
		'Use Internal'. The message is always encoded as 7-bit ASCII text and has the teleservice ID 'CMT-95'. For other formats,
		create an SMS message file and select it via method RsCmwCdma2kSig.Configure.Sms.Outgoing.File.value. \n
			:param sms_internal: String parameter to specify the message text.
		"""
		param = Conversions.value_to_quoted_str(sms_internal)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:SMS:OUTGoing:INTernal {param}')

	def clone(self) -> 'Outgoing':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Outgoing(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
