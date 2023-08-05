from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Incoming:
	"""Incoming commands group definition. 3 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("incoming", core, parent)

	@property
	def file(self):
		"""file commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_file'):
			from .Incoming_.File import File
			self._file = File(self._core, self._base)
		return self._file

	def get_cs_sms(self) -> bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SMS:INComing:CSSMs \n
		Snippet: value: bool = driver.configure.sms.incoming.get_cs_sms() \n
		Enable or disable that the R&S CMW concatenates received message files to one file. The received files have to arrive in
		a specified interval and need the same header information about encoding, teleservice id and sent MS number. Otherwise
		each received SMS message is saved separately. \n
			:return: concatenate_sms: OFF | ON OFF: Disable concatenation ON: Enable concatenation of multiple messages
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:SMS:INComing:CSSMs?')
		return Conversions.str_to_bool(response)

	def set_cs_sms(self, concatenate_sms: bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SMS:INComing:CSSMs \n
		Snippet: driver.configure.sms.incoming.set_cs_sms(concatenate_sms = False) \n
		Enable or disable that the R&S CMW concatenates received message files to one file. The received files have to arrive in
		a specified interval and need the same header information about encoding, teleservice id and sent MS number. Otherwise
		each received SMS message is saved separately. \n
			:param concatenate_sms: OFF | ON OFF: Disable concatenation ON: Enable concatenation of multiple messages
		"""
		param = Conversions.bool_to_str(concatenate_sms)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:SMS:INComing:CSSMs {param}')

	def clone(self) -> 'Incoming':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Incoming(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
