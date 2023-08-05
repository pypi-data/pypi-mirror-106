from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EftProtocol:
	"""EftProtocol commands group definition. 6 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("eftProtocol", core, parent)

	@property
	def drc(self):
		"""drc commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_drc'):
			from .EftProtocol_.Drc import Drc
			self._drc = Drc(self._core, self._base)
		return self._drc

	@property
	def dsc(self):
		"""dsc commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_dsc'):
			from .EftProtocol_.Dsc import Dsc
			self._dsc = Dsc(self._core, self._base)
		return self._dsc

	@property
	def ack(self):
		"""ack commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ack'):
			from .EftProtocol_.Ack import Ack
			self._ack = Ack(self._core, self._base)
		return self._ack

	def clone(self) -> 'EftProtocol':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EftProtocol(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
