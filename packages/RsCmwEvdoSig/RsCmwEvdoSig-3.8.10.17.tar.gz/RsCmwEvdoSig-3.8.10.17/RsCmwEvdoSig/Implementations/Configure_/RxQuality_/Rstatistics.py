from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rstatistics:
	"""Rstatistics commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rstatistics", core, parent)

	def set(self) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:RSTatistics \n
		Snippet: driver.configure.rxQuality.rstatistics.set() \n
		Clears the statistics for all receiver quality measurements and restarts the measurements. \n
		"""
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:RXQuality:RSTatistics')

	def set_with_opc(self) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:RSTatistics \n
		Snippet: driver.configure.rxQuality.rstatistics.set_with_opc() \n
		Clears the statistics for all receiver quality measurements and restarts the measurements. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwEvdoSig.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'CONFigure:EVDO:SIGNaling<Instance>:RXQuality:RSTatistics')
