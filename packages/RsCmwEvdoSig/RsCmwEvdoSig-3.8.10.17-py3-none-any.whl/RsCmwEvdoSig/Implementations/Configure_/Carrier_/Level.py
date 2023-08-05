from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("level", core, parent)

	def get_absolute(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:CARRier:LEVel:ABSolute \n
		Snippet: value: int = driver.configure.carrier.level.get_absolute() \n
		Sets/gets the absolute 1xEV-DO power level for a carrier. Preselect the related carrier using the method RsCmwEvdoSig.
		Configure.Carrier.setting command. While the query can be executed for all carriers, setting the power level is only
		possible for carrier 0. The power level of carriers 1 and 2 are specified via their level relative to carrier 0 -
		implicitly determining the absolute levels. \n
			:return: level_absolute: Range: -180 dBm to 90 dBm, Unit: dBm
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:CARRier:LEVel:ABSolute?')
		return Conversions.str_to_int(response)

	def set_absolute(self, level_absolute: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:CARRier:LEVel:ABSolute \n
		Snippet: driver.configure.carrier.level.set_absolute(level_absolute = 1) \n
		Sets/gets the absolute 1xEV-DO power level for a carrier. Preselect the related carrier using the method RsCmwEvdoSig.
		Configure.Carrier.setting command. While the query can be executed for all carriers, setting the power level is only
		possible for carrier 0. The power level of carriers 1 and 2 are specified via their level relative to carrier 0 -
		implicitly determining the absolute levels. \n
			:param level_absolute: Range: -180 dBm to 90 dBm, Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(level_absolute)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:CARRier:LEVel:ABSolute {param}')

	def get_relative(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:CARRier:LEVel:RELative \n
		Snippet: value: int = driver.configure.carrier.level.get_relative() \n
		Sets/gets the relative 1xEV-DO power for a carrier in the sector implemented by the signaling application. Preselect the
		related carrier using the method RsCmwEvdoSig.Configure.Carrier.setting command. While the query can be executed for all
		carriers (with return value 0 for carrier 0) , setting the relative 1xEV-DO power is only possible for carriers 1 and 2. \n
			:return: level_relative: The level is relative to the main carrier's absolute power. Range: -20 dB to 0 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:CARRier:LEVel:RELative?')
		return Conversions.str_to_int(response)

	def set_relative(self, level_relative: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:CARRier:LEVel:RELative \n
		Snippet: driver.configure.carrier.level.set_relative(level_relative = 1) \n
		Sets/gets the relative 1xEV-DO power for a carrier in the sector implemented by the signaling application. Preselect the
		related carrier using the method RsCmwEvdoSig.Configure.Carrier.setting command. While the query can be executed for all
		carriers (with return value 0 for carrier 0) , setting the relative 1xEV-DO power is only possible for carriers 1 and 2. \n
			:param level_relative: The level is relative to the main carrier's absolute power. Range: -20 dB to 0 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(level_relative)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:CARRier:LEVel:RELative {param}')
