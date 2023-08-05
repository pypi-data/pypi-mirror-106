from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bandwidth:
	"""Bandwidth commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("bandwidth", core, parent)

	def get_ratio(self) -> float:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:FADing:AWGN:BWIDth:RATio \n
		Snippet: value: float = driver.configure.fading.awgn.bandwidth.get_ratio() \n
		Queries the AWGN minimal noise to system bandwidth ratio for the AWGN inserted via the internal fading module. \n
			:return: ratio: Range: 1 to 250
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:FADing:AWGN:BWIDth:RATio?')
		return Conversions.str_to_float(response)

	def set_ratio(self, ratio: float) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:FADing:AWGN:BWIDth:RATio \n
		Snippet: driver.configure.fading.awgn.bandwidth.set_ratio(ratio = 1.0) \n
		Queries the AWGN minimal noise to system bandwidth ratio for the AWGN inserted via the internal fading module. \n
			:param ratio: Range: 1 to 250
		"""
		param = Conversions.decimal_value_to_str(ratio)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:FADing:AWGN:BWIDth:RATio {param}')

	def get_noise(self) -> float:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:FADing:AWGN:BWIDth:NOISe \n
		Snippet: value: float = driver.configure.fading.awgn.bandwidth.get_noise() \n
		Queries the bandwidth of the AWGN inserted via the internal fading module. \n
			:return: noise_bandwidth: Range: 0 Hz to 80 MHz , Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:FADing:AWGN:BWIDth:NOISe?')
		return Conversions.str_to_float(response)
