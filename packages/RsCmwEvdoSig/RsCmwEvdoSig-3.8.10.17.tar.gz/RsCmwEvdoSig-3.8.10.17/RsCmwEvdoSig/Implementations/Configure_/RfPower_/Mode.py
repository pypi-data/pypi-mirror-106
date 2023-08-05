from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("mode", core, parent)

	# noinspection PyTypeChecker
	def get_awgn(self) -> enums.AwgnMode:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RFPower:MODE:AWGN \n
		Snippet: value: enums.AwgnMode = driver.configure.rfPower.mode.get_awgn() \n
		Selects the operating mode of the AWGN generator. The AWGN level range (method RsCmwEvdoSig.Configure.RfPower.Level.awgn)
		depends on the operating mode. \n
			:return: awgn_mode: NORMal | HPOWer AWGN mode normal or high-power
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:RFPower:MODE:AWGN?')
		return Conversions.str_to_scalar_enum(response, enums.AwgnMode)

	def set_awgn(self, awgn_mode: enums.AwgnMode) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RFPower:MODE:AWGN \n
		Snippet: driver.configure.rfPower.mode.set_awgn(awgn_mode = enums.AwgnMode.HPOWer) \n
		Selects the operating mode of the AWGN generator. The AWGN level range (method RsCmwEvdoSig.Configure.RfPower.Level.awgn)
		depends on the operating mode. \n
			:param awgn_mode: NORMal | HPOWer AWGN mode normal or high-power
		"""
		param = Conversions.enum_scalar_to_str(awgn_mode, enums.AwgnMode)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:RFPower:MODE:AWGN {param}')
