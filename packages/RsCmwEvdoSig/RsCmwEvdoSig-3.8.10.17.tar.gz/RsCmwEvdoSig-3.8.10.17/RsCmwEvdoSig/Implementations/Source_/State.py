from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("state", core, parent)

	# noinspection PyTypeChecker
	class AllStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Main_State: enums.MainGenState: OFF | ON | RFHandover ON: generator has been turned on OFF: generator switched off RFHandover: Ready for handover, i.e. the signaling application is ready to receive an inter-RAT handover from another signaling application (e.g. LTE) , see 'Inter-RAT Handover' for details.
			- Sync_State: enums.SyncState: PENDing | ADJusted PENDing: the generator has been turned on (off) but the signal is not yet (still) available ADJusted: the physical output signal corresponds to the main generator state (signal off for main state OFF, signal on for main state ON)"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Main_State', enums.MainGenState),
			ArgStruct.scalar_enum('Sync_State', enums.SyncState)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Main_State: enums.MainGenState = None
			self.Sync_State: enums.SyncState = None

	# noinspection PyTypeChecker
	def get_all(self) -> AllStruct:
		"""SCPI: SOURce:EVDO:SIGNaling<instance>:STATe:ALL \n
		Snippet: value: AllStruct = driver.source.state.get_all() \n
		Returns detailed information about the '1xEV-DO Signaling' generator state. \n
			:return: structure: for return value, see the help for AllStruct structure arguments.
		"""
		return self._core.io.query_struct('SOURce:EVDO:SIGNaling<Instance>:STATe:ALL?', self.__class__.AllStruct())

	def get_value(self) -> bool:
		"""SCPI: SOURce:EVDO:SIGNaling<instance>:STATe \n
		Snippet: value: bool = driver.source.state.get_value() \n
		Turns the 1xEV-DO signaling generator (the cell) off or on. \n
			:return: main_state: No help available
		"""
		response = self._core.io.query_str_with_opc('SOURce:EVDO:SIGNaling<Instance>:STATe?')
		return Conversions.str_to_bool(response)

	def set_value(self, main_state: bool) -> None:
		"""SCPI: SOURce:EVDO:SIGNaling<instance>:STATe \n
		Snippet: driver.source.state.set_value(main_state = False) \n
		Turns the 1xEV-DO signaling generator (the cell) off or on. \n
			:param main_state: No help available
		"""
		param = Conversions.bool_to_str(main_state)
		self._core.io.write_with_opc(f'SOURce:EVDO:SIGNaling<Instance>:STATe {param}')
