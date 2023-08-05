from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cstatus:
	"""Cstatus commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cstatus", core, parent)

	def get_meid(self) -> float:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:TEST:CSTatus:MEID \n
		Snippet: value: float = driver.configure.test.cstatus.get_meid() \n
		No command help available \n
			:return: meid: No help available
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:TEST:CSTatus:MEID?')
		return Conversions.str_to_float(response)

	def set_meid(self, meid: float) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:TEST:CSTatus:MEID \n
		Snippet: driver.configure.test.cstatus.set_meid(meid = 1.0) \n
		No command help available \n
			:param meid: No help available
		"""
		param = Conversions.decimal_value_to_str(meid)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:TEST:CSTatus:MEID {param}')

	def get_esn(self) -> float:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:TEST:CSTatus:ESN \n
		Snippet: value: float = driver.configure.test.cstatus.get_esn() \n
		No command help available \n
			:return: esn: No help available
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:TEST:CSTatus:ESN?')
		return Conversions.str_to_float(response)

	def set_esn(self, esn: float) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:TEST:CSTatus:ESN \n
		Snippet: driver.configure.test.cstatus.set_esn(esn = 1.0) \n
		No command help available \n
			:param esn: No help available
		"""
		param = Conversions.decimal_value_to_str(esn)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:TEST:CSTatus:ESN {param}')
