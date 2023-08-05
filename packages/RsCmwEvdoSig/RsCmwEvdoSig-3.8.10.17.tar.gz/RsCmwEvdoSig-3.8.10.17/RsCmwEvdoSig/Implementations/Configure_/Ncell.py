from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ncell:
	"""Ncell commands group definition. 15 total commands, 4 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ncell", core, parent)

	@property
	def all(self):
		"""all commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_all'):
			from .Ncell_.All import All
			self._all = All(self._core, self._base)
		return self._all

	@property
	def evdo(self):
		"""evdo commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_evdo'):
			from .Ncell_.Evdo import Evdo
			self._evdo = Evdo(self._core, self._base)
		return self._evdo

	@property
	def cdma(self):
		"""cdma commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cdma'):
			from .Ncell_.Cdma import Cdma
			self._cdma = Cdma(self._core, self._base)
		return self._cdma

	@property
	def lte(self):
		"""lte commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_lte'):
			from .Ncell_.Lte import Lte
			self._lte = Lte(self._core, self._base)
		return self._lte

	def get_rlm_eutra(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NCELl:RLMeutra \n
		Snippet: value: int = driver.configure.ncell.get_rlm_eutra() \n
		Configures the low reselection threshold value for LTE neighbor cells. \n
			:return: rx_lev_min_eutra_common: No help available
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:NCELl:RLMeutra?')
		return Conversions.str_to_int(response)

	def set_rlm_eutra(self, rx_lev_min_eutra_common: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NCELl:RLMeutra \n
		Snippet: driver.configure.ncell.set_rlm_eutra(rx_lev_min_eutra_common = 1) \n
		Configures the low reselection threshold value for LTE neighbor cells. \n
			:param rx_lev_min_eutra_common: Range: 0 to 96
		"""
		param = Conversions.decimal_value_to_str(rx_lev_min_eutra_common)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:NCELl:RLMeutra {param}')

	def get_thr_serving(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NCELl:THRServing \n
		Snippet: value: int = driver.configure.ncell.get_thr_serving() \n
		Specifies the limit for pilot power level below which the AT triggers cell reselection to a neighbor cell in the
		candidate set. \n
			:return: thresh_serving: Range: 0 to 63
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:NCELl:THRServing?')
		return Conversions.str_to_int(response)

	def set_thr_serving(self, thresh_serving: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NCELl:THRServing \n
		Snippet: driver.configure.ncell.set_thr_serving(thresh_serving = 1) \n
		Specifies the limit for pilot power level below which the AT triggers cell reselection to a neighbor cell in the
		candidate set. \n
			:param thresh_serving: Range: 0 to 63
		"""
		param = Conversions.decimal_value_to_str(thresh_serving)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:NCELl:THRServing {param}')

	def get_mr_timer(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NCELl:MRTimer \n
		Snippet: value: int = driver.configure.ncell.get_mr_timer() \n
		Maximum time for the access terminal to execute the cell reselection. \n
			:return: max_reselection_timer: No help available
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:NCELl:MRTimer?')
		return Conversions.str_to_int(response)

	def set_mr_timer(self, max_reselection_timer: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NCELl:MRTimer \n
		Snippet: driver.configure.ncell.set_mr_timer(max_reselection_timer = 1) \n
		Maximum time for the access terminal to execute the cell reselection. \n
			:param max_reselection_timer: Range: 0 to 15
		"""
		param = Conversions.decimal_value_to_str(max_reselection_timer)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:NCELl:MRTimer {param}')

	def clone(self) -> 'Ncell':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ncell(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
