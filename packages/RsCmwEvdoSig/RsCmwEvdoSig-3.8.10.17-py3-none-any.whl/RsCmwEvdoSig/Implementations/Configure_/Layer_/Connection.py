from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Connection:
	"""Connection commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("connection", core, parent)

	def get_ro_messages(self) -> bool:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:CONNection:ROMessages \n
		Snippet: value: bool = driver.configure.layer.connection.get_ro_messages() \n
		Sets the 'redirect' bit in the QuickConfig message of the overhead messages protocol to '1'. \n
			:return: ro_messages: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:CONNection:ROMessages?')
		return Conversions.str_to_bool(response)

	def set_ro_messages(self, ro_messages: bool) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:CONNection:ROMessages \n
		Snippet: driver.configure.layer.connection.set_ro_messages(ro_messages = False) \n
		Sets the 'redirect' bit in the QuickConfig message of the overhead messages protocol to '1'. \n
			:param ro_messages: OFF | ON
		"""
		param = Conversions.bool_to_str(ro_messages)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:LAYer:CONNection:ROMessages {param}')

	def get_pd_threshold(self) -> float:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:CONNection:PDTHreshold \n
		Snippet: value: float = driver.configure.layer.connection.get_pd_threshold() \n
		Defines the pilot power (relative to the total 1xEV-DO power) below which the AT starts the pilot supervision timer and
		eventually announces that it has lost the network connection. \n
			:return: pd_threshold: Range: -31.5 dB to 0 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:CONNection:PDTHreshold?')
		return Conversions.str_to_float(response)

	def set_pd_threshold(self, pd_threshold: float) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:CONNection:PDTHreshold \n
		Snippet: driver.configure.layer.connection.set_pd_threshold(pd_threshold = 1.0) \n
		Defines the pilot power (relative to the total 1xEV-DO power) below which the AT starts the pilot supervision timer and
		eventually announces that it has lost the network connection. \n
			:param pd_threshold: Range: -31.5 dB to 0 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(pd_threshold)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:LAYer:CONNection:PDTHreshold {param}')

	def get_rlf_offset(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:CONNection:RLFoffset \n
		Snippet: value: int = driver.configure.layer.connection.get_rlf_offset() \n
		Delays the reverse traffic data channel and reverse rate indicator channel (RRI) transmissions of the AT by an integer
		number of slots related to the system time-aligned frame boundary. \n
			:return: rlf_offset: Range: 0 to 15
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:CONNection:RLFoffset?')
		return Conversions.str_to_int(response)

	def set_rlf_offset(self, rlf_offset: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:CONNection:RLFoffset \n
		Snippet: driver.configure.layer.connection.set_rlf_offset(rlf_offset = 1) \n
		Delays the reverse traffic data channel and reverse rate indicator channel (RRI) transmissions of the AT by an integer
		number of slots related to the system time-aligned frame boundary. \n
			:param rlf_offset: Range: 0 to 15
		"""
		param = Conversions.decimal_value_to_str(rlf_offset)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:LAYer:CONNection:RLFoffset {param}')
