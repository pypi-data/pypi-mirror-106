from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cstatus:
	"""Cstatus commands group definition. 16 total commands, 1 Sub-groups, 14 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cstatus", core, parent)

	@property
	def pcChannel(self):
		"""pcChannel commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_pcChannel'):
			from .Cstatus_.PcChannel import PcChannel
			self._pcChannel = PcChannel(self._core, self._base)
		return self._pcChannel

	# noinspection PyTypeChecker
	def get_afl_carriers(self) -> enums.LinkCarrier:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:CSTatus:AFLCarriers \n
		Snippet: value: enums.LinkCarrier = driver.configure.cstatus.get_afl_carriers() \n
		Queries the current state of a forward link carrier. Preselect the related carrier using the method RsCmwEvdoSig.
		Configure.Carrier.setting command.
			INTRO_CMD_HELP: Note that a carrier can only be active on the AT if it is: \n
			- Enabled on the cell (using method RsCmwEvdoSig.Configure.Network.Pilot.An.active)
			- Assigned to the AT (using method RsCmwEvdoSig.Configure.Network.Pilot.At.assigned )  \n
			:return: act_fwd_link_carr: ACTive | NACTive | NCConnected | DISabled ACTive: The carrier is assigned to the AT and the traffic channel is active. NACTive: The carrier is assigned to the AT but the traffic channel is inactive. NCConnected: The carrier is assigned to the AT but the AT is not connected. DISabled: The carrier is not assigned to the AT.
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:CSTatus:AFLCarriers?')
		return Conversions.str_to_scalar_enum(response, enums.LinkCarrier)

	# noinspection PyTypeChecker
	def get_arl_carriers(self) -> enums.LinkCarrier:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:CSTatus:ARLCarriers \n
		Snippet: value: enums.LinkCarrier = driver.configure.cstatus.get_arl_carriers() \n
		Queries the current state of a reverse link carrier. Preselect the related carrier using the method RsCmwEvdoSig.
		Configure.Carrier.setting command.
			INTRO_CMD_HELP: Note that a carrier can only be active on the AT if it is: \n
			- Enabled on the cell (using method RsCmwEvdoSig.Configure.Network.Pilot.An.active)
			- Assigned to the AT (using method RsCmwEvdoSig.Configure.Network.Pilot.At.assigned )  \n
			:return: act_rev_link_carr: ACTive | NACTive | NCConnected | DISabled ACTive: The carrier is assigned to the AT and the traffic channel is active. NACTive: The carrier is assigned to the AT but the traffic channel is inactive. NCConnected: The carrier is assigned to the AT but the AT is not connected. DISabled: The carrier is not assigned to the AT.
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:CSTatus:ARLCarriers?')
		return Conversions.str_to_scalar_enum(response, enums.LinkCarrier)

	# noinspection PyTypeChecker
	def get_pl_subtype(self) -> enums.PlSubtype:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:CSTatus:PLSubtype \n
		Snippet: value: enums.PlSubtype = driver.configure.cstatus.get_pl_subtype() \n
			INTRO_CMD_HELP: Queries the active physical layer subtype, which in turn depends on the selected network release (method RsCmwEvdoSig.Configure.Network.release) : \n
			- With release 0 , the R&S CMW uses subtype 0
			- With revision A, the R&S CMW uses subtype 2
			- With revision B and more than 1 active carrier , the R&S CMW uses subtype 3; otherwise it uses subtype 2 \n
			:return: pl_subtype: ST01 | ST2 | ST3 Physical layer subtype 0/1, 2 or 3.
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:CSTatus:PLSubtype?')
		return Conversions.str_to_scalar_enum(response, enums.PlSubtype)

	def get_irat(self) -> bool:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:CSTatus:IRAT \n
		Snippet: value: bool = driver.configure.cstatus.get_irat() \n
		Indicates whether an inter-RAT handover is supported (as agreed during session negotiation) . Currently this command does
		not return valid results. \n
			:return: inter_rat: OFF
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:CSTatus:IRAT?')
		return Conversions.str_to_bool(response)

	def get_application(self) -> str:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:CSTatus:APPLication \n
		Snippet: value: str = driver.configure.cstatus.get_application() \n
		Returns the active test or packet applications along with the streams they are using. \n
			:return: application: Comma-separated string of tuples s:Application Name, where s is the stream number, e.g. 1:FETAP
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:CSTatus:APPLication?')
		return trim_str_response(response)

	def get_uati(self) -> str:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:CSTatus:UATI \n
		Snippet: value: str = driver.configure.cstatus.get_uati() \n
		Queries the unicast access terminal identifier (UATI) of the AT. \n
			:return: uati: 8-digit hexadecimal number Range: #H0 to #HFFFFFFFF (8 digits)
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:CSTatus:UATI?')
		return trim_str_response(response)

	def get_esn(self) -> str:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:CSTatus:ESN \n
		Snippet: value: str = driver.configure.cstatus.get_esn() \n
		Queries the electronic serial number of the connected AT. \n
			:return: esn: 8-digit hexadecimal number Range: #H0 to #HFFFFFFFF (8 digits)
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:CSTatus:ESN?')
		return trim_str_response(response)

	def get_meid(self) -> str:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:CSTatus:MEID \n
		Snippet: value: str = driver.configure.cstatus.get_meid() \n
		Queries the mobile equipment identifier (MEID) of the connected AT. \n
			:return: meid: 14-digit hexadecimal number Range: #H0 to #HFFFFFFFFFFFFFF (14 digits)
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:CSTatus:MEID?')
		return trim_str_response(response)

	def get_ehrpd(self) -> bool:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:CSTatus:EHRPd \n
		Snippet: value: bool = driver.configure.cstatus.get_ehrpd() \n
		Queries whether the AT supports eHRPD. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:CSTatus:EHRPd?')
		return Conversions.str_to_bool(response)

	def get_log(self) -> str:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:CSTatus:LOG \n
		Snippet: value: str = driver.configure.cstatus.get_log() \n
		Reports events and errors like connection state changes, RRC connection establishment/release and authentication failure. \n
			:return: con_status_log: Report as a string
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:CSTatus:LOG?')
		return trim_str_response(response)

	def get_ilc_mask(self) -> str:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:CSTatus:ILCMask \n
		Snippet: value: str = driver.configure.cstatus.get_ilc_mask() \n
		Queries the reverse traffic channel in phase long code mask associated with the access terminal's session. \n
			:return: lc_mask_i: The long code mask in hexadecimal notation. Range: #H0 to #H3FFFFFFFFFF
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:CSTatus:ILCMask?')
		return trim_str_response(response)

	def get_qlcmask(self) -> str:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:CSTatus:QLCMask \n
		Snippet: value: str = driver.configure.cstatus.get_qlcmask() \n
		Queries the reverse traffic channel quadrature-phase long code mask associated with the access terminal's session. \n
			:return: lc_mask_q: The long code mask in hexadecimal notation. Range: #H0 to #H3FFFFFFFFFF
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:CSTatus:QLCMask?')
		return trim_str_response(response)

	def get_mr_bandwidth(self) -> float:
		"""SCPI: CONFigure:EVDO:SIGNaling<Instance>:CSTatus:MRBandwidth \n
		Snippet: value: float = driver.configure.cstatus.get_mr_bandwidth() \n
		Queries the maximum reverse link bandwidth reported by the AT. \n
			:return: max_rev_bandwidth: Range: 0 Hz to 20 MHz, Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:CSTatus:MRBandwidth?')
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.PrefAppMode:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:CSTatus:MODE \n
		Snippet: value: enums.PrefAppMode = driver.configure.cstatus.get_mode() \n
		Queries the negotiated packet standard of the current connection. \n
			:return: mode: EHRPd | HRPD Enhanced HRPD or high rate packet data (HRPD)
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:CSTatus:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.PrefAppMode)

	def clone(self) -> 'Cstatus':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cstatus(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
