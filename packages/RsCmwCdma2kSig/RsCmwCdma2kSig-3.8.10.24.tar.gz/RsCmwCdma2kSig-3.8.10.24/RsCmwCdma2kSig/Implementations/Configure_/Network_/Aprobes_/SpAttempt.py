from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpAttempt:
	"""SpAttempt commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("spAttempt", core, parent)

	def get_rsp(self) -> int:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:APRobes:SPATtempt:RSP \n
		Snippet: value: int = driver.configure.network.aprobes.spAttempt.get_rsp() \n
		Maximum number of access probe sequences for an access channel or enhanced access channel response(MAX_RSP_SEQ) . \n
			:return: sequ_per_attempt: Range: 1 to 15
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:APRobes:SPATtempt:RSP?')
		return Conversions.str_to_int(response)

	def set_rsp(self, sequ_per_attempt: int) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:APRobes:SPATtempt:RSP \n
		Snippet: driver.configure.network.aprobes.spAttempt.set_rsp(sequ_per_attempt = 1) \n
		Maximum number of access probe sequences for an access channel or enhanced access channel response(MAX_RSP_SEQ) . \n
			:param sequ_per_attempt: Range: 1 to 15
		"""
		param = Conversions.decimal_value_to_str(sequ_per_attempt)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:APRobes:SPATtempt:RSP {param}')

	def get_req(self) -> int:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:APRobes:SPATtempt:REQ \n
		Snippet: value: int = driver.configure.network.aprobes.spAttempt.get_req() \n
		Maximum number of access probe sequences for an access channel or enhanced access channel request (MAX_REQ_SEQ) . \n
			:return: seq_attempt_req: Range: 1 to 15
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:NETWork:APRobes:SPATtempt:REQ?')
		return Conversions.str_to_int(response)

	def set_req(self, seq_attempt_req: int) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:NETWork:APRobes:SPATtempt:REQ \n
		Snippet: driver.configure.network.aprobes.spAttempt.set_req(seq_attempt_req = 1) \n
		Maximum number of access probe sequences for an access channel or enhanced access channel request (MAX_REQ_SEQ) . \n
			:param seq_attempt_req: Range: 1 to 15
		"""
		param = Conversions.decimal_value_to_str(seq_attempt_req)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:NETWork:APRobes:SPATtempt:REQ {param}')
