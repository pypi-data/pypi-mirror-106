from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Per:
	"""Per commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("per", core, parent)

	# noinspection PyTypeChecker
	def get_evaluation(self) -> enums.PerEvaluation:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:LIMit:PER:EVALuation \n
		Snippet: value: enums.PerEvaluation = driver.configure.rxQuality.limit.per.get_evaluation() \n
		Defines whether the limits specified for the forward and reverse link packet error rate (PER) measurements is evaluated
		per carrier or over all carriers. This setting only affects multi-carrier evaluations. \n
			:return: limit_evaluation: PERCarrier | ALLCarriers
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:RXQuality:LIMit:PER:EVALuation?')
		return Conversions.str_to_scalar_enum(response, enums.PerEvaluation)

	def set_evaluation(self, limit_evaluation: enums.PerEvaluation) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:RXQuality:LIMit:PER:EVALuation \n
		Snippet: driver.configure.rxQuality.limit.per.set_evaluation(limit_evaluation = enums.PerEvaluation.ALLCarriers) \n
		Defines whether the limits specified for the forward and reverse link packet error rate (PER) measurements is evaluated
		per carrier or over all carriers. This setting only affects multi-carrier evaluations. \n
			:param limit_evaluation: PERCarrier | ALLCarriers
		"""
		param = Conversions.enum_scalar_to_str(limit_evaluation, enums.PerEvaluation)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:RXQuality:LIMit:PER:EVALuation {param}')
