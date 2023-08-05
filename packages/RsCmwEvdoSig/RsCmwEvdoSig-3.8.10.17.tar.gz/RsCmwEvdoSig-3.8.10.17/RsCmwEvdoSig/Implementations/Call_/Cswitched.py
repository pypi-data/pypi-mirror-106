from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cswitched:
	"""Cswitched commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cswitched", core, parent)

	def set_action(self, cs_action: enums.CswitchedAction) -> None:
		"""SCPI: CALL:EVDO:SIGNaling<instance>:CSWitched:ACTion \n
		Snippet: driver.call.cswitched.set_action(cs_action = enums.CswitchedAction.CLOSe) \n
		Controls the setup and release of an 1xEV-DO connection. The command initiates a transition between different connection
		states; to be queried via method RsCmwEvdoSig.Cswitched.State.fetch. For details, refer to 'Connection States'. \n
			:param cs_action: CONNect | DISConnect | CLOSe | HANDoff Transition between connection states
		"""
		param = Conversions.enum_scalar_to_str(cs_action, enums.CswitchedAction)
		self._core.io.write_with_opc(f'CALL:EVDO:SIGNaling<Instance>:CSWitched:ACTion {param}')
