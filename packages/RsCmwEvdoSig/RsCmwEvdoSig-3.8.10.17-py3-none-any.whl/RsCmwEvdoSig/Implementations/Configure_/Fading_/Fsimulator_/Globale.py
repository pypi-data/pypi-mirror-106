from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Globale:
	"""Globale commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("globale", core, parent)

	def get_seed(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:FADing:FSIMulator:GLOBal:SEED \n
		Snippet: value: int = driver.configure.fading.fsimulator.globale.get_seed() \n
		Sets the start seed for the pseudo-random fading algorithm. \n
			:return: seed: Range: 0 to 9
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:FADing:FSIMulator:GLOBal:SEED?')
		return Conversions.str_to_int(response)

	def set_seed(self, seed: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:FADing:FSIMulator:GLOBal:SEED \n
		Snippet: driver.configure.fading.fsimulator.globale.set_seed(seed = 1) \n
		Sets the start seed for the pseudo-random fading algorithm. \n
			:param seed: Range: 0 to 9
		"""
		param = Conversions.decimal_value_to_str(seed)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:FADing:FSIMulator:GLOBal:SEED {param}')
