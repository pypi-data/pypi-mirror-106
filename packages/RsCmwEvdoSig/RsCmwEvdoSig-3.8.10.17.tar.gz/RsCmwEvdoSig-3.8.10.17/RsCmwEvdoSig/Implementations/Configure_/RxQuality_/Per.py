from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Per:
	"""Per commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("per", core, parent)

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:PER:TOUT \n
		Snippet: value: float = driver.configure.rxQuality.per.get_timeout() \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually ([ON | OFF] key or [RESTART | STOP] key) .
		When the measurement has completed the first measurement cycle (first single shot) , the statistical depth is reached and
		the timer is reset. If the first measurement cycle has not been completed when the timer expires, the measurement is
		stopped. The measurement state changes to RDY. The reliability indicator is set to 1, indicating that a measurement
		timeout occurred. Still running READ, FETCh or CALCulate commands are completed, returning the available results.
		At least for some results, there are no values at all or the statistical depth has not been reached. A timeout of 0 s
		corresponds to an infinite measurement timeout. \n
			:return: timeout: Unit: s
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:RXQuality:PER:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, timeout: float) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:PER:TOUT \n
		Snippet: driver.configure.rxQuality.per.set_timeout(timeout = 1.0) \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually ([ON | OFF] key or [RESTART | STOP] key) .
		When the measurement has completed the first measurement cycle (first single shot) , the statistical depth is reached and
		the timer is reset. If the first measurement cycle has not been completed when the timer expires, the measurement is
		stopped. The measurement state changes to RDY. The reliability indicator is set to 1, indicating that a measurement
		timeout occurred. Still running READ, FETCh or CALCulate commands are completed, returning the available results.
		At least for some results, there are no values at all or the statistical depth has not been reached. A timeout of 0 s
		corresponds to an infinite measurement timeout. \n
			:param timeout: Unit: s
		"""
		param = Conversions.decimal_value_to_str(timeout)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:RXQuality:PER:TOUT {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:PER:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.rxQuality.per.get_repetition() \n
		Specifies the repetition mode of the packet error rate (PER) measurement. The repetition mode specifies whether the
		measurement is stopped after a single-shot or repeated continuously. Use method RsCmwEvdoSig.Configure.RxQuality.FlPer.
		mtpsent or method RsCmwEvdoSig.Configure.RxQuality.RlPer.mpSent to determine the number of test packets per single shot. \n
			:return: repetition: SINGleshot | CONTinuous SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:RXQuality:PER:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:PER:REPetition \n
		Snippet: driver.configure.rxQuality.per.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		Specifies the repetition mode of the packet error rate (PER) measurement. The repetition mode specifies whether the
		measurement is stopped after a single-shot or repeated continuously. Use method RsCmwEvdoSig.Configure.RxQuality.FlPer.
		mtpsent or method RsCmwEvdoSig.Configure.RxQuality.RlPer.mpSent to determine the number of test packets per single shot. \n
			:param repetition: SINGleshot | CONTinuous SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:RXQuality:PER:REPetition {param}')
