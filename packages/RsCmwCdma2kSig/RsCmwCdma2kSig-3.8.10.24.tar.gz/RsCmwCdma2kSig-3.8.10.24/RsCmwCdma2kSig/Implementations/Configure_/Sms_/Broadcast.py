from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Broadcast:
	"""Broadcast commands group definition. 6 total commands, 1 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("broadcast", core, parent)

	@property
	def service(self):
		"""service commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_service'):
			from .Broadcast_.Service import Service
			self._service = Service(self._core, self._base)
		return self._service

	def get_cmas(self) -> bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SMS:BROadcast:CMAS \n
		Snippet: value: bool = driver.configure.sms.broadcast.get_cmas() \n
		No command help available \n
			:return: is_cmas: No help available
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:SMS:BROadcast:CMAS?')
		return Conversions.str_to_bool(response)

	def set_cmas(self, is_cmas: bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SMS:BROadcast:CMAS \n
		Snippet: driver.configure.sms.broadcast.set_cmas(is_cmas = False) \n
		No command help available \n
			:param is_cmas: No help available
		"""
		param = Conversions.bool_to_str(is_cmas)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:SMS:BROadcast:CMAS {param}')

	def get_wea(self) -> bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<instance>:SMS:BROadcast:WEA \n
		Snippet: value: bool = driver.configure.sms.broadcast.get_wea() \n
		Specifies whether the message is used for the measurement of the wireless emergency alerts (WEA) solution, formerly known
		as the commercial mobile alert system (CMAS) . \n
			:return: wea: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:SMS:BROadcast:WEA?')
		return Conversions.str_to_bool(response)

	def set_wea(self, wea: bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<instance>:SMS:BROadcast:WEA \n
		Snippet: driver.configure.sms.broadcast.set_wea(wea = False) \n
		Specifies whether the message is used for the measurement of the wireless emergency alerts (WEA) solution, formerly known
		as the commercial mobile alert system (CMAS) . \n
			:param wea: OFF | ON
		"""
		param = Conversions.bool_to_str(wea)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:SMS:BROadcast:WEA {param}')

	def get_internal(self) -> str:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SMS:BROadcast:INTernal \n
		Snippet: value: str = driver.configure.sms.broadcast.get_internal() \n
		String parameter to specify the message text. \n
			:return: internal_message: No help available
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:SMS:BROadcast:INTernal?')
		return trim_str_response(response)

	def set_internal(self, internal_message: str) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SMS:BROadcast:INTernal \n
		Snippet: driver.configure.sms.broadcast.set_internal(internal_message = '1') \n
		String parameter to specify the message text. \n
			:param internal_message: No help available
		"""
		param = Conversions.value_to_quoted_str(internal_message)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:SMS:BROadcast:INTernal {param}')

	# noinspection PyTypeChecker
	def get_language(self) -> enums.Language:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SMS:BROadcast:LANGuage \n
		Snippet: value: enums.Language = driver.configure.sms.broadcast.get_language() \n
		Selects the language of the broadcast SMS. \n
			:return: language: UNDefined | ENGLish | FRENch | SPANish | JAPanese | KORean | CHINese | HEBRew | PORTuguese | HINDi | TURKish | HUNGarian | POLish | CZECh | ARABic | RUSSian | ICELandic | GERMan | ITALian | DUTCh | SWEDish | DANish | FINNish | NORWegian | GREek | BENGali | GUJarati | KANNada | MALayalam | ORIYa | PUNJabi | TAMil | TELugu | URDU | BAHasa | THAI | TAGalog | SWAHili | AFRikaans | HAUSa | VIETnamese
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:SMS:BROadcast:LANGuage?')
		return Conversions.str_to_scalar_enum(response, enums.Language)

	def set_language(self, language: enums.Language) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SMS:BROadcast:LANGuage \n
		Snippet: driver.configure.sms.broadcast.set_language(language = enums.Language.AFRikaans) \n
		Selects the language of the broadcast SMS. \n
			:param language: UNDefined | ENGLish | FRENch | SPANish | JAPanese | KORean | CHINese | HEBRew | PORTuguese | HINDi | TURKish | HUNGarian | POLish | CZECh | ARABic | RUSSian | ICELandic | GERMan | ITALian | DUTCh | SWEDish | DANish | FINNish | NORWegian | GREek | BENGali | GUJarati | KANNada | MALayalam | ORIYa | PUNJabi | TAMil | TELugu | URDU | BAHasa | THAI | TAGalog | SWAHili | AFRikaans | HAUSa | VIETnamese
		"""
		param = Conversions.enum_scalar_to_str(language, enums.Language)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:SMS:BROadcast:LANGuage {param}')

	# noinspection PyTypeChecker
	def get_priority(self) -> enums.PriorityB:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SMS:BROadcast:PRIority \n
		Snippet: value: enums.PriorityB = driver.configure.sms.broadcast.get_priority() \n
		Sets the priority of the broadcast SMS. \n
			:return: priority: NORMal | INTeractive | URGent | EMERgency
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:SMS:BROadcast:PRIority?')
		return Conversions.str_to_scalar_enum(response, enums.PriorityB)

	def set_priority(self, priority: enums.PriorityB) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:SMS:BROadcast:PRIority \n
		Snippet: driver.configure.sms.broadcast.set_priority(priority = enums.PriorityB.EMERgency) \n
		Sets the priority of the broadcast SMS. \n
			:param priority: NORMal | INTeractive | URGent | EMERgency
		"""
		param = Conversions.enum_scalar_to_str(priority, enums.PriorityB)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:SMS:BROadcast:PRIority {param}')

	def clone(self) -> 'Broadcast':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Broadcast(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
