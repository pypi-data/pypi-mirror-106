from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RlPer:
	"""RlPer commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rlPer", core, parent)

	def get_mp_sent(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:RLPer:MPSent \n
		Snippet: value: int = driver.configure.rxQuality.rlPer.get_mp_sent() \n
		Defines the length of a single shot reverse link PER measurement, i.e. the maximum number of test packets sent by the AT. \n
			:return: max_packets_sent: Range: 1 to 10000
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:RXQuality:RLPer:MPSent?')
		return Conversions.str_to_int(response)

	def set_mp_sent(self, max_packets_sent: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:RLPer:MPSent \n
		Snippet: driver.configure.rxQuality.rlPer.set_mp_sent(max_packets_sent = 1) \n
		Defines the length of a single shot reverse link PER measurement, i.e. the maximum number of test packets sent by the AT. \n
			:param max_packets_sent: Range: 1 to 10000
		"""
		param = Conversions.decimal_value_to_str(max_packets_sent)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:RXQuality:RLPer:MPSent {param}')

	# noinspection PyTypeChecker
	def get_scondition(self) -> enums.PerStopCondition:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:RLPer:SCONdition \n
		Snippet: value: enums.PerStopCondition = driver.configure.rxQuality.rlPer.get_scondition() \n
		Qualifies whether the measurement is stopped after a failed limit check or continued. SLFail means that the measurement
		is stopped and reaches the RDY state when one of the results exceeds the limits. \n
			:return: stop_condition: NONE | ALEXceeded | MCLexceeded | MPERexceeded NONE: Continue measurement irrespective of the limit check ALEXceeded: Stop if any limit is exceeded MCLexceeded: Stop if minimum confidence level is exceeded MPERexceeded: Stop if max. PER is exceeded
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:RXQuality:RLPer:SCONdition?')
		return Conversions.str_to_scalar_enum(response, enums.PerStopCondition)

	def set_scondition(self, stop_condition: enums.PerStopCondition) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:RLPer:SCONdition \n
		Snippet: driver.configure.rxQuality.rlPer.set_scondition(stop_condition = enums.PerStopCondition.ALEXceeded) \n
		Qualifies whether the measurement is stopped after a failed limit check or continued. SLFail means that the measurement
		is stopped and reaches the RDY state when one of the results exceeds the limits. \n
			:param stop_condition: NONE | ALEXceeded | MCLexceeded | MPERexceeded NONE: Continue measurement irrespective of the limit check ALEXceeded: Stop if any limit is exceeded MCLexceeded: Stop if minimum confidence level is exceeded MPERexceeded: Stop if max. PER is exceeded
		"""
		param = Conversions.enum_scalar_to_str(stop_condition, enums.PerStopCondition)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:RXQuality:RLPer:SCONdition {param}')
