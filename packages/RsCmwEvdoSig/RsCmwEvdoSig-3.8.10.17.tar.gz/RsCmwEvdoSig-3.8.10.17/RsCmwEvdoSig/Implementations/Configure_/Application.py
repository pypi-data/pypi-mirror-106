from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Application:
	"""Application commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("application", core, parent)

	def get_dsignaling(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:APPLication:DSIGnaling \n
		Snippet: value: int = driver.configure.application.get_dsignaling() \n
		Queries the stream and the state of the default signaling application. The response is fixed: The default signaling
		application is always enabled and assigned to stream 0. \n
			:return: stream: Range: 0
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:APPLication:DSIGnaling?')
		return Conversions.str_to_int(response)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.ApplicationMode:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:APPLication:MODE \n
		Snippet: value: enums.ApplicationMode = driver.configure.application.get_mode() \n
		Selects the application to be instantiated. \n
			:return: mode: FWD | REV | FAR | PACKet FWD: forward test application REV: reverse test application FAR: forward and reverse test application PACKet: packet application
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:APPLication:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ApplicationMode)

	def set_mode(self, mode: enums.ApplicationMode) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:APPLication:MODE \n
		Snippet: driver.configure.application.set_mode(mode = enums.ApplicationMode.FAR) \n
		Selects the application to be instantiated. \n
			:param mode: FWD | REV | FAR | PACKet FWD: forward test application REV: reverse test application FAR: forward and reverse test application PACKet: packet application
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ApplicationMode)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:APPLication:MODE {param}')

	def get_value(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:APPLication \n
		Snippet: value: int = driver.configure.application.get_value() \n
		Queries the stream occupied by the configured session application (see method RsCmwEvdoSig.Configure.Application.mode) .
		Setting this value has no effect as the selected stream is a result of the session negotiation. \n
			:return: stream: Range: 1 to 3
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:APPLication?')
		return Conversions.str_to_int(response)

	def set_value(self, stream: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:APPLication \n
		Snippet: driver.configure.application.set_value(stream = 1) \n
		Queries the stream occupied by the configured session application (see method RsCmwEvdoSig.Configure.Application.mode) .
		Setting this value has no effect as the selected stream is a result of the session negotiation. \n
			:param stream: Range: 1 to 3
		"""
		param = Conversions.decimal_value_to_str(stream)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:APPLication {param}')
