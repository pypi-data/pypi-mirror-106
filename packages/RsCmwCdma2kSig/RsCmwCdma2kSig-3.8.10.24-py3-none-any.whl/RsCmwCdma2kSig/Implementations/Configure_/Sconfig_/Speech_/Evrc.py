from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Evrc:
	"""Evrc commands group definition. 4 total commands, 0 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("evrc", core, parent)

	def get_eopoint(self) -> int:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SCONfig:SPEech:EVRC:EOPoint \n
		Snippet: value: int = driver.configure.sconfig.speech.evrc.get_eopoint() \n
		Flag signaling average encoding rate for the selected service option. \n
			:return: encoder_op_point: See 'Speech Services' Range: 0 to 7
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:SCONfig:SPEech:EVRC:EOPoint?')
		return Conversions.str_to_int(response)

	def set_eopoint(self, encoder_op_point: int) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SCONfig:SPEech:EVRC:EOPoint \n
		Snippet: driver.configure.sconfig.speech.evrc.set_eopoint(encoder_op_point = 1) \n
		Flag signaling average encoding rate for the selected service option. \n
			:param encoder_op_point: See 'Speech Services' Range: 0 to 7
		"""
		param = Conversions.decimal_value_to_str(encoder_op_point)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:SCONfig:SPEech:EVRC:EOPoint {param}')

	# noinspection PyTypeChecker
	def get_ae_rate(self) -> enums.AvgEncodingRate:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SCONfig:SPEech:EVRC:AERate \n
		Snippet: value: enums.AvgEncodingRate = driver.configure.sconfig.speech.evrc.get_ae_rate() \n
		Defines the average encoding rate for active speech (channel encoding rates) . This setting is dependent from the
		selected service option, see also 'Speech Services' \n
			:return: aver_encod_rate: R93K | R85K | R75K | R70K | R66K | R62K | R58K | R48K R93K: 9.3 kbit/s R85K: 8.5 kbit/s R75K: 7.5 kbit/s R70K: 7.0 kbit/s R66K: 6.6 kbit/s R62K: 6.2 kbit/s R58K: 5.8 kbit/s R48K: 4.8 kbit/s
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:SCONfig:SPEech:EVRC:AERate?')
		return Conversions.str_to_scalar_enum(response, enums.AvgEncodingRate)

	def set_ae_rate(self, aver_encod_rate: enums.AvgEncodingRate) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SCONfig:SPEech:EVRC:AERate \n
		Snippet: driver.configure.sconfig.speech.evrc.set_ae_rate(aver_encod_rate = enums.AvgEncodingRate.R48K) \n
		Defines the average encoding rate for active speech (channel encoding rates) . This setting is dependent from the
		selected service option, see also 'Speech Services' \n
			:param aver_encod_rate: R93K | R85K | R75K | R70K | R66K | R62K | R58K | R48K R93K: 9.3 kbit/s R85K: 8.5 kbit/s R75K: 7.5 kbit/s R70K: 7.0 kbit/s R66K: 6.6 kbit/s R62K: 6.2 kbit/s R58K: 5.8 kbit/s R48K: 4.8 kbit/s
		"""
		param = Conversions.enum_scalar_to_str(aver_encod_rate, enums.AvgEncodingRate)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:SCONfig:SPEech:EVRC:AERate {param}')

	# noinspection PyTypeChecker
	def get_rrestriction(self) -> enums.RateRestriction:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SCONfig:SPEech:EVRC:RREStriction \n
		Snippet: value: enums.RateRestriction = driver.configure.sconfig.speech.evrc.get_rrestriction() \n
		Configures rate restrictions in the reverse link. \n
			:return: rate_restrict: AUTO | FULL | HALF | QUARter | EIGHth AUTO: no restriction FULL: frames at the full rate set HALF: frames at the 1/2 rate set QUARter: frames at the 1/4 rate set EIGHth: frames at the 1/8 rate set
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:SCONfig:SPEech:EVRC:RREStriction?')
		return Conversions.str_to_scalar_enum(response, enums.RateRestriction)

	def set_rrestriction(self, rate_restrict: enums.RateRestriction) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SCONfig:SPEech:EVRC:RREStriction \n
		Snippet: driver.configure.sconfig.speech.evrc.set_rrestriction(rate_restrict = enums.RateRestriction.AUTO) \n
		Configures rate restrictions in the reverse link. \n
			:param rate_restrict: AUTO | FULL | HALF | QUARter | EIGHth AUTO: no restriction FULL: frames at the full rate set HALF: frames at the 1/2 rate set QUARter: frames at the 1/4 rate set EIGHth: frames at the 1/8 rate set
		"""
		param = Conversions.enum_scalar_to_str(rate_restrict, enums.RateRestriction)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:SCONfig:SPEech:EVRC:RREStriction {param}')

	def set_ivo_coder(self, init_vo_coder: bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SCONfig:SPEech:EVRC:IVOCoder \n
		Snippet: driver.configure.sconfig.speech.evrc.set_ivo_coder(init_vo_coder = False) \n
		Triggers the enhanced variable rate codec settings. \n
			:param init_vo_coder: OFF | ON
		"""
		param = Conversions.bool_to_str(init_vo_coder)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:SCONfig:SPEech:EVRC:IVOCoder {param}')
