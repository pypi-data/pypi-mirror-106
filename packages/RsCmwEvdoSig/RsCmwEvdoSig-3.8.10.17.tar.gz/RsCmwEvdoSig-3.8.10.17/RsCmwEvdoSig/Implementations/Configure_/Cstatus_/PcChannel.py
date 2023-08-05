from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PcChannel:
	"""PcChannel commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pcChannel", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:CSTatus:PCCHannel:ENABle \n
		Snippet: value: bool = driver.configure.cstatus.pcChannel.get_enable() \n
		Queries the state of the 'Preferred Control Channel Enable' flag. The flag indicates whether the AT selects the preferred
		control channel cycle. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:CSTatus:PCCHannel:ENABle?')
		return Conversions.str_to_bool(response)

	def get_cycle(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:CSTatus:PCCHannel:CYCLe \n
		Snippet: value: int = driver.configure.cstatus.pcChannel.get_cycle() \n
		Queries the control channel cycle in which the AT makes a transition out of the dormant state to monitor the control
		channel. \n
			:return: cycle: Range: 0 to 32767 , Unit: (control channel cycles)
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:CSTatus:PCCHannel:CYCLe?')
		return Conversions.str_to_int(response)
