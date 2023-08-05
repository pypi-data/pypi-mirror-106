from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ....Internal.Types import DataType
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("state", core, parent)

	def fetch(self) -> str:
		"""SCPI: FETCh:EVDO:SIGNaling<instance>:RXQuality:RLPer:STATe \n
		Snippet: value: str = driver.rxQuality.rlPer.state.fetch() \n
		Returns a string containing status information about the measurement. \n
		Use RsCmwEvdoSig.reliability.last_value to read the updated reliability indicator. \n
			:return: status: See table below"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:EVDO:SIGNaling<Instance>:RXQuality:RLPer:STATe?', suppressed)
		return trim_str_response(response)
