from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ....Internal.Types import DataType
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cstate:
	"""Cstate commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cstate", core, parent)

	# noinspection PyTypeChecker
	def fetch(self) -> List[enums.CarrierStatus]:
		"""SCPI: FETCh:EVDO:SIGNaling<instance>:RXQuality:RLPer:CSTate \n
		Snippet: value: List[enums.CarrierStatus] = driver.rxQuality.rlPer.cstate.fetch() \n
		Returns status information about the carrier. \n
		Use RsCmwEvdoSig.reliability.last_value to read the updated reliability indicator. \n
			:return: carrier_status: OK | VIOLated | STALe | INACtive"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:EVDO:SIGNaling<Instance>:RXQuality:RLPer:CSTate?', suppressed)
		return Conversions.str_to_list_enum(response, enums.CarrierStatus)
