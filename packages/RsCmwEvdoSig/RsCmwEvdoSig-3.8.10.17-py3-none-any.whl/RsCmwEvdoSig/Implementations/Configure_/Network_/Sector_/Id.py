from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Id:
	"""Id commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("id", core, parent)

	def get_ansi(self) -> float:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:SECTor:ID:ANSI \n
		Snippet: value: float = driver.configure.network.sector.id.get_ansi() \n
		Defines the 24-bit sector ID, to be used if the ANSI-41 format is selected (method RsCmwEvdoSig.Configure.Network.Sector.
		formatPy) . \n
			:return: ansi_41_sector_id: Sector ID, 6-digit hexadecimal number Range: #H000000 to #HFFFFFF
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:NETWork:SECTor:ID:ANSI?')
		return Conversions.str_to_float(response)

	def set_ansi(self, ansi_41_sector_id: float) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:SECTor:ID:ANSI \n
		Snippet: driver.configure.network.sector.id.set_ansi(ansi_41_sector_id = 1.0) \n
		Defines the 24-bit sector ID, to be used if the ANSI-41 format is selected (method RsCmwEvdoSig.Configure.Network.Sector.
		formatPy) . \n
			:param ansi_41_sector_id: Sector ID, 6-digit hexadecimal number Range: #H000000 to #HFFFFFF
		"""
		param = Conversions.decimal_value_to_str(ansi_41_sector_id)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:NETWork:SECTor:ID:ANSI {param}')

	def get_manual(self) -> float:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:SECTor:ID:MANual \n
		Snippet: value: float = driver.configure.network.sector.id.get_manual() \n
		Defines the 128-bit overall ID of the sector, to be used if the manual format is selected (method RsCmwEvdoSig.Configure.
		Network.Sector.formatPy) . \n
			:return: manual_sector_id: Sector ID, 32-digit hexadecimal number Range: #H000000000000000000000000 to #HFFFFFFFFFFFFFFFFFFFFFFFF
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:NETWork:SECTor:ID:MANual?')
		return Conversions.str_to_float(response)

	def set_manual(self, manual_sector_id: float) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:SECTor:ID:MANual \n
		Snippet: driver.configure.network.sector.id.set_manual(manual_sector_id = 1.0) \n
		Defines the 128-bit overall ID of the sector, to be used if the manual format is selected (method RsCmwEvdoSig.Configure.
		Network.Sector.formatPy) . \n
			:param manual_sector_id: Sector ID, 32-digit hexadecimal number Range: #H000000000000000000000000 to #HFFFFFFFFFFFFFFFFFFFFFFFF
		"""
		param = Conversions.decimal_value_to_str(manual_sector_id)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:NETWork:SECTor:ID:MANual {param}')
