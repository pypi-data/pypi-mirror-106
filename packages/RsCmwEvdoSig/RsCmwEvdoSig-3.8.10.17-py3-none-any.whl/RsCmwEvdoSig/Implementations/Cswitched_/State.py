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
	def fetch(self) -> enums.ConnectionState:
		"""SCPI: FETCh:EVDO:SIGNaling<instance>:CSWitched:STATe \n
		Snippet: value: enums.ConnectionState = driver.cswitched.state.fetch() \n
		Returns the connection state of an 1xEV-DO connection. Use method RsCmwEvdoSig.Call.Cswitched.action to initiate a
		transition between different connection states. The connection state changes to ON when the signaling generator is
		started (method RsCmwEvdoSig.Source.State.value ON) . To make sure that a forward 1xEV-DO signal is available, query the
		sector state: method RsCmwEvdoSig.Source.State.all must return ON, ADJ. \n
			:return: cs_state: OFF | ON | IDLE | SNEGotiation | SOPen | PAGing | CONNected Connection state; for details refer to 'Connection States'."""
		response = self._core.io.query_str(f'FETCh:EVDO:SIGNaling<Instance>:CSWitched:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.ConnectionState)
