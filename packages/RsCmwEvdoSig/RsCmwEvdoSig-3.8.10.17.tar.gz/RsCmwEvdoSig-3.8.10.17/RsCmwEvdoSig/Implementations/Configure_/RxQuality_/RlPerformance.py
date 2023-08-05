from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RlPerformance:
	"""RlPerformance commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rlPerformance", core, parent)

	def get_mframes(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:RLPFormance:MFRames \n
		Snippet: value: int = driver.configure.rxQuality.rlPerformance.get_mframes() \n
		Defines the maximum duration of the 'Forward Link Throughput' / 'Reverse Link Throughput' measurement as a number of 26.
		66 ms CDMA2000 frames. \n
			:return: max_frames: Range: 1 to 10000
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:RXQuality:RLPFormance:MFRames?')
		return Conversions.str_to_int(response)

	def set_mframes(self, max_frames: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:RLPFormance:MFRames \n
		Snippet: driver.configure.rxQuality.rlPerformance.set_mframes(max_frames = 1) \n
		Defines the maximum duration of the 'Forward Link Throughput' / 'Reverse Link Throughput' measurement as a number of 26.
		66 ms CDMA2000 frames. \n
			:param max_frames: Range: 1 to 10000
		"""
		param = Conversions.decimal_value_to_str(max_frames)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:RXQuality:RLPFormance:MFRames {param}')
