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
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:APPLication:FMCTap:LBACk:ENABle \n
		Snippet: value: bool = driver.configure.layer.application.fmctap.lback.get_enable() \n
		Queries whether the AT under test transmits FMCTAP loopback packets to measure packet error rate (PER) . \n
			:return: lback: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:APPLication:FMCTap:LBACk:ENABle?')
		return Conversions.str_to_bool(response)
