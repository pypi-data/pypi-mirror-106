from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Result:
	"""Result commands group definition. 5 total commands, 0 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("result", core, parent)

	def get_ferf_ch(self) -> bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RXQuality:RESult:FERFch \n
		Snippet: value: bool = driver.configure.rxQuality.result.get_ferf_ch() \n
		Enables or disables the evaluation and display of 'FER FCH', 'FER SCH0', 'RLP', 'PSTRength' or 'SPEech' results. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RXQuality:RESult:FERFch?')
		return Conversions.str_to_bool(response)

	def set_ferf_ch(self, enable: bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RXQuality:RESult:FERFch \n
		Snippet: driver.configure.rxQuality.result.set_ferf_ch(enable = False) \n
		Enables or disables the evaluation and display of 'FER FCH', 'FER SCH0', 'RLP', 'PSTRength' or 'SPEech' results. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RXQuality:RESult:FERFch {param}')

	def get_fers_ch(self) -> bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RXQuality:RESult:FERSch \n
		Snippet: value: bool = driver.configure.rxQuality.result.get_fers_ch() \n
		Enables or disables the evaluation and display of 'FER FCH', 'FER SCH0', 'RLP', 'PSTRength' or 'SPEech' results. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RXQuality:RESult:FERSch?')
		return Conversions.str_to_bool(response)

	def set_fers_ch(self, enable: bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RXQuality:RESult:FERSch \n
		Snippet: driver.configure.rxQuality.result.set_fers_ch(enable = False) \n
		Enables or disables the evaluation and display of 'FER FCH', 'FER SCH0', 'RLP', 'PSTRength' or 'SPEech' results. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RXQuality:RESult:FERSch {param}')

	def get_rlp(self) -> bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RXQuality:RESult:RLP \n
		Snippet: value: bool = driver.configure.rxQuality.result.get_rlp() \n
		Enables or disables the evaluation and display of 'FER FCH', 'FER SCH0', 'RLP', 'PSTRength' or 'SPEech' results. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RXQuality:RESult:RLP?')
		return Conversions.str_to_bool(response)

	def set_rlp(self, enable: bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RXQuality:RESult:RLP \n
		Snippet: driver.configure.rxQuality.result.set_rlp(enable = False) \n
		Enables or disables the evaluation and display of 'FER FCH', 'FER SCH0', 'RLP', 'PSTRength' or 'SPEech' results. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RXQuality:RESult:RLP {param}')

	def get_speech(self) -> bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RXQuality:RESult:SPEech \n
		Snippet: value: bool = driver.configure.rxQuality.result.get_speech() \n
		Enables or disables the evaluation and display of 'FER FCH', 'FER SCH0', 'RLP', 'PSTRength' or 'SPEech' results. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RXQuality:RESult:SPEech?')
		return Conversions.str_to_bool(response)

	def set_speech(self, enable: bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RXQuality:RESult:SPEech \n
		Snippet: driver.configure.rxQuality.result.set_speech(enable = False) \n
		Enables or disables the evaluation and display of 'FER FCH', 'FER SCH0', 'RLP', 'PSTRength' or 'SPEech' results. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RXQuality:RESult:SPEech {param}')

	def get_pstrength(self) -> bool:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RXQuality:RESult:PSTRength \n
		Snippet: value: bool = driver.configure.rxQuality.result.get_pstrength() \n
		Enables or disables the evaluation and display of 'FER FCH', 'FER SCH0', 'RLP', 'PSTRength' or 'SPEech' results. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RXQuality:RESult:PSTRength?')
		return Conversions.str_to_bool(response)

	def set_pstrength(self, enable: bool) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RXQuality:RESult:PSTRength \n
		Snippet: driver.configure.rxQuality.result.set_pstrength(enable = False) \n
		Enables or disables the evaluation and display of 'FER FCH', 'FER SCH0', 'RLP', 'PSTRength' or 'SPEech' results. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RXQuality:RESult:PSTRength {param}')
