from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Soption:
	"""Soption commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("soption", core, parent)

	def set_action(self, cs_action: enums.CsAction) -> None:
		"""SCPI: CALL:CDMA:SIGNaling<Instance>:SOPTion<So>:ACTion \n
		Snippet: driver.call.soption.set_action(cs_action = enums.CsAction.BROadcast) \n
		Initiates a transition between different connection states; to be queried via method RsCmwCdma2kSig.Soption.State.fetch.
		For details, refer to 'Connection States'. \n
			:param cs_action: CONNect | DISConnect | UNRegister | SMS | HANDoff Transition between connection states.
		"""
		param = Conversions.enum_scalar_to_str(cs_action, enums.CsAction)
		self._core.io.write_with_opc(f'CALL:CDMA:SIGNaling<Instance>:SOPTion1:ACTion {param}')
