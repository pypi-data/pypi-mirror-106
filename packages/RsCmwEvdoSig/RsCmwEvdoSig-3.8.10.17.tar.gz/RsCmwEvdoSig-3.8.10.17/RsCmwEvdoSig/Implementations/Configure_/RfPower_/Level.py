from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("level", core, parent)

	def get_awgn(self) -> float or bool:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RFPower:LEVel:AWGN \n
		Snippet: value: float or bool = driver.configure.rfPower.level.get_awgn() \n
		Sets/gets the state and level of the AWGN generator relative to the '1xEV-DO Power' (method RsCmwEvdoSig.Configure.
		RfPower.evdo) . The AWGN level range depends on the operating mode of the AWGN generator (method RsCmwEvdoSig.Configure.
		RfPower.Mode.awgn) . With the 'set' command, the AWGN generator can be turned OFF or ON and the level can be set. If the
		level is set, the generator is automatically turned ON. The query returns either the OFF state or the level if the
		generator state is ON. \n
			:return: awgn_level: Range: Between -25 dB and +4 dB (normal mode) or between -12 dB and 11.70 dB (high-power mode) , Unit: dB Additional OFF/ON disables/enables the AWGN signal
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:RFPower:LEVel:AWGN?')
		return Conversions.str_to_float_or_bool(response)

	def set_awgn(self, awgn_level: float or bool) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RFPower:LEVel:AWGN \n
		Snippet: driver.configure.rfPower.level.set_awgn(awgn_level = 1.0) \n
		Sets/gets the state and level of the AWGN generator relative to the '1xEV-DO Power' (method RsCmwEvdoSig.Configure.
		RfPower.evdo) . The AWGN level range depends on the operating mode of the AWGN generator (method RsCmwEvdoSig.Configure.
		RfPower.Mode.awgn) . With the 'set' command, the AWGN generator can be turned OFF or ON and the level can be set. If the
		level is set, the generator is automatically turned ON. The query returns either the OFF state or the level if the
		generator state is ON. \n
			:param awgn_level: Range: Between -25 dB and +4 dB (normal mode) or between -12 dB and 11.70 dB (high-power mode) , Unit: dB Additional OFF/ON disables/enables the AWGN signal
		"""
		param = Conversions.decimal_or_bool_value_to_str(awgn_level)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:RFPower:LEVel:AWGN {param}')
