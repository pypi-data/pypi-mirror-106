from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Smax:
	"""Smax commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("smax", core, parent)

	def get_index(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:APPLication:RETap:SMAX:INDex \n
		Snippet: value: int = driver.configure.layer.application.retap.smax.get_index() \n
		Selects the maximum data rate index for RETAP packets. Use method RsCmwEvdoSig.Configure.Layer.Application.Retap.Smax.
		size to query the corresponding packet size. \n
			:return: max_index: Range: 1 to 12
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:APPLication:RETap:SMAX:INDex?')
		return Conversions.str_to_int(response)

	def set_index(self, max_index: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:APPLication:RETap:SMAX:INDex \n
		Snippet: driver.configure.layer.application.retap.smax.set_index(max_index = 1) \n
		Selects the maximum data rate index for RETAP packets. Use method RsCmwEvdoSig.Configure.Layer.Application.Retap.Smax.
		size to query the corresponding packet size. \n
			:param max_index: Range: 1 to 12
		"""
		param = Conversions.decimal_value_to_str(max_index)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:LAYer:APPLication:RETap:SMAX:INDex {param}')

	def get_size(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:APPLication:RETap:SMAX:SIZE \n
		Snippet: value: int = driver.configure.layer.application.retap.smax.get_size() \n
		Queries the packet size for the selected maximum data rate index (method RsCmwEvdoSig.Configure.Layer.Application.Retap.
		Smax.index) . \n
			:return: max_size: Range: 0 bits to 12.288E+3 bits
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:APPLication:RETap:SMAX:SIZE?')
		return Conversions.str_to_int(response)
