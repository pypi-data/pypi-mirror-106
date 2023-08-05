from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Limit:
	"""Limit commands group definition. 5 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("limit", core, parent)

	@property
	def per(self):
		"""per commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_per'):
			from .Limit_.Per import Per
			self._per = Per(self._core, self._base)
		return self._per

	@property
	def flPer(self):
		"""flPer commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_flPer'):
			from .Limit_.FlPer import FlPer
			self._flPer = FlPer(self._core, self._base)
		return self._flPer

	@property
	def rlPer(self):
		"""rlPer commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_rlPer'):
			from .Limit_.RlPer import RlPer
			self._rlPer = RlPer(self._core, self._base)
		return self._rlPer

	def clone(self) -> 'Limit':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Limit(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
