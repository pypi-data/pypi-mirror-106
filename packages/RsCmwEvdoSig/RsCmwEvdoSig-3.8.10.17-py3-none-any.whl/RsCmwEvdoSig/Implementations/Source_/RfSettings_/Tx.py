from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tx:
	"""Tx commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("tx", core, parent)

	def get_eattenuation(self) -> float:
		"""SCPI: SOURce:EVDO:SIGNaling<instance>:RFSettings:TX:EATTenuation \n
		Snippet: value: float = driver.source.rfSettings.tx.get_eattenuation() \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the output connector. \n
			:return: tx_ext_att: Range: -50 dB to 90 dB, Unit: dB
		"""
		response = self._core.io.query_str('SOURce:EVDO:SIGNaling<Instance>:RFSettings:TX:EATTenuation?')
		return Conversions.str_to_float(response)

	def set_eattenuation(self, tx_ext_att: float) -> None:
		"""SCPI: SOURce:EVDO:SIGNaling<instance>:RFSettings:TX:EATTenuation \n
		Snippet: driver.source.rfSettings.tx.set_eattenuation(tx_ext_att = 1.0) \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the output connector. \n
			:param tx_ext_att: Range: -50 dB to 90 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(tx_ext_att)
		self._core.io.write(f'SOURce:EVDO:SIGNaling<Instance>:RFSettings:TX:EATTenuation {param}')
