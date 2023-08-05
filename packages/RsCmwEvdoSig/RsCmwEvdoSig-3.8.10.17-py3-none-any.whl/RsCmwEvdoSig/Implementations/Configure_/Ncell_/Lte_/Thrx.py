from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Thrx:
	"""Thrx commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: NeighborCell, default value after init: NeighborCell.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("thrx", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_neighborCell_get', 'repcap_neighborCell_set', repcap.NeighborCell.Nr1)

	def repcap_neighborCell_set(self, enum_value: repcap.NeighborCell) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to NeighborCell.Default
		Default value after init: NeighborCell.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_neighborCell_get(self) -> repcap.NeighborCell:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	def set(self, lte_thresh_x: int, neighborCell=repcap.NeighborCell.Default) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NCELl:LTE:THRX<n> \n
		Snippet: driver.configure.ncell.lte.thrx.set(lte_thresh_x = 1, neighborCell = repcap.NeighborCell.Default) \n
		Specifies the minimum required quality threshold of the reselection target cell. \n
			:param lte_thresh_x: Range: 0 to 31
			:param neighborCell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Thrx')"""
		param = Conversions.decimal_value_to_str(lte_thresh_x)
		neighborCell_cmd_val = self._base.get_repcap_cmd_value(neighborCell, repcap.NeighborCell)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:NCELl:LTE:THRX{neighborCell_cmd_val} {param}')

	def get(self, neighborCell=repcap.NeighborCell.Default) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NCELl:LTE:THRX<n> \n
		Snippet: value: int = driver.configure.ncell.lte.thrx.get(neighborCell = repcap.NeighborCell.Default) \n
		Specifies the minimum required quality threshold of the reselection target cell. \n
			:param neighborCell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Thrx')
			:return: lte_thresh_x: Range: 0 to 31"""
		neighborCell_cmd_val = self._base.get_repcap_cmd_value(neighborCell, repcap.NeighborCell)
		response = self._core.io.query_str(f'CONFigure:EVDO:SIGNaling<Instance>:NCELl:LTE:THRX{neighborCell_cmd_val}?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Thrx':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Thrx(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
