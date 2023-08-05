from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rlp:
	"""Rlp commands group definition. 18 total commands, 0 Sub-groups, 18 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rlp", core, parent)

	# noinspection PyTypeChecker
	class DunSegmentedStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rx: int: Number of RLP frames received in the last update period Range: 0 to 9.999999E+6
			- Rx_Total: int: Total number of RLP frames received during the PPP connection Range: 0 to 9.999999E+6
			- Tx: int: Number of RLP frames transmitted in the last update period Range: 0 to 9.999999E+6
			- Tx_Total: int: Total number of RLP frames transmitted during the PPP connection Range: 0 to 9.999999E+6"""
		__meta_args_list = [
			ArgStruct.scalar_int('Rx'),
			ArgStruct.scalar_int('Rx_Total'),
			ArgStruct.scalar_int('Tx'),
			ArgStruct.scalar_int('Tx_Total')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx: int = None
			self.Rx_Total: int = None
			self.Tx: int = None
			self.Tx_Total: int = None

	def get_dun_segmented(self) -> DunSegmentedStruct:
		"""SCPI: SENSe:CDMA:SIGNaling<Instance>:RXQuality:RLP:DUNSegmented \n
		Snippet: value: DunSegmentedStruct = driver.sense.rxQuality.rlp.get_dun_segmented() \n
		Queries number of RLP data frames of different types. See 'RLP and IP Statistics'. \n
			:return: structure: for return value, see the help for DunSegmentedStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:CDMA:SIGNaling<Instance>:RXQuality:RLP:DUNSegmented?', self.__class__.DunSegmentedStruct())

	# noinspection PyTypeChecker
	class DsegmentedStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rx: int: Number of RLP frames received in the last update period Range: 0 to 9.999999E+6
			- Rx_Total: int: Total number of RLP frames received during the PPP connection Range: 0 to 9.999999E+6
			- Tx: int: Number of RLP frames transmitted in the last update period Range: 0 to 9.999999E+6
			- Tx_Total: int: Total number of RLP frames transmitted during the PPP connection Range: 0 to 9.999999E+6"""
		__meta_args_list = [
			ArgStruct.scalar_int('Rx'),
			ArgStruct.scalar_int('Rx_Total'),
			ArgStruct.scalar_int('Tx'),
			ArgStruct.scalar_int('Tx_Total')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx: int = None
			self.Rx_Total: int = None
			self.Tx: int = None
			self.Tx_Total: int = None

	def get_dsegmented(self) -> DsegmentedStruct:
		"""SCPI: SENSe:CDMA:SIGNaling<Instance>:RXQuality:RLP:DSEGmented \n
		Snippet: value: DsegmentedStruct = driver.sense.rxQuality.rlp.get_dsegmented() \n
		Queries number of RLP data frames of different types. See 'RLP and IP Statistics'. \n
			:return: structure: for return value, see the help for DsegmentedStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:CDMA:SIGNaling<Instance>:RXQuality:RLP:DSEGmented?', self.__class__.DsegmentedStruct())

	# noinspection PyTypeChecker
	class FillStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rx: int: Number of RLP frames received in the last update period Range: 0 to 9.999999E+6
			- Rx_Total: int: Total number of RLP frames received during the PPP connection Range: 0 to 9.999999E+6
			- Tx: int: Number of RLP frames transmitted in the last update period Range: 0 to 9.999999E+6
			- Tx_Total: int: Total number of RLP frames transmitted during the PPP connection Range: 0 to 9.999999E+6"""
		__meta_args_list = [
			ArgStruct.scalar_int('Rx'),
			ArgStruct.scalar_int('Rx_Total'),
			ArgStruct.scalar_int('Tx'),
			ArgStruct.scalar_int('Tx_Total')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx: int = None
			self.Rx_Total: int = None
			self.Tx: int = None
			self.Tx_Total: int = None

	def get_fill(self) -> FillStruct:
		"""SCPI: SENSe:CDMA:SIGNaling<Instance>:RXQuality:RLP:FILL \n
		Snippet: value: FillStruct = driver.sense.rxQuality.rlp.get_fill() \n
		Queries number of RLP data frames of different types. See 'RLP and IP Statistics'. \n
			:return: structure: for return value, see the help for FillStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:CDMA:SIGNaling<Instance>:RXQuality:RLP:FILL?', self.__class__.FillStruct())

	# noinspection PyTypeChecker
	class IdleStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rx: int: Number of RLP frames received in the last update period Range: 0 to 9.999999E+6
			- Rx_Total: int: Total number of RLP frames received during the PPP connection Range: 0 to 9.999999E+6
			- Tx: int: Number of RLP frames transmitted in the last update period Range: 0 to 9.999999E+6
			- Tx_Total: int: Total number of RLP frames transmitted during the PPP connection Range: 0 to 9.999999E+6"""
		__meta_args_list = [
			ArgStruct.scalar_int('Rx'),
			ArgStruct.scalar_int('Rx_Total'),
			ArgStruct.scalar_int('Tx'),
			ArgStruct.scalar_int('Tx_Total')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx: int = None
			self.Rx_Total: int = None
			self.Tx: int = None
			self.Tx_Total: int = None

	def get_idle(self) -> IdleStruct:
		"""SCPI: SENSe:CDMA:SIGNaling<Instance>:RXQuality:RLP:IDLE \n
		Snippet: value: IdleStruct = driver.sense.rxQuality.rlp.get_idle() \n
		Queries number of RLP data frames of different types. See 'RLP and IP Statistics'. \n
			:return: structure: for return value, see the help for IdleStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:CDMA:SIGNaling<Instance>:RXQuality:RLP:IDLE?', self.__class__.IdleStruct())

	# noinspection PyTypeChecker
	class NakStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rx: int: Number of RLP frames received in the last update period Range: 0 to 9.999999E+6
			- Rx_Total: int: Total number of RLP frames received during the PPP connection Range: 0 to 9.999999E+6
			- Tx: int: Number of RLP frames transmitted in the last update period Range: 0 to 9.999999E+6
			- Tx_Total: int: Total number of RLP frames transmitted during the PPP connection Range: 0 to 9.999999E+6"""
		__meta_args_list = [
			ArgStruct.scalar_int('Rx'),
			ArgStruct.scalar_int('Rx_Total'),
			ArgStruct.scalar_int('Tx'),
			ArgStruct.scalar_int('Tx_Total')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx: int = None
			self.Rx_Total: int = None
			self.Tx: int = None
			self.Tx_Total: int = None

	def get_nak(self) -> NakStruct:
		"""SCPI: SENSe:CDMA:SIGNaling<Instance>:RXQuality:RLP:NAK \n
		Snippet: value: NakStruct = driver.sense.rxQuality.rlp.get_nak() \n
		Queries number of NAK RLP control frame that requests the retransmission of one or more data frames. \n
			:return: structure: for return value, see the help for NakStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:CDMA:SIGNaling<Instance>:RXQuality:RLP:NAK?', self.__class__.NakStruct())

	# noinspection PyTypeChecker
	class SyncStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rx: int: Number of RLP frames received in the last update period Range: 0 to 9.999999E+6
			- Rx_Total: int: Total number of RLP frames received during the PPP connection Range: 0 to 9.999999E+6
			- Tx: int: Number of RLP frames transmitted in the last update period Range: 0 to 9.999999E+6
			- Tx_Total: int: Total number of RLP frames transmitted during the PPP connection Range: 0 to 9.999999E+6"""
		__meta_args_list = [
			ArgStruct.scalar_int('Rx'),
			ArgStruct.scalar_int('Rx_Total'),
			ArgStruct.scalar_int('Tx'),
			ArgStruct.scalar_int('Tx_Total')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx: int = None
			self.Rx_Total: int = None
			self.Tx: int = None
			self.Tx_Total: int = None

	def get_sync(self) -> SyncStruct:
		"""SCPI: SENSe:CDMA:SIGNaling<Instance>:RXQuality:RLP:SYNC \n
		Snippet: value: SyncStruct = driver.sense.rxQuality.rlp.get_sync() \n
		Queries number of SYNC RLP control frames used during RLP initialization. See 'RLP and IP Statistics'. \n
			:return: structure: for return value, see the help for SyncStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:CDMA:SIGNaling<Instance>:RXQuality:RLP:SYNC?', self.__class__.SyncStruct())

	# noinspection PyTypeChecker
	class AckStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rx: int: Number of RLP frames received in the last update period Range: 0 to 9.999999E+6
			- Rx_Total: int: Total number of RLP frames received during the PPP connection Range: 0 to 9.999999E+6
			- Tx: int: Number of RLP frames transmitted in the last update period Range: 0 to 9.999999E+6
			- Tx_Total: int: Total number of RLP frames transmitted during the PPP connection Range: 0 to 9.999999E+6"""
		__meta_args_list = [
			ArgStruct.scalar_int('Rx'),
			ArgStruct.scalar_int('Rx_Total'),
			ArgStruct.scalar_int('Tx'),
			ArgStruct.scalar_int('Tx_Total')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx: int = None
			self.Rx_Total: int = None
			self.Tx: int = None
			self.Tx_Total: int = None

	def get_ack(self) -> AckStruct:
		"""SCPI: SENSe:CDMA:SIGNaling<Instance>:RXQuality:RLP:ACK \n
		Snippet: value: AckStruct = driver.sense.rxQuality.rlp.get_ack() \n
		Queries number of ACK RLP control frames used during RLP initialization. See 'RLP and IP Statistics'. \n
			:return: structure: for return value, see the help for AckStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:CDMA:SIGNaling<Instance>:RXQuality:RLP:ACK?', self.__class__.AckStruct())

	# noinspection PyTypeChecker
	class SackStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rx: int: Number of RLP frames received in the last update period Range: 0 to 9.999999E+6
			- Rx_Total: int: Total number of RLP frames received during the PPP connection Range: 0 to 9.999999E+6
			- Tx: int: Number of RLP frames transmitted in the last update period Range: 0 to 9.999999E+6
			- Tx_Total: int: Total number of RLP frames transmitted during the PPP connection Range: 0 to 9.999999E+6"""
		__meta_args_list = [
			ArgStruct.scalar_int('Rx'),
			ArgStruct.scalar_int('Rx_Total'),
			ArgStruct.scalar_int('Tx'),
			ArgStruct.scalar_int('Tx_Total')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx: int = None
			self.Rx_Total: int = None
			self.Tx: int = None
			self.Tx_Total: int = None

	def get_sack(self) -> SackStruct:
		"""SCPI: SENSe:CDMA:SIGNaling<Instance>:RXQuality:RLP:SACK \n
		Snippet: value: SackStruct = driver.sense.rxQuality.rlp.get_sack() \n
		Queries number of RLP control frames of different types used during RLP initialization. See 'RLP and IP Statistics'. \n
			:return: structure: for return value, see the help for SackStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:CDMA:SIGNaling<Instance>:RXQuality:RLP:SACK?', self.__class__.SackStruct())

	# noinspection PyTypeChecker
	class BdataStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rx: int: Number of RLP frames received in the last update period Range: 0 to 9.999999E+6
			- Rx_Total: int: Total number of RLP frames received during the PPP connection Range: 0 to 9.999999E+6
			- Tx: int: Number of RLP frames transmitted in the last update period Range: 0 to 9.999999E+6
			- Tx_Total: int: Total number of RLP frames transmitted during the PPP connection Range: 0 to 9.999999E+6"""
		__meta_args_list = [
			ArgStruct.scalar_int('Rx'),
			ArgStruct.scalar_int('Rx_Total'),
			ArgStruct.scalar_int('Tx'),
			ArgStruct.scalar_int('Tx_Total')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx: int = None
			self.Rx_Total: int = None
			self.Tx: int = None
			self.Tx_Total: int = None

	def get_bdata(self) -> BdataStruct:
		"""SCPI: SENSe:CDMA:SIGNaling<Instance>:RXQuality:RLP:BDATa \n
		Snippet: value: BdataStruct = driver.sense.rxQuality.rlp.get_bdata() \n
		Queries number of RLP data frames in B, C and D format. See 'RLP and IP Statistics'. \n
			:return: structure: for return value, see the help for BdataStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:CDMA:SIGNaling<Instance>:RXQuality:RLP:BDATa?', self.__class__.BdataStruct())

	# noinspection PyTypeChecker
	class CdataStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rx: int: Number of RLP frames received in the last update period Range: 0 to 9.999999E+6
			- Rx_Total: int: Total number of RLP frames received during the PPP connection Range: 0 to 9.999999E+6
			- Tx: int: Number of RLP frames transmitted in the last update period Range: 0 to 9.999999E+6
			- Tx_Total: int: Total number of RLP frames transmitted during the PPP connection Range: 0 to 9.999999E+6"""
		__meta_args_list = [
			ArgStruct.scalar_int('Rx'),
			ArgStruct.scalar_int('Rx_Total'),
			ArgStruct.scalar_int('Tx'),
			ArgStruct.scalar_int('Tx_Total')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx: int = None
			self.Rx_Total: int = None
			self.Tx: int = None
			self.Tx_Total: int = None

	def get_cdata(self) -> CdataStruct:
		"""SCPI: SENSe:CDMA:SIGNaling<Instance>:RXQuality:RLP:CDATa \n
		Snippet: value: CdataStruct = driver.sense.rxQuality.rlp.get_cdata() \n
		Queries number of RLP data frames in B, C and D format. See 'RLP and IP Statistics'. \n
			:return: structure: for return value, see the help for CdataStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:CDMA:SIGNaling<Instance>:RXQuality:RLP:CDATa?', self.__class__.CdataStruct())

	# noinspection PyTypeChecker
	class DdataStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rx: int: Number of RLP frames received in the last update period Range: 0 to 9.999999E+6
			- Rx_Total: int: Total number of RLP frames received during the PPP connection Range: 0 to 9.999999E+6
			- Tx: int: Number of RLP frames transmitted in the last update period Range: 0 to 9.999999E+6
			- Tx_Total: int: Total number of RLP frames transmitted during the PPP connection Range: 0 to 9.999999E+6"""
		__meta_args_list = [
			ArgStruct.scalar_int('Rx'),
			ArgStruct.scalar_int('Rx_Total'),
			ArgStruct.scalar_int('Tx'),
			ArgStruct.scalar_int('Tx_Total')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx: int = None
			self.Rx_Total: int = None
			self.Tx: int = None
			self.Tx_Total: int = None

	def get_ddata(self) -> DdataStruct:
		"""SCPI: SENSe:CDMA:SIGNaling<Instance>:RXQuality:RLP:DDATa \n
		Snippet: value: DdataStruct = driver.sense.rxQuality.rlp.get_ddata() \n
		Queries number of RLP data frames in B, C and D format. See 'RLP and IP Statistics'. \n
			:return: structure: for return value, see the help for DdataStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:CDMA:SIGNaling<Instance>:RXQuality:RLP:DDATa?', self.__class__.DdataStruct())

	# noinspection PyTypeChecker
	class ReasemblyStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rx: int: Number of RLP frames received in the last update period Range: 0 to 9.999999E+6
			- Rx_Total: int: Total number of RLP frames received during the PPP connection Range: 0 to 9.999999E+6
			- Tx: int: Number of RLP frames transmitted in the last update period Range: 0 to 9.999999E+6
			- Tx_Total: int: Total number of RLP frames transmitted during the PPP connection Range: 0 to 9.999999E+6"""
		__meta_args_list = [
			ArgStruct.scalar_int('Rx'),
			ArgStruct.scalar_int('Rx_Total'),
			ArgStruct.scalar_int('Tx'),
			ArgStruct.scalar_int('Tx_Total')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx: int = None
			self.Rx_Total: int = None
			self.Tx: int = None
			self.Tx_Total: int = None

	def get_reasembly(self) -> ReasemblyStruct:
		"""SCPI: SENSe:CDMA:SIGNaling<Instance>:RXQuality:RLP:REASembly \n
		Snippet: value: ReasemblyStruct = driver.sense.rxQuality.rlp.get_reasembly() \n
		Queries number of RLP control frames associated with RLP reassembly, sent between MS and AN. See 'RLP and IP Statistics'. \n
			:return: structure: for return value, see the help for ReasemblyStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:CDMA:SIGNaling<Instance>:RXQuality:RLP:REASembly?', self.__class__.ReasemblyStruct())

	# noinspection PyTypeChecker
	class BlankStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rx: int: Number of RLP frames received in the last update period Range: 0 to 9.999999E+6
			- Rx_Total: int: Total number of RLP frames received during the PPP connection Range: 0 to 9.999999E+6
			- Tx: int: Number of RLP frames transmitted in the last update period Range: 0 to 9.999999E+6
			- Tx_Total: int: Total number of RLP frames transmitted during the PPP connection Range: 0 to 9.999999E+6"""
		__meta_args_list = [
			ArgStruct.scalar_int('Rx'),
			ArgStruct.scalar_int('Rx_Total'),
			ArgStruct.scalar_int('Tx'),
			ArgStruct.scalar_int('Tx_Total')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx: int = None
			self.Rx_Total: int = None
			self.Tx: int = None
			self.Tx_Total: int = None

	def get_blank(self) -> BlankStruct:
		"""SCPI: SENSe:CDMA:SIGNaling<Instance>:RXQuality:RLP:BLANk \n
		Snippet: value: BlankStruct = driver.sense.rxQuality.rlp.get_blank() \n
		Queries number of RLP frames with no encapsulated data. \n
			:return: structure: for return value, see the help for BlankStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:CDMA:SIGNaling<Instance>:RXQuality:RLP:BLANk?', self.__class__.BlankStruct())

	# noinspection PyTypeChecker
	class InvalidStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rx: int: Number of RLP frames received in the last update period Range: 0 to 9.999999E+6
			- Rx_Total: int: Total number of RLP frames received during the PPP connection Range: 0 to 9.999999E+6
			- Tx: int: Number of RLP frames transmitted in the last update period Range: 0 to 9.999999E+6
			- Tx_Total: int: Total number of RLP frames transmitted during the PPP connection Range: 0 to 9.999999E+6"""
		__meta_args_list = [
			ArgStruct.scalar_int('Rx'),
			ArgStruct.scalar_int('Rx_Total'),
			ArgStruct.scalar_int('Tx'),
			ArgStruct.scalar_int('Tx_Total')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx: int = None
			self.Rx_Total: int = None
			self.Tx: int = None
			self.Tx_Total: int = None

	def get_invalid(self) -> InvalidStruct:
		"""SCPI: SENSe:CDMA:SIGNaling<Instance>:RXQuality:RLP:INValid \n
		Snippet: value: InvalidStruct = driver.sense.rxQuality.rlp.get_invalid() \n
		Queries number of RLP frames evaluated by RLP validity check as invalid. \n
			:return: structure: for return value, see the help for InvalidStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:CDMA:SIGNaling<Instance>:RXQuality:RLP:INValid?', self.__class__.InvalidStruct())

	# noinspection PyTypeChecker
	class SummaryStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rx: int: Number of RLP frames received in the last update period Range: 0 to 9.999999E+6
			- Rx_Total: int: Total number of RLP frames received since the beginning of the PPP connection Range: 0 to 9.999999E+6
			- Tx: int: Number of RLP frames transmitted in the last update period Range: 0 to 9.999999E+6
			- Tx_Total: int: Total number of RLP frames transmitted since the beginning of the PPP connection Range: 0 to 9.999999E+6"""
		__meta_args_list = [
			ArgStruct.scalar_int('Rx'),
			ArgStruct.scalar_int('Rx_Total'),
			ArgStruct.scalar_int('Tx'),
			ArgStruct.scalar_int('Tx_Total')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx: int = None
			self.Rx_Total: int = None
			self.Tx: int = None
			self.Tx_Total: int = None

	def get_summary(self) -> SummaryStruct:
		"""SCPI: SENSe:CDMA:SIGNaling<Instance>:RXQuality:RLP:SUMMary \n
		Snippet: value: SummaryStruct = driver.sense.rxQuality.rlp.get_summary() \n
		Queries total number of RLP frames from the measured RLP messages. \n
			:return: structure: for return value, see the help for SummaryStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:CDMA:SIGNaling<Instance>:RXQuality:RLP:SUMMary?', self.__class__.SummaryStruct())

	# noinspection PyTypeChecker
	class PppTotalStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rx: int: Total size of data received Range: 0 KB to 9.999999E+6 KB
			- Tx: int: Total size of data transmitted Range: 0 KB to 9.999999E+6 KB"""
		__meta_args_list = [
			ArgStruct.scalar_int('Rx'),
			ArgStruct.scalar_int('Tx')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx: int = None
			self.Tx: int = None

	def get_ppp_total(self) -> PppTotalStruct:
		"""SCPI: SENSe:CDMA:SIGNaling<Instance>:RXQuality:RLP:PPPTotal \n
		Snippet: value: PppTotalStruct = driver.sense.rxQuality.rlp.get_ppp_total() \n
		Queries total number of bytes the R&S CMW received (Rx) and sent (Tx) since the beginning of the PPP connection. \n
			:return: structure: for return value, see the help for PppTotalStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:CDMA:SIGNaling<Instance>:RXQuality:RLP:PPPTotal?', self.__class__.PppTotalStruct())

	# noinspection PyTypeChecker
	class DrateStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rx: float: Data rate in receive direction Range: 0 kbit/s to 9.999999E+6 kbit/s
			- Tx: float: Data rate in transmit direction Range: 0 kbit/s to 9.999999E+6 kbit/s"""
		__meta_args_list = [
			ArgStruct.scalar_float('Rx'),
			ArgStruct.scalar_float('Tx')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx: float = None
			self.Tx: float = None

	def get_drate(self) -> DrateStruct:
		"""SCPI: SENSe:CDMA:SIGNaling<Instance>:RXQuality:RLP:DRATe \n
		Snippet: value: DrateStruct = driver.sense.rxQuality.rlp.get_drate() \n
		Displays current data rate in kbit/s, averaged over the update period. \n
			:return: structure: for return value, see the help for DrateStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:CDMA:SIGNaling<Instance>:RXQuality:RLP:DRATe?', self.__class__.DrateStruct())

	def get_state(self) -> str:
		"""SCPI: SENSe:CDMA:SIGNaling<Instance>:RXQuality:RLP:STATe \n
		Snippet: value: str = driver.sense.rxQuality.rlp.get_state() \n
		Returns a string containing status information about the measurement. \n
			:return: status: See table below.
		"""
		response = self._core.io.query_str('SENSe:CDMA:SIGNaling<Instance>:RXQuality:RLP:STATe?')
		return trim_str_response(response)
