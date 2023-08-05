from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LrMessage:
	"""LrMessage commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("lrMessage", core, parent)

	def get_rflag(self) -> bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SMS:INFO:LRMessage:RFLag \n
		Snippet: value: bool = driver.configure.sms.info.lrMessage.get_rflag() \n
		Specifies whether the command method RsCmwCdma2kSig.Configure.Sms.Info.LrMessage.value was called for the last received
		message or not. Therefore it is possible to verify if the last received message was read and postprocessed or if it is a
		new received message that has not been read yet. Whenever the R&S CMW receives a new message the flag is reset to OFF. \n
			:return: last_rec_mess_read: OFF | ON OFF: Command method RsCmwCdma2kSig.Configure.Sms.Info.LrMessage.value was not called for the last received message. ON: Command method RsCmwCdma2kSig.Configure.Sms.Info.LrMessage.value was called for the last received message.
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:SMS:INFO:LRMessage:RFLag?')
		return Conversions.str_to_bool(response)

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Timestamp: str: String parameter, specifies when the message was received.
			- Teleservice_Id: str: String parameter, shows the teleservice identifier. CMT-91 | CPT-95 | CMT-95 | VMN-95 | WAP | WEMT | SCPT | CATPT
			- Message_Encoding: str: String parameter, shows the encoding of the message. ASCII, binary, Unicode
			- Message_Text: str: Message text. According to the encoding type the viewed content is encoded as binary, ASCII or Unicode.
			- Message_Length: int: Shows the number (decimal) of characters of the message text. Range: 0 to 10E+3
			- Message_Segments: int: Number of the current message segment. Range: 0 to 1000
			- Used_Send_Method: enums.SmsSendMethod: PCH | SO6 | SO14 | ACH | TCH Used send method for the message. PCH: Paging channel SO6: Service option 6 SO14: Service option 14 ACC: Access channel TCH: Traffic channel"""
		__meta_args_list = [
			ArgStruct.scalar_str('Timestamp'),
			ArgStruct.scalar_str('Teleservice_Id'),
			ArgStruct.scalar_str('Message_Encoding'),
			ArgStruct.scalar_str('Message_Text'),
			ArgStruct.scalar_int('Message_Length'),
			ArgStruct.scalar_int('Message_Segments'),
			ArgStruct.scalar_enum('Used_Send_Method', enums.SmsSendMethod)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Timestamp: str = None
			self.Teleservice_Id: str = None
			self.Message_Encoding: str = None
			self.Message_Text: str = None
			self.Message_Length: int = None
			self.Message_Segments: int = None
			self.Used_Send_Method: enums.SmsSendMethod = None

	def get_value(self) -> ValueStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SMS:INFO:LRMessage \n
		Snippet: value: ValueStruct = driver.configure.sms.info.lrMessage.get_value() \n
		Query information of the last received message. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:SMS:INFO:LRMessage?', self.__class__.ValueStruct())
