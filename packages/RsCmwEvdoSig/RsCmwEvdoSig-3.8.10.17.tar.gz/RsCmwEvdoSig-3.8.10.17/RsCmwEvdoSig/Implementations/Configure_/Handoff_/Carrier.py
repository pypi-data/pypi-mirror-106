from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Carrier:
	"""Carrier commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("carrier", core, parent)

	def get_channel(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:HANDoff:CARRier:CHANnel \n
		Snippet: value: int = driver.configure.handoff.carrier.get_channel() \n
		Sets/gets the channel for a carrier in the handoff destination cell. Preselect the related carrier using the method
		RsCmwEvdoSig.Configure.Carrier.setting command. \n
			:return: carrier_channel: The range of possible channels depends on the destination cell's selected band class. For an overview, see 'Band Classes'. The values below are for band class BC0 (US Cellular) . Range: 1 to 799, 991 to 1323
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:HANDoff:CARRier:CHANnel?')
		return Conversions.str_to_int(response)

	def set_channel(self, carrier_channel: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:HANDoff:CARRier:CHANnel \n
		Snippet: driver.configure.handoff.carrier.set_channel(carrier_channel = 1) \n
		Sets/gets the channel for a carrier in the handoff destination cell. Preselect the related carrier using the method
		RsCmwEvdoSig.Configure.Carrier.setting command. \n
			:param carrier_channel: The range of possible channels depends on the destination cell's selected band class. For an overview, see 'Band Classes'. The values below are for band class BC0 (US Cellular) . Range: 1 to 799, 991 to 1323
		"""
		param = Conversions.decimal_value_to_str(carrier_channel)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:HANDoff:CARRier:CHANnel {param}')

	def get_fl_frequency(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:HANDoff:CARRier:FLFRequency \n
		Snippet: value: int = driver.configure.handoff.carrier.get_fl_frequency() \n
		Gets the forward link frequency for a carrier in the handoff destination cell. Preselect the related carrier using the
		method RsCmwEvdoSig.Configure.Carrier.setting command. This frequency is determined by the handoff destination cell's
		main carrier channel and the related carrier's channel offset. \n
			:return: cfwd_link_freq: Range: 100 MHz to 6.1 GHz
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:HANDoff:CARRier:FLFRequency?')
		return Conversions.str_to_int(response)

	def get_rl_frequency(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:HANDoff:CARRier:RLFRequency \n
		Snippet: value: int = driver.configure.handoff.carrier.get_rl_frequency() \n
		Gets the reverse link frequency for a carrier in the handoff destination cell. Preselect the related carrier using the
		method RsCmwEvdoSig.Configure.Carrier.setting command. This frequency is determined by the handoff destination cell's
		main carrier channel and the related carrier's channel offset. \n
			:return: crev_link_freq: Range: 100 MHz to 6.1 GHz
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:HANDoff:CARRier:RLFRequency?')
		return Conversions.str_to_int(response)
