from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Security:
	"""Security commands group definition. 4 total commands, 0 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("security", core, parent)

	def get_skey(self) -> str:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:SECurity:SKEY \n
		Snippet: value: str = driver.configure.network.security.get_skey() \n
		Sets/gets the shared authentication key of the EAP-AKA' access authentication. \n
			:return: secret_key: 32 hexadecimal digits
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:NETWork:SECurity:SKEY?')
		return trim_str_response(response)

	def set_skey(self, secret_key: str) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:SECurity:SKEY \n
		Snippet: driver.configure.network.security.set_skey(secret_key = r1) \n
		Sets/gets the shared authentication key of the EAP-AKA' access authentication. \n
			:param secret_key: 32 hexadecimal digits
		"""
		param = Conversions.value_to_str(secret_key)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:NETWork:SECurity:SKEY {param}')

	def get_opc(self) -> str:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:SECurity:OPC \n
		Snippet: value: str = driver.configure.network.security.get_opc() \n
		Sets/gets the operator variant Key (OPC) of the EAP-AKA' access authentication. \n
			:return: operator_var_key: 32 hexadecimal digits
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:NETWork:SECurity:OPC?')
		return trim_str_response(response)

	def set_opc(self, operator_var_key: str) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:SECurity:OPC \n
		Snippet: driver.configure.network.security.set_opc(operator_var_key = r1) \n
		Sets/gets the operator variant Key (OPC) of the EAP-AKA' access authentication. \n
			:param operator_var_key: 32 hexadecimal digits
		"""
		param = Conversions.value_to_str(operator_var_key)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:NETWork:SECurity:OPC {param}')

	def get_authenticate(self) -> str:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:SECurity:AUTHenticat \n
		Snippet: value: str = driver.configure.network.security.get_authenticate() \n
		Sets/gets the authentication management field (AMF) of the EAP-AKA' access authentication. \n
			:return: authentication: 4 hexadecimal digits
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:NETWork:SECurity:AUTHenticat?')
		return trim_str_response(response)

	def set_authenticate(self, authentication: str) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:SECurity:AUTHenticat \n
		Snippet: driver.configure.network.security.set_authenticate(authentication = r1) \n
		Sets/gets the authentication management field (AMF) of the EAP-AKA' access authentication. \n
			:param authentication: 4 hexadecimal digits
		"""
		param = Conversions.value_to_str(authentication)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:NETWork:SECurity:AUTHenticat {param}')

	def get_sqn(self) -> str:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:SECurity:SQN \n
		Snippet: value: str = driver.configure.network.security.get_sqn() \n
		Sets/gets the sequence number sent to the AT in the EAP-request / AKA'-challenge message. \n
			:return: sequence_number: 12 hexadecimal digits
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:NETWork:SECurity:SQN?')
		return trim_str_response(response)

	def set_sqn(self, sequence_number: str) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:SECurity:SQN \n
		Snippet: driver.configure.network.security.set_sqn(sequence_number = r1) \n
		Sets/gets the sequence number sent to the AT in the EAP-request / AKA'-challenge message. \n
			:param sequence_number: 12 hexadecimal digits
		"""
		param = Conversions.value_to_str(sequence_number)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:NETWork:SECurity:SQN {param}')
