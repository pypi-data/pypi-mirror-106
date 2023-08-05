from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ack:
	"""Ack commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ack", core, parent)

	# noinspection PyTypeChecker
	def get_fmode(self) -> enums.Fmode:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:APPLication:FTAP:ACK:FMODe \n
		Snippet: value: enums.Fmode = driver.configure.layer.application.ftap.ack.get_fmode() \n
		Configures the ACK channel in the reverse signal that the AT uses for the acknowledgment of test packets received on the
		forward traffic channel. \n
			:return: fmode: NUSed | AALWays | NAALways Not used, ACK always, NACK always
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:LAYer:APPLication:FTAP:ACK:FMODe?')
		return Conversions.str_to_scalar_enum(response, enums.Fmode)

	def set_fmode(self, fmode: enums.Fmode) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:LAYer:APPLication:FTAP:ACK:FMODe \n
		Snippet: driver.configure.layer.application.ftap.ack.set_fmode(fmode = enums.Fmode.AALWays) \n
		Configures the ACK channel in the reverse signal that the AT uses for the acknowledgment of test packets received on the
		forward traffic channel. \n
			:param fmode: NUSed | AALWays | NAALways Not used, ACK always, NACK always
		"""
		param = Conversions.enum_scalar_to_str(fmode, enums.Fmode)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:LAYer:APPLication:FTAP:ACK:FMODe {param}')
