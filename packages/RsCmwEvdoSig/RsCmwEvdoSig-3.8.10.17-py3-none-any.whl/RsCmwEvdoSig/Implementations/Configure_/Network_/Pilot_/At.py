from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class At:
	"""At commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("at", core, parent)

	def get_assigned(self) -> bool:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:PILot:AT:ASSigned \n
		Snippet: value: bool = driver.configure.network.pilot.at.get_assigned() \n
		Sets/gets the assignment state of a pilot. Assigning a pilot to the AT adds the pilot to the AT's active set (managed by
		the AN via TrafficChannelAssignment messages) . Preselect the related pilot using the method RsCmwEvdoSig.Configure.Pilot.
		setting command. \n
			:return: assigned_to_at: OFF | ON A pilot can only be assigned to the AT if it is activated on the AN (see method RsCmwEvdoSig.Configure.Network.Pilot.An.active) . Note that pilot 0 cannot be unassigned. ON for pilot 0, OFF for pilots 1 and 2
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:NETWork:PILot:AT:ASSigned?')
		return Conversions.str_to_bool(response)

	def set_assigned(self, assigned_to_at: bool) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:PILot:AT:ASSigned \n
		Snippet: driver.configure.network.pilot.at.set_assigned(assigned_to_at = False) \n
		Sets/gets the assignment state of a pilot. Assigning a pilot to the AT adds the pilot to the AT's active set (managed by
		the AN via TrafficChannelAssignment messages) . Preselect the related pilot using the method RsCmwEvdoSig.Configure.Pilot.
		setting command. \n
			:param assigned_to_at: OFF | ON A pilot can only be assigned to the AT if it is activated on the AN (see method RsCmwEvdoSig.Configure.Network.Pilot.An.active) . Note that pilot 0 cannot be unassigned. ON for pilot 0, OFF for pilots 1 and 2
		"""
		param = Conversions.bool_to_str(assigned_to_at)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:NETWork:PILot:AT:ASSigned {param}')

	def get_acquired(self) -> bool:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:PILot:AT:ACQuired \n
		Snippet: value: bool = driver.configure.network.pilot.at.get_acquired() \n
		Queries if a pilot is being acquired by the AT, i.e. if the corresponding carrier is carrying traffic. Preselect the
		related pilot using the method RsCmwEvdoSig.Configure.Pilot.setting command.
			INTRO_CMD_HELP: Note that a pilot can only be acquired by the AT if it is: \n
			- Activated on the cell (using method RsCmwEvdoSig.Configure.Network.Pilot.An.active)
			- Assigned to the AT (using method RsCmwEvdoSig.Configure.Network.Pilot.At.assigned )
		Use method RsCmwEvdoSig.Configure.Cstatus.aflCarriers to obtain more information on the carrier states. \n
			:return: acquired_by_at: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:NETWork:PILot:AT:ACQuired?')
		return Conversions.str_to_bool(response)
