from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Network:
	"""Network commands group definition. 2 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("network", core, parent)

	@property
	def pilot(self):
		"""pilot commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pilot'):
			from .Network_.Pilot import Pilot
			self._pilot = Pilot(self._core, self._base)
		return self._pilot

	def clone(self) -> 'Network':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Network(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
