from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LtOffset:
	"""LtOffset commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ltOffset", core, parent)

	def get_hex(self) -> str:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:SYSTem:LTOFfset:HEX \n
		Snippet: value: str = driver.configure.system.ltOffset.get_hex() \n
		Displays time offset from UTC in hexadecimal format according to the local time zone. \n
			:return: local_time_off_hex: LocalTimeOffset = (sign(h) *(abs(h) *60+m) ) AND ((1UL11) -1) Range: #H000 to #HFFF
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:SYSTem:LTOFfset:HEX?')
		return trim_str_response(response)

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Sign: enums.SlopeType: NEGative | POSitive Position related to meridian NEGative: west from meridian POSitive: east from meridian
			- Hour: int: Difference from UTC Range: 00 to 17, Unit: hour
			- Minute: int: Difference from UTC Range: 00 to 59, Unit: min"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Sign', enums.SlopeType),
			ArgStruct.scalar_int('Hour'),
			ArgStruct.scalar_int('Minute')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Sign: enums.SlopeType = None
			self.Hour: int = None
			self.Minute: int = None

	# noinspection PyTypeChecker
	def get_value(self) -> ValueStruct:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:SYSTem:LTOFfset \n
		Snippet: value: ValueStruct = driver.configure.system.ltOffset.get_value() \n
		Defines the time offset from UTC according to the local time zone. Possible range is from -17:04 to +17:03 \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:EVDO:SIGNaling<Instance>:SYSTem:LTOFfset?', self.__class__.ValueStruct())

	def set_value(self, value: ValueStruct) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:SYSTem:LTOFfset \n
		Snippet: driver.configure.system.ltOffset.set_value(value = ValueStruct()) \n
		Defines the time offset from UTC according to the local time zone. Possible range is from -17:04 to +17:03 \n
			:param value: see the help for ValueStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:EVDO:SIGNaling<Instance>:SYSTem:LTOFfset', value)
