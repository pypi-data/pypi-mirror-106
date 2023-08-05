from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PropertyPy:
	"""PropertyPy commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("propertyPy", core, parent)

	def get_cld_time(self) -> float or bool:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:PROPerty:CLDTime \n
		Snippet: value: float or bool = driver.configure.network.propertyPy.get_cld_time() \n
		Defines the time in s after which a connection is considered to be lost. \n
			:return: cld_time: Range: 2 s to 6 s, Unit: s Additional OFF/ON disables/enables the call loss detect timer
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:NETWork:PROPerty:CLDTime?')
		return Conversions.str_to_float_or_bool(response)

	def set_cld_time(self, cld_time: float or bool) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:PROPerty:CLDTime \n
		Snippet: driver.configure.network.propertyPy.set_cld_time(cld_time = 1.0) \n
		Defines the time in s after which a connection is considered to be lost. \n
			:param cld_time: Range: 2 s to 6 s, Unit: s Additional OFF/ON disables/enables the call loss detect timer
		"""
		param = Conversions.decimal_or_bool_value_to_str(cld_time)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:NETWork:PROPerty:CLDTime {param}')

	def get_fpactivity(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:PROPerty:FPACtivity \n
		Snippet: value: int = driver.configure.network.propertyPy.get_fpactivity() \n
		Defines the percentage of forward packets that the R&S CMW directs to the AT under test. \n
			:return: activity: Range: 0 % to 100 %, Unit: %
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:NETWork:PROPerty:FPACtivity?')
		return Conversions.str_to_int(response)

	def set_fpactivity(self, activity: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:PROPerty:FPACtivity \n
		Snippet: driver.configure.network.propertyPy.set_fpactivity(activity = 1) \n
		Defines the percentage of forward packets that the R&S CMW directs to the AT under test. \n
			:param activity: Range: 0 % to 100 %, Unit: %
		"""
		param = Conversions.decimal_value_to_str(activity)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:NETWork:PROPerty:FPACtivity {param}')

	def get_irat(self) -> bool:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:PROPerty:IRAT \n
		Snippet: value: bool = driver.configure.network.propertyPy.get_irat() \n
		Flag for inter-RAT operability. \n
			:return: inter_rat: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:NETWork:PROPerty:IRAT?')
		return Conversions.str_to_bool(response)

	def set_irat(self, inter_rat: bool) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:PROPerty:IRAT \n
		Snippet: driver.configure.network.propertyPy.set_irat(inter_rat = False) \n
		Flag for inter-RAT operability. \n
			:param inter_rat: OFF | ON
		"""
		param = Conversions.bool_to_str(inter_rat)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:NETWork:PROPerty:IRAT {param}')
