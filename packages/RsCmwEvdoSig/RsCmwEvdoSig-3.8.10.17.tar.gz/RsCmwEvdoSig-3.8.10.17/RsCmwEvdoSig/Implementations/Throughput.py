from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Throughput:
	"""Throughput commands group definition. 5 total commands, 1 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("throughput", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .Throughput_.State import State
			self._state = State(self._core, self._base)
		return self._state

	def initiate(self) -> None:
		"""SCPI: INITiate:EVDO:SIGNaling<instance>:THRoughput \n
		Snippet: driver.throughput.initiate() \n
		These remote commands control the throughput (performance) measurement - either forward or reverse, depending on the
		current test application mode (see method RsCmwEvdoSig.Configure.Application.mode) .
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'INITiate:EVDO:SIGNaling<Instance>:THRoughput')

	def initiate_with_opc(self) -> None:
		"""SCPI: INITiate:EVDO:SIGNaling<instance>:THRoughput \n
		Snippet: driver.throughput.initiate_with_opc() \n
		These remote commands control the throughput (performance) measurement - either forward or reverse, depending on the
		current test application mode (see method RsCmwEvdoSig.Configure.Application.mode) .
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCmwEvdoSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'INITiate:EVDO:SIGNaling<Instance>:THRoughput')

	def stop(self) -> None:
		"""SCPI: STOP:EVDO:SIGNaling<instance>:THRoughput \n
		Snippet: driver.throughput.stop() \n
		These remote commands control the throughput (performance) measurement - either forward or reverse, depending on the
		current test application mode (see method RsCmwEvdoSig.Configure.Application.mode) .
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'STOP:EVDO:SIGNaling<Instance>:THRoughput')

	def stop_with_opc(self) -> None:
		"""SCPI: STOP:EVDO:SIGNaling<instance>:THRoughput \n
		Snippet: driver.throughput.stop_with_opc() \n
		These remote commands control the throughput (performance) measurement - either forward or reverse, depending on the
		current test application mode (see method RsCmwEvdoSig.Configure.Application.mode) .
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCmwEvdoSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'STOP:EVDO:SIGNaling<Instance>:THRoughput')

	def abort(self) -> None:
		"""SCPI: ABORt:EVDO:SIGNaling<instance>:THRoughput \n
		Snippet: driver.throughput.abort() \n
		These remote commands control the throughput (performance) measurement - either forward or reverse, depending on the
		current test application mode (see method RsCmwEvdoSig.Configure.Application.mode) .
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'ABORt:EVDO:SIGNaling<Instance>:THRoughput')

	def abort_with_opc(self) -> None:
		"""SCPI: ABORt:EVDO:SIGNaling<instance>:THRoughput \n
		Snippet: driver.throughput.abort_with_opc() \n
		These remote commands control the throughput (performance) measurement - either forward or reverse, depending on the
		current test application mode (see method RsCmwEvdoSig.Configure.Application.mode) .
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCmwEvdoSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'ABORt:EVDO:SIGNaling<Instance>:THRoughput')

	def clone(self) -> 'Throughput':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Throughput(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
