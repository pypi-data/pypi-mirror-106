from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Drc:
	"""Drc commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("drc", core, parent)

	def get_cover(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:MAC:DFTProtocol:DRC:COVer \n
		Snippet: value: int = driver.configure.layer.mac.dftProtocol.drc.get_cover() \n
		Specifies the DRC cover value that the AT is to use on its data rate control (DRC) channel (for subtype 0/1 signals only)
		. \n
			:return: drc_cover: Range: 1 to 6
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:MAC:DFTProtocol:DRC:COVer?')
		return Conversions.str_to_int(response)

	def set_cover(self, drc_cover: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:MAC:DFTProtocol:DRC:COVer \n
		Snippet: driver.configure.layer.mac.dftProtocol.drc.set_cover(drc_cover = 1) \n
		Specifies the DRC cover value that the AT is to use on its data rate control (DRC) channel (for subtype 0/1 signals only)
		. \n
			:param drc_cover: Range: 1 to 6
		"""
		param = Conversions.decimal_value_to_str(drc_cover)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:LAYer:MAC:DFTProtocol:DRC:COVer {param}')

	def get_length(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:MAC:DFTProtocol:DRC:LENGth \n
		Snippet: value: int = driver.configure.layer.mac.dftProtocol.drc.get_length() \n
		Defines the number of slots that the AT uses to send a single DRC (for subtype 0/1 signals only) . \n
			:return: drc_length: Range: 1 slots to 8 slots
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:MAC:DFTProtocol:DRC:LENGth?')
		return Conversions.str_to_int(response)

	def set_length(self, drc_length: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:MAC:DFTProtocol:DRC:LENGth \n
		Snippet: driver.configure.layer.mac.dftProtocol.drc.set_length(drc_length = 1) \n
		Defines the number of slots that the AT uses to send a single DRC (for subtype 0/1 signals only) . \n
			:param drc_length: Range: 1 slots to 8 slots
		"""
		param = Conversions.decimal_value_to_str(drc_length)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:LAYer:MAC:DFTProtocol:DRC:LENGth {param}')

	def get_cgain(self) -> float:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:MAC:DFTProtocol:DRC:CGAin \n
		Snippet: value: float = driver.configure.layer.mac.dftProtocol.drc.get_cgain() \n
		Defines the ratio of the power of the reverse data rate control channel to the power of the reverse pilot channel (for
		subtype 0/1 signals only) . \n
			:return: drcc_gain: Range: -9 dB to 6 dB
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:MAC:DFTProtocol:DRC:CGAin?')
		return Conversions.str_to_float(response)

	def set_cgain(self, drcc_gain: float) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:MAC:DFTProtocol:DRC:CGAin \n
		Snippet: driver.configure.layer.mac.dftProtocol.drc.set_cgain(drcc_gain = 1.0) \n
		Defines the ratio of the power of the reverse data rate control channel to the power of the reverse pilot channel (for
		subtype 0/1 signals only) . \n
			:param drcc_gain: Range: -9 dB to 6 dB
		"""
		param = Conversions.decimal_value_to_str(drcc_gain)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:LAYer:MAC:DFTProtocol:DRC:CGAin {param}')
