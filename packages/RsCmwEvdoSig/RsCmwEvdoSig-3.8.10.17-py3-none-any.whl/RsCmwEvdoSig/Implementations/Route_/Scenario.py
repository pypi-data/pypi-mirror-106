from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scenario:
	"""Scenario commands group definition. 8 total commands, 2 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("scenario", core, parent)

	@property
	def scFading(self):
		"""scFading commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_scFading'):
			from .Scenario_.ScFading import ScFading
			self._scFading = ScFading(self._core, self._base)
		return self._scFading

	@property
	def hmFading(self):
		"""hmFading commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_hmFading'):
			from .Scenario_.HmFading import HmFading
			self._hmFading = HmFading(self._core, self._base)
		return self._hmFading

	# noinspection PyTypeChecker
	class ScellStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rx_Connector: enums.RxConnector: RF connector for the input path
			- Rx_Converter: enums.RxConverter: RX module for the input path
			- Tx_Connector: enums.TxConnector: RF connector for the output path
			- Tx_Converter: enums.TxConverter: TX module for the output path"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Rx_Connector', enums.RxConnector),
			ArgStruct.scalar_enum('Rx_Converter', enums.RxConverter),
			ArgStruct.scalar_enum('Tx_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_Converter', enums.TxConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx_Connector: enums.RxConnector = None
			self.Rx_Converter: enums.RxConverter = None
			self.Tx_Connector: enums.TxConnector = None
			self.Tx_Converter: enums.TxConverter = None

	# noinspection PyTypeChecker
	def get_scell(self) -> ScellStruct:
		"""SCPI: ROUTe:EVDO:SIGNaling<instance>:SCENario:SCELl \n
		Snippet: value: ScellStruct = driver.route.scenario.get_scell() \n
		Activates the standalone scenario and selects the signal paths. For possible connector and converter values, see 'Values
		for Signal Path Selection'. \n
			:return: structure: for return value, see the help for ScellStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:EVDO:SIGNaling<Instance>:SCENario:SCELl?', self.__class__.ScellStruct())

	def set_scell(self, value: ScellStruct) -> None:
		"""SCPI: ROUTe:EVDO:SIGNaling<instance>:SCENario:SCELl \n
		Snippet: driver.route.scenario.set_scell(value = ScellStruct()) \n
		Activates the standalone scenario and selects the signal paths. For possible connector and converter values, see 'Values
		for Signal Path Selection'. \n
			:param value: see the help for ScellStruct structure arguments.
		"""
		self._core.io.write_struct('ROUTe:EVDO:SIGNaling<Instance>:SCENario:SCELl', value)

	# noinspection PyTypeChecker
	class HmodeStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rx_Connector: enums.RxConnector: RF connector for the input path
			- Rx_Converter: enums.RxConverter: RX module for the input path
			- Tx_Connector: enums.TxConnector: RF connector for the output path
			- Tx_Converter: enums.TxConverter: TX module for the output path"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Rx_Connector', enums.RxConnector),
			ArgStruct.scalar_enum('Rx_Converter', enums.RxConverter),
			ArgStruct.scalar_enum('Tx_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_Converter', enums.TxConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx_Connector: enums.RxConnector = None
			self.Rx_Converter: enums.RxConverter = None
			self.Tx_Connector: enums.TxConnector = None
			self.Tx_Converter: enums.TxConverter = None

	# noinspection PyTypeChecker
	def get_hmode(self) -> HmodeStruct:
		"""SCPI: ROUTe:EVDO:SIGNaling<instance>:SCENario:HMODe \n
		Snippet: value: HmodeStruct = driver.route.scenario.get_hmode() \n
		Activates the hybrid mode scenario and selects the signal paths. For possible connector and converter values, see 'Values
		for Signal Path Selection'. \n
			:return: structure: for return value, see the help for HmodeStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:EVDO:SIGNaling<Instance>:SCENario:HMODe?', self.__class__.HmodeStruct())

	def set_hmode(self, value: HmodeStruct) -> None:
		"""SCPI: ROUTe:EVDO:SIGNaling<instance>:SCENario:HMODe \n
		Snippet: driver.route.scenario.set_hmode(value = HmodeStruct()) \n
		Activates the hybrid mode scenario and selects the signal paths. For possible connector and converter values, see 'Values
		for Signal Path Selection'. \n
			:param value: see the help for HmodeStruct structure arguments.
		"""
		self._core.io.write_struct('ROUTe:EVDO:SIGNaling<Instance>:SCENario:HMODe', value)

	# noinspection PyTypeChecker
	class HmliteStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rx_Connector: enums.RxConnector: RF connector for the input path
			- Rx_Converter: enums.RxConverter: RX module for the input path
			- Tx_Connector: enums.TxConnector: RF connector for the output path
			- Tx_Converter: enums.TxConverter: TX module for the output path"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Rx_Connector', enums.RxConnector),
			ArgStruct.scalar_enum('Rx_Converter', enums.RxConverter),
			ArgStruct.scalar_enum('Tx_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Tx_Converter', enums.TxConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx_Connector: enums.RxConnector = None
			self.Rx_Converter: enums.RxConverter = None
			self.Tx_Connector: enums.TxConnector = None
			self.Tx_Converter: enums.TxConverter = None

	# noinspection PyTypeChecker
	def get_hmlite(self) -> HmliteStruct:
		"""SCPI: ROUTe:EVDO:SIGNaling<instance>:SCENario:HMLite \n
		Snippet: value: HmliteStruct = driver.route.scenario.get_hmlite() \n
		Activates the 'Hybrid Mode Lite' scenario and selects the signal path. For possible connector and converter values, see
		'Values for Signal Path Selection'. \n
			:return: structure: for return value, see the help for HmliteStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:EVDO:SIGNaling<Instance>:SCENario:HMLite?', self.__class__.HmliteStruct())

	def set_hmlite(self, value: HmliteStruct) -> None:
		"""SCPI: ROUTe:EVDO:SIGNaling<instance>:SCENario:HMLite \n
		Snippet: driver.route.scenario.set_hmlite(value = HmliteStruct()) \n
		Activates the 'Hybrid Mode Lite' scenario and selects the signal path. For possible connector and converter values, see
		'Values for Signal Path Selection'. \n
			:param value: see the help for HmliteStruct structure arguments.
		"""
		self._core.io.write_struct('ROUTe:EVDO:SIGNaling<Instance>:SCENario:HMLite', value)

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Scenario: enums.Scenario: SCELl | HMODe | HMLite | SCFading | HMFading SCEL: Standard cell HMOD: Hybrid mode HMLite: Hybrid mode lite SCFading: Standard cell fading HMFading: Hybrid mode with fading
			- Fader: enums.SourceInt: EXTernal | INTernal Only returned for fading scenario (SCF) Indicates whether internal or external fading is active."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Scenario', enums.Scenario),
			ArgStruct.scalar_enum('Fader', enums.SourceInt)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Scenario: enums.Scenario = None
			self.Fader: enums.SourceInt = None

	# noinspection PyTypeChecker
	def get_value(self) -> ValueStruct:
		"""SCPI: ROUTe:EVDO:SIGNaling<instance>:SCENario \n
		Snippet: value: ValueStruct = driver.route.scenario.get_value() \n
		Returns the active scenario. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:EVDO:SIGNaling<Instance>:SCENario?', self.__class__.ValueStruct())

	def clone(self) -> 'Scenario':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Scenario(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
