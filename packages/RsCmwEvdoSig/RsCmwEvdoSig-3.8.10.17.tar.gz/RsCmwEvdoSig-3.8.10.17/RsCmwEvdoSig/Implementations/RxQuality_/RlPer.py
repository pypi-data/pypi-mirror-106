from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.Types import DataType
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ...Internal.ArgSingleList import ArgSingleList
from ...Internal.ArgSingle import ArgSingle
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RlPer:
	"""RlPer commands group definition. 5 total commands, 2 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rlPer", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .RlPer_.State import State
			self._state = State(self._core, self._base)
		return self._state

	@property
	def cstate(self):
		"""cstate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cstate'):
			from .RlPer_.Cstate import Cstate
			self._cstate = Cstate(self._core, self._base)
		return self._cstate

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Macp_Kts_Transm: int: No parameter help available
			- Rl_Macp_Kts_Errors: int: No parameter help available
			- Rl_Conf_Level: float: No parameter help available
			- Rl_Per: float: The reverse link packet error rate (for the selected carrier) . Range: 0 % to 100 %
			- Tt_Macp_Kts_Errors: int: No parameter help available
			- Tt_Conf_Level: float: No parameter help available
			- Tt_Per: float: The rate of MAC packets the R&S CMW failed to receive successfully (on the selected carrier) . This result is available for physical layer subtypes 2 and 3 only. Range: 0 % to 100 %
			- Mac_Packets_Sent: int: No parameter help available
			- All_Macp_Kts_Trans: int: No parameter help available
			- All_Macp_Kts_Error: int: No parameter help available
			- All_Rl_Conf_Level: float: No parameter help available
			- All_Rl_Per: float: No parameter help available
			- All_Ttp_Kts_Errors: int: No parameter help available
			- All_Tt_Conf_Level: float: No parameter help available
			- All_Tt_Per: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Macp_Kts_Transm'),
			ArgStruct.scalar_int('Rl_Macp_Kts_Errors'),
			ArgStruct.scalar_float('Rl_Conf_Level'),
			ArgStruct.scalar_float('Rl_Per'),
			ArgStruct.scalar_int('Tt_Macp_Kts_Errors'),
			ArgStruct.scalar_float('Tt_Conf_Level'),
			ArgStruct.scalar_float('Tt_Per'),
			ArgStruct.scalar_int('Mac_Packets_Sent'),
			ArgStruct.scalar_int('All_Macp_Kts_Trans'),
			ArgStruct.scalar_int('All_Macp_Kts_Error'),
			ArgStruct.scalar_float('All_Rl_Conf_Level'),
			ArgStruct.scalar_float('All_Rl_Per'),
			ArgStruct.scalar_int('All_Ttp_Kts_Errors'),
			ArgStruct.scalar_float('All_Tt_Conf_Level'),
			ArgStruct.scalar_float('All_Tt_Per')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Macp_Kts_Transm: int = None
			self.Rl_Macp_Kts_Errors: int = None
			self.Rl_Conf_Level: float = None
			self.Rl_Per: float = None
			self.Tt_Macp_Kts_Errors: int = None
			self.Tt_Conf_Level: float = None
			self.Tt_Per: float = None
			self.Mac_Packets_Sent: int = None
			self.All_Macp_Kts_Trans: int = None
			self.All_Macp_Kts_Error: int = None
			self.All_Rl_Conf_Level: float = None
			self.All_Rl_Per: float = None
			self.All_Ttp_Kts_Errors: int = None
			self.All_Tt_Conf_Level: float = None
			self.All_Tt_Per: float = None

	def read(self, data_rate: enums.RevLinkPerDataRate = None) -> ResultData:
		"""SCPI: READ:EVDO:SIGNaling<instance>:RXQuality:RLPer \n
		Snippet: value: ResultData = driver.rxQuality.rlPer.read(data_rate = enums.RevLinkPerDataRate.R0K0) \n
			INTRO_CMD_HELP: Returns the 'Reverse Link PER' measurement results for: \n
			- The specified data rate
			- The selected carrier (in multi-carrier scenarios, see 'Reverse Link Packet Error Rate Measurement')
		Preselect the related carrier using the method RsCmwEvdoSig.Configure.Carrier.setting command. The values described
		below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each
		result listed below. The number to the left of each result parameter is provided for easy identification of the parameter
		position within the result array. \n
			:param data_rate: R0K0 | R19K2 | R38K4 | R76K8 | R115k2 | R153k6 | R230k4 | R307k2 | R460k8 | R614k4 | R921k6 | R1228k8 | R1843k2 | TOTal This query parameter specifies the data rate for which the results are returned, i.e. it selects a row in the 'Reverse Link PER' result table. If it is omitted, the command returns the TOTal results, i.e. the aggregates over all data rates. Note that the 'composite' return values are aggregates over all carriers and data rates, i.e. no matter which data rate is specified, always the TOTal values are returned.
			:return: structure: for return value, see the help for ResultData structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('data_rate', data_rate, DataType.Enum, True))
		return self._core.io.query_struct(f'READ:EVDO:SIGNaling<Instance>:RXQuality:RLPer? {param}'.rstrip(), self.__class__.ResultData())

	def fetch(self, data_rate: enums.RevLinkPerDataRate = None) -> ResultData:
		"""SCPI: FETCh:EVDO:SIGNaling<instance>:RXQuality:RLPer \n
		Snippet: value: ResultData = driver.rxQuality.rlPer.fetch(data_rate = enums.RevLinkPerDataRate.R0K0) \n
			INTRO_CMD_HELP: Returns the 'Reverse Link PER' measurement results for: \n
			- The specified data rate
			- The selected carrier (in multi-carrier scenarios, see 'Reverse Link Packet Error Rate Measurement')
		Preselect the related carrier using the method RsCmwEvdoSig.Configure.Carrier.setting command. The values described
		below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each
		result listed below. The number to the left of each result parameter is provided for easy identification of the parameter
		position within the result array. \n
			:param data_rate: R0K0 | R19K2 | R38K4 | R76K8 | R115k2 | R153k6 | R230k4 | R307k2 | R460k8 | R614k4 | R921k6 | R1228k8 | R1843k2 | TOTal This query parameter specifies the data rate for which the results are returned, i.e. it selects a row in the 'Reverse Link PER' result table. If it is omitted, the command returns the TOTal results, i.e. the aggregates over all data rates. Note that the 'composite' return values are aggregates over all carriers and data rates, i.e. no matter which data rate is specified, always the TOTal values are returned.
			:return: structure: for return value, see the help for ResultData structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('data_rate', data_rate, DataType.Enum, True))
		return self._core.io.query_struct(f'FETCh:EVDO:SIGNaling<Instance>:RXQuality:RLPer? {param}'.rstrip(), self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Macp_Kts_Transm: float: No parameter help available
			- Rl_Macp_Kts_Errors: float: No parameter help available
			- Rl_Conf_Level: float: No parameter help available
			- Rl_Per: float: The reverse link packet error rate (for the selected carrier) . Range: 0 % to 100 %
			- Tt_Macp_Kts_Errors: float: No parameter help available
			- Tt_Conf_Level: float: No parameter help available
			- Tt_Per: float: The rate of MAC packets the R&S CMW failed to receive successfully (on the selected carrier) . This result is available for physical layer subtypes 2 and 3 only. Range: 0 % to 100 %
			- Mac_Packets_Sent: float: No parameter help available
			- All_Macp_Kts_Trans: float: No parameter help available
			- All_Macp_Kts_Error: float: No parameter help available
			- All_Rl_Conf_Level: float: No parameter help available
			- All_Rl_Per: float: No parameter help available
			- All_Ttp_Kts_Errors: float: No parameter help available
			- All_Tt_Conf_Level: float: No parameter help available
			- All_Tt_Per: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Macp_Kts_Transm'),
			ArgStruct.scalar_float('Rl_Macp_Kts_Errors'),
			ArgStruct.scalar_float('Rl_Conf_Level'),
			ArgStruct.scalar_float('Rl_Per'),
			ArgStruct.scalar_float('Tt_Macp_Kts_Errors'),
			ArgStruct.scalar_float('Tt_Conf_Level'),
			ArgStruct.scalar_float('Tt_Per'),
			ArgStruct.scalar_float('Mac_Packets_Sent'),
			ArgStruct.scalar_float('All_Macp_Kts_Trans'),
			ArgStruct.scalar_float('All_Macp_Kts_Error'),
			ArgStruct.scalar_float('All_Rl_Conf_Level'),
			ArgStruct.scalar_float('All_Rl_Per'),
			ArgStruct.scalar_float('All_Ttp_Kts_Errors'),
			ArgStruct.scalar_float('All_Tt_Conf_Level'),
			ArgStruct.scalar_float('All_Tt_Per')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Macp_Kts_Transm: float = None
			self.Rl_Macp_Kts_Errors: float = None
			self.Rl_Conf_Level: float = None
			self.Rl_Per: float = None
			self.Tt_Macp_Kts_Errors: float = None
			self.Tt_Conf_Level: float = None
			self.Tt_Per: float = None
			self.Mac_Packets_Sent: float = None
			self.All_Macp_Kts_Trans: float = None
			self.All_Macp_Kts_Error: float = None
			self.All_Rl_Conf_Level: float = None
			self.All_Rl_Per: float = None
			self.All_Ttp_Kts_Errors: float = None
			self.All_Tt_Conf_Level: float = None
			self.All_Tt_Per: float = None

	def calculate(self, data_rate: enums.RevLinkPerDataRate = None) -> CalculateStruct:
		"""SCPI: CALCulate:EVDO:SIGNaling<instance>:RXQuality:RLPer \n
		Snippet: value: CalculateStruct = driver.rxQuality.rlPer.calculate(data_rate = enums.RevLinkPerDataRate.R0K0) \n
			INTRO_CMD_HELP: Returns the 'Reverse Link PER' measurement results for: \n
			- The specified data rate
			- The selected carrier (in multi-carrier scenarios, see 'Reverse Link Packet Error Rate Measurement')
		Preselect the related carrier using the method RsCmwEvdoSig.Configure.Carrier.setting command. The values described
		below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each
		result listed below. The number to the left of each result parameter is provided for easy identification of the parameter
		position within the result array. \n
			:param data_rate: R0K0 | R19K2 | R38K4 | R76K8 | R115k2 | R153k6 | R230k4 | R307k2 | R460k8 | R614k4 | R921k6 | R1228k8 | R1843k2 | TOTal This query parameter specifies the data rate for which the results are returned, i.e. it selects a row in the 'Reverse Link PER' result table. If it is omitted, the command returns the TOTal results, i.e. the aggregates over all data rates. Note that the 'composite' return values are aggregates over all carriers and data rates, i.e. no matter which data rate is specified, always the TOTal values are returned.
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('data_rate', data_rate, DataType.Enum, True))
		return self._core.io.query_struct(f'CALCulate:EVDO:SIGNaling<Instance>:RXQuality:RLPer? {param}'.rstrip(), self.__class__.CalculateStruct())

	def clone(self) -> 'RlPer':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RlPer(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
