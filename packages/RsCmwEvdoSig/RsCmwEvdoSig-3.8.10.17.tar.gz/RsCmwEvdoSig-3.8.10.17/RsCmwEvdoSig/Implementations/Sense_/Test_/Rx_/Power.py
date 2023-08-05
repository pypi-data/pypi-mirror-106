from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("power", core, parent)

	# noinspection PyTypeChecker
	def get_state(self) -> enums.RxSignalState:
		"""SCPI: SENSe:EVDO:SIGNaling<instance>:TEST:RX:POWer:STATe \n
		Snippet: value: enums.RxSignalState = driver.sense.test.rx.power.get_state() \n
		Queries the quality of the RX signal from the connected AT. \n
			:return: state: NAV | LOW | OK | HIGH NAV: no signal from AT detected LOW: the AT power is below the expected range OK: the AT power is in the expected range HIGH: the AT power is above the expected range
		"""
		response = self._core.io.query_str('SENSe:EVDO:SIGNaling<Instance>:TEST:RX:POWer:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.RxSignalState)
