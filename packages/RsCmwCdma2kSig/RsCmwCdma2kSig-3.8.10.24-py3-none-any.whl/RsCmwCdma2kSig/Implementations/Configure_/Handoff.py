from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Handoff:
	"""Handoff commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("handoff", core, parent)

	# noinspection PyTypeChecker
	def get_bclass(self) -> enums.BandClass:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:HANDoff:BCLass \n
		Snippet: value: enums.BandClass = driver.configure.handoff.get_bclass() \n
		Selects a handoff destination band class. See also: 'Band Classes' \n
			:return: band_class: USC | KCEL | NAPC | TACS | JTAC | KPCS | N45T | IM2K | NA7C | B18M | NA9C | NA8S | PA4M | PA8M | IEXT | USPC | AWS | U25B | PS7C | LO7C | LBANd | SBANd USC: BC 0, US-Cellular KCEL: BC 0, Korean Cellular NAPC: BC 1, North American PCS TACS: BC 2, TACS Band JTAC: BC 3, JTACS Band KPCS: BC 4, Korean PCS N45T: BC 5, NMT-450 IM2K: BC 6, IMT-2000 NA7C: BC 7, Upper 700 MHz B18M: BC 8, 1800 MHz Band NA9C: BC 9, North American 900 MHz NA8S: BC 10, Secondary 800 MHz PA4M: BC 11, European 400 MHz PAMR PA8M: BC 12, 800 MHz PAMR IEXT: BC 13, IMT-2000 2.5 GHz Extension USPC: BC 14, US PCS 1900 MHz AWS: BC 15, AWS Band U25B: BC 16, US 2.5 GHz Band PS7C: BC 18, Public Safety Band 700 MHz LO7C: BC 19, Lower 700 MHz LBAN: BC 20, L-Band SBAN: BC 21, S-Band
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:HANDoff:BCLass?')
		return Conversions.str_to_scalar_enum(response, enums.BandClass)

	def set_bclass(self, band_class: enums.BandClass) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:HANDoff:BCLass \n
		Snippet: driver.configure.handoff.set_bclass(band_class = enums.BandClass.AWS) \n
		Selects a handoff destination band class. See also: 'Band Classes' \n
			:param band_class: USC | KCEL | NAPC | TACS | JTAC | KPCS | N45T | IM2K | NA7C | B18M | NA9C | NA8S | PA4M | PA8M | IEXT | USPC | AWS | U25B | PS7C | LO7C | LBANd | SBANd USC: BC 0, US-Cellular KCEL: BC 0, Korean Cellular NAPC: BC 1, North American PCS TACS: BC 2, TACS Band JTAC: BC 3, JTACS Band KPCS: BC 4, Korean PCS N45T: BC 5, NMT-450 IM2K: BC 6, IMT-2000 NA7C: BC 7, Upper 700 MHz B18M: BC 8, 1800 MHz Band NA9C: BC 9, North American 900 MHz NA8S: BC 10, Secondary 800 MHz PA4M: BC 11, European 400 MHz PAMR PA8M: BC 12, 800 MHz PAMR IEXT: BC 13, IMT-2000 2.5 GHz Extension USPC: BC 14, US PCS 1900 MHz AWS: BC 15, AWS Band U25B: BC 16, US 2.5 GHz Band PS7C: BC 18, Public Safety Band 700 MHz LO7C: BC 19, Lower 700 MHz LBAN: BC 20, L-Band SBAN: BC 21, S-Band
		"""
		param = Conversions.enum_scalar_to_str(band_class, enums.BandClass)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:HANDoff:BCLass {param}')

	def get_channel(self) -> int:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:HANDoff:CHANnel \n
		Snippet: value: int = driver.configure.handoff.get_channel() \n
		Selects the RF channel in the destination band class/network. The range of values depends on the selected band class
		(method RsCmwCdma2kSig.Configure.Handoff.bclass) . For an overview of available band classes and the corresponding
		channels, see 'Band Classes'. \n
			:return: channel: Range: Depends on selected frequency band.
		"""
		response = self._core.io.query_str('CONFigure:CDMA:SIGNaling<Instance>:HANDoff:CHANnel?')
		return Conversions.str_to_int(response)

	def set_channel(self, channel: int) -> None:
		"""SCPI: CONFigure:CDMA:SIGNaling<Instance>:HANDoff:CHANnel \n
		Snippet: driver.configure.handoff.set_channel(channel = 1) \n
		Selects the RF channel in the destination band class/network. The range of values depends on the selected band class
		(method RsCmwCdma2kSig.Configure.Handoff.bclass) . For an overview of available band classes and the corresponding
		channels, see 'Band Classes'. \n
			:param channel: Range: Depends on selected frequency band.
		"""
		param = Conversions.decimal_value_to_str(channel)
		self._core.io.write(f'CONFigure:CDMA:SIGNaling<Instance>:HANDoff:CHANnel {param}')
