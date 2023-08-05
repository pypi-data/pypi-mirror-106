from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RxQuality:
	"""RxQuality commands group definition. 25 total commands, 5 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rxQuality", core, parent)

	@property
	def flPer(self):
		"""flPer commands group. 2 Sub-classes, 3 commands."""
		if not hasattr(self, '_flPer'):
			from .RxQuality_.FlPer import FlPer
			self._flPer = FlPer(self._core, self._base)
		return self._flPer

	@property
	def rlPer(self):
		"""rlPer commands group. 2 Sub-classes, 3 commands."""
		if not hasattr(self, '_rlPer'):
			from .RxQuality_.RlPer import RlPer
			self._rlPer = RlPer(self._core, self._base)
		return self._rlPer

	@property
	def flPerformance(self):
		"""flPerformance commands group. 2 Sub-classes, 3 commands."""
		if not hasattr(self, '_flPerformance'):
			from .RxQuality_.FlPerformance import FlPerformance
			self._flPerformance = FlPerformance(self._core, self._base)
		return self._flPerformance

	@property
	def rlPerformance(self):
		"""rlPerformance commands group. 2 Sub-classes, 3 commands."""
		if not hasattr(self, '_rlPerformance'):
			from .RxQuality_.RlPerformance import RlPerformance
			self._rlPerformance = RlPerformance(self._core, self._base)
		return self._rlPerformance

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .RxQuality_.State import State
			self._state = State(self._core, self._base)
		return self._state

	def initiate(self) -> None:
		"""SCPI: INITiate:EVDO:SIGNaling<instance>:RXQuality \n
		Snippet: driver.rxQuality.initiate() \n
		No command help available \n
		"""
		self._core.io.write(f'INITiate:EVDO:SIGNaling<Instance>:RXQuality')

	def initiate_with_opc(self) -> None:
		"""SCPI: INITiate:EVDO:SIGNaling<instance>:RXQuality \n
		Snippet: driver.rxQuality.initiate_with_opc() \n
		No command help available \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCmwEvdoSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'INITiate:EVDO:SIGNaling<Instance>:RXQuality')

	def stop(self) -> None:
		"""SCPI: STOP:EVDO:SIGNaling<instance>:RXQuality \n
		Snippet: driver.rxQuality.stop() \n
		No command help available \n
		"""
		self._core.io.write(f'STOP:EVDO:SIGNaling<Instance>:RXQuality')

	def stop_with_opc(self) -> None:
		"""SCPI: STOP:EVDO:SIGNaling<instance>:RXQuality \n
		Snippet: driver.rxQuality.stop_with_opc() \n
		No command help available \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCmwEvdoSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'STOP:EVDO:SIGNaling<Instance>:RXQuality')

	def abort(self) -> None:
		"""SCPI: ABORt:EVDO:SIGNaling<instance>:RXQuality \n
		Snippet: driver.rxQuality.abort() \n
		No command help available \n
		"""
		self._core.io.write(f'ABORt:EVDO:SIGNaling<Instance>:RXQuality')

	def abort_with_opc(self) -> None:
		"""SCPI: ABORt:EVDO:SIGNaling<instance>:RXQuality \n
		Snippet: driver.rxQuality.abort_with_opc() \n
		No command help available \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCmwEvdoSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'ABORt:EVDO:SIGNaling<Instance>:RXQuality')

	def clone(self) -> 'RxQuality':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RxQuality(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
