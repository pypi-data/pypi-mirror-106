from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("state", core, parent)

	# noinspection PyTypeChecker
	def fetch(self) -> enums.PdState:
		"""SCPI: FETCh:EVDO:SIGNaling<instance>:PDATa:STATe \n
		Snippet: value: enums.PdState = driver.pdata.state.fetch() \n
		Returns the state of the packet data (PPP) connection. \n
			:return: pd_state: OFF | ON | DORMant | CONNected"""
		response = self._core.io.query_str(f'FETCh:EVDO:SIGNaling<Instance>:PDATa:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.PdState)
