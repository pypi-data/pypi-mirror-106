from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal import Conversions
from .. import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Configure:
	"""Configure commands group definition. 242 total commands, 20 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("configure", core, parent)

	@property
	def test(self):
		"""test commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_test'):
			from .Configure_.Test import Test
			self._test = Test(self._core, self._base)
		return self._test

	@property
	def rfSettings(self):
		"""rfSettings commands group. 0 Sub-classes, 7 commands."""
		if not hasattr(self, '_rfSettings'):
			from .Configure_.RfSettings import RfSettings
			self._rfSettings = RfSettings(self._core, self._base)
		return self._rfSettings

	@property
	def fading(self):
		"""fading commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_fading'):
			from .Configure_.Fading import Fading
			self._fading = Fading(self._core, self._base)
		return self._fading

	@property
	def iqIn(self):
		"""iqIn commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqIn'):
			from .Configure_.IqIn import IqIn
			self._iqIn = IqIn(self._core, self._base)
		return self._iqIn

	@property
	def mmonitor(self):
		"""mmonitor commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_mmonitor'):
			from .Configure_.Mmonitor import Mmonitor
			self._mmonitor = Mmonitor(self._core, self._base)
		return self._mmonitor

	@property
	def cstatus(self):
		"""cstatus commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_cstatus'):
			from .Configure_.Cstatus import Cstatus
			self._cstatus = Cstatus(self._core, self._base)
		return self._cstatus

	@property
	def rfPower(self):
		"""rfPower commands group. 3 Sub-classes, 5 commands."""
		if not hasattr(self, '_rfPower'):
			from .Configure_.RfPower import RfPower
			self._rfPower = RfPower(self._core, self._base)
		return self._rfPower

	@property
	def layer(self):
		"""layer commands group. 6 Sub-classes, 2 commands."""
		if not hasattr(self, '_layer'):
			from .Configure_.Layer import Layer
			self._layer = Layer(self._core, self._base)
		return self._layer

	@property
	def rpControl(self):
		"""rpControl commands group. 1 Sub-classes, 4 commands."""
		if not hasattr(self, '_rpControl'):
			from .Configure_.RpControl import RpControl
			self._rpControl = RpControl(self._core, self._base)
		return self._rpControl

	@property
	def system(self):
		"""system commands group. 1 Sub-classes, 7 commands."""
		if not hasattr(self, '_system'):
			from .Configure_.System import System
			self._system = System(self._core, self._base)
		return self._system

	@property
	def sconfig(self):
		"""sconfig commands group. 4 Sub-classes, 2 commands."""
		if not hasattr(self, '_sconfig'):
			from .Configure_.Sconfig import Sconfig
			self._sconfig = Sconfig(self._core, self._base)
		return self._sconfig

	@property
	def network(self):
		"""network commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_network'):
			from .Configure_.Network import Network
			self._network = Network(self._core, self._base)
		return self._network

	@property
	def connection(self):
		"""connection commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_connection'):
			from .Configure_.Connection import Connection
			self._connection = Connection(self._core, self._base)
		return self._connection

	@property
	def msInfo(self):
		"""msInfo commands group. 0 Sub-classes, 9 commands."""
		if not hasattr(self, '_msInfo'):
			from .Configure_.MsInfo import MsInfo
			self._msInfo = MsInfo(self._core, self._base)
		return self._msInfo

	@property
	def capabilities(self):
		"""capabilities commands group. 5 Sub-classes, 9 commands."""
		if not hasattr(self, '_capabilities'):
			from .Configure_.Capabilities import Capabilities
			self._capabilities = Capabilities(self._core, self._base)
		return self._capabilities

	@property
	def handoff(self):
		"""handoff commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_handoff'):
			from .Configure_.Handoff import Handoff
			self._handoff = Handoff(self._core, self._base)
		return self._handoff

	@property
	def reconfigure(self):
		"""reconfigure commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_reconfigure'):
			from .Configure_.Reconfigure import Reconfigure
			self._reconfigure = Reconfigure(self._core, self._base)
		return self._reconfigure

	@property
	def preconfigure(self):
		"""preconfigure commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_preconfigure'):
			from .Configure_.Preconfigure import Preconfigure
			self._preconfigure = Preconfigure(self._core, self._base)
		return self._preconfigure

	@property
	def sms(self):
		"""sms commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_sms'):
			from .Configure_.Sms import Sms
			self._sms = Sms(self._core, self._base)
		return self._sms

	@property
	def rxQuality(self):
		"""rxQuality commands group. 6 Sub-classes, 2 commands."""
		if not hasattr(self, '_rxQuality'):
			from .Configure_.RxQuality import RxQuality
			self._rxQuality = RxQuality(self._core, self._base)
		return self._rxQuality

	# noinspection PyTypeChecker
	def get_display(self) -> enums.DisplayTab:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:DISPlay \n
		Snippet: value: enums.DisplayTab = driver.configure.get_display() \n
		Selects the view to be shown when the display is switched on during remote control. \n
			:return: tab: FERFch | FERSch0 | RLP | SPEech RX measurement: 'FER FCH', 'FER SCH0', 'RLP', 'Speech'
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:DISPlay?')
		return Conversions.str_to_scalar_enum(response, enums.DisplayTab)

	def set_display(self, tab: enums.DisplayTab) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:DISPlay \n
		Snippet: driver.configure.set_display(tab = enums.DisplayTab.FERFch) \n
		Selects the view to be shown when the display is switched on during remote control. \n
			:param tab: FERFch | FERSch0 | RLP | SPEech RX measurement: 'FER FCH', 'FER SCH0', 'RLP', 'Speech'
		"""
		param = Conversions.enum_scalar_to_str(tab, enums.DisplayTab)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:DISPlay {param}')

	def get_etoe(self) -> bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:ETOE \n
		Snippet: value: bool = driver.configure.get_etoe() \n
		Enables the setup of a connection between the signaling unit and the data application unit (DAU) , required for IP-based
		data tests involving the DAU. \n
			:return: end_to_end_enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:ETOE?')
		return Conversions.str_to_bool(response)

	def set_etoe(self, end_to_end_enable: bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:ETOE \n
		Snippet: driver.configure.set_etoe(end_to_end_enable = False) \n
		Enables the setup of a connection between the signaling unit and the data application unit (DAU) , required for IP-based
		data tests involving the DAU. \n
			:param end_to_end_enable: OFF | ON
		"""
		param = Conversions.bool_to_str(end_to_end_enable)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:ETOE {param}')

	def get_es_code(self) -> bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:ESCode \n
		Snippet: value: bool = driver.configure.get_es_code() \n
		No command help available \n
			:return: espeech_codec: No help available
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:ESCode?')
		return Conversions.str_to_bool(response)

	def set_es_code(self, espeech_codec: bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:ESCode \n
		Snippet: driver.configure.set_es_code(espeech_codec = False) \n
		No command help available \n
			:param espeech_codec: No help available
		"""
		param = Conversions.bool_to_str(espeech_codec)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:ESCode {param}')

	def clone(self) -> 'Configure':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Configure(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
