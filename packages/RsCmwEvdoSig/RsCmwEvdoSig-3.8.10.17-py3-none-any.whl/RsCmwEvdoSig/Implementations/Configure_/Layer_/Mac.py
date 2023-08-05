from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mac:
	"""Mac commands group definition. 20 total commands, 3 Sub-groups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("mac", core, parent)

	@property
	def eftProtocol(self):
		"""eftProtocol commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_eftProtocol'):
			from .Mac_.EftProtocol import EftProtocol
			self._eftProtocol = EftProtocol(self._core, self._base)
		return self._eftProtocol

	@property
	def dftProtocol(self):
		"""dftProtocol commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_dftProtocol'):
			from .Mac_.DftProtocol import DftProtocol
			self._dftProtocol = DftProtocol(self._core, self._base)
		return self._dftProtocol

	@property
	def drtProtocol(self):
		"""drtProtocol commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_drtProtocol'):
			from .Mac_.DrtProtocol import DrtProtocol
			self._drtProtocol = DrtProtocol(self._core, self._base)
		return self._drtProtocol

	# noinspection PyTypeChecker
	def get_ttopt(self) -> enums.T2Pmode:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:MAC:TTOPt \n
		Snippet: value: enums.T2Pmode = driver.configure.layer.mac.get_ttopt() \n
		Sets the T2P values in the session negotiation regarding the test purpose. \n
			:return: mode: TPUT | RFCO TPUT: Throughput optimized RFCO: RF conformance
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:MAC:TTOPt?')
		return Conversions.str_to_scalar_enum(response, enums.T2Pmode)

	def set_ttopt(self, mode: enums.T2Pmode) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:MAC:TTOPt \n
		Snippet: driver.configure.layer.mac.set_ttopt(mode = enums.T2Pmode.RFCO) \n
		Sets the T2P values in the session negotiation regarding the test purpose. \n
			:param mode: TPUT | RFCO TPUT: Throughput optimized RFCO: RF conformance
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.T2Pmode)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:LAYer:MAC:TTOPt {param}')

	# noinspection PyTypeChecker
	def get_drate(self) -> enums.CtrlChannelDataRate:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:MAC:DRATe \n
		Snippet: value: enums.CtrlChannelDataRate = driver.configure.layer.mac.get_drate() \n
		Defines the data rate for asynchronous control channels. \n
			:return: data_rate: R384 | R768
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:MAC:DRATe?')
		return Conversions.str_to_scalar_enum(response, enums.CtrlChannelDataRate)

	def set_drate(self, data_rate: enums.CtrlChannelDataRate) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:MAC:DRATe \n
		Snippet: driver.configure.layer.mac.set_drate(data_rate = enums.CtrlChannelDataRate.R384) \n
		Defines the data rate for asynchronous control channels. \n
			:param data_rate: R384 | R768
		"""
		param = Conversions.enum_scalar_to_str(data_rate, enums.CtrlChannelDataRate)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:LAYer:MAC:DRATe {param}')

	def get_sseed(self) -> str:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:MAC:SSEed \n
		Snippet: value: str = driver.configure.layer.mac.get_sseed() \n
		Queries the session seed parameter which is negotiated between the R&S CMW and the AT. \n
			:return: sseed: Range: 0 to 4.294967295E+9
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:MAC:SSEed?')
		return trim_str_response(response)

	def get_mp_sequences(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:MAC:MPSequences \n
		Snippet: value: int = driver.configure.layer.mac.get_mp_sequences() \n
		Specifies the maximum number of access probe sequences for a single access attempt. \n
			:return: mp_sequences: Range: 1 to 15
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:MAC:MPSequences?')
		return Conversions.str_to_int(response)

	def set_mp_sequences(self, mp_sequences: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:MAC:MPSequences \n
		Snippet: driver.configure.layer.mac.set_mp_sequences(mp_sequences = 1) \n
		Specifies the maximum number of access probe sequences for a single access attempt. \n
			:param mp_sequences: Range: 1 to 15
		"""
		param = Conversions.decimal_value_to_str(mp_sequences)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:LAYer:MAC:MPSequences {param}')

	def get_ip_backoff(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:MAC:IPBackoff \n
		Snippet: value: int = driver.configure.layer.mac.get_ip_backoff() \n
		Defines the upper limit of the backoff range (in units of 'access cycle duration' defined in the 'Network' section) which
		the AT uses between access probes. \n
			:return: ip_backoff: Range: 1 to 15
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:MAC:IPBackoff?')
		return Conversions.str_to_int(response)

	def set_ip_backoff(self, ip_backoff: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:MAC:IPBackoff \n
		Snippet: driver.configure.layer.mac.set_ip_backoff(ip_backoff = 1) \n
		Defines the upper limit of the backoff range (in units of 'access cycle duration' defined in the 'Network' section) which
		the AT uses between access probes. \n
			:param ip_backoff: Range: 1 to 15
		"""
		param = Conversions.decimal_value_to_str(ip_backoff)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:LAYer:MAC:IPBackoff {param}')

	def get_ips_backoff(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:MAC:IPSBackoff \n
		Snippet: value: int = driver.configure.layer.mac.get_ips_backoff() \n
		Defines the upper limit of the backoff range in units of access cycle duration (defined in the 'Network' section) which
		the AT uses between access probe sequences. \n
			:return: ips_backoff: Range: 1 to 15
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:MAC:IPSBackoff?')
		return Conversions.str_to_int(response)

	def set_ips_backoff(self, ips_backoff: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:MAC:IPSBackoff \n
		Snippet: driver.configure.layer.mac.set_ips_backoff(ips_backoff = 1) \n
		Defines the upper limit of the backoff range in units of access cycle duration (defined in the 'Network' section) which
		the AT uses between access probe sequences. \n
			:param ips_backoff: Range: 1 to 15
		"""
		param = Conversions.decimal_value_to_str(ips_backoff)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:LAYer:MAC:IPSBackoff {param}')

	def clone(self) -> 'Mac':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mac(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
