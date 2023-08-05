from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ipv:
	"""Ipv commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: IpAddress, default value after init: IpAddress.Version4"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ipv", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_ipAddress_get', 'repcap_ipAddress_set', repcap.IpAddress.Version4)

	def repcap_ipAddress_set(self, enum_value: repcap.IpAddress) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to IpAddress.Default
		Default value after init: IpAddress.Version4"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_ipAddress_get(self) -> repcap.IpAddress:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	def get(self, ipAddress=repcap.IpAddress.Default) -> str:
		"""SCPI: SENSe:EVDO:SIGNaling<instance>:ATADdress:IPV<n> \n
		Snippet: value: str = driver.sense.atAddress.ipv.get(ipAddress = repcap.IpAddress.Default) \n
		Returns the IPv4 address (<n> = 4) or the IPv6 prefix (<n> = 6) assigned to the AT by the DAU. \n
			:param ipAddress: optional repeated capability selector. Default value: Version4 (settable in the interface 'Ipv')
			:return: ip_address: IP address/prefix as string"""
		ipAddress_cmd_val = self._base.get_repcap_cmd_value(ipAddress, repcap.IpAddress)
		response = self._core.io.query_str(f'SENSe:EVDO:SIGNaling<Instance>:ATADdress:IPV{ipAddress_cmd_val}?')
		return trim_str_response(response)

	def clone(self) -> 'Ipv':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ipv(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
