from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Handoff:
	"""Handoff commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("handoff", core, parent)

	def start(self) -> None:
		"""SCPI: CALL:EVDO:SIGNaling<instance>:HANDoff:STARt \n
		Snippet: driver.call.handoff.start() \n
		Initiates a handoff to the previously configured destination cell. After the handoff, the destination cell settings
		replace the current cell settings. \n
		"""
		self._core.io.write(f'CALL:EVDO:SIGNaling<Instance>:HANDoff:STARt')

	def start_with_opc(self) -> None:
		"""SCPI: CALL:EVDO:SIGNaling<instance>:HANDoff:STARt \n
		Snippet: driver.call.handoff.start_with_opc() \n
		Initiates a handoff to the previously configured destination cell. After the handoff, the destination cell settings
		replace the current cell settings. \n
		Same as start, but waits for the operation to complete before continuing further. Use the RsCmwEvdoSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'CALL:EVDO:SIGNaling<Instance>:HANDoff:STARt')
