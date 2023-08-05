from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mac:
	"""Mac commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("mac", core, parent)

	# noinspection PyTypeChecker
	class IndexStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rev_0: int: Range: 5 to 63
			- Rev_A: int: Range: 5 to 127
			- Rev_B: int: Range: 5 to 127"""
		__meta_args_list = [
			ArgStruct.scalar_int('Rev_0'),
			ArgStruct.scalar_int('Rev_A'),
			ArgStruct.scalar_int('Rev_B')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rev_0: int = None
			self.Rev_A: int = None
			self.Rev_B: int = None

	def get_index(self) -> IndexStruct:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:MAC:INDex \n
		Snippet: value: IndexStruct = driver.configure.mac.get_index() \n
		Sets/gets a pilot's (associated carrier's) MAC index. Preselect the related pilot using the method RsCmwEvdoSig.Configure.
		Pilot.setting command. \n
			:return: structure: for return value, see the help for IndexStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:EVDO:SIGNaling<Instance>:MAC:INDex?', self.__class__.IndexStruct())

	def set_index(self, value: IndexStruct) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:MAC:INDex \n
		Snippet: driver.configure.mac.set_index(value = IndexStruct()) \n
		Sets/gets a pilot's (associated carrier's) MAC index. Preselect the related pilot using the method RsCmwEvdoSig.Configure.
		Pilot.setting command. \n
			:param value: see the help for IndexStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:EVDO:SIGNaling<Instance>:MAC:INDex', value)
