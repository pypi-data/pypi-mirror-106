from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Path:
	"""Path commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: Path, default value after init: Path.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("path", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_path_get', 'repcap_path_set', repcap.Path.Nr1)

	def repcap_path_set(self, enum_value: repcap.Path) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Path.Default
		Default value after init: Path.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_path_get(self) -> repcap.Path:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Sample_Rate: enums.SampleRate: M100 Fixed value, indicating a sample rate of 100 Msps (100 MHz)
			- Pep: float: Peak envelope power of the baseband signal Range: -60 dBFS to 0 dBFS , Unit: dBFS
			- Crest_Factor: float: Crest factor of the baseband signal Range: 0 dB to 60 dB, Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Sample_Rate', enums.SampleRate),
			ArgStruct.scalar_float('Pep'),
			ArgStruct.scalar_float('Crest_Factor')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Sample_Rate: enums.SampleRate = None
			self.Pep: float = None
			self.Crest_Factor: float = None

	def get(self, path=repcap.Path.Default) -> GetStruct:
		"""SCPI: SENSe:EVDO:SIGNaling<instance>:IQOut:PATH<n> \n
		Snippet: value: GetStruct = driver.sense.iqOut.path.get(path = repcap.Path.Default) \n
		Queries properties of the baseband signal at the I/Q output. \n
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Path')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		path_cmd_val = self._base.get_repcap_cmd_value(path, repcap.Path)
		return self._core.io.query_struct(f'SENSe:EVDO:SIGNaling<Instance>:IQOut:PATH{path_cmd_val}?', self.__class__.GetStruct())

	def clone(self) -> 'Path':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Path(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
