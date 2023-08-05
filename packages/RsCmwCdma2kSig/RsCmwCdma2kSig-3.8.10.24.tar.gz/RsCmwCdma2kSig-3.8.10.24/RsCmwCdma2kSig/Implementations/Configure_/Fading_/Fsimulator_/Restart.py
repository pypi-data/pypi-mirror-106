from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Restart:
	"""Restart commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("restart", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.FadingSimRestartMode:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:FADing:FSIMulator:RESTart:MODE \n
		Snippet: value: enums.FadingSimRestartMode = driver.configure.fading.fsimulator.restart.get_mode() \n
		Sets the restart mode of the fading simulator. \n
			:return: restart_mode: AUTO | MANual | TRIGger AUTO: fading automatically starts with the DL signal MANual: fading is started and restarted manually (see method RsCmwCdma2kSig.Configure.Fading.Fsimulator.Restart.set) TRIGger: fading start is triggered by external trigger
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:FADing:FSIMulator:RESTart:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.FadingSimRestartMode)

	def set_mode(self, restart_mode: enums.FadingSimRestartMode) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:FADing:FSIMulator:RESTart:MODE \n
		Snippet: driver.configure.fading.fsimulator.restart.set_mode(restart_mode = enums.FadingSimRestartMode.AUTO) \n
		Sets the restart mode of the fading simulator. \n
			:param restart_mode: AUTO | MANual | TRIGger AUTO: fading automatically starts with the DL signal MANual: fading is started and restarted manually (see method RsCmwCdma2kSig.Configure.Fading.Fsimulator.Restart.set) TRIGger: fading start is triggered by external trigger
		"""
		param = Conversions.enum_scalar_to_str(restart_mode, enums.FadingSimRestartMode)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:FADing:FSIMulator:RESTart:MODE {param}')

	def set(self) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:FADing:FSIMulator:RESTart \n
		Snippet: driver.configure.fading.fsimulator.restart.set() \n
		Restarts the fading process in MANual mode (see method RsCmwCdma2kSig.Configure.Fading.Fsimulator.Restart.mode) . \n
		"""
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:FADing:FSIMulator:RESTart')

	def set_with_opc(self) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:FADing:FSIMulator:RESTart \n
		Snippet: driver.configure.fading.fsimulator.restart.set_with_opc() \n
		Restarts the fading process in MANual mode (see method RsCmwCdma2kSig.Configure.Fading.Fsimulator.Restart.mode) . \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwCdma2kSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'CONFigure:CDMA:SIGNaling<Instance>:FADing:FSIMulator:RESTart')
