from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lback:
	"""Lback commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("lback", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:APPLication:FTAP:LBACk:ENABle \n
		Snippet: value: bool = driver.configure.layer.application.ftap.lback.get_enable() \n
		Indicates whether the AT under test can transmit FTAP loopback packets to provide packet error rate (PER) information. \n
			:return: lback: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:APPLication:FTAP:LBACk:ENABle?')
		return Conversions.str_to_bool(response)
