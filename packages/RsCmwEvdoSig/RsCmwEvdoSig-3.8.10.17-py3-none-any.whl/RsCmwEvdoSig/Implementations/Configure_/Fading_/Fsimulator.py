from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fsimulator:
	"""Fsimulator commands group definition. 9 total commands, 3 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("fsimulator", core, parent)

	@property
	def globale(self):
		"""globale commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_globale'):
			from .Fsimulator_.Globale import Globale
			self._globale = Globale(self._core, self._base)
		return self._globale

	@property
	def restart(self):
		"""restart commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_restart'):
			from .Fsimulator_.Restart import Restart
			self._restart = Restart(self._core, self._base)
		return self._restart

	@property
	def iloss(self):
		"""iloss commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_iloss'):
			from .Fsimulator_.Iloss import Iloss
			self._iloss = Iloss(self._core, self._base)
		return self._iloss

	# noinspection PyTypeChecker
	def get_kconstant(self) -> enums.KeepConstant:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:FADing:FSIMulator:KCONstant \n
		Snippet: value: enums.KeepConstant = driver.configure.fading.fsimulator.get_kconstant() \n
		No command help available \n
			:return: keep_constant: No help available
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:FADing:FSIMulator:KCONstant?')
		return Conversions.str_to_scalar_enum(response, enums.KeepConstant)

	def set_kconstant(self, keep_constant: enums.KeepConstant) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:FADing:FSIMulator:KCONstant \n
		Snippet: driver.configure.fading.fsimulator.set_kconstant(keep_constant = enums.KeepConstant.DSHift) \n
		No command help available \n
			:param keep_constant: No help available
		"""
		param = Conversions.enum_scalar_to_str(keep_constant, enums.KeepConstant)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:FADing:FSIMulator:KCONstant {param}')

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:FADing:FSIMulator:ENABle \n
		Snippet: value: bool = driver.configure.fading.fsimulator.get_enable() \n
		Enables/disables the fading simulator. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:FADing:FSIMulator:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:FADing:FSIMulator:ENABle \n
		Snippet: driver.configure.fading.fsimulator.set_enable(enable = False) \n
		Enables/disables the fading simulator. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:FADing:FSIMulator:ENABle {param}')

	# noinspection PyTypeChecker
	def get_standard(self) -> enums.FsimStandard:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:FADing:FSIMulator:STANdard \n
		Snippet: value: enums.FsimStandard = driver.configure.fading.fsimulator.get_standard() \n
		Selects one of the propagation conditions defined in the table 6.4.1-1 of 3GPP2 C.S0032. \n
			:return: standard: P1 | P2 | P3 | P4 | P5 EVDO1 to EVDO5 P1: Two paths, speed 15 km/h (band classes 5, 11) , 8 km/h (other band classes) P2: One path, speed 3 km/h, exception: 6 km/h for band classes 5, 11 P3: One path, speed 30 km/h, exception: 58 km/h for band classes 5, 11 P4: Three paths, speed 100 km/h, exception: 192 km/h for band classes 5, 11 P5: Two paths, speed 0 km/h
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:FADing:FSIMulator:STANdard?')
		return Conversions.str_to_scalar_enum(response, enums.FsimStandard)

	def set_standard(self, standard: enums.FsimStandard) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:FADing:FSIMulator:STANdard \n
		Snippet: driver.configure.fading.fsimulator.set_standard(standard = enums.FsimStandard.P1) \n
		Selects one of the propagation conditions defined in the table 6.4.1-1 of 3GPP2 C.S0032. \n
			:param standard: P1 | P2 | P3 | P4 | P5 EVDO1 to EVDO5 P1: Two paths, speed 15 km/h (band classes 5, 11) , 8 km/h (other band classes) P2: One path, speed 3 km/h, exception: 6 km/h for band classes 5, 11 P3: One path, speed 30 km/h, exception: 58 km/h for band classes 5, 11 P4: Three paths, speed 100 km/h, exception: 192 km/h for band classes 5, 11 P5: Two paths, speed 0 km/h
		"""
		param = Conversions.enum_scalar_to_str(standard, enums.FsimStandard)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:FADing:FSIMulator:STANdard {param}')

	def clone(self) -> 'Fsimulator':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Fsimulator(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
