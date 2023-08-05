from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Result:
	"""Result commands group definition. 5 total commands, 0 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("result", core, parent)

	def get_fl_per(self) -> bool:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:RESult:FLPer \n
		Snippet: value: bool = driver.configure.rxQuality.result.get_fl_per() \n
		Enables/disables the view of the following RX measurements as indicated by the last mnemonics: 'Forward Link PER',
		'Forward Link Throughput', 'Reverse Link PER', 'Reverse Link Throughput' and 'RLP & IP Statistics' (data) .
		For a disabled view, results are not displayed or calculated. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:RXQuality:RESult:FLPer?')
		return Conversions.str_to_bool(response)

	def set_fl_per(self, enable: bool) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:RESult:FLPer \n
		Snippet: driver.configure.rxQuality.result.set_fl_per(enable = False) \n
		Enables/disables the view of the following RX measurements as indicated by the last mnemonics: 'Forward Link PER',
		'Forward Link Throughput', 'Reverse Link PER', 'Reverse Link Throughput' and 'RLP & IP Statistics' (data) .
		For a disabled view, results are not displayed or calculated. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:RXQuality:RESult:FLPer {param}')

	def get_rl_per(self) -> bool:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:RESult:RLPer \n
		Snippet: value: bool = driver.configure.rxQuality.result.get_rl_per() \n
		Enables/disables the view of the following RX measurements as indicated by the last mnemonics: 'Forward Link PER',
		'Forward Link Throughput', 'Reverse Link PER', 'Reverse Link Throughput' and 'RLP & IP Statistics' (data) .
		For a disabled view, results are not displayed or calculated. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:RXQuality:RESult:RLPer?')
		return Conversions.str_to_bool(response)

	def set_rl_per(self, enable: bool) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:RESult:RLPer \n
		Snippet: driver.configure.rxQuality.result.set_rl_per(enable = False) \n
		Enables/disables the view of the following RX measurements as indicated by the last mnemonics: 'Forward Link PER',
		'Forward Link Throughput', 'Reverse Link PER', 'Reverse Link Throughput' and 'RLP & IP Statistics' (data) .
		For a disabled view, results are not displayed or calculated. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:RXQuality:RESult:RLPer {param}')

	def get_fl_performance(self) -> bool:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:RESult:FLPFormance \n
		Snippet: value: bool = driver.configure.rxQuality.result.get_fl_performance() \n
		Enables/disables the view of the following RX measurements as indicated by the last mnemonics: 'Forward Link PER',
		'Forward Link Throughput', 'Reverse Link PER', 'Reverse Link Throughput' and 'RLP & IP Statistics' (data) .
		For a disabled view, results are not displayed or calculated. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:RXQuality:RESult:FLPFormance?')
		return Conversions.str_to_bool(response)

	def set_fl_performance(self, enable: bool) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:RESult:FLPFormance \n
		Snippet: driver.configure.rxQuality.result.set_fl_performance(enable = False) \n
		Enables/disables the view of the following RX measurements as indicated by the last mnemonics: 'Forward Link PER',
		'Forward Link Throughput', 'Reverse Link PER', 'Reverse Link Throughput' and 'RLP & IP Statistics' (data) .
		For a disabled view, results are not displayed or calculated. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:RXQuality:RESult:FLPFormance {param}')

	def get_rl_performance(self) -> bool:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:RESult:RLPFormance \n
		Snippet: value: bool = driver.configure.rxQuality.result.get_rl_performance() \n
		Enables/disables the view of the following RX measurements as indicated by the last mnemonics: 'Forward Link PER',
		'Forward Link Throughput', 'Reverse Link PER', 'Reverse Link Throughput' and 'RLP & IP Statistics' (data) .
		For a disabled view, results are not displayed or calculated. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:RXQuality:RESult:RLPFormance?')
		return Conversions.str_to_bool(response)

	def set_rl_performance(self, enable: bool) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:RESult:RLPFormance \n
		Snippet: driver.configure.rxQuality.result.set_rl_performance(enable = False) \n
		Enables/disables the view of the following RX measurements as indicated by the last mnemonics: 'Forward Link PER',
		'Forward Link Throughput', 'Reverse Link PER', 'Reverse Link Throughput' and 'RLP & IP Statistics' (data) .
		For a disabled view, results are not displayed or calculated. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:RXQuality:RESult:RLPFormance {param}')

	def get_ip_statistics(self) -> bool:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:RESult:IPSTatistics \n
		Snippet: value: bool = driver.configure.rxQuality.result.get_ip_statistics() \n
		Enables/disables the view of the following RX measurements as indicated by the last mnemonics: 'Forward Link PER',
		'Forward Link Throughput', 'Reverse Link PER', 'Reverse Link Throughput' and 'RLP & IP Statistics' (data) .
		For a disabled view, results are not displayed or calculated. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:RXQuality:RESult:IPSTatistics?')
		return Conversions.str_to_bool(response)

	def set_ip_statistics(self, enable: bool) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:RESult:IPSTatistics \n
		Snippet: driver.configure.rxQuality.result.set_ip_statistics(enable = False) \n
		Enables/disables the view of the following RX measurements as indicated by the last mnemonics: 'Forward Link PER',
		'Forward Link Throughput', 'Reverse Link PER', 'Reverse Link Throughput' and 'RLP & IP Statistics' (data) .
		For a disabled view, results are not displayed or calculated. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:RXQuality:RESult:IPSTatistics {param}')
