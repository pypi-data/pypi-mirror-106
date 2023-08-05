from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Application:
	"""Application commands group definition. 36 total commands, 7 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("application", core, parent)

	@property
	def fmctap(self):
		"""fmctap commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_fmctap'):
			from .Application_.Fmctap import Fmctap
			self._fmctap = Fmctap(self._core, self._base)
		return self._fmctap

	@property
	def rmctap(self):
		"""rmctap commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_rmctap'):
			from .Application_.Rmctap import Rmctap
			self._rmctap = Rmctap(self._core, self._base)
		return self._rmctap

	@property
	def ftap(self):
		"""ftap commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ftap'):
			from .Application_.Ftap import Ftap
			self._ftap = Ftap(self._core, self._base)
		return self._ftap

	@property
	def rtap(self):
		"""rtap commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_rtap'):
			from .Application_.Rtap import Rtap
			self._rtap = Rtap(self._core, self._base)
		return self._rtap

	@property
	def fetap(self):
		"""fetap commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_fetap'):
			from .Application_.Fetap import Fetap
			self._fetap = Fetap(self._core, self._base)
		return self._fetap

	@property
	def retap(self):
		"""retap commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_retap'):
			from .Application_.Retap import Retap
			self._retap = Retap(self._core, self._base)
		return self._retap

	@property
	def packet(self):
		"""packet commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_packet'):
			from .Application_.Packet import Packet
			self._packet = Packet(self._core, self._base)
		return self._packet

	def clone(self) -> 'Application':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Application(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
