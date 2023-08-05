from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pilot:
	"""Pilot commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pilot", core, parent)

	def get_setting(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:PILot:SETTing \n
		Snippet: value: int = driver.configure.pilot.get_setting() \n
		Sets/gets the pilot to which subsequent pilot-related commands apply. \n
			:return: set_pilot: Range: 0 to 2
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:PILot:SETTing?')
		return Conversions.str_to_int(response)

	def set_setting(self, set_pilot: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:PILot:SETTing \n
		Snippet: driver.configure.pilot.set_setting(set_pilot = 1) \n
		Sets/gets the pilot to which subsequent pilot-related commands apply. \n
			:param set_pilot: Range: 0 to 2
		"""
		param = Conversions.decimal_value_to_str(set_pilot)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:PILot:SETTing {param}')
