from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class File:
	"""File commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("file", core, parent)

	# noinspection PyTypeChecker
	class InfoStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Timestamp: str: String parameter, time stamp of sending.
			- Teleservice_Id: str: String parameter, shows the teleservice identifier. CMT-91 | CPT-95 | CMT-95 | VMN-95 | WAP | WEMT | SCPT | CATPT
			- Message_Encoding: str: String parameter, shows the encoding of the message. ASCII, binary, Unicode
			- Message_Text: str: String parameter, shows the message text.
			- Message_Length: int: Shows the number (decimal) of characters of the message text. Range: 0 to 10E+3
			- Message_Segments: int: Shows the number (decimal) of the current received message segment of a large SMS message. If 'Concatenate Sequential SMS' is checked and if multiple message files for one large SMS message are received, the counter increments. Otherwise the parameter has always value '1'. Range: 0 to 1000
			- Used_Send_Method: enums.SmsSendMethod: SO6 | SO14 | ACH | TCH Shows the used send method of the MS. SO6: Service option 6 SO14: Service option 14 ACH: Access channel TCH: Traffic channel"""
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

	def get_info(self) -> InfoStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SMS:INComing:FILE:INFO \n
		Snippet: value: InfoStruct = driver.configure.sms.incoming.file.get_info() \n
		Display information of the received message file referenced by method RsCmwCdma2kSig.Configure.Sms.Incoming.File.value. \n
			:return: structure: for return value, see the help for InfoStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:SMS:INComing:FILE:INFO?', self.__class__.InfoStruct())

	def get_value(self) -> str:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SMS:INComing:FILE \n
		Snippet: value: str = driver.configure.sms.incoming.file.get_value() \n
		Selects a received message file. The files are stored in directory D:/Rohde-Schwarz/CMW/Data/sms/CDMA2000/Received. \n
			:return: sms_file: String parameter to specify the received message file.
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:SMS:INComing:FILE?')
		return trim_str_response(response)

	def set_value(self, sms_file: str) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SMS:INComing:FILE \n
		Snippet: driver.configure.sms.incoming.file.set_value(sms_file = '1') \n
		Selects a received message file. The files are stored in directory D:/Rohde-Schwarz/CMW/Data/sms/CDMA2000/Received. \n
			:param sms_file: String parameter to specify the received message file.
		"""
		param = Conversions.value_to_quoted_str(sms_file)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:SMS:INComing:FILE {param}')
