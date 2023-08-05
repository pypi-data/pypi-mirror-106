from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sector:
	"""Sector commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sector", core, parent)

	def get_setting(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:SECTor:SETTing \n
		Snippet: value: int = driver.configure.sector.get_setting() \n
		Sets/gets the sector to which subsequent sector-related commands apply. \n
			:return: set_sector: Only sector 0 supported in the current release Range: 0 to 0
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:SECTor:SETTing?')
		return Conversions.str_to_int(response)

	def set_setting(self, set_sector: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:SECTor:SETTing \n
		Snippet: driver.configure.sector.set_setting(set_sector = 1) \n
		Sets/gets the sector to which subsequent sector-related commands apply. \n
			:param set_sector: Only sector 0 supported in the current release Range: 0 to 0
		"""
		param = Conversions.decimal_value_to_str(set_sector)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:SECTor:SETTing {param}')
