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
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:APPLication:RMCTap:SMAX:INDex \n
		Snippet: value: int = driver.configure.layer.application.rmctap.smax.get_index() \n
		Selects the maximum packet size index for RMCTAP test packets on this carrier. Preselect the related carrier using the
		method RsCmwEvdoSig.Configure.Carrier.setting command. Use method RsCmwEvdoSig.Configure.Layer.Application.Rmctap.Smax.
		size to query the corresponding packet size. \n
			:return: max_index: Range: 1 to 12
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:APPLication:RMCTap:SMAX:INDex?')
		return Conversions.str_to_int(response)

	def set_index(self, max_index: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:APPLication:RMCTap:SMAX:INDex \n
		Snippet: driver.configure.layer.application.rmctap.smax.set_index(max_index = 1) \n
		Selects the maximum packet size index for RMCTAP test packets on this carrier. Preselect the related carrier using the
		method RsCmwEvdoSig.Configure.Carrier.setting command. Use method RsCmwEvdoSig.Configure.Layer.Application.Rmctap.Smax.
		size to query the corresponding packet size. \n
			:param max_index: Range: 1 to 12
		"""
		param = Conversions.decimal_value_to_str(max_index)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:LAYer:APPLication:RMCTap:SMAX:INDex {param}')

	def get_size(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:APPLication:RMCTap:SMAX:SIZE \n
		Snippet: value: int = driver.configure.layer.application.rmctap.smax.get_size() \n
		Queries the maximum RMCTAP test packet size on a carrier. Preselect the related carrier using the method RsCmwEvdoSig.
		Configure.Carrier.setting command. The maximum packet size is determined by the selected minimum packet size index
		(method RsCmwEvdoSig.Configure.Layer.Application.Retap.Smin.index) . \n
			:return: max_size: Range: 0 bits to 12.288E+3 bits
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:APPLication:RMCTap:SMAX:SIZE?')
		return Conversions.str_to_int(response)
