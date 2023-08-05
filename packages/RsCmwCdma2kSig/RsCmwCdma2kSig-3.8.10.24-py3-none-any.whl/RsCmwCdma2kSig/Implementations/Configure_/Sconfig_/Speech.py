from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Speech:
	"""Speech commands group definition. 6 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("speech", core, parent)

	@property
	def evrc(self):
		"""evrc commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_evrc'):
			from .Speech_.Evrc import Evrc
			self._evrc = Evrc(self._core, self._base)
		return self._evrc

	# noinspection PyTypeChecker
	def get_vcoder(self) -> enums.VoiceCoder:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SCONfig:SPEech:VCODer \n
		Snippet: value: enums.VoiceCoder = driver.configure.sconfig.speech.get_vcoder() \n
		Configures the CS connection setup for the selected service option. \n
			:return: voice_coder: ECHO | CODE ECHO: the setup for the loopback with delay. The R&S CMW sends back all data received on the FCH after the specified 'Echo Delay' (method RsCmwCdma2kSig.Configure.Sconfig.Speech.edelay) without invoking the speech codec. CODE: the setup for the bidirectional audio connection from the speech encoder/decoder to the DUT involving the audio measurements application with the codec board.
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:SCONfig:SPEech:VCODer?')
		return Conversions.str_to_scalar_enum(response, enums.VoiceCoder)

	def set_vcoder(self, voice_coder: enums.VoiceCoder) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SCONfig:SPEech:VCODer \n
		Snippet: driver.configure.sconfig.speech.set_vcoder(voice_coder = enums.VoiceCoder.CODE) \n
		Configures the CS connection setup for the selected service option. \n
			:param voice_coder: ECHO | CODE ECHO: the setup for the loopback with delay. The R&S CMW sends back all data received on the FCH after the specified 'Echo Delay' (method RsCmwCdma2kSig.Configure.Sconfig.Speech.edelay) without invoking the speech codec. CODE: the setup for the bidirectional audio connection from the speech encoder/decoder to the DUT involving the audio measurements application with the codec board.
		"""
		param = Conversions.enum_scalar_to_str(voice_coder, enums.VoiceCoder)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:SCONfig:SPEech:VCODer {param}')

	def get_edelay(self) -> float:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SCONfig:SPEech:EDELay \n
		Snippet: value: float = driver.configure.sconfig.speech.get_edelay() \n
		Defines the time that the R&S CMW waits before it loops back the received data if the 'Voice Coder' (method
		RsCmwCdma2kSig.Configure.Sconfig.Speech.vcoder) is set to Echo mode. \n
			:return: echo_delay: Range: 0.02 to 10, Unit: seconds
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:SCONfig:SPEech:EDELay?')
		return Conversions.str_to_float(response)

	def set_edelay(self, echo_delay: float) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SCONfig:SPEech:EDELay \n
		Snippet: driver.configure.sconfig.speech.set_edelay(echo_delay = 1.0) \n
		Defines the time that the R&S CMW waits before it loops back the received data if the 'Voice Coder' (method
		RsCmwCdma2kSig.Configure.Sconfig.Speech.vcoder) is set to Echo mode. \n
			:param echo_delay: Range: 0.02 to 10, Unit: seconds
		"""
		param = Conversions.decimal_value_to_str(echo_delay)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:SCONfig:SPEech:EDELay {param}')

	def clone(self) -> 'Speech':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Speech(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
