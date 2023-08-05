from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Packet:
	"""Packet commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("packet", core, parent)

	# noinspection PyTypeChecker
	def get_preferred(self) -> enums.PrefApplication:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:APPLication:PACKet:PREFerred \n
		Snippet: value: enums.PrefApplication = driver.configure.layer.application.packet.get_preferred() \n
		Selects the packet application the R&S CMW initially proposes to the AT during session negotiation.
		See 'Packet Applications' for details. \n
			:return: pref_application: DPA | EMPA EMPA: Enhanced multi-flow packet application DPA: Default packet application
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:APPLication:PACKet:PREFerred?')
		return Conversions.str_to_scalar_enum(response, enums.PrefApplication)

	def set_preferred(self, pref_application: enums.PrefApplication) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:APPLication:PACKet:PREFerred \n
		Snippet: driver.configure.layer.application.packet.set_preferred(pref_application = enums.PrefApplication.DPA) \n
		Selects the packet application the R&S CMW initially proposes to the AT during session negotiation.
		See 'Packet Applications' for details. \n
			:param pref_application: DPA | EMPA EMPA: Enhanced multi-flow packet application DPA: Default packet application
		"""
		param = Conversions.enum_scalar_to_str(pref_application, enums.PrefApplication)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:LAYer:APPLication:PACKet:PREFerred {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.PrefAppMode:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:APPLication:PACKet:MODE \n
		Snippet: value: enums.PrefAppMode = driver.configure.layer.application.packet.get_mode() \n
		Sets the preferred standard to be signaled during the connection setup. \n
			:return: pref_mode: EHRPd | HRPD Enhanced HRPD or high rate packet data (HRPD)
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:APPLication:PACKet:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.PrefAppMode)

	def set_mode(self, pref_mode: enums.PrefAppMode) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:APPLication:PACKet:MODE \n
		Snippet: driver.configure.layer.application.packet.set_mode(pref_mode = enums.PrefAppMode.EHRPd) \n
		Sets the preferred standard to be signaled during the connection setup. \n
			:param pref_mode: EHRPd | HRPD Enhanced HRPD or high rate packet data (HRPD)
		"""
		param = Conversions.enum_scalar_to_str(pref_mode, enums.PrefAppMode)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:LAYer:APPLication:PACKet:MODE {param}')
