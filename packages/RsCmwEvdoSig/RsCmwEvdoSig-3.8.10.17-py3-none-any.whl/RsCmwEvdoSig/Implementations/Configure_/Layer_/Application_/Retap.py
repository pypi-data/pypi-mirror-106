from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Retap:
	"""Retap commands group definition. 5 total commands, 2 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("retap", core, parent)

	@property
	def smin(self):
		"""smin commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_smin'):
			from .Retap_.Smin import Smin
			self._smin = Smin(self._core, self._base)
		return self._smin

	@property
	def smax(self):
		"""smax commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_smax'):
			from .Retap_.Smax import Smax
			self._smax = Smax(self._core, self._base)
		return self._smax

	def get_ttarget(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:APPLication:RETap:TTARget \n
		Snippet: value: int = driver.configure.layer.application.retap.get_ttarget() \n
		No command help available \n
			:return: terminat_target: No help available
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:APPLication:RETap:TTARget?')
		return Conversions.str_to_int(response)

	def set_ttarget(self, terminat_target: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:APPLication:RETap:TTARget \n
		Snippet: driver.configure.layer.application.retap.set_ttarget(terminat_target = 1) \n
		No command help available \n
			:param terminat_target: No help available
		"""
		param = Conversions.decimal_value_to_str(terminat_target)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:LAYer:APPLication:RETap:TTARget {param}')

	def clone(self) -> 'Retap':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Retap(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
