from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rmctap:
	"""Rmctap commands group definition. 4 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rmctap", core, parent)

	@property
	def smin(self):
		"""smin commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_smin'):
			from .Rmctap_.Smin import Smin
			self._smin = Smin(self._core, self._base)
		return self._smin

	@property
	def smax(self):
		"""smax commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_smax'):
			from .Rmctap_.Smax import Smax
			self._smax = Smax(self._core, self._base)
		return self._smax

	def clone(self) -> 'Rmctap':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rmctap(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
