from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rmax:
	"""Rmax commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rmax", core, parent)

	def get_index(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:APPLication:RTAP:RMAX:INDex \n
		Snippet: value: int = driver.configure.layer.application.rtap.rmax.get_index() \n
		Selects the maximum data rate index for RTAP packets. Use method RsCmwEvdoSig.Configure.Layer.Application.Rtap.Rmax.rate
		to query the corresponding data rate. \n
			:return: rmax_index: Range: 1 to 5
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:APPLication:RTAP:RMAX:INDex?')
		return Conversions.str_to_int(response)

	def set_index(self, rmax_index: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:APPLication:RTAP:RMAX:INDex \n
		Snippet: driver.configure.layer.application.rtap.rmax.set_index(rmax_index = 1) \n
		Selects the maximum data rate index for RTAP packets. Use method RsCmwEvdoSig.Configure.Layer.Application.Rtap.Rmax.rate
		to query the corresponding data rate. \n
			:param rmax_index: Range: 1 to 5
		"""
		param = Conversions.decimal_value_to_str(rmax_index)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:LAYer:APPLication:RTAP:RMAX:INDex {param}')

	def get_rate(self) -> float:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:APPLication:RTAP:RMAX:RATE \n
		Snippet: value: float = driver.configure.layer.application.rtap.rmax.get_rate() \n
		Queries the data rate for the selected maximum data rate index (method RsCmwEvdoSig.Configure.Layer.Application.Rtap.Rmax.
		index) . \n
			:return: rmax_rate: Range: 0 kbit/s to 153.6 kbit/s
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:APPLication:RTAP:RMAX:RATE?')
		return Conversions.str_to_float(response)
