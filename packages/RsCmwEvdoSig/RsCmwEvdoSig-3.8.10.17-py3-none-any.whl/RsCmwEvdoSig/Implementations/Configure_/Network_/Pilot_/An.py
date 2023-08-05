from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class An:
	"""An commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("an", core, parent)

	def get_active(self) -> bool:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:PILot:AN:ACTive \n
		Snippet: value: bool = driver.configure.network.pilot.an.get_active() \n
		Sets/gets the state of a pilot in the cell implemented by the signaling application. Preselect the related pilot using
		the method RsCmwEvdoSig.Configure.Pilot.setting command. \n
			:return: active_on_an: OFF | ON When set to OFF, the related carrier is physically disabled on the cell. Note that pilot 0 cannot be turned OFF.
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:NETWork:PILot:AN:ACTive?')
		return Conversions.str_to_bool(response)

	def set_active(self, active_on_an: bool) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:PILot:AN:ACTive \n
		Snippet: driver.configure.network.pilot.an.set_active(active_on_an = False) \n
		Sets/gets the state of a pilot in the cell implemented by the signaling application. Preselect the related pilot using
		the method RsCmwEvdoSig.Configure.Pilot.setting command. \n
			:param active_on_an: OFF | ON When set to OFF, the related carrier is physically disabled on the cell. Note that pilot 0 cannot be turned OFF.
		"""
		param = Conversions.bool_to_str(active_on_an)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:NETWork:PILot:AN:ACTive {param}')
