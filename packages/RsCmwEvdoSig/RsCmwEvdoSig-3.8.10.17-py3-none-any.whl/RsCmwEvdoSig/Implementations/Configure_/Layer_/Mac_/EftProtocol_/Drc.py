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
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:MAC:EFTProtocol:DRC:COVer \n
		Snippet: value: int = driver.configure.layer.mac.eftProtocol.drc.get_cover() \n
		Specifies the DRC cover value that the AT is to use on its data rate control (DRC) channel (for subtype 2 and 3 signals
		only) . \n
			:return: drc_cover: Range: 1 to 6
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:MAC:EFTProtocol:DRC:COVer?')
		return Conversions.str_to_int(response)

	def set_cover(self, drc_cover: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:MAC:EFTProtocol:DRC:COVer \n
		Snippet: driver.configure.layer.mac.eftProtocol.drc.set_cover(drc_cover = 1) \n
		Specifies the DRC cover value that the AT is to use on its data rate control (DRC) channel (for subtype 2 and 3 signals
		only) . \n
			:param drc_cover: Range: 1 to 6
		"""
		param = Conversions.decimal_value_to_str(drc_cover)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:LAYer:MAC:EFTProtocol:DRC:COVer {param}')

	def get_length(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:MAC:EFTProtocol:DRC:LENGth \n
		Snippet: value: int = driver.configure.layer.mac.eftProtocol.drc.get_length() \n
		Defines the number of slots that the AT uses to send a single DRC message on a carrier (for subtype 2 and 3 signals only)
		. Preselect the related carrier using the method RsCmwEvdoSig.Configure.Carrier.setting command. \n
			:return: drc_length: Range: 1 to 8, Unit: slots
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:MAC:EFTProtocol:DRC:LENGth?')
		return Conversions.str_to_int(response)

	def set_length(self, drc_length: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:MAC:EFTProtocol:DRC:LENGth \n
		Snippet: driver.configure.layer.mac.eftProtocol.drc.set_length(drc_length = 1) \n
		Defines the number of slots that the AT uses to send a single DRC message on a carrier (for subtype 2 and 3 signals only)
		. Preselect the related carrier using the method RsCmwEvdoSig.Configure.Carrier.setting command. \n
			:param drc_length: Range: 1 to 8, Unit: slots
		"""
		param = Conversions.decimal_value_to_str(drc_length)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:LAYer:MAC:EFTProtocol:DRC:LENGth {param}')

	def get_cgain(self) -> float:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:MAC:EFTProtocol:DRC:CGAin \n
		Snippet: value: float = driver.configure.layer.mac.eftProtocol.drc.get_cgain() \n
		Defines a carrier's power level ratio of the reverse data rate control channel relative to the reverse pilot channel
		(subtype 2 and 3 signals only) . Preselect the related carrier using the method RsCmwEvdoSig.Configure.Carrier.setting
		command. \n
			:return: drcc_gain: Range: -9 dB to 6 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:MAC:EFTProtocol:DRC:CGAin?')
		return Conversions.str_to_float(response)

	def set_cgain(self, drcc_gain: float) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:MAC:EFTProtocol:DRC:CGAin \n
		Snippet: driver.configure.layer.mac.eftProtocol.drc.set_cgain(drcc_gain = 1.0) \n
		Defines a carrier's power level ratio of the reverse data rate control channel relative to the reverse pilot channel
		(subtype 2 and 3 signals only) . Preselect the related carrier using the method RsCmwEvdoSig.Configure.Carrier.setting
		command. \n
			:param drcc_gain: Range: -9 dB to 6 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(drcc_gain)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:LAYer:MAC:EFTProtocol:DRC:CGAin {param}')
