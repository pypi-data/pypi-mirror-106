from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RxQuality:
	"""RxQuality commands group definition. 22 total commands, 6 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rxQuality", core, parent)

	@property
	def result(self):
		"""result commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_result'):
			from .RxQuality_.Result import Result
			self._result = Result(self._core, self._base)
		return self._result

	@property
	def ferfCh(self):
		"""ferfCh commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_ferfCh'):
			from .RxQuality_.FerfCh import FerfCh
			self._ferfCh = FerfCh(self._core, self._base)
		return self._ferfCh

	@property
	def fersCh(self):
		"""fersCh commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_fersCh'):
			from .RxQuality_.FersCh import FersCh
			self._fersCh = FersCh(self._core, self._base)
		return self._fersCh

	@property
	def rstatistics(self):
		"""rstatistics commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rstatistics'):
			from .RxQuality_.Rstatistics import Rstatistics
			self._rstatistics = Rstatistics(self._core, self._base)
		return self._rstatistics

	@property
	def pstrength(self):
		"""pstrength commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_pstrength'):
			from .RxQuality_.Pstrength import Pstrength
			self._pstrength = Pstrength(self._core, self._base)
		return self._pstrength

	@property
	def limit(self):
		"""limit commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_limit'):
			from .RxQuality_.Limit import Limit
			self._limit = Limit(self._core, self._base)
		return self._limit

	def get_urate(self) -> float:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RXQuality:URATe \n
		Snippet: value: float = driver.configure.rxQuality.get_urate() \n
		Defines update rate for RLP and speech view. \n
			:return: update_rate: Range: 0.25 s to 2 s
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RXQuality:URATe?')
		return Conversions.str_to_float(response)

	def set_urate(self, update_rate: float) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RXQuality:URATe \n
		Snippet: driver.configure.rxQuality.set_urate(update_rate = 1.0) \n
		Defines update rate for RLP and speech view. \n
			:param update_rate: Range: 0.25 s to 2 s
		"""
		param = Conversions.decimal_value_to_str(update_rate)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RXQuality:URATe {param}')

	def get_window_size(self) -> int:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RXQuality:WINDowsize \n
		Snippet: value: int = driver.configure.rxQuality.get_window_size() \n
		Sets the active window size in an RLP measurement. \n
			:return: size: Range: 10 s to 240 s , Unit: s
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RXQuality:WINDowsize?')
		return Conversions.str_to_int(response)

	def set_window_size(self, size: int) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RXQuality:WINDowsize \n
		Snippet: driver.configure.rxQuality.set_window_size(size = 1) \n
		Sets the active window size in an RLP measurement. \n
			:param size: Range: 10 s to 240 s , Unit: s
		"""
		param = Conversions.decimal_value_to_str(size)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RXQuality:WINDowsize {param}')

	def clone(self) -> 'RxQuality':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RxQuality(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
