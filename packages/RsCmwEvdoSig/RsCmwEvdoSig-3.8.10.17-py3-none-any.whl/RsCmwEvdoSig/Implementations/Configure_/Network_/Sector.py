from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sector:
	"""Sector commands group definition. 9 total commands, 1 Sub-groups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sector", core, parent)

	@property
	def id(self):
		"""id commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_id'):
			from .Sector_.Id import Id
			self._id = Id(self._core, self._base)
		return self._id

	def get_pn_offset(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:SECTor:PNOFfset \n
		Snippet: value: int = driver.configure.network.sector.get_pn_offset() \n
		Defines the pilot PN offset index of the generated forward 1xEV-DO signal. \n
			:return: pn_offset: Range: 0 to 511
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:NETWork:SECTor:PNOFfset?')
		return Conversions.str_to_int(response)

	def set_pn_offset(self, pn_offset: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:SECTor:PNOFfset \n
		Snippet: driver.configure.network.sector.set_pn_offset(pn_offset = 1) \n
		Defines the pilot PN offset index of the generated forward 1xEV-DO signal. \n
			:param pn_offset: Range: 0 to 511
		"""
		param = Conversions.decimal_value_to_str(pn_offset)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:NETWork:SECTor:PNOFfset {param}')

	def get_clr_code(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:SECTor:CLRCode \n
		Snippet: value: int = driver.configure.network.sector.get_clr_code() \n
		Defines the 8-bit color code of the sector. \n
			:return: clr_code: Range: 0 to 255
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:NETWork:SECTor:CLRCode?')
		return Conversions.str_to_int(response)

	def set_clr_code(self, clr_code: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:SECTor:CLRCode \n
		Snippet: driver.configure.network.sector.set_clr_code(clr_code = 1) \n
		Defines the 8-bit color code of the sector. \n
			:param clr_code: Range: 0 to 255
		"""
		param = Conversions.decimal_value_to_str(clr_code)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:NETWork:SECTor:CLRCode {param}')

	def get_smask(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:SECTor:SMASk \n
		Snippet: value: int = driver.configure.network.sector.get_smask() \n
		Defines the 8-bit sector subnet identifier. \n
			:return: smask: Range: 0 to 128
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:NETWork:SECTor:SMASk?')
		return Conversions.str_to_int(response)

	def set_smask(self, smask: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:SECTor:SMASk \n
		Snippet: driver.configure.network.sector.set_smask(smask = 1) \n
		Defines the 8-bit sector subnet identifier. \n
			:param smask: Range: 0 to 128
		"""
		param = Conversions.decimal_value_to_str(smask)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:NETWork:SECTor:SMASk {param}')

	def get_cnt_code(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:SECTor:CNTCode \n
		Snippet: value: int = driver.configure.network.sector.get_cnt_code() \n
		Defines the 3-digit decimal representation of the country code associated with the sector. \n
			:return: cnt_code: Range: 0 to 999
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:NETWork:SECTor:CNTCode?')
		return Conversions.str_to_int(response)

	def set_cnt_code(self, cnt_code: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:SECTor:CNTCode \n
		Snippet: driver.configure.network.sector.set_cnt_code(cnt_code = 1) \n
		Defines the 3-digit decimal representation of the country code associated with the sector. \n
			:param cnt_code: Range: 0 to 999
		"""
		param = Conversions.decimal_value_to_str(cnt_code)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:NETWork:SECTor:CNTCode {param}')

	# noinspection PyTypeChecker
	def get_format_py(self) -> enums.SectorIdFormat:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:SECTor:FORMat \n
		Snippet: value: enums.SectorIdFormat = driver.configure.network.sector.get_format_py() \n
		Selects the input format for the 128-bit overall sector ID. \n
			:return: format_py: A41N | MANual ANSI-41 or manual entry
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:NETWork:SECTor:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.SectorIdFormat)

	def set_format_py(self, format_py: enums.SectorIdFormat) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:SECTor:FORMat \n
		Snippet: driver.configure.network.sector.set_format_py(format_py = enums.SectorIdFormat.A41N) \n
		Selects the input format for the 128-bit overall sector ID. \n
			:param format_py: A41N | MANual ANSI-41 or manual entry
		"""
		param = Conversions.enum_scalar_to_str(format_py, enums.SectorIdFormat)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:NETWork:SECTor:FORMat {param}')

	def get_npbits(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:SECTor:NPBits \n
		Snippet: value: int = driver.configure.network.sector.get_npbits() \n
		Defines the number of parity bits, to be used if the ANSI-41 format is selected (method RsCmwEvdoSig.Configure.Network.
		Sector.formatPy) . \n
			:return: ansi_41_pbits: Range: 1 to 64
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:NETWork:SECTor:NPBits?')
		return Conversions.str_to_int(response)

	def set_npbits(self, ansi_41_pbits: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:SECTor:NPBits \n
		Snippet: driver.configure.network.sector.set_npbits(ansi_41_pbits = 1) \n
		Defines the number of parity bits, to be used if the ANSI-41 format is selected (method RsCmwEvdoSig.Configure.Network.
		Sector.formatPy) . \n
			:param ansi_41_pbits: Range: 1 to 64
		"""
		param = Conversions.decimal_value_to_str(ansi_41_pbits)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:NETWork:SECTor:NPBits {param}')

	def get_id_overall(self) -> str:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:SECTor:IDOVerall \n
		Snippet: value: str = driver.configure.network.sector.get_id_overall() \n
		Queries the 128-bit overall ID of the sector in ANSI-41 format (method RsCmwEvdoSig.Configure.Network.Sector.formatPy) . \n
			:return: ansi_41_overall_id: 32-digit hexadecimal number
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:NETWork:SECTor:IDOVerall?')
		return trim_str_response(response)

	def clone(self) -> 'Sector':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sector(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
