from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.Types import DataType
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ...Internal.ArgSingleList import ArgSingleList
from ...Internal.ArgSingle import ArgSingle
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RlPerformance:
	"""RlPerformance commands group definition. 5 total commands, 2 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rlPerformance", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .RlPerformance_.State import State
			self._state = State(self._core, self._base)
		return self._state

	@property
	def cstate(self):
		"""cstate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cstate'):
			from .RlPerformance_.Cstate import Cstate
			self._cstate = Cstate(self._core, self._base)
		return self._cstate

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Packet_Size: str: The packet size given as string representations of the enum constants S128 | S256 | S512 | S1K | S2K | S3K | S4K | S5K | S6K | S7K | S8K | TOTal corresponding to the data rates in bit: 128, 256, 512, 1024, 2048, 3072, 4096, 5120, 6144, 7162, 8192.
			- Mac_Pack_Received: int: The number of MAC packets successfully received by the R&S CMW (on the selected carrier) . Range: 0 to 10E+3
			- Th_Vs_Test_Time: float: The average throughput in kbit/s (on the selected carrier) during the test time Range: 0 kbit/s to 99.99999E+3 kbit/s
			- Test_Time: int: The elapsed test time as the number of 26.67 ms CDMA frames. Range: 0 to 10E+3
			- All_Th_Vs_Test_Time: float: The average throughput in kbit/s (on the selected carrier) during the test time Range: 0 kbit/s to 99.99999E+3 kbit/s"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_str('Packet_Size'),
			ArgStruct.scalar_int('Mac_Pack_Received'),
			ArgStruct.scalar_float('Th_Vs_Test_Time'),
			ArgStruct.scalar_int('Test_Time'),
			ArgStruct.scalar_float('All_Th_Vs_Test_Time')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Packet_Size: str = None
			self.Mac_Pack_Received: int = None
			self.Th_Vs_Test_Time: float = None
			self.Test_Time: int = None
			self.All_Th_Vs_Test_Time: float = None

	def read(self, data_rate: enums.RevLinkPerDataRate = None) -> ResultData:
		"""SCPI: READ:EVDO:SIGNaling<instance>:RXQuality:RLPFormance \n
		Snippet: value: ResultData = driver.rxQuality.rlPerformance.read(data_rate = enums.RevLinkPerDataRate.R0K0) \n
		Returns the results of the 'Reverse Link Throughput' measurement for the specified data rate (and the selected carrier in
		multi-carrier scenarios) , see 'Reverse Link Throughput Measurement'. Preselect the related carrier using the method
		RsCmwEvdoSig.Configure.Carrier.setting command. The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
			:param data_rate: R0K0 | R19K2 | R38K4 | R76K8 | R115k2 | R153k6 | R230k4 | R307k2 | R460k8 | R614k4 | R921k6 | R1228k8 | R1843k2 | TOTal This query parameter specifies the data rate for which the results are returned, i.e. it selects a row in the 'Reverse Link Throughput' result table. If omitted, the TOTal values are returned, i.e. the aggregates over all data rates. Note that the 'composite' return values are aggregates over all carriers and data rates, i.e. no matter which data rate is specified, always the TOTal values are returned.
			:return: structure: for return value, see the help for ResultData structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('data_rate', data_rate, DataType.Enum, True))
		return self._core.io.query_struct(f'READ:EVDO:SIGNaling<Instance>:RXQuality:RLPFormance? {param}'.rstrip(), self.__class__.ResultData())

	def fetch(self, data_rate: enums.RevLinkPerDataRate = None) -> ResultData:
		"""SCPI: FETCh:EVDO:SIGNaling<instance>:RXQuality:RLPFormance \n
		Snippet: value: ResultData = driver.rxQuality.rlPerformance.fetch(data_rate = enums.RevLinkPerDataRate.R0K0) \n
		Returns the results of the 'Reverse Link Throughput' measurement for the specified data rate (and the selected carrier in
		multi-carrier scenarios) , see 'Reverse Link Throughput Measurement'. Preselect the related carrier using the method
		RsCmwEvdoSig.Configure.Carrier.setting command. The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
			:param data_rate: R0K0 | R19K2 | R38K4 | R76K8 | R115k2 | R153k6 | R230k4 | R307k2 | R460k8 | R614k4 | R921k6 | R1228k8 | R1843k2 | TOTal This query parameter specifies the data rate for which the results are returned, i.e. it selects a row in the 'Reverse Link Throughput' result table. If omitted, the TOTal values are returned, i.e. the aggregates over all data rates. Note that the 'composite' return values are aggregates over all carriers and data rates, i.e. no matter which data rate is specified, always the TOTal values are returned.
			:return: structure: for return value, see the help for ResultData structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('data_rate', data_rate, DataType.Enum, True))
		return self._core.io.query_struct(f'FETCh:EVDO:SIGNaling<Instance>:RXQuality:RLPFormance? {param}'.rstrip(), self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Packet_Size: str: The packet size given as string representations of the enum constants S128 | S256 | S512 | S1K | S2K | S3K | S4K | S5K | S6K | S7K | S8K | TOTal corresponding to the data rates in bit: 128, 256, 512, 1024, 2048, 3072, 4096, 5120, 6144, 7162, 8192.
			- Mac_Pack_Received: float: The number of MAC packets successfully received by the R&S CMW (on the selected carrier) . Range: 0 to 10E+3
			- Th_Vs_Test_Time: float: The average throughput in kbit/s (on the selected carrier) during the test time Range: 0 kbit/s to 99.99999E+3 kbit/s
			- Test_Time: float: The elapsed test time as the number of 26.67 ms CDMA frames. Range: 0 to 10E+3
			- All_Th_Vs_Test_Time: float: The average throughput in kbit/s (on the selected carrier) during the test time Range: 0 kbit/s to 99.99999E+3 kbit/s"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_str('Packet_Size'),
			ArgStruct.scalar_float('Mac_Pack_Received'),
			ArgStruct.scalar_float('Th_Vs_Test_Time'),
			ArgStruct.scalar_float('Test_Time'),
			ArgStruct.scalar_float('All_Th_Vs_Test_Time')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Packet_Size: str = None
			self.Mac_Pack_Received: float = None
			self.Th_Vs_Test_Time: float = None
			self.Test_Time: float = None
			self.All_Th_Vs_Test_Time: float = None

	def calculate(self, data_rate: enums.RevLinkPerDataRate = None) -> CalculateStruct:
		"""SCPI: CALCulate:EVDO:SIGNaling<instance>:RXQuality:RLPFormance \n
		Snippet: value: CalculateStruct = driver.rxQuality.rlPerformance.calculate(data_rate = enums.RevLinkPerDataRate.R0K0) \n
		Returns the results of the 'Reverse Link Throughput' measurement for the specified data rate (and the selected carrier in
		multi-carrier scenarios) , see 'Reverse Link Throughput Measurement'. Preselect the related carrier using the method
		RsCmwEvdoSig.Configure.Carrier.setting command. The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
			:param data_rate: R0K0 | R19K2 | R38K4 | R76K8 | R115k2 | R153k6 | R230k4 | R307k2 | R460k8 | R614k4 | R921k6 | R1228k8 | R1843k2 | TOTal This query parameter specifies the data rate for which the results are returned, i.e. it selects a row in the 'Reverse Link Throughput' result table. If omitted, the TOTal values are returned, i.e. the aggregates over all data rates. Note that the 'composite' return values are aggregates over all carriers and data rates, i.e. no matter which data rate is specified, always the TOTal values are returned.
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('data_rate', data_rate, DataType.Enum, True))
		return self._core.io.query_struct(f'CALCulate:EVDO:SIGNaling<Instance>:RXQuality:RLPFormance? {param}'.rstrip(), self.__class__.CalculateStruct())

	def clone(self) -> 'RlPerformance':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RlPerformance(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
