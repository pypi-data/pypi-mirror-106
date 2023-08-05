from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Length:
	"""Length commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("length", core, parent)

	def set(self, segment_length: int, segment=repcap.Segment.Default) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RPControl:SEGMent<nr>:LENGth \n
		Snippet: driver.configure.rpControl.segment.length.set(segment_length = 1, segment = repcap.Segment.Default) \n
		Sets the length of the segment of the user-specific power control bits. \n
			:param segment_length: Segment length Range: 0 bits to 128 bits , Unit: bit
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')"""
		param = Conversions.decimal_value_to_str(segment_length)
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:RPControl:SEGMent{segment_cmd_val}:LENGth {param}')

	def get(self, segment=repcap.Segment.Default) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RPControl:SEGMent<nr>:LENGth \n
		Snippet: value: int = driver.configure.rpControl.segment.length.get(segment = repcap.Segment.Default) \n
		Sets the length of the segment of the user-specific power control bits. \n
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
			:return: segment_length: Segment length Range: 0 bits to 128 bits , Unit: bit"""
		segment_cmd_val = self._base.get_repcap_cmd_value(segment, repcap.Segment)
		response = self._core.io.query_str(f'CONFigure:EVDO:SIGNaling<Instance>:RPControl:SEGMent{segment_cmd_val}:LENGth?')
		return Conversions.str_to_int(response)
