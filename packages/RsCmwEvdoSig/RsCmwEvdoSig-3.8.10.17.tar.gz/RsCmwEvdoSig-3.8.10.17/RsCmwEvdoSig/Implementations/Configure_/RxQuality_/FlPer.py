from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FlPer:
	"""FlPer commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("flPer", core, parent)

	def get_mtpsent(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:FLPer:MTPSent \n
		Snippet: value: int = driver.configure.rxQuality.flPer.get_mtpsent() \n
		Defines the length of a single shot forward link PER measurement, i.e. the maximum number of test packets sent. \n
			:return: max_test_pack_sent: Range: 1 to 10000
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:RXQuality:FLPer:MTPSent?')
		return Conversions.str_to_int(response)

	def set_mtpsent(self, max_test_pack_sent: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:FLPer:MTPSent \n
		Snippet: driver.configure.rxQuality.flPer.set_mtpsent(max_test_pack_sent = 1) \n
		Defines the length of a single shot forward link PER measurement, i.e. the maximum number of test packets sent. \n
			:param max_test_pack_sent: Range: 1 to 10000
		"""
		param = Conversions.decimal_value_to_str(max_test_pack_sent)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:RXQuality:FLPer:MTPSent {param}')

	# noinspection PyTypeChecker
	def get_scondition(self) -> enums.PerStopCondition:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:FLPer:SCONdition \n
		Snippet: value: enums.PerStopCondition = driver.configure.rxQuality.flPer.get_scondition() \n
		Qualifies whether the measurement is stopped after a failed limit check or continued. SLFail means that the measurement
		is stopped and reaches the RDY state when one of the results exceeds the limits. \n
			:return: stop_condition: NONE | ALEXceeded | MCLexceeded | MPERexceeded NONE: Continue measurement irrespective of the limit check ALEXceeded: Stop if any limit is exceeded MCLexceeded: Stop if minimum confidence level is exceeded MPERexceeded: Stop if max. PER is exceeded
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:RXQuality:FLPer:SCONdition?')
		return Conversions.str_to_scalar_enum(response, enums.PerStopCondition)

	def set_scondition(self, stop_condition: enums.PerStopCondition) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:FLPer:SCONdition \n
		Snippet: driver.configure.rxQuality.flPer.set_scondition(stop_condition = enums.PerStopCondition.ALEXceeded) \n
		Qualifies whether the measurement is stopped after a failed limit check or continued. SLFail means that the measurement
		is stopped and reaches the RDY state when one of the results exceeds the limits. \n
			:param stop_condition: NONE | ALEXceeded | MCLexceeded | MPERexceeded NONE: Continue measurement irrespective of the limit check ALEXceeded: Stop if any limit is exceeded MCLexceeded: Stop if minimum confidence level is exceeded MPERexceeded: Stop if max. PER is exceeded
		"""
		param = Conversions.enum_scalar_to_str(stop_condition, enums.PerStopCondition)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:RXQuality:FLPer:SCONdition {param}')
