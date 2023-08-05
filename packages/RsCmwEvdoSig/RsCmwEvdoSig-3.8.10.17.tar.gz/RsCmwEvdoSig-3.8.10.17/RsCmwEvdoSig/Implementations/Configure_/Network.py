from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Network:
	"""Network commands group definition. 30 total commands, 5 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("network", core, parent)

	@property
	def sector(self):
		"""sector commands group. 1 Sub-classes, 7 commands."""
		if not hasattr(self, '_sector'):
			from .Network_.Sector import Sector
			self._sector = Sector(self._core, self._base)
		return self._sector

	@property
	def pilot(self):
		"""pilot commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pilot'):
			from .Network_.Pilot import Pilot
			self._pilot = Pilot(self._core, self._base)
		return self._pilot

	@property
	def propertyPy(self):
		"""propertyPy commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_propertyPy'):
			from .Network_.PropertyPy import PropertyPy
			self._propertyPy = PropertyPy(self._core, self._base)
		return self._propertyPy

	@property
	def aprobes(self):
		"""aprobes commands group. 0 Sub-classes, 9 commands."""
		if not hasattr(self, '_aprobes'):
			from .Network_.Aprobes import Aprobes
			self._aprobes = Aprobes(self._core, self._base)
		return self._aprobes

	@property
	def security(self):
		"""security commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_security'):
			from .Network_.Security import Security
			self._security = Security(self._core, self._base)
		return self._security

	def get_sid(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:SID \n
		Snippet: value: int = driver.configure.network.get_sid() \n
		Defines the 15-bit system ID that the R&S CMW broadcasts on its forward 1xEV-DO signal \n
			:return: system_id: Range: 0 to 32767 (2^15 - 1)
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:NETWork:SID?')
		return Conversions.str_to_int(response)

	def set_sid(self, system_id: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:SID \n
		Snippet: driver.configure.network.set_sid(system_id = 1) \n
		Defines the 15-bit system ID that the R&S CMW broadcasts on its forward 1xEV-DO signal \n
			:param system_id: Range: 0 to 32767 (2^15 - 1)
		"""
		param = Conversions.decimal_value_to_str(system_id)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:NETWork:SID {param}')

	# noinspection PyTypeChecker
	def get_release(self) -> enums.NetworkRelease:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:RELease \n
		Snippet: value: enums.NetworkRelease = driver.configure.network.get_release() \n
		Selects the network release for the signaling tests. \n
			:return: release: R0 | RA | RB Release 0, A or B
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:NETWork:RELease?')
		return Conversions.str_to_scalar_enum(response, enums.NetworkRelease)

	def set_release(self, release: enums.NetworkRelease) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:RELease \n
		Snippet: driver.configure.network.set_release(release = enums.NetworkRelease.R0) \n
		Selects the network release for the signaling tests. \n
			:param release: R0 | RA | RB Release 0, A or B
		"""
		param = Conversions.enum_scalar_to_str(release, enums.NetworkRelease)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:NETWork:RELease {param}')

	def clone(self) -> 'Network':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Network(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
