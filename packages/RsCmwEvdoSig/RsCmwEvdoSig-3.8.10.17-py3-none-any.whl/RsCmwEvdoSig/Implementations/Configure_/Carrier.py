from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Carrier:
	"""Carrier commands group definition. 6 total commands, 1 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("carrier", core, parent)

	@property
	def level(self):
		"""level commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_level'):
			from .Carrier_.Level import Level
			self._level = Level(self._core, self._base)
		return self._level

	def get_setting(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:CARRier:SETTing \n
		Snippet: value: int = driver.configure.carrier.get_setting() \n
		Sets/gets the carrier to which subsequent carrier-related commands apply. \n
			:return: set_carrier: Range: 0 to 2
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:CARRier:SETTing?')
		return Conversions.str_to_int(response)

	def set_setting(self, set_carrier: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:CARRier:SETTing \n
		Snippet: driver.configure.carrier.set_setting(set_carrier = 1) \n
		Sets/gets the carrier to which subsequent carrier-related commands apply. \n
			:param set_carrier: Range: 0 to 2
		"""
		param = Conversions.decimal_value_to_str(set_carrier)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:CARRier:SETTing {param}')

	def get_channel(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:CARRier:CHANnel \n
		Snippet: value: int = driver.configure.carrier.get_channel() \n
		Sets/gets the channel for a carrier in the sector implemented by the signaling application. Preselect the related carrier
		using the method RsCmwEvdoSig.Configure.Carrier.setting command. \n
			:return: carrier_channel: The range of possible channels depends on the selected band class. The values below are for band class BC0 (US-Cellular) . For an overview, see 'Band Classes'. Range: 1 to 799, 991 to 1323
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:CARRier:CHANnel?')
		return Conversions.str_to_int(response)

	def set_channel(self, carrier_channel: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:CARRier:CHANnel \n
		Snippet: driver.configure.carrier.set_channel(carrier_channel = 1) \n
		Sets/gets the channel for a carrier in the sector implemented by the signaling application. Preselect the related carrier
		using the method RsCmwEvdoSig.Configure.Carrier.setting command. \n
			:param carrier_channel: The range of possible channels depends on the selected band class. The values below are for band class BC0 (US-Cellular) . For an overview, see 'Band Classes'. Range: 1 to 799, 991 to 1323
		"""
		param = Conversions.decimal_value_to_str(carrier_channel)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:CARRier:CHANnel {param}')

	def get_fl_frequency(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:CARRier:FLFRequency \n
		Snippet: value: int = driver.configure.carrier.get_fl_frequency() \n
		Gets the forward link frequency for a carrier in the cell implemented by the signaling application. Preselect the related
		carrier using the method RsCmwEvdoSig.Configure.Carrier.setting command. This frequency is determined by the cell's main
		carrier channel and the related carrier's channel offset. \n
			:return: cfwd_link_freq: Range: 100 MHz to 6.1 GHz
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:CARRier:FLFRequency?')
		return Conversions.str_to_int(response)

	def get_rl_frequency(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:CARRier:RLFRequency \n
		Snippet: value: int = driver.configure.carrier.get_rl_frequency() \n
		Gets the reverse link frequency for a carrier in the cell implemented by the signaling application. Preselect the related
		carrier using the method RsCmwEvdoSig.Configure.Carrier.setting command. This frequency is determined by the cell's main
		carrier channel and the related carrier's channel offset. \n
			:return: crev_link_freq: Range: 100 MHz to 6.1 GHz
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:CARRier:RLFRequency?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Carrier':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Carrier(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
