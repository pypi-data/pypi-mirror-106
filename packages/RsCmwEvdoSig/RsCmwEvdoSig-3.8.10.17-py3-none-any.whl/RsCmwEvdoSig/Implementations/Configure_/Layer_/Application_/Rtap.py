from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rtap:
	"""Rtap commands group definition. 4 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rtap", core, parent)

	@property
	def rmin(self):
		"""rmin commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_rmin'):
			from .Rtap_.Rmin import Rmin
			self._rmin = Rmin(self._core, self._base)
		return self._rmin

	@property
	def rmax(self):
		"""rmax commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_rmax'):
			from .Rtap_.Rmax import Rmax
			self._rmax = Rmax(self._core, self._base)
		return self._rmax

	def clone(self) -> 'Rtap':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rtap(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
