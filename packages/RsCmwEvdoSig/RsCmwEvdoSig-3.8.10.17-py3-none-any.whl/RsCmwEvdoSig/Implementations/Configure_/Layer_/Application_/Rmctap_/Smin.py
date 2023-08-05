from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Smin:
	"""Smin commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("smin", core, parent)

	def get_index(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:APPLication:RMCTap:SMIN:INDex \n
		Snippet: value: int = driver.configure.layer.application.rmctap.smin.get_index() \n
		Selects the minimum packet size index for RMCTAP test packets on this carrier. Preselect the related carrier using the
		method RsCmwEvdoSig.Configure.Carrier.setting command. Use method RsCmwEvdoSig.Configure.Layer.Application.Retap.Smin.
		size to query the corresponding packet size. \n
			:return: min_index: Range: 0 to 12
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:APPLication:RMCTap:SMIN:INDex?')
		return Conversions.str_to_int(response)

	def set_index(self, min_index: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:APPLication:RMCTap:SMIN:INDex \n
		Snippet: driver.configure.layer.application.rmctap.smin.set_index(min_index = 1) \n
		Selects the minimum packet size index for RMCTAP test packets on this carrier. Preselect the related carrier using the
		method RsCmwEvdoSig.Configure.Carrier.setting command. Use method RsCmwEvdoSig.Configure.Layer.Application.Retap.Smin.
		size to query the corresponding packet size. \n
			:param min_index: Range: 0 to 12
		"""
		param = Conversions.decimal_value_to_str(min_index)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:LAYer:APPLication:RMCTap:SMIN:INDex {param}')

	def get_size(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:APPLication:RMCTap:SMIN:SIZE \n
		Snippet: value: int = driver.configure.layer.application.rmctap.smin.get_size() \n
		Queries the minimum RMCTAP test packet size on a carrier. Preselect the related carrier using the method RsCmwEvdoSig.
		Configure.Carrier.setting command. The minimum packet size is determined by the selected minimum packet size index
		(method RsCmwEvdoSig.Configure.Layer.Application.Retap.Smin.index) . \n
			:return: min_size: Range: 0 bits to 12.288E+3 bits
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:APPLication:RMCTap:SMIN:SIZE?')
		return Conversions.str_to_int(response)
