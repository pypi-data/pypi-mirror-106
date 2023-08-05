from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Session:
	"""Session commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("session", core, parent)

	def get_is_timeout(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:SESSion:ISTimeout \n
		Snippet: value: int = driver.configure.layer.session.get_is_timeout() \n
		Specifies the time after which the AT, if it does not detect any traffic from the R&S CMW directed to it, closes the
		session. \n
			:return: is_timeout: Range: 0 min to 65.535E+3 min
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:SESSion:ISTimeout?')
		return Conversions.str_to_int(response)

	def set_is_timeout(self, is_timeout: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:SESSion:ISTimeout \n
		Snippet: driver.configure.layer.session.set_is_timeout(is_timeout = 1) \n
		Specifies the time after which the AT, if it does not detect any traffic from the R&S CMW directed to it, closes the
		session. \n
			:param is_timeout: Range: 0 min to 65.535E+3 min
		"""
		param = Conversions.decimal_value_to_str(is_timeout)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:LAYer:SESSion:ISTimeout {param}')

	def get_sn_included(self) -> bool:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:SESSion:SNINcluded \n
		Snippet: value: bool = driver.configure.layer.session.get_sn_included() \n
		Specifies whether the ATISubnetMask field and the UATI104 field are included in the UATI assignment message. \n
			:return: sn_included: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:SESSion:SNINcluded?')
		return Conversions.str_to_bool(response)

	def set_sn_included(self, sn_included: bool) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:SESSion:SNINcluded \n
		Snippet: driver.configure.layer.session.set_sn_included(sn_included = False) \n
		Specifies whether the ATISubnetMask field and the UATI104 field are included in the UATI assignment message. \n
			:param sn_included: OFF | ON
		"""
		param = Conversions.bool_to_str(sn_included)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:LAYer:SESSion:SNINcluded {param}')
