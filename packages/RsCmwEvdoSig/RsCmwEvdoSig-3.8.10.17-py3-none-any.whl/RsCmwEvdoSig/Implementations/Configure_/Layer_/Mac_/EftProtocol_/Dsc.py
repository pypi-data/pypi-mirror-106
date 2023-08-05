from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dsc:
	"""Dsc commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dsc", core, parent)

	def get_value(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:MAC:EFTProtocol:DSC:VALue \n
		Snippet: value: int = driver.configure.layer.mac.eftProtocol.dsc.get_value() \n
		Specifies the value that the AT is to use on the data source channel (DSC) to select the serving sector simulated by the
		R&S CMW (for subtype 2 and 3 signals only) . \n
			:return: dsc_value: Range: 1 to 7
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:MAC:EFTProtocol:DSC:VALue?')
		return Conversions.str_to_int(response)

	def set_value(self, dsc_value: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:MAC:EFTProtocol:DSC:VALue \n
		Snippet: driver.configure.layer.mac.eftProtocol.dsc.set_value(dsc_value = 1) \n
		Specifies the value that the AT is to use on the data source channel (DSC) to select the serving sector simulated by the
		R&S CMW (for subtype 2 and 3 signals only) . \n
			:param dsc_value: Range: 1 to 7
		"""
		param = Conversions.decimal_value_to_str(dsc_value)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:LAYer:MAC:EFTProtocol:DSC:VALue {param}')

	def get_cgain(self) -> float:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:MAC:EFTProtocol:DSC:CGAin \n
		Snippet: value: float = driver.configure.layer.mac.eftProtocol.dsc.get_cgain() \n
		Sets the power of the reverse DSC relative to the power of the reverse pilot channel (for subtype 2 and 3 signals only) . \n
			:return: dscch_gain: Range: -15.5 dB to 0 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:MAC:EFTProtocol:DSC:CGAin?')
		return Conversions.str_to_float(response)

	def set_cgain(self, dscch_gain: float) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:MAC:EFTProtocol:DSC:CGAin \n
		Snippet: driver.configure.layer.mac.eftProtocol.dsc.set_cgain(dscch_gain = 1.0) \n
		Sets the power of the reverse DSC relative to the power of the reverse pilot channel (for subtype 2 and 3 signals only) . \n
			:param dscch_gain: Range: -15.5 dB to 0 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(dscch_gain)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:LAYer:MAC:EFTProtocol:DSC:CGAin {param}')
