from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FlPer:
	"""FlPer commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("flPer", core, parent)

	def get_mper(self) -> float:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:LIMit:FLPer:MPER \n
		Snippet: value: float = driver.configure.rxQuality.limit.flPer.get_mper() \n
		Defines an upper limit for the measured forward / reverse link packet error ratio (PER) . \n
			:return: max_per: Range: 0 % to 100 %, Unit: %
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:RXQuality:LIMit:FLPer:MPER?')
		return Conversions.str_to_float(response)

	def set_mper(self, max_per: float) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:LIMit:FLPer:MPER \n
		Snippet: driver.configure.rxQuality.limit.flPer.set_mper(max_per = 1.0) \n
		Defines an upper limit for the measured forward / reverse link packet error ratio (PER) . \n
			:param max_per: Range: 0 % to 100 %, Unit: %
		"""
		param = Conversions.decimal_value_to_str(max_per)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:RXQuality:LIMit:FLPer:MPER {param}')

	def get_clevel(self) -> float:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:LIMit:FLPer:CLEVel \n
		Snippet: value: float = driver.configure.rxQuality.limit.flPer.get_clevel() \n
		Defines the minimum confidence level for the forward / reverse link PER measurement. \n
			:return: min_confid_level: Range: 0 % to 100 %, Unit: %
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:RXQuality:LIMit:FLPer:CLEVel?')
		return Conversions.str_to_float(response)

	def set_clevel(self, min_confid_level: float) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:LIMit:FLPer:CLEVel \n
		Snippet: driver.configure.rxQuality.limit.flPer.set_clevel(min_confid_level = 1.0) \n
		Defines the minimum confidence level for the forward / reverse link PER measurement. \n
			:param min_confid_level: Range: 0 % to 100 %, Unit: %
		"""
		param = Conversions.decimal_value_to_str(min_confid_level)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:RXQuality:LIMit:FLPer:CLEVel {param}')
