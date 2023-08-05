from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpAddress:
	"""IpAddress commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ipAddress", core, parent)

	def set(self, index: enums.IpAddressIndex) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:MMONitor:IPADdress \n
		Snippet: driver.configure.mmonitor.ipAddress.set(index = enums.IpAddressIndex.IP1) \n
		Select/get the target IP address for message monitoring (method RsCmwEvdoSig.Configure.Mmonitor.enable) .
		The IP addresses are centrally managed from the 'Setup' dialog. \n
			:param index: IP1 | IP2 | IP3
		"""
		param = Conversions.enum_scalar_to_str(index, enums.IpAddressIndex)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:MMONitor:IPADdress {param}')

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Index: enums.IpAddressIndex: IP1 | IP2 | IP3
			- Ip_Address: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Index', enums.IpAddressIndex),
			ArgStruct.scalar_str('Ip_Address')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Index: enums.IpAddressIndex = None
			self.Ip_Address: str = None

	def get(self) -> GetStruct:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:MMONitor:IPADdress \n
		Snippet: value: GetStruct = driver.configure.mmonitor.ipAddress.get() \n
		Select/get the target IP address for message monitoring (method RsCmwEvdoSig.Configure.Mmonitor.enable) .
		The IP addresses are centrally managed from the 'Setup' dialog. \n
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:EVDO:SIGNaling<Instance>:MMONitor:IPADdress?', self.__class__.GetStruct())
