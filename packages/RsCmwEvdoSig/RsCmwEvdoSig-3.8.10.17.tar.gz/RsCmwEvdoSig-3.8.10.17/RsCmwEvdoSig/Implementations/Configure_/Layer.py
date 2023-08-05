from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Layer:
	"""Layer commands group definition. 61 total commands, 4 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("layer", core, parent)

	@property
	def connection(self):
		"""connection commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_connection'):
			from .Layer_.Connection import Connection
			self._connection = Connection(self._core, self._base)
		return self._connection

	@property
	def application(self):
		"""application commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_application'):
			from .Layer_.Application import Application
			self._application = Application(self._core, self._base)
		return self._application

	@property
	def mac(self):
		"""mac commands group. 3 Sub-classes, 6 commands."""
		if not hasattr(self, '_mac'):
			from .Layer_.Mac import Mac
			self._mac = Mac(self._core, self._base)
		return self._mac

	@property
	def session(self):
		"""session commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_session'):
			from .Layer_.Session import Session
			self._session = Session(self._core, self._base)
		return self._session

	def clone(self) -> 'Layer':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Layer(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
