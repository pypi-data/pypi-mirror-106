from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sense:
	"""Sense commands group definition. 13 total commands, 6 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sense", core, parent)

	@property
	def test(self):
		"""test commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_test'):
			from .Sense_.Test import Test
			self._test = Test(self._core, self._base)
		return self._test

	@property
	def iqOut(self):
		"""iqOut commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqOut'):
			from .Sense_.IqOut import IqOut
			self._iqOut = IqOut(self._core, self._base)
		return self._iqOut

	@property
	def anAddress(self):
		"""anAddress commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_anAddress'):
			from .Sense_.AnAddress import AnAddress
			self._anAddress = AnAddress(self._core, self._base)
		return self._anAddress

	@property
	def atAddress(self):
		"""atAddress commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_atAddress'):
			from .Sense_.AtAddress import AtAddress
			self._atAddress = AtAddress(self._core, self._base)
		return self._atAddress

	@property
	def rxQuality(self):
		"""rxQuality commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rxQuality'):
			from .Sense_.RxQuality import RxQuality
			self._rxQuality = RxQuality(self._core, self._base)
		return self._rxQuality

	@property
	def elog(self):
		"""elog commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_elog'):
			from .Sense_.Elog import Elog
			self._elog = Elog(self._core, self._base)
		return self._elog

	def clone(self) -> 'Sense':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sense(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
