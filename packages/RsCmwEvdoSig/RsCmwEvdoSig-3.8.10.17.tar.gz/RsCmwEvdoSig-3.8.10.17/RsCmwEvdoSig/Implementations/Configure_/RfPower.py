from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfPower:
	"""RfPower commands group definition. 7 total commands, 2 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rfPower", core, parent)

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .RfPower_.Mode import Mode
			self._mode = Mode(self._core, self._base)
		return self._mode

	@property
	def level(self):
		"""level commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_level'):
			from .RfPower_.Level import Level
			self._level = Level(self._core, self._base)
		return self._level

	def get_evdo(self) -> float:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RFPower:EVDO \n
		Snippet: value: float = driver.configure.rfPower.get_evdo() \n
		Defines the absolute power of the generated forward 1xEV-DO signal, excluding a possible AWGN contribution. The allowed
		value range can be calculated as follows: Range (EVDOPower) = Range (Output Power) - External Attenuation - AWGNPower
		Range (Output Power) = -130 dBm to 0 dBm (RFx COM) or -120 dBm to 13 dBm (RFx OUT) ; please also notice the ranges quoted
		in the data sheet. \n
			:return: evdo_power: Range: see above , Unit: dBm
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:RFPower:EVDO?')
		return Conversions.str_to_float(response)

	def set_evdo(self, evdo_power: float) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RFPower:EVDO \n
		Snippet: driver.configure.rfPower.set_evdo(evdo_power = 1.0) \n
		Defines the absolute power of the generated forward 1xEV-DO signal, excluding a possible AWGN contribution. The allowed
		value range can be calculated as follows: Range (EVDOPower) = Range (Output Power) - External Attenuation - AWGNPower
		Range (Output Power) = -130 dBm to 0 dBm (RFx COM) or -120 dBm to 13 dBm (RFx OUT) ; please also notice the ranges quoted
		in the data sheet. \n
			:param evdo_power: Range: see above , Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(evdo_power)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:RFPower:EVDO {param}')

	def get_output(self) -> float:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RFPower:OUTPut \n
		Snippet: value: float = driver.configure.rfPower.get_output() \n
		Queries the output power at the selected RF output connector: the sum of the '1xEV-DO Power' (method RsCmwEvdoSig.
		Configure.RfPower.evdo) and the AWGN (method RsCmwEvdoSig.Configure.RfPower.Level.awgn) . The allowed value: Range
		(Output Power) = -130 dBm to 0 dBm (RFx COM) or -120 dBm to 13 dBm (RFx OUT) ; please also notice the ranges quoted in
		the data sheet. \n
			:return: output_power: Range: see above , Unit: dBm
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:RFPower:OUTPut?')
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	def get_epmode(self) -> enums.ExpPowerMode:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RFPower:EPMode \n
		Snippet: value: enums.ExpPowerMode = driver.configure.rfPower.get_epmode() \n
		Selects the algorithm which the tester uses to configure its input path. \n
			:return: exp_power_mode: MANual | OLRule | MAX | MIN | AUTO MANual: Manual setting, according to method RsCmwEvdoSig.Configure.RfPower.manual OLRule: According to open loop rule MAX: Maximum AT power MIN: Minimum AT power AUTO: Autoranging, according to received signal
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:RFPower:EPMode?')
		return Conversions.str_to_scalar_enum(response, enums.ExpPowerMode)

	def set_epmode(self, exp_power_mode: enums.ExpPowerMode) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RFPower:EPMode \n
		Snippet: driver.configure.rfPower.set_epmode(exp_power_mode = enums.ExpPowerMode.AUTO) \n
		Selects the algorithm which the tester uses to configure its input path. \n
			:param exp_power_mode: MANual | OLRule | MAX | MIN | AUTO MANual: Manual setting, according to method RsCmwEvdoSig.Configure.RfPower.manual OLRule: According to open loop rule MAX: Maximum AT power MIN: Minimum AT power AUTO: Autoranging, according to received signal
		"""
		param = Conversions.enum_scalar_to_str(exp_power_mode, enums.ExpPowerMode)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:RFPower:EPMode {param}')

	def get_manual(self) -> float:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RFPower:MANual \n
		Snippet: value: float = driver.configure.rfPower.get_manual() \n
		Defines the expected absolute input power at the input connector for 'Expected Power Mode' = 'Manual' (method
		RsCmwEvdoSig.Configure.RfPower.epmode MANual) . \n
			:return: manual_exp_power: Range: -47 dBm to 55 dBm, Unit: dBm
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:RFPower:MANual?')
		return Conversions.str_to_float(response)

	def set_manual(self, manual_exp_power: float) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RFPower:MANual \n
		Snippet: driver.configure.rfPower.set_manual(manual_exp_power = 1.0) \n
		Defines the expected absolute input power at the input connector for 'Expected Power Mode' = 'Manual' (method
		RsCmwEvdoSig.Configure.RfPower.epmode MANual) . \n
			:param manual_exp_power: Range: -47 dBm to 55 dBm, Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(manual_exp_power)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:RFPower:MANual {param}')

	def get_expected(self) -> float:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RFPower:EXPected \n
		Snippet: value: float = driver.configure.rfPower.get_expected() \n
		Queries the calculated value of the expected input power from the AT. The input power range is stated in the data sheet. \n
			:return: exp_nom_power: Unit: dBm
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:RFPower:EXPected?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'RfPower':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RfPower(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
