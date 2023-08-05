from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AnAddress:
	"""AnAddress commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("anAddress", core, parent)

	def get_ipv(self) -> str:
		"""SCPI: SENSe:EVDO:SIGNaling<instance>:ANADdress:IPV<n> \n
		Snippet: value: str = driver.sense.anAddress.get_ipv() \n
		No command help available \n
			:return: an_address: No help available
		"""
		response = self._core.io.query_str('SENSe:EVDO:SIGNaling<Instance>:ANADdress:IPV4?')
		return trim_str_response(response)
