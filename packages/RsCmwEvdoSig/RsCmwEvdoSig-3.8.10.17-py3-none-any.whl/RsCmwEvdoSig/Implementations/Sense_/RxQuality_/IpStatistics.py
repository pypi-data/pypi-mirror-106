from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpStatistics:
	"""IpStatistics commands group definition. 7 total commands, 0 Sub-groups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ipStatistics", core, parent)

	def get_state(self) -> str:
		"""SCPI: SENSe:EVDO:SIGNaling<instance>:RXQuality:IPSTatistics:STATe \n
		Snippet: value: str = driver.sense.rxQuality.ipStatistics.get_state() \n
		Status of the RLP & IP statistics \n
			:return: status: See table below
		"""
		response = self._core.io.query_str('SENSe:EVDO:SIGNaling<Instance>:RXQuality:IPSTatistics:STATe?')
		return trim_str_response(response)

	# noinspection PyTypeChecker
	class ResetStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rx: int: Number of packets received in the last update period Range: 0 to 0.999999E+6
			- Rx_Total: int: Total number of packets received since the beginning of the PPP connection Range: 0 to 0.999999E+6
			- Tx: int: Number of packets transmitted in the last update period Range: 0 to 0.999999E+6
			- Tx_Total: int: Total number of packets transmitted Range: 0 to 0.999999E+6"""
		__meta_args_list = [
			ArgStruct.scalar_int('Rx'),
			ArgStruct.scalar_int('Rx_Total'),
			ArgStruct.scalar_int('Tx'),
			ArgStruct.scalar_int('Tx_Total')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx: int = None
			self.Rx_Total: int = None
			self.Tx: int = None
			self.Tx_Total: int = None

	def get_reset(self) -> ResetStruct:
		"""SCPI: SENSe:EVDO:SIGNaling<instance>:RXQuality:IPSTatistics:RESet \n
		Snippet: value: ResetStruct = driver.sense.rxQuality.ipStatistics.get_reset() \n
		Number of packets associated with RLP reset messages, which are sent between AT and AN to reset RLP. \n
			:return: structure: for return value, see the help for ResetStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:EVDO:SIGNaling<Instance>:RXQuality:IPSTatistics:RESet?', self.__class__.ResetStruct())

	# noinspection PyTypeChecker
	class RackStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rx: int: Number of packets received in the last update period Range: 0 to 0.999999E+6
			- Rx_Total: int: Total number of packets received since the beginning of the PPP connection Range: 0 to 0.999999E+6
			- Tx: int: Number of packets transmitted in the last update period Range: 0 to 0.999999E+6
			- Tx_Total: int: Total number of packets transmitted Range: 0 to 0.999999E+6"""
		__meta_args_list = [
			ArgStruct.scalar_int('Rx'),
			ArgStruct.scalar_int('Rx_Total'),
			ArgStruct.scalar_int('Tx'),
			ArgStruct.scalar_int('Tx_Total')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx: int = None
			self.Rx_Total: int = None
			self.Tx: int = None
			self.Tx_Total: int = None

	def get_rack(self) -> RackStruct:
		"""SCPI: SENSe:EVDO:SIGNaling<instance>:RXQuality:IPSTatistics:RACK \n
		Snippet: value: RackStruct = driver.sense.rxQuality.ipStatistics.get_rack() \n
		Number of packets associated with RLP reset ACK messages, which are sent between AT and AN to complete the RLP reset
		procedure. \n
			:return: structure: for return value, see the help for RackStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:EVDO:SIGNaling<Instance>:RXQuality:IPSTatistics:RACK?', self.__class__.RackStruct())

	# noinspection PyTypeChecker
	class NakStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rx: int: Number of packets received in the last update period Range: 0 to 0.999999E+6
			- Rx_Total: int: Total number of packets received since the beginning of the PPP connection Range: 0 to 0.999999E+6
			- Tx: int: Number of packets transmitted in the last update period Range: 0 to 0.999999E+6
			- Tx_Total: int: Total number of packets transmitted Range: 0 to 0.999999E+6"""
		__meta_args_list = [
			ArgStruct.scalar_int('Rx'),
			ArgStruct.scalar_int('Rx_Total'),
			ArgStruct.scalar_int('Tx'),
			ArgStruct.scalar_int('Tx_Total')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx: int = None
			self.Rx_Total: int = None
			self.Tx: int = None
			self.Tx_Total: int = None

	def get_nak(self) -> NakStruct:
		"""SCPI: SENSe:EVDO:SIGNaling<instance>:RXQuality:IPSTatistics:NAK \n
		Snippet: value: NakStruct = driver.sense.rxQuality.ipStatistics.get_nak() \n
		Number of NAK control packets, requesting the retransmission of one or more data octets. \n
			:return: structure: for return value, see the help for NakStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:EVDO:SIGNaling<Instance>:RXQuality:IPSTatistics:NAK?', self.__class__.NakStruct())

	# noinspection PyTypeChecker
	class SummaryStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rx: int: Number of packets received in the last update period Range: 0 to 0.999999E+6
			- Rx_Total: int: Total number of packets received since the beginning of the PPP connection Range: 0 to 0.999999E+6
			- Tx: int: Number of packets transmitted in the last update period Range: 0 to 0.999999E+6
			- Tx_Total: int: Total number of packets transmitted Range: 0 to 0.999999E+6"""
		__meta_args_list = [
			ArgStruct.scalar_int('Rx'),
			ArgStruct.scalar_int('Rx_Total'),
			ArgStruct.scalar_int('Tx'),
			ArgStruct.scalar_int('Tx_Total')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx: int = None
			self.Rx_Total: int = None
			self.Tx: int = None
			self.Tx_Total: int = None

	def get_summary(self) -> SummaryStruct:
		"""SCPI: SENSe:EVDO:SIGNaling<instance>:RXQuality:IPSTatistics:SUMMary \n
		Snippet: value: SummaryStruct = driver.sense.rxQuality.ipStatistics.get_summary() \n
		Total number of packets from the measured RLP messages. As the list contains all packet types, this value is equal to the
		total number of RLP packets received. \n
			:return: structure: for return value, see the help for SummaryStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:EVDO:SIGNaling<Instance>:RXQuality:IPSTatistics:SUMMary?', self.__class__.SummaryStruct())

	# noinspection PyTypeChecker
	class PppTotalStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rx: int: Total size of data received Range: 0 KB to 0.999999E+6 KB
			- Tx: int: Total size of data transmitted Range: 0 KB to 0.999999E+6 KB"""
		__meta_args_list = [
			ArgStruct.scalar_int('Rx'),
			ArgStruct.scalar_int('Tx')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx: int = None
			self.Tx: int = None

	def get_ppp_total(self) -> PppTotalStruct:
		"""SCPI: SENSe:EVDO:SIGNaling<instance>:RXQuality:IPSTatistics:PPPTotal \n
		Snippet: value: PppTotalStruct = driver.sense.rxQuality.ipStatistics.get_ppp_total() \n
		Total number of bytes the R&S CMW received (Rx) and sent (Tx) since the beginning of the PPP connection. \n
			:return: structure: for return value, see the help for PppTotalStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:EVDO:SIGNaling<Instance>:RXQuality:IPSTatistics:PPPTotal?', self.__class__.PppTotalStruct())

	# noinspection PyTypeChecker
	class DrateStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rx: float: Data rate in receive direction Range: 0 kbit/s to 0.999999E+6 kbit/s
			- Tx: float: Data rate in transmit direction Range: 0 kbit/s to 0.999999E+6 kbit/s"""
		__meta_args_list = [
			ArgStruct.scalar_float('Rx'),
			ArgStruct.scalar_float('Tx')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx: float = None
			self.Tx: float = None

	def get_drate(self) -> DrateStruct:
		"""SCPI: SENSe:EVDO:SIGNaling<instance>:RXQuality:IPSTatistics:DRATe \n
		Snippet: value: DrateStruct = driver.sense.rxQuality.ipStatistics.get_drate() \n
		Current received data rate in kbit/s, averaged over the update period. \n
			:return: structure: for return value, see the help for DrateStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:EVDO:SIGNaling<Instance>:RXQuality:IPSTatistics:DRATe?', self.__class__.DrateStruct())
