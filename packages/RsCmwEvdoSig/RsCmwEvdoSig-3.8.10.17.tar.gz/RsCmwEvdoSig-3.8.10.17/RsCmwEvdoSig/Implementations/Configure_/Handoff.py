from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Handoff:
	"""Handoff commands group definition. 7 total commands, 2 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("handoff", core, parent)

	@property
	def carrier(self):
		"""carrier commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_carrier'):
			from .Handoff_.Carrier import Carrier
			self._carrier = Carrier(self._core, self._base)
		return self._carrier

	@property
	def network(self):
		"""network commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_network'):
			from .Handoff_.Network import Network
			self._network = Network(self._core, self._base)
		return self._network

	# noinspection PyTypeChecker
	def get_bclass(self) -> enums.BandClass:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:HANDoff:BCLass \n
		Snippet: value: enums.BandClass = driver.configure.handoff.get_bclass() \n
		Selects a handoff destination band class/network; see 'Band Classes'. \n
			:return: band_class: USC | KCEL | NAPC | TACS | JTAC | KPCS | N45T | IM2K | NA7C | B18M | NA9C | NA8S | PA4M | PA8M | IEXT | USPC | AWS | U25B | U25F | PS7C | LO7C | LBANd | SBANd USC: BC 0, US-Cellular KCEL: BC 0, Korean Cellular NAPC: BC 1, North American PCS TACS: BC 2, TACS Band JTAC: BC 3, JTACS Band KPCS: BC 4, Korean PCS N45T: BC 5, NMT-450 IM2K: BC 6, IMT-2000 NA7C: BC 7, Upper 700 MHz B18M: BC 8, 1800 MHz Band NA9C: BC 9, North American 900 MHz NA8S: BC 10, Secondary 800 MHz PA4M: BC 11, European 400 MHz PAMR PA8M: BC 12, 800 MHz PAMR IEXT: BC 13, IMT-2000 2.5 GHz Extension USPC: BC 14, US PCS 1900 MHz AWS: BC 15, AWS Band U25B: BC 16, US 2.5 GHz Band PS7C: BC 18, Public Safety Band 700 MHz LO7C: BC 19, Lower 700 MHz LBAN: BC 20, L-Band SBAN: BC 21, S-Band
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:HANDoff:BCLass?')
		return Conversions.str_to_scalar_enum(response, enums.BandClass)

	def set_bclass(self, band_class: enums.BandClass) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:HANDoff:BCLass \n
		Snippet: driver.configure.handoff.set_bclass(band_class = enums.BandClass.AWS) \n
		Selects a handoff destination band class/network; see 'Band Classes'. \n
			:param band_class: USC | KCEL | NAPC | TACS | JTAC | KPCS | N45T | IM2K | NA7C | B18M | NA9C | NA8S | PA4M | PA8M | IEXT | USPC | AWS | U25B | U25F | PS7C | LO7C | LBANd | SBANd USC: BC 0, US-Cellular KCEL: BC 0, Korean Cellular NAPC: BC 1, North American PCS TACS: BC 2, TACS Band JTAC: BC 3, JTACS Band KPCS: BC 4, Korean PCS N45T: BC 5, NMT-450 IM2K: BC 6, IMT-2000 NA7C: BC 7, Upper 700 MHz B18M: BC 8, 1800 MHz Band NA9C: BC 9, North American 900 MHz NA8S: BC 10, Secondary 800 MHz PA4M: BC 11, European 400 MHz PAMR PA8M: BC 12, 800 MHz PAMR IEXT: BC 13, IMT-2000 2.5 GHz Extension USPC: BC 14, US PCS 1900 MHz AWS: BC 15, AWS Band U25B: BC 16, US 2.5 GHz Band PS7C: BC 18, Public Safety Band 700 MHz LO7C: BC 19, Lower 700 MHz LBAN: BC 20, L-Band SBAN: BC 21, S-Band
		"""
		param = Conversions.enum_scalar_to_str(band_class, enums.BandClass)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:HANDoff:BCLass {param}')

	def get_channel(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:HANDoff:CHANnel \n
		Snippet: value: int = driver.configure.handoff.get_channel() \n
		Sets/gets the main RF channel (the only one for network releases 0/A) in the handoff destination cell. \n
			:return: channel: The reset value and the range of possible channels depend on the selected band class; for an overview see 'Band Classes'. The values below are for band class BC0 (US Cellular) . Range: 1 to 799, 991 to 1323
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:HANDoff:CHANnel?')
		return Conversions.str_to_int(response)

	def set_channel(self, channel: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:HANDoff:CHANnel \n
		Snippet: driver.configure.handoff.set_channel(channel = 1) \n
		Sets/gets the main RF channel (the only one for network releases 0/A) in the handoff destination cell. \n
			:param channel: The reset value and the range of possible channels depend on the selected band class; for an overview see 'Band Classes'. The values below are for band class BC0 (US Cellular) . Range: 1 to 799, 991 to 1323
		"""
		param = Conversions.decimal_value_to_str(channel)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:HANDoff:CHANnel {param}')

	def clone(self) -> 'Handoff':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Handoff(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
