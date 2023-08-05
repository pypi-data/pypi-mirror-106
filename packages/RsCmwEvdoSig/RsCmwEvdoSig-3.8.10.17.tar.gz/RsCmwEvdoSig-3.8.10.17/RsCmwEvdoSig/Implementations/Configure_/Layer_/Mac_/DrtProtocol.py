from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DrtProtocol:
	"""DrtProtocol commands group definition. 4 total commands, 0 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("drtProtocol", core, parent)

	def get_donom(self) -> float:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:MAC:DRTProtocol:DONom \n
		Snippet: value: float = driver.configure.layer.mac.drtProtocol.get_donom() \n
		Defines the nominal offset of the reverse traffic channel power from the reverse pilot channel power. In the current
		version, this parameter is not supported. \n
			:return: data_offset_nom: Range: depending on test settings , Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:MAC:DRTProtocol:DONom?')
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	class DrateStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- R_9_K: float: Range: -2 dB to 1.75 dB, Unit: dB
			- R_19_K: float: Range: -2 dB to 1.75 dB, Unit: dB
			- R_38_K: float: Range: -2 dB to 1.75 dB, Unit: dB
			- R_76_K: float: Range: -2 dB to 1.75 dB, Unit: dB
			- R_153_K: float: Range: -2 dB to 1.75 dB, Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_float('R_9_K'),
			ArgStruct.scalar_float('R_19_K'),
			ArgStruct.scalar_float('R_38_K'),
			ArgStruct.scalar_float('R_76_K'),
			ArgStruct.scalar_float('R_153_K')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.R_9_K: float = None
			self.R_19_K: float = None
			self.R_38_K: float = None
			self.R_76_K: float = None
			self.R_153_K: float = None

	def get_drate(self) -> DrateStruct:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:MAC:DRTProtocol:DRATe \n
		Snippet: value: DrateStruct = driver.configure.layer.mac.drtProtocol.get_drate() \n
		Defines the ratio of the reverse traffic channel power at different data rates to the reverse pilot channel power. \n
			:return: structure: for return value, see the help for DrateStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:EVDO:SIGNaling<Instance>:LAYer:MAC:DRTProtocol:DRATe?', self.__class__.DrateStruct())

	def set_drate(self, value: DrateStruct) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:MAC:DRTProtocol:DRATe \n
		Snippet: driver.configure.layer.mac.drtProtocol.set_drate(value = DrateStruct()) \n
		Defines the ratio of the reverse traffic channel power at different data rates to the reverse pilot channel power. \n
			:param value: see the help for DrateStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:EVDO:SIGNaling<Instance>:LAYer:MAC:DRTProtocol:DRATe', value)

	# noinspection PyTypeChecker
	class ItransitionStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- R_9_K: str: Range: #H00 to #HFF
			- R_19_K: str: Range: #H00 to #HFF
			- R_38_K: str: Range: #H00 to #HFF
			- R_76_K: str: Range: #H00 to #HFF"""
		__meta_args_list = [
			ArgStruct.scalar_raw_str('R_9_K'),
			ArgStruct.scalar_raw_str('R_19_K'),
			ArgStruct.scalar_raw_str('R_38_K'),
			ArgStruct.scalar_raw_str('R_76_K')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.R_9_K: str = None
			self.R_19_K: str = None
			self.R_38_K: str = None
			self.R_76_K: str = None

	def get_itransition(self) -> ItransitionStruct:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:MAC:DRTProtocol:ITRansition \n
		Snippet: value: ItransitionStruct = driver.configure.layer.mac.drtProtocol.get_itransition() \n
		Defines the probability of the access terminal to increase its transmission rate to the next higher data rate. \n
			:return: structure: for return value, see the help for ItransitionStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:EVDO:SIGNaling<Instance>:LAYer:MAC:DRTProtocol:ITRansition?', self.__class__.ItransitionStruct())

	def set_itransition(self, value: ItransitionStruct) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:MAC:DRTProtocol:ITRansition \n
		Snippet: driver.configure.layer.mac.drtProtocol.set_itransition(value = ItransitionStruct()) \n
		Defines the probability of the access terminal to increase its transmission rate to the next higher data rate. \n
			:param value: see the help for ItransitionStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:EVDO:SIGNaling<Instance>:LAYer:MAC:DRTProtocol:ITRansition', value)

	# noinspection PyTypeChecker
	class DtransitionStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- R_19_K: str: Range: #H00 to #HFF
			- R_38_K: str: Range: #H00 to #HFF
			- R_76_K: str: Range: #H00 to #HFF
			- R_153_K: str: Range: #H00 to #HFF"""
		__meta_args_list = [
			ArgStruct.scalar_raw_str('R_19_K'),
			ArgStruct.scalar_raw_str('R_38_K'),
			ArgStruct.scalar_raw_str('R_76_K'),
			ArgStruct.scalar_raw_str('R_153_K')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.R_19_K: str = None
			self.R_38_K: str = None
			self.R_76_K: str = None
			self.R_153_K: str = None

	def get_dtransition(self) -> DtransitionStruct:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:MAC:DRTProtocol:DTRansition \n
		Snippet: value: DtransitionStruct = driver.configure.layer.mac.drtProtocol.get_dtransition() \n
		Defines the probability of the access terminal to decrease its transmission rate to the next lower data rate. \n
			:return: structure: for return value, see the help for DtransitionStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:EVDO:SIGNaling<Instance>:LAYer:MAC:DRTProtocol:DTRansition?', self.__class__.DtransitionStruct())

	def set_dtransition(self, value: DtransitionStruct) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:MAC:DRTProtocol:DTRansition \n
		Snippet: driver.configure.layer.mac.drtProtocol.set_dtransition(value = DtransitionStruct()) \n
		Defines the probability of the access terminal to decrease its transmission rate to the next lower data rate. \n
			:param value: see the help for DtransitionStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:EVDO:SIGNaling<Instance>:LAYer:MAC:DRTProtocol:DTRansition', value)
