from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FlPer:
	"""FlPer commands group definition. 5 total commands, 2 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("flPer", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .FlPer_.State import State
			self._state = State(self._core, self._base)
		return self._state

	@property
	def cstate(self):
		"""cstate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cstate'):
			from .FlPer_.Cstate import Cstate
			self._cstate = Cstate(self._core, self._base)
		return self._cstate

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Per: float: Current forward link packet error rate (for the selected carrier) Range: 0 % to 100 %, Unit: %
			- Confidence_Level: float: Confidence level (for the selected carrier) Range: 0 % to 100 %, Unit: %
			- Packet_Errors: int: Number of detected packet errors (for the selected carrier) Range: 0 to 100E+3
			- Test_Packets_Sent: int: Packets sent (on the selected carrier) Range: 0 to 100E+3
			- Total_Per: float: No parameter help available
			- Total_Conf_Level: float: No parameter help available
			- Total_Pack_Errors: int: No parameter help available
			- Total_Test_Psent: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Per'),
			ArgStruct.scalar_float('Confidence_Level'),
			ArgStruct.scalar_int('Packet_Errors'),
			ArgStruct.scalar_int('Test_Packets_Sent'),
			ArgStruct.scalar_float('Total_Per'),
			ArgStruct.scalar_float('Total_Conf_Level'),
			ArgStruct.scalar_int('Total_Pack_Errors'),
			ArgStruct.scalar_int('Total_Test_Psent')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Per: float = None
			self.Confidence_Level: float = None
			self.Packet_Errors: int = None
			self.Test_Packets_Sent: int = None
			self.Total_Per: float = None
			self.Total_Conf_Level: float = None
			self.Total_Pack_Errors: int = None
			self.Total_Test_Psent: int = None

	def read(self) -> ResultData:
		"""SCPI: READ:EVDO:SIGNaling<instance>:RXQuality:FLPer \n
		Snippet: value: ResultData = driver.rxQuality.flPer.read() \n
		Returns the results of the 'Forward Link PER' measurement (for the selected carrier) , see 'Forward Link Packet Error
		Rate Measurement'. Preselect the related carrier using the method RsCmwEvdoSig.Configure.Carrier.setting command.
		The values described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead,
		one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:EVDO:SIGNaling<Instance>:RXQuality:FLPer?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:EVDO:SIGNaling<instance>:RXQuality:FLPer \n
		Snippet: value: ResultData = driver.rxQuality.flPer.fetch() \n
		Returns the results of the 'Forward Link PER' measurement (for the selected carrier) , see 'Forward Link Packet Error
		Rate Measurement'. Preselect the related carrier using the method RsCmwEvdoSig.Configure.Carrier.setting command.
		The values described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead,
		one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:EVDO:SIGNaling<Instance>:RXQuality:FLPer?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: See 'Reliability Indicator'
			- Per: float: Current forward link packet error rate (for the selected carrier) Range: 0 % to 100 %, Unit: %
			- Confidence_Level: float: Confidence level (for the selected carrier) Range: 0 % to 100 %, Unit: %
			- Packet_Errors: float: Number of detected packet errors (for the selected carrier) Range: 0 to 100E+3
			- Test_Packets_Sent: float: Packets sent (on the selected carrier) Range: 0 to 100E+3
			- Total_Per: float: No parameter help available
			- Total_Conf_Level: float: No parameter help available
			- Total_Pack_Errors: float: No parameter help available
			- Total_Test_Psent: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Per'),
			ArgStruct.scalar_float('Confidence_Level'),
			ArgStruct.scalar_float('Packet_Errors'),
			ArgStruct.scalar_float('Test_Packets_Sent'),
			ArgStruct.scalar_float('Total_Per'),
			ArgStruct.scalar_float('Total_Conf_Level'),
			ArgStruct.scalar_float('Total_Pack_Errors'),
			ArgStruct.scalar_float('Total_Test_Psent')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Per: float = None
			self.Confidence_Level: float = None
			self.Packet_Errors: float = None
			self.Test_Packets_Sent: float = None
			self.Total_Per: float = None
			self.Total_Conf_Level: float = None
			self.Total_Pack_Errors: float = None
			self.Total_Test_Psent: float = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:EVDO:SIGNaling<instance>:RXQuality:FLPer \n
		Snippet: value: CalculateStruct = driver.rxQuality.flPer.calculate() \n
		Returns the results of the 'Forward Link PER' measurement (for the selected carrier) , see 'Forward Link Packet Error
		Rate Measurement'. Preselect the related carrier using the method RsCmwEvdoSig.Configure.Carrier.setting command.
		The values described below are returned by FETCh and READ commands. CALCulate commands return limit check results instead,
		one value for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:EVDO:SIGNaling<Instance>:RXQuality:FLPer?', self.__class__.CalculateStruct())

	def clone(self) -> 'FlPer':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FlPer(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
