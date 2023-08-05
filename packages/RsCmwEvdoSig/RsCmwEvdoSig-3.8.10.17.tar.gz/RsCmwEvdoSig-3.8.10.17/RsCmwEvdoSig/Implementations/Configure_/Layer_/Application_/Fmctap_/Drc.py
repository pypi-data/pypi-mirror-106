from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Drc:
	"""Drc commands group definition. 5 total commands, 0 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("drc", core, parent)

	def get_type_py(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:APPLication:FMCTap:DRC:TYPE \n
		Snippet: value: int = driver.configure.layer.application.fmctap.drc.get_type_py() \n
		Selects the type of FMCTAP test packets to be used. Preselect the related carrier using the method RsCmwEvdoSig.Configure.
		Carrier.setting command. Use the queries in the ...DRC... subsystem to query the corresponding DRC index, packet size,
		data rate, and slot count. \n
			:return: drc_type: Range: 1 to 37
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:APPLication:FMCTap:DRC:TYPE?')
		return Conversions.str_to_int(response)

	def set_type_py(self, drc_type: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:APPLication:FMCTap:DRC:TYPE \n
		Snippet: driver.configure.layer.application.fmctap.drc.set_type_py(drc_type = 1) \n
		Selects the type of FMCTAP test packets to be used. Preselect the related carrier using the method RsCmwEvdoSig.Configure.
		Carrier.setting command. Use the queries in the ...DRC... subsystem to query the corresponding DRC index, packet size,
		data rate, and slot count. \n
			:param drc_type: Range: 1 to 37
		"""
		param = Conversions.decimal_value_to_str(drc_type)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:LAYer:APPLication:FMCTap:DRC:TYPE {param}')

	def get_index(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:APPLication:FMCTap:DRC:INDex \n
		Snippet: value: int = driver.configure.layer.application.fmctap.drc.get_index() \n
		Queries the data rate index for the FMCTAP test packet stream on a particular carrier. Preselect the related carrier
		using the method RsCmwEvdoSig.Configure.Carrier.setting command. The DRC index is determined by the selected packet type
		(method RsCmwEvdoSig.Configure.Layer.Application.Fmctap.Drc.typePy) . \n
			:return: drc_index: Range: 1 to 14
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:APPLication:FMCTap:DRC:INDex?')
		return Conversions.str_to_int(response)

	def get_size(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:APPLication:FMCTap:DRC:SIZE \n
		Snippet: value: int = driver.configure.layer.application.fmctap.drc.get_size() \n
		Queries the size of the FMCTAP test packets sent on a particular carrier. Preselect the related carrier using the method
		RsCmwEvdoSig.Configure.Carrier.setting command. The packet size is determined by the selected packet type (method
		RsCmwEvdoSig.Configure.Layer.Application.Fmctap.Drc.typePy) . \n
			:return: drc_size: Range: 128 to 5120
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:APPLication:FMCTap:DRC:SIZE?')
		return Conversions.str_to_int(response)

	def get_rate(self) -> float:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:APPLication:FMCTap:DRC:RATE \n
		Snippet: value: float = driver.configure.layer.application.fmctap.drc.get_rate() \n
		Queries the data rate of the FMCTAP test packet stream sent on a particular carrier. Preselect the related carrier using
		the method RsCmwEvdoSig.Configure.Carrier.setting command. The data rate is determined by the selected packet type
		(method RsCmwEvdoSig.Configure.Layer.Application.Fmctap.Drc.typePy) . \n
			:return: drc_rate: Range: 4.8 kbit/s to 3072 kbit/s
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:APPLication:FMCTap:DRC:RATE?')
		return Conversions.str_to_float(response)

	def get_slots(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:APPLication:FMCTap:DRC:SLOTs \n
		Snippet: value: int = driver.configure.layer.application.fmctap.drc.get_slots() \n
		Queries the slot count of an FMCTAP test packet sent on a particular carrier. Preselect the related carrier using the
		method RsCmwEvdoSig.Configure.Carrier.setting command. The slot count is determined by the selected packet type (method
		RsCmwEvdoSig.Configure.Layer.Application.Fmctap.Drc.typePy) . \n
			:return: drc_slots: Range: 1 to 16
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:APPLication:FMCTap:DRC:SLOTs?')
		return Conversions.str_to_int(response)
