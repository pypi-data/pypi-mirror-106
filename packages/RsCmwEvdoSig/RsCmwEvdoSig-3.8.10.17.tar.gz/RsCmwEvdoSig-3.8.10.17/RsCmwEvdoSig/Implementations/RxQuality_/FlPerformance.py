from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.Types import DataType
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ...Internal.ArgSingleList import ArgSingleList
from ...Internal.ArgSingle import ArgSingle
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FlPerformance:
	"""FlPerformance commands group definition. 5 total commands, 2 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("flPerformance", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .FlPerformance_.State import State
			self._state = State(self._core, self._base)
		return self._state

	@property
	def cstate(self):
		"""cstate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cstate'):
			from .FlPerformance_.Cstate import Cstate
			self._cstate = Cstate(self._core, self._base)
		return self._cstate

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Mac_Pack_Received: int: MAC packets received Range: 0 or higher
			- Phy_Packet_Slots: int: Physical packet slots Range: 0 or higher
			- Th_Vs_Test_Time: float: Throughput vs. test time Range: 0 kbit/s or higher
			- Th_Vs_Transm_Slots: float: Throughput vs. transmitted slots Range: 0 kbit/s or higher
			- Test_Time: int: Test time Range: 0 to 10000, Unit: no. of CDMA frames
			- All_Th_Vs_Test_Time: float: No parameter help available
			- All_Th_Vs_Tra_Slots: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Mac_Pack_Received'),
			ArgStruct.scalar_int('Phy_Packet_Slots'),
			ArgStruct.scalar_float('Th_Vs_Test_Time'),
			ArgStruct.scalar_float('Th_Vs_Transm_Slots'),
			ArgStruct.scalar_int('Test_Time'),
			ArgStruct.scalar_float('All_Th_Vs_Test_Time'),
			ArgStruct.scalar_float('All_Th_Vs_Tra_Slots')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Mac_Pack_Received: int = None
			self.Phy_Packet_Slots: int = None
			self.Th_Vs_Test_Time: float = None
			self.Th_Vs_Transm_Slots: float = None
			self.Test_Time: int = None
			self.All_Th_Vs_Test_Time: float = None
			self.All_Th_Vs_Tra_Slots: float = None

	def read(self, packet_size: enums.PacketSize = None) -> ResultData:
		"""SCPI: READ:EVDO:SIGNaling<instance>:RXQuality:FLPFormance \n
		Snippet: value: ResultData = driver.rxQuality.flPerformance.read(packet_size = enums.PacketSize.S128) \n
		Returns the results of the 'Forward Link Throughput' measurement for the specified packet size (and the selected carrier
		in multi-carrier scenarios) , see 'Forward Link Throughput Measurement'. Preselect the related carrier using the method
		RsCmwEvdoSig.Configure.Carrier.setting command. The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
			:param packet_size: S128 | S256 | S512 | S1K | S2K | S3K | S4K | S5K | S6K | S7K | S8K | TOTal In bit: 128, 256, 512, 1024, 2048, 3072, 4096, 5120, 6144, 7162, 8192 This query parameter represents the physical layer packet size for which the results are returned, i.e. it selects a row in the 'Forward Link Throughput' result table. If this parameter is omitted, the command returns the TOTal results, i.e. the aggregates over all packet sizes. Note that the 'composite' return values are aggregates over all carriers and packet sizes, i.e. no matter which packet size is specified, always the TOTal values are returned.
			:return: structure: for return value, see the help for ResultData structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('packet_size', packet_size, DataType.Enum, True))
		return self._core.io.query_struct(f'READ:EVDO:SIGNaling<Instance>:RXQuality:FLPFormance? {param}'.rstrip(), self.__class__.ResultData())

	def fetch(self, packet_size: enums.PacketSize = None) -> ResultData:
		"""SCPI: FETCh:EVDO:SIGNaling<instance>:RXQuality:FLPFormance \n
		Snippet: value: ResultData = driver.rxQuality.flPerformance.fetch(packet_size = enums.PacketSize.S128) \n
		Returns the results of the 'Forward Link Throughput' measurement for the specified packet size (and the selected carrier
		in multi-carrier scenarios) , see 'Forward Link Throughput Measurement'. Preselect the related carrier using the method
		RsCmwEvdoSig.Configure.Carrier.setting command. The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
			:param packet_size: S128 | S256 | S512 | S1K | S2K | S3K | S4K | S5K | S6K | S7K | S8K | TOTal In bit: 128, 256, 512, 1024, 2048, 3072, 4096, 5120, 6144, 7162, 8192 This query parameter represents the physical layer packet size for which the results are returned, i.e. it selects a row in the 'Forward Link Throughput' result table. If this parameter is omitted, the command returns the TOTal results, i.e. the aggregates over all packet sizes. Note that the 'composite' return values are aggregates over all carriers and packet sizes, i.e. no matter which packet size is specified, always the TOTal values are returned.
			:return: structure: for return value, see the help for ResultData structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('packet_size', packet_size, DataType.Enum, True))
		return self._core.io.query_struct(f'FETCh:EVDO:SIGNaling<Instance>:RXQuality:FLPFormance? {param}'.rstrip(), self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Mac_Pack_Received: float: MAC packets received Range: 0 or higher
			- Phy_Packet_Slots: float: Physical packet slots Range: 0 or higher
			- Th_Vs_Test_Time: float: Throughput vs. test time Range: 0 kbit/s or higher
			- Th_Vs_Transm_Slots: float: Throughput vs. transmitted slots Range: 0 kbit/s or higher
			- Test_Time: float: Test time Range: 0 to 10000, Unit: no. of CDMA frames
			- All_Th_Vs_Test_Time: float: No parameter help available
			- All_Th_Vs_Tra_Slots: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Mac_Pack_Received'),
			ArgStruct.scalar_float('Phy_Packet_Slots'),
			ArgStruct.scalar_float('Th_Vs_Test_Time'),
			ArgStruct.scalar_float('Th_Vs_Transm_Slots'),
			ArgStruct.scalar_float('Test_Time'),
			ArgStruct.scalar_float('All_Th_Vs_Test_Time'),
			ArgStruct.scalar_float('All_Th_Vs_Tra_Slots')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Mac_Pack_Received: float = None
			self.Phy_Packet_Slots: float = None
			self.Th_Vs_Test_Time: float = None
			self.Th_Vs_Transm_Slots: float = None
			self.Test_Time: float = None
			self.All_Th_Vs_Test_Time: float = None
			self.All_Th_Vs_Tra_Slots: float = None

	def calculate(self, packet_size: enums.PacketSize = None) -> CalculateStruct:
		"""SCPI: CALCulate:EVDO:SIGNaling<instance>:RXQuality:FLPFormance \n
		Snippet: value: CalculateStruct = driver.rxQuality.flPerformance.calculate(packet_size = enums.PacketSize.S128) \n
		Returns the results of the 'Forward Link Throughput' measurement for the specified packet size (and the selected carrier
		in multi-carrier scenarios) , see 'Forward Link Throughput Measurement'. Preselect the related carrier using the method
		RsCmwEvdoSig.Configure.Carrier.setting command. The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
			:param packet_size: S128 | S256 | S512 | S1K | S2K | S3K | S4K | S5K | S6K | S7K | S8K | TOTal In bit: 128, 256, 512, 1024, 2048, 3072, 4096, 5120, 6144, 7162, 8192 This query parameter represents the physical layer packet size for which the results are returned, i.e. it selects a row in the 'Forward Link Throughput' result table. If this parameter is omitted, the command returns the TOTal results, i.e. the aggregates over all packet sizes. Note that the 'composite' return values are aggregates over all carriers and packet sizes, i.e. no matter which packet size is specified, always the TOTal values are returned.
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('packet_size', packet_size, DataType.Enum, True))
		return self._core.io.query_struct(f'CALCulate:EVDO:SIGNaling<Instance>:RXQuality:FLPFormance? {param}'.rstrip(), self.__class__.CalculateStruct())

	def clone(self) -> 'FlPerformance':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FlPerformance(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
