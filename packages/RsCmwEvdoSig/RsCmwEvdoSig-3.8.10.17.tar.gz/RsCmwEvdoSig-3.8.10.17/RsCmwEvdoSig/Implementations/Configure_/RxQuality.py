from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RxQuality:
	"""RxQuality commands group definition. 24 total commands, 10 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rxQuality", core, parent)

	@property
	def carrier(self):
		"""carrier commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_carrier'):
			from .RxQuality_.Carrier import Carrier
			self._carrier = Carrier(self._core, self._base)
		return self._carrier

	@property
	def rstatistics(self):
		"""rstatistics commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rstatistics'):
			from .RxQuality_.Rstatistics import Rstatistics
			self._rstatistics = Rstatistics(self._core, self._base)
		return self._rstatistics

	@property
	def per(self):
		"""per commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_per'):
			from .RxQuality_.Per import Per
			self._per = Per(self._core, self._base)
		return self._per

	@property
	def flPer(self):
		"""flPer commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_flPer'):
			from .RxQuality_.FlPer import FlPer
			self._flPer = FlPer(self._core, self._base)
		return self._flPer

	@property
	def rlPer(self):
		"""rlPer commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_rlPer'):
			from .RxQuality_.RlPer import RlPer
			self._rlPer = RlPer(self._core, self._base)
		return self._rlPer

	@property
	def throughput(self):
		"""throughput commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_throughput'):
			from .RxQuality_.Throughput import Throughput
			self._throughput = Throughput(self._core, self._base)
		return self._throughput

	@property
	def flPerformance(self):
		"""flPerformance commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_flPerformance'):
			from .RxQuality_.FlPerformance import FlPerformance
			self._flPerformance = FlPerformance(self._core, self._base)
		return self._flPerformance

	@property
	def rlPerformance(self):
		"""rlPerformance commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rlPerformance'):
			from .RxQuality_.RlPerformance import RlPerformance
			self._rlPerformance = RlPerformance(self._core, self._base)
		return self._rlPerformance

	@property
	def result(self):
		"""result commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_result'):
			from .RxQuality_.Result import Result
			self._result = Result(self._core, self._base)
		return self._result

	@property
	def limit(self):
		"""limit commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_limit'):
			from .RxQuality_.Limit import Limit
			self._limit = Limit(self._core, self._base)
		return self._limit

	def get_uperiod(self) -> float:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:UPERiod \n
		Snippet: value: float = driver.configure.rxQuality.get_uperiod() \n
		Defines the time interval after which the R&S CMW evaluates and displays a new set of measurement results. \n
			:return: update_period: Range: 0.25 s to 2 s, Unit: s
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:RXQuality:UPERiod?')
		return Conversions.str_to_float(response)

	def set_uperiod(self, update_period: float) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:UPERiod \n
		Snippet: driver.configure.rxQuality.set_uperiod(update_period = 1.0) \n
		Defines the time interval after which the R&S CMW evaluates and displays a new set of measurement results. \n
			:param update_period: Range: 0.25 s to 2 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(update_period)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:RXQuality:UPERiod {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.rxQuality.get_repetition() \n
		No command help available \n
			:return: repetition: No help available
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:RXQuality:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:REPetition \n
		Snippet: driver.configure.rxQuality.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		No command help available \n
			:param repetition: No help available
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:RXQuality:REPetition {param}')

	def clone(self) -> 'RxQuality':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RxQuality(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
