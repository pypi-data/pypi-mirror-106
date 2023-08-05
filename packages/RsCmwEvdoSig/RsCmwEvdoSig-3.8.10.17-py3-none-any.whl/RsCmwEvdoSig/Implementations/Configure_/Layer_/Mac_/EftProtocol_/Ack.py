from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ack:
	"""Ack commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ack", core, parent)

	def get_cgain(self) -> float:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:MAC:EFTProtocol:ACK:CGAin \n
		Snippet: value: float = driver.configure.layer.mac.eftProtocol.ack.get_cgain() \n
		Defines the ratio of the power of the reverse ACK channel to the power of the reverse pilot channel on a carrier (for
		subtype 2 and 3 signals only) . Preselect the related carrier using the method RsCmwEvdoSig.Configure.Carrier.
		setting command. \n
			:return: ackc_gain: Range: -3 dB to 6 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:MAC:EFTProtocol:ACK:CGAin?')
		return Conversions.str_to_float(response)

	def set_cgain(self, ackc_gain: float) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:MAC:EFTProtocol:ACK:CGAin \n
		Snippet: driver.configure.layer.mac.eftProtocol.ack.set_cgain(ackc_gain = 1.0) \n
		Defines the ratio of the power of the reverse ACK channel to the power of the reverse pilot channel on a carrier (for
		subtype 2 and 3 signals only) . Preselect the related carrier using the method RsCmwEvdoSig.Configure.Carrier.
		setting command. \n
			:param ackc_gain: Range: -3 dB to 6 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(ackc_gain)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:LAYer:MAC:EFTProtocol:ACK:CGAin {param}')
