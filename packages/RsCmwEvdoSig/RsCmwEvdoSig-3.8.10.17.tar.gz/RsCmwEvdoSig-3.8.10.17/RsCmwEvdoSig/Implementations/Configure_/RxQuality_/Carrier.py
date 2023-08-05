from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Carrier:
	"""Carrier commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("carrier", core, parent)

	def get_select(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:CARRier:SELect \n
		Snippet: value: int = driver.configure.rxQuality.carrier.get_select() \n
		Gets/sets the carrier whose results are retrieved in subsequent FETch/READ/CALCulate commands. Applies to PL subtype 3
		only. \n
			:return: selected_carrier: Range: 0 to 2
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:RXQuality:CARRier:SELect?')
		return Conversions.str_to_int(response)

	def set_select(self, selected_carrier: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:CARRier:SELect \n
		Snippet: driver.configure.rxQuality.carrier.set_select(selected_carrier = 1) \n
		Gets/sets the carrier whose results are retrieved in subsequent FETch/READ/CALCulate commands. Applies to PL subtype 3
		only. \n
			:param selected_carrier: Range: 0 to 2
		"""
		param = Conversions.decimal_value_to_str(selected_carrier)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:RXQuality:CARRier:SELect {param}')
