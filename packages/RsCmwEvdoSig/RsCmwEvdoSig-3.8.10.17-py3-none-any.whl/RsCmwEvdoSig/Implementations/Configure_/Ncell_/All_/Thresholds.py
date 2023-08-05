from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Thresholds:
	"""Thresholds commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("thresholds", core, parent)

	# noinspection PyTypeChecker
	class LowStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Valid: bool: No parameter help available
			- Low: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Valid'),
			ArgStruct.scalar_int('Low')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Valid: bool = None
			self.Low: int = None

	def get_low(self) -> LowStruct:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NCELl:ALL:THResholds:LOW \n
		Snippet: value: LowStruct = driver.configure.ncell.all.thresholds.get_low() \n
		No command help available \n
			:return: structure: for return value, see the help for LowStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:EVDO:SIGNaling<Instance>:NCELl:ALL:THResholds:LOW?', self.__class__.LowStruct())

	def set_low(self, value: LowStruct) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NCELl:ALL:THResholds:LOW \n
		Snippet: driver.configure.ncell.all.thresholds.set_low(value = LowStruct()) \n
		No command help available \n
			:param value: see the help for LowStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:EVDO:SIGNaling<Instance>:NCELl:ALL:THResholds:LOW', value)

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Valid: bool: No parameter help available
			- High: int: No parameter help available
			- Low: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Valid'),
			ArgStruct.scalar_int('High'),
			ArgStruct.scalar_int('Low')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Valid: bool = None
			self.High: int = None
			self.Low: int = None

	def get_value(self) -> ValueStruct:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NCELl:ALL:THResholds \n
		Snippet: value: ValueStruct = driver.configure.ncell.all.thresholds.get_value() \n
		No command help available \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:EVDO:SIGNaling<Instance>:NCELl:ALL:THResholds?', self.__class__.ValueStruct())

	def set_value(self, value: ValueStruct) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NCELl:ALL:THResholds \n
		Snippet: driver.configure.ncell.all.thresholds.set_value(value = ValueStruct()) \n
		No command help available \n
			:param value: see the help for ValueStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:EVDO:SIGNaling<Instance>:NCELl:ALL:THResholds', value)
