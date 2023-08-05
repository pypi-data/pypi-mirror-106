from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rx:
	"""Rx commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rx", core, parent)

	def get_eattenuation(self) -> float:
		"""SCPI: SOURce:EVDO:SIGNaling<instance>:RFSettings:RX:EATTenuation \n
		Snippet: value: float = driver.source.rfSettings.rx.get_eattenuation() \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the input connector. \n
			:return: rx_ext_att: Range: -50 dB to 90 dB, Unit: dB
		"""
		response = self._core.io.query_str('SOURce:EVDO:SIGNaling<Instance>:RFSettings:RX:EATTenuation?')
		return Conversions.str_to_float(response)

	def set_eattenuation(self, rx_ext_att: float) -> None:
		"""SCPI: SOURce:EVDO:SIGNaling<instance>:RFSettings:RX:EATTenuation \n
		Snippet: driver.source.rfSettings.rx.set_eattenuation(rx_ext_att = 1.0) \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the input connector. \n
			:param rx_ext_att: Range: -50 dB to 90 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(rx_ext_att)
		self._core.io.write(f'SOURce:EVDO:SIGNaling<Instance>:RFSettings:RX:EATTenuation {param}')
