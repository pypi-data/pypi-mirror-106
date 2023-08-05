from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class At:
	"""At commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("at", core, parent)

	def get_assigned(self) -> bool:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:HANDoff:NETWork:PILot:AT:ASSigned \n
		Snippet: value: bool = driver.configure.handoff.network.pilot.at.get_assigned() \n
		Sets/gets the assignment state of a pilot in the handoff destination cell. Assigning a pilot to the AT adds the pilot to
		the AT's active set in the destination cell. Preselect the related pilot using the method RsCmwEvdoSig.Configure.Pilot.
		setting command. \n
			:return: assigned_to_at: OFF | ON A pilot can only be assigned to the AT if it is activated on the destination cell (see method RsCmwEvdoSig.Configure.Handoff.Network.Pilot.An.active) . Note that pilot 0 cannot be unassigned.
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:HANDoff:NETWork:PILot:AT:ASSigned?')
		return Conversions.str_to_bool(response)

	def set_assigned(self, assigned_to_at: bool) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:HANDoff:NETWork:PILot:AT:ASSigned \n
		Snippet: driver.configure.handoff.network.pilot.at.set_assigned(assigned_to_at = False) \n
		Sets/gets the assignment state of a pilot in the handoff destination cell. Assigning a pilot to the AT adds the pilot to
		the AT's active set in the destination cell. Preselect the related pilot using the method RsCmwEvdoSig.Configure.Pilot.
		setting command. \n
			:param assigned_to_at: OFF | ON A pilot can only be assigned to the AT if it is activated on the destination cell (see method RsCmwEvdoSig.Configure.Handoff.Network.Pilot.An.active) . Note that pilot 0 cannot be unassigned.
		"""
		param = Conversions.bool_to_str(assigned_to_at)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:HANDoff:NETWork:PILot:AT:ASSigned {param}')
