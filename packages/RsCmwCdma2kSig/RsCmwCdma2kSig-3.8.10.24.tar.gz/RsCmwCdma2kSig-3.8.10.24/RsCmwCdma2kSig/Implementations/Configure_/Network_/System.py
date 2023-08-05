from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class System:
	"""System commands group definition. 7 total commands, 3 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("system", core, parent)

	@property
	def awin(self):
		"""awin commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_awin'):
			from .System_.Awin import Awin
			self._awin = Awin(self._core, self._base)
		return self._awin

	@property
	def nwin(self):
		"""nwin commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nwin'):
			from .System_.Nwin import Nwin
			self._nwin = Nwin(self._core, self._base)
		return self._nwin

	@property
	def rwin(self):
		"""rwin commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rwin'):
			from .System_.Rwin import Rwin
			self._rwin = Rwin(self._core, self._base)
		return self._rwin

	def get_sid(self) -> int:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:SYSTem:SID \n
		Snippet: value: int = driver.configure.network.system.get_sid() \n
		Defines the 15-bit system ID that the R&S CMW broadcasts on its forward signal. \n
			:return: system_id_number: Range: 0 to 32767 (15 bits)
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:SYSTem:SID?')
		return Conversions.str_to_int(response)

	def set_sid(self, system_id_number: int) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:SYSTem:SID \n
		Snippet: driver.configure.network.system.set_sid(system_id_number = 1) \n
		Defines the 15-bit system ID that the R&S CMW broadcasts on its forward signal. \n
			:param system_id_number: Range: 0 to 32767 (15 bits)
		"""
		param = Conversions.decimal_value_to_str(system_id_number)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:SYSTem:SID {param}')

	def get_prevision(self) -> int:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:SYSTem:PREVision \n
		Snippet: value: int = driver.configure.network.system.get_prevision() \n
		Sets the preferred revision of the protocol for the R&S CMW to use. \n
			:return: prevision: Range: 3 to 7
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:SYSTem:PREVision?')
		return Conversions.str_to_int(response)

	def set_prevision(self, prevision: int) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:SYSTem:PREVision \n
		Snippet: driver.configure.network.system.set_prevision(prevision = 1) \n
		Sets the preferred revision of the protocol for the R&S CMW to use. \n
			:param prevision: Range: 3 to 7
		"""
		param = Conversions.decimal_value_to_str(prevision)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:SYSTem:PREVision {param}')

	def get_mp_revision(self) -> int:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:SYSTem:MPRevision \n
		Snippet: value: int = driver.configure.network.system.get_mp_revision() \n
		Set the minimum protocol revision required from the mobile station. \n
			:return: mp_revision: Range: 1 to 7
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:SYSTem:MPRevision?')
		return Conversions.str_to_int(response)

	def set_mp_revision(self, mp_revision: int) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:SYSTem:MPRevision \n
		Snippet: driver.configure.network.system.set_mp_revision(mp_revision = 1) \n
		Set the minimum protocol revision required from the mobile station. \n
			:param mp_revision: Range: 1 to 7
		"""
		param = Conversions.decimal_value_to_str(mp_revision)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:SYSTem:MPRevision {param}')

	def get_bsid(self) -> int:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:SYSTem:BSID \n
		Snippet: value: int = driver.configure.network.system.get_bsid() \n
		Specifies the ID of base station. \n
			:return: bsid_number: Range: 0 to 65535 (16 bits)
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:SYSTem:BSID?')
		return Conversions.str_to_int(response)

	def set_bsid(self, bsid_number: int) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:SYSTem:BSID \n
		Snippet: driver.configure.network.system.set_bsid(bsid_number = 1) \n
		Specifies the ID of base station. \n
			:param bsid_number: Range: 0 to 65535 (16 bits)
		"""
		param = Conversions.decimal_value_to_str(bsid_number)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:SYSTem:BSID {param}')

	def clone(self) -> 'System':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = System(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
