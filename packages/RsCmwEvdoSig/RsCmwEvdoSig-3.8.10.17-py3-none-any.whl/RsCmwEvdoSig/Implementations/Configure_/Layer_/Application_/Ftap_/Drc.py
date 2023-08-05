from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Drc:
	"""Drc commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("drc", core, parent)

	def get_index(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:APPLication:FTAP:DRC:INDex \n
		Snippet: value: int = driver.configure.layer.application.ftap.drc.get_index() \n
		Selects the data rate index for FTAP packets. Data rate index '0' stops the flow of FTAP packets to the AT. Use method
		RsCmwEvdoSig.Configure.Layer.Application.Ftap.Drc.rate and method RsCmwEvdoSig.Configure.Layer.Application.Ftap.Drc.slots
		to query the data rate and slot count for the selected index. \n
			:return: drc_index: Range: 0 to 12
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:APPLication:FTAP:DRC:INDex?')
		return Conversions.str_to_int(response)

	def set_index(self, drc_index: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:APPLication:FTAP:DRC:INDex \n
		Snippet: driver.configure.layer.application.ftap.drc.set_index(drc_index = 1) \n
		Selects the data rate index for FTAP packets. Data rate index '0' stops the flow of FTAP packets to the AT. Use method
		RsCmwEvdoSig.Configure.Layer.Application.Ftap.Drc.rate and method RsCmwEvdoSig.Configure.Layer.Application.Ftap.Drc.slots
		to query the data rate and slot count for the selected index. \n
			:param drc_index: Range: 0 to 12
		"""
		param = Conversions.decimal_value_to_str(drc_index)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:LAYer:APPLication:FTAP:DRC:INDex {param}')

	def get_rate(self) -> float:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:APPLication:FTAP:DRC:RATE \n
		Snippet: value: float = driver.configure.layer.application.ftap.drc.get_rate() \n
		Queries the data rate for the selected FTAP data rate index (method RsCmwEvdoSig.Configure.Layer.Application.Ftap.Drc.
		index) . \n
			:return: drc_rate: Range: 0 kbit/s to 2457.6 kbit/s
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:APPLication:FTAP:DRC:RATE?')
		return Conversions.str_to_float(response)

	def get_slots(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:APPLication:FTAP:DRC:SLOTs \n
		Snippet: value: int = driver.configure.layer.application.ftap.drc.get_slots() \n
		Queries the slot count for the selected FTAP data rate index (method RsCmwEvdoSig.Configure.Layer.Application.Ftap.Drc.
		index) . \n
			:return: drc_slots: Range: 1 to 16
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:APPLication:FTAP:DRC:SLOTs?')
		return Conversions.str_to_int(response)
