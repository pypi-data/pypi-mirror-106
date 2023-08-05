from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class System:
	"""System commands group definition. 8 total commands, 1 Sub-groups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("system", core, parent)

	@property
	def ltOffset(self):
		"""ltOffset commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ltOffset'):
			from .System_.LtOffset import LtOffset
			self._ltOffset = LtOffset(self._core, self._base)
		return self._ltOffset

	# noinspection PyTypeChecker
	def get_tsource(self) -> enums.TimeSource:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:SYSTem:TSOurce \n
		Snippet: value: enums.TimeSource = driver.configure.system.get_tsource() \n
		Queries/sets the time source for the derivation of the CMDA system time. \n
			:return: source_time: CMWTime | DATE | SYNC CMWTime: CMW time (Windows time) DATE: Date and time as specified in method RsCmwEvdoSig.Configure.System.date and method RsCmwEvdoSig.Configure.System.time SYNC: Sync code
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:SYSTem:TSOurce?')
		return Conversions.str_to_scalar_enum(response, enums.TimeSource)

	def set_tsource(self, source_time: enums.TimeSource) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:SYSTem:TSOurce \n
		Snippet: driver.configure.system.set_tsource(source_time = enums.TimeSource.CMWTime) \n
		Queries/sets the time source for the derivation of the CMDA system time. \n
			:param source_time: CMWTime | DATE | SYNC CMWTime: CMW time (Windows time) DATE: Date and time as specified in method RsCmwEvdoSig.Configure.System.date and method RsCmwEvdoSig.Configure.System.time SYNC: Sync code
		"""
		param = Conversions.enum_scalar_to_str(source_time, enums.TimeSource)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:SYSTem:TSOurce {param}')

	# noinspection PyTypeChecker
	class DateStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Day: int: Range: 1 to 31
			- Month: int: Range: 1 to 12
			- Year: int: Range: 2011 to 9999"""
		__meta_args_list = [
			ArgStruct.scalar_int('Day'),
			ArgStruct.scalar_int('Month'),
			ArgStruct.scalar_int('Year')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Day: int = None
			self.Month: int = None
			self.Year: int = None

	def get_date(self) -> DateStruct:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:SYSTem:DATE \n
		Snippet: value: DateStruct = driver.configure.system.get_date() \n
		Date setting for CDMA system time source DATE (see method RsCmwEvdoSig.Configure.System.tsource) . \n
			:return: structure: for return value, see the help for DateStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:EVDO:SIGNaling<Instance>:SYSTem:DATE?', self.__class__.DateStruct())

	def set_date(self, value: DateStruct) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:SYSTem:DATE \n
		Snippet: driver.configure.system.set_date(value = DateStruct()) \n
		Date setting for CDMA system time source DATE (see method RsCmwEvdoSig.Configure.System.tsource) . \n
			:param value: see the help for DateStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:EVDO:SIGNaling<Instance>:SYSTem:DATE', value)

	# noinspection PyTypeChecker
	class TimeStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Hour: int: Range: 0 to 23
			- Minute: int: Range: 0 to 59
			- Second: int: Range: 0 to 59"""
		__meta_args_list = [
			ArgStruct.scalar_int('Hour'),
			ArgStruct.scalar_int('Minute'),
			ArgStruct.scalar_int('Second')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Hour: int = None
			self.Minute: int = None
			self.Second: int = None

	def get_time(self) -> TimeStruct:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:SYSTem:TIME \n
		Snippet: value: TimeStruct = driver.configure.system.get_time() \n
		Time setting for CDMA system time source 'Date / Time' (see method RsCmwEvdoSig.Configure.System.tsource) . \n
			:return: structure: for return value, see the help for TimeStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:EVDO:SIGNaling<Instance>:SYSTem:TIME?', self.__class__.TimeStruct())

	def set_time(self, value: TimeStruct) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:SYSTem:TIME \n
		Snippet: driver.configure.system.set_time(value = TimeStruct()) \n
		Time setting for CDMA system time source 'Date / Time' (see method RsCmwEvdoSig.Configure.System.tsource) . \n
			:param value: see the help for TimeStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:EVDO:SIGNaling<Instance>:SYSTem:TIME', value)

	def get_sync(self) -> str:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:SYSTem:SYNC \n
		Snippet: value: str = driver.configure.system.get_sync() \n
		Sets/queries the sync code. The sync code is required to synchronize the system time for 'Hybrid Mode on Two (or More)
		SUU': query the sync code generated by the 'synchronization master' (after SUU and set it on the 'synchronization slave'. \n
			:return: sync_code: No help available
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:SYSTem:SYNC?')
		return trim_str_response(response)

	def set_sync(self, sync_code: str) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:SYSTem:SYNC \n
		Snippet: driver.configure.system.set_sync(sync_code = r1) \n
		Sets/queries the sync code. The sync code is required to synchronize the system time for 'Hybrid Mode on Two (or More)
		SUU': query the sync code generated by the 'synchronization master' (after SUU and set it on the 'synchronization slave'. \n
			:param sync_code: No help available
		"""
		param = Conversions.value_to_str(sync_code)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:SYSTem:SYNC {param}')

	# noinspection PyTypeChecker
	def get_atime(self) -> enums.ApplyTimeAt:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:SYSTem:ATIMe \n
		Snippet: value: enums.ApplyTimeAt = driver.configure.system.get_atime() \n
		Defines when the configured time source (method RsCmwEvdoSig.Configure.System.tsource) is applied to the SUU hosting the
		signaling application. Note that this setting is performance critical because applying the time at signal ON takes 3 to 4
		seconds. \n
			:return: apply_time_at: SUSO | EVER | NEXT SUSO (signaling unit startup only) : the time setting is only applied when the SUU starts up EVER: the time setting is applied at every signal ON NEXT: the time setting is applied at next signal ON; note that after the next signal ON the R&S CMW switches back to SUSO
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:SYSTem:ATIMe?')
		return Conversions.str_to_scalar_enum(response, enums.ApplyTimeAt)

	def set_atime(self, apply_time_at: enums.ApplyTimeAt) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:SYSTem:ATIMe \n
		Snippet: driver.configure.system.set_atime(apply_time_at = enums.ApplyTimeAt.EVER) \n
		Defines when the configured time source (method RsCmwEvdoSig.Configure.System.tsource) is applied to the SUU hosting the
		signaling application. Note that this setting is performance critical because applying the time at signal ON takes 3 to 4
		seconds. \n
			:param apply_time_at: SUSO | EVER | NEXT SUSO (signaling unit startup only) : the time setting is only applied when the SUU starts up EVER: the time setting is applied at every signal ON NEXT: the time setting is applied at next signal ON; note that after the next signal ON the R&S CMW switches back to SUSO
		"""
		param = Conversions.enum_scalar_to_str(apply_time_at, enums.ApplyTimeAt)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:SYSTem:ATIMe {param}')

	def get_lseconds(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:SYSTem:LSEConds \n
		Snippet: value: int = driver.configure.system.get_lseconds() \n
		Adjusts track of leap second correction to UTC. \n
			:return: leap_seconds: Correction to the solar time Range: 0 to 255, Unit: s
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:SYSTem:LSEConds?')
		return Conversions.str_to_int(response)

	def set_lseconds(self, leap_seconds: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:SYSTem:LSEConds \n
		Snippet: driver.configure.system.set_lseconds(leap_seconds = 1) \n
		Adjusts track of leap second correction to UTC. \n
			:param leap_seconds: Correction to the solar time Range: 0 to 255, Unit: s
		"""
		param = Conversions.decimal_value_to_str(leap_seconds)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:SYSTem:LSEConds {param}')

	def clone(self) -> 'System':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = System(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
