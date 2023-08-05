from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Info:
	"""Info commands group definition. 3 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("info", core, parent)

	@property
	def lrMessage(self):
		"""lrMessage commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_lrMessage'):
			from .Info_.LrMessage import LrMessage
			self._lrMessage = LrMessage(self._core, self._base)
		return self._lrMessage

	# noinspection PyTypeChecker
	class LsMessageStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Timestamp: str: Information about sent time of the message.
			- Acknowledgement: enums.AckState: NACK | ACK ACK: MS acknowledged last message. NACK: MS did not acknowledge last message. (Not requested or failed.)
			- Cause_Code: str: String parameter, provides the delivery status of the message user data. Refer to 'SMS_Cause_Code'.
			- Message_Length: int: Shows the number (decimal) of characters of the message text. Range: 0 to 10E+3
			- Message_Segments: int: Number of the current segment. Range: 0 to 1000
			- Used_Send_Method: enums.SmsSendMethod: PCH | SO6 | SO14 | TCH Used send method of the last sent message. PCH: Paging channel SO6: Service option 6 SO14: Service option 14 TCH: Traffic channel"""
		__meta_args_list = [
			ArgStruct.scalar_str('Timestamp'),
			ArgStruct.scalar_enum('Acknowledgement', enums.AckState),
			ArgStruct.scalar_str('Cause_Code'),
			ArgStruct.scalar_int('Message_Length'),
			ArgStruct.scalar_int('Message_Segments'),
			ArgStruct.scalar_enum('Used_Send_Method', enums.SmsSendMethod)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Timestamp: str = None
			self.Acknowledgement: enums.AckState = None
			self.Cause_Code: str = None
			self.Message_Length: int = None
			self.Message_Segments: int = None
			self.Used_Send_Method: enums.SmsSendMethod = None

	def get_ls_message(self) -> LsMessageStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SMS:INFO:LSMessage \n
		Snippet: value: LsMessageStruct = driver.configure.sms.info.get_ls_message() \n
		Query information of the last sent message. \n
			:return: structure: for return value, see the help for LsMessageStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:SMS:INFO:LSMessage?', self.__class__.LsMessageStruct())

	def clone(self) -> 'Info':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Info(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
