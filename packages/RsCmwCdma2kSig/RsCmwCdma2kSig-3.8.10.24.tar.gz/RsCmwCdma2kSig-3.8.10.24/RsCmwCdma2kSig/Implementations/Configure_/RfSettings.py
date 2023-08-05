from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfSettings:
	"""RfSettings commands group definition. 7 total commands, 0 Sub-groups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rfSettings", core, parent)

	# noinspection PyTypeChecker
	class EattenuationStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rf_Input_Ext_Att: float: Range: -50 dB to 90 dB, Unit: dB
			- Rf_Output_Ext_Att: float: Range: -50 dB to 90 dB, Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_float('Rf_Input_Ext_Att'),
			ArgStruct.scalar_float('Rf_Output_Ext_Att')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rf_Input_Ext_Att: float = None
			self.Rf_Output_Ext_Att: float = None

	def get_eattenuation(self) -> EattenuationStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFSettings:EATTenuation \n
		Snippet: value: EattenuationStruct = driver.configure.rfSettings.get_eattenuation() \n
		Defines the external attenuations (or gain, if the value is negative) , to be applied to the selected RF input and output
		connectors. \n
			:return: structure: for return value, see the help for EattenuationStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:RFSettings:EATTenuation?', self.__class__.EattenuationStruct())

	def set_eattenuation(self, value: EattenuationStruct) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFSettings:EATTenuation \n
		Snippet: driver.configure.rfSettings.set_eattenuation(value = EattenuationStruct()) \n
		Defines the external attenuations (or gain, if the value is negative) , to be applied to the selected RF input and output
		connectors. \n
			:param value: see the help for EattenuationStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:CDMA:SIGNaling<Instance>:RFSettings:EATTenuation', value)

	# noinspection PyTypeChecker
	def get_bclass(self) -> enums.BandClass:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFSettings:BCLass \n
		Snippet: value: enums.BandClass = driver.configure.rfSettings.get_bclass() \n
		Selects the band class (BC) . If the current center frequency is valid for this BC, the corresponding channel number is
		also calculated and set. See also: 'Band Classes' \n
			:return: band_class: USC | KCEL | NAPC | TACS | JTAC | KPCS | N45T | IM2K | NA7C | B18M | NA9C | NA8S | PA4M | PA8M | IEXT | USPC | AWS | U25B | PS7C | LO7C | LBANd | SBANd USC: BC 0, US-Cellular KCEL: BC 0, Korean Cellular NAPC: BC 1, North American PCS TACS: BC 2, TACS Band JTAC: BC 3, JTACS Band KPCS: BC 4, Korean PCS N45T: BC 5, NMT-450 IM2K: BC 6, IMT-2000 NA7C: BC 7, Upper 700 MHz B18M: BC 8, 1800 MHz Band NA9C: BC 9, North American 900 MHz NA8S: BC 10, Secondary 800 MHz PA4M: BC 11, European 400 MHz PAMR PA8M: BC 12, 800 MHz PAMR IEXT: BC 13, IMT-2000 2.5 GHz Extension USPC: BC 14, US PCS 1900 MHz AWS: BC 15, AWS Band U25B: BC 16, US 2.5 GHz Band PS7C: BC 18, Public Safety Band 700 MHz LO7C: BC 19, Lower 700 MHz LBAN: BC 20, L-Band SBAN: BC 21, S-Band
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RFSettings:BCLass?')
		return Conversions.str_to_scalar_enum(response, enums.BandClass)

	def set_bclass(self, band_class: enums.BandClass) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFSettings:BCLass \n
		Snippet: driver.configure.rfSettings.set_bclass(band_class = enums.BandClass.AWS) \n
		Selects the band class (BC) . If the current center frequency is valid for this BC, the corresponding channel number is
		also calculated and set. See also: 'Band Classes' \n
			:param band_class: USC | KCEL | NAPC | TACS | JTAC | KPCS | N45T | IM2K | NA7C | B18M | NA9C | NA8S | PA4M | PA8M | IEXT | USPC | AWS | U25B | PS7C | LO7C | LBANd | SBANd USC: BC 0, US-Cellular KCEL: BC 0, Korean Cellular NAPC: BC 1, North American PCS TACS: BC 2, TACS Band JTAC: BC 3, JTACS Band KPCS: BC 4, Korean PCS N45T: BC 5, NMT-450 IM2K: BC 6, IMT-2000 NA7C: BC 7, Upper 700 MHz B18M: BC 8, 1800 MHz Band NA9C: BC 9, North American 900 MHz NA8S: BC 10, Secondary 800 MHz PA4M: BC 11, European 400 MHz PAMR PA8M: BC 12, 800 MHz PAMR IEXT: BC 13, IMT-2000 2.5 GHz Extension USPC: BC 14, US PCS 1900 MHz AWS: BC 15, AWS Band U25B: BC 16, US 2.5 GHz Band PS7C: BC 18, Public Safety Band 700 MHz LO7C: BC 19, Lower 700 MHz LBAN: BC 20, L-Band SBAN: BC 21, S-Band
		"""
		param = Conversions.enum_scalar_to_str(band_class, enums.BandClass)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RFSettings:BCLass {param}')

	# noinspection PyTypeChecker
	class FrequencyStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Forward_Link_Freq: float: Range: 0 Hz to 6.1 GHz
			- Reverse_Link_Freq: float: Range: 0 Hz to 6.1 GHz"""
		__meta_args_list = [
			ArgStruct.scalar_float('Forward_Link_Freq'),
			ArgStruct.scalar_float('Reverse_Link_Freq')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Forward_Link_Freq: float = None
			self.Reverse_Link_Freq: float = None

	def get_frequency(self) -> FrequencyStruct:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFSettings:FREQuency \n
		Snippet: value: FrequencyStruct = driver.configure.rfSettings.get_frequency() \n
		Queries the forward and reverse link frequency, depending on the selected band class and channel. \n
			:return: structure: for return value, see the help for FrequencyStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:CDMA:SIGNaling<Instance>:RFSettings:FREQuency?', self.__class__.FrequencyStruct())

	def get_fl_frequency(self) -> float:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFSettings:FLFRequency \n
		Snippet: value: float = driver.configure.rfSettings.get_fl_frequency() \n
		Queries the forward signal frequency of the RF generator. \n
			:return: frequency: Range: 0 Hz to 6.1 GHz, Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RFSettings:FLFRequency?')
		return Conversions.str_to_float(response)

	def get_rl_frequency(self) -> float:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFSettings:RLFRequency \n
		Snippet: value: float = driver.configure.rfSettings.get_rl_frequency() \n
		Queries the reverse frequency. \n
			:return: frequency: Range: 0 Hz to 6.1 GHz, Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RFSettings:RLFRequency?')
		return Conversions.str_to_float(response)

	def get_foffset(self) -> float:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFSettings:FOFFset \n
		Snippet: value: float = driver.configure.rfSettings.get_foffset() \n
		Selects a positive or negative offset frequency to be added to the center frequency of the forward and reverse link. \n
			:return: freq_offset: Range: -50 kHz to 50 kHz, Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RFSettings:FOFFset?')
		return Conversions.str_to_float(response)

	def set_foffset(self, freq_offset: float) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFSettings:FOFFset \n
		Snippet: driver.configure.rfSettings.set_foffset(freq_offset = 1.0) \n
		Selects a positive or negative offset frequency to be added to the center frequency of the forward and reverse link. \n
			:param freq_offset: Range: -50 kHz to 50 kHz, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(freq_offset)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RFSettings:FOFFset {param}')

	def get_channel(self) -> int:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFSettings:CHANnel \n
		Snippet: value: int = driver.configure.rfSettings.get_channel() \n
		Sets the RF carrier frequency as CDMA2000 channel number. If the channel number is valid for the current frequency band,
		the corresponding center frequency is calculated and set. If the channel number is queried while an out-of-band frequency
		is set, the response is 'INV'. See also: 'Band Classes' \n
			:return: channel: Range: Depends on selected frequency band.
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:RFSettings:CHANnel?')
		return Conversions.str_to_int(response)

	def set_channel(self, channel: int) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:RFSettings:CHANnel \n
		Snippet: driver.configure.rfSettings.set_channel(channel = 1) \n
		Sets the RF carrier frequency as CDMA2000 channel number. If the channel number is valid for the current frequency band,
		the corresponding center frequency is calculated and set. If the channel number is queried while an out-of-band frequency
		is set, the response is 'INV'. See also: 'Band Classes' \n
			:param channel: Range: Depends on selected frequency band.
		"""
		param = Conversions.decimal_value_to_str(channel)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:RFSettings:CHANnel {param}')
