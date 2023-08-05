from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fmctap:
	"""Fmctap commands group definition. 8 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("fmctap", core, parent)

	@property
	def drc(self):
		"""drc commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_drc'):
			from .Fmctap_.Drc import Drc
			self._drc = Drc(self._core, self._base)
		return self._drc

	@property
	def lback(self):
		"""lback commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lback'):
			from .Fmctap_.Lback import Lback
			self._lback = Lback(self._core, self._base)
		return self._lback

	@property
	def ack(self):
		"""ack commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ack'):
			from .Fmctap_.Ack import Ack
			self._ack = Ack(self._core, self._base)
		return self._ack

	def clone(self) -> 'Fmctap':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Fmctap(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
