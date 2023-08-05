from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DftProtocol:
	"""DftProtocol commands group definition. 4 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dftProtocol", core, parent)

	@property
	def drc(self):
		"""drc commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_drc'):
			from .DftProtocol_.Drc import Drc
			self._drc = Drc(self._core, self._base)
		return self._drc

	@property
	def ack(self):
		"""ack commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ack'):
			from .DftProtocol_.Ack import Ack
			self._ack = Ack(self._core, self._base)
		return self._ack

	def clone(self) -> 'DftProtocol':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DftProtocol(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
