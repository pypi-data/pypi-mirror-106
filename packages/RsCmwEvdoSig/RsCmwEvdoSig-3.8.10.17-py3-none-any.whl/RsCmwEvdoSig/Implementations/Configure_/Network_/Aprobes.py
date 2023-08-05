from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Aprobes:
	"""Aprobes commands group definition. 9 total commands, 0 Sub-groups, 9 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("aprobes", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.ProbesAckMode:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:APRobes:MODE \n
		Snippet: value: enums.ProbesAckMode = driver.configure.network.aprobes.get_mode() \n
		Specifies whether the tester acknowledges or ignores access probes from the AT. \n
			:return: mode: ACKN | IGN
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:NETWork:APRobes:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ProbesAckMode)

	def set_mode(self, mode: enums.ProbesAckMode) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:APRobes:MODE \n
		Snippet: driver.configure.network.aprobes.set_mode(mode = enums.ProbesAckMode.ACKN) \n
		Specifies whether the tester acknowledges or ignores access probes from the AT. \n
			:param mode: ACKN | IGN
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ProbesAckMode)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:NETWork:APRobes:MODE {param}')

	def get_iadjust(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:APRobes:IADJust \n
		Snippet: value: int = driver.configure.network.aprobes.get_iadjust() \n
		Specifies the initial power offset for access probes (INIT_PWR parameter in the access parameters message) . \n
			:return: iadjust: Range: -16 dB to 15 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:NETWork:APRobes:IADJust?')
		return Conversions.str_to_int(response)

	def set_iadjust(self, iadjust: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:APRobes:IADJust \n
		Snippet: driver.configure.network.aprobes.set_iadjust(iadjust = 1) \n
		Specifies the initial power offset for access probes (INIT_PWR parameter in the access parameters message) . \n
			:param iadjust: Range: -16 dB to 15 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(iadjust)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:NETWork:APRobes:IADJust {param}')

	def get_ol_adjust(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:APRobes:OLADjust \n
		Snippet: value: int = driver.configure.network.aprobes.get_ol_adjust() \n
		Specifies the nominal transmit power offset (NOM_PWR) to be used by ATs for the given band class in the open loop power
		estimate. \n
			:return: ol_adjust: Range: -81 dB to -66 dB , Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:NETWork:APRobes:OLADjust?')
		return Conversions.str_to_int(response)

	def set_ol_adjust(self, ol_adjust: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:APRobes:OLADjust \n
		Snippet: driver.configure.network.aprobes.set_ol_adjust(ol_adjust = 1) \n
		Specifies the nominal transmit power offset (NOM_PWR) to be used by ATs for the given band class in the open loop power
		estimate. \n
			:param ol_adjust: Range: -81 dB to -66 dB , Unit: dB
		"""
		param = Conversions.decimal_value_to_str(ol_adjust)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:NETWork:APRobes:OLADjust {param}')

	def get_pincrement(self) -> float:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:APRobes:PINCrement \n
		Snippet: value: float = driver.configure.network.aprobes.get_pincrement() \n
		Defines the step size of power increases (PWR_STEP) between consecutive access probes. \n
			:return: pincrement: Range: 0 dB to 7.5 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:NETWork:APRobes:PINCrement?')
		return Conversions.str_to_float(response)

	def set_pincrement(self, pincrement: float) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:APRobes:PINCrement \n
		Snippet: driver.configure.network.aprobes.set_pincrement(pincrement = 1.0) \n
		Defines the step size of power increases (PWR_STEP) between consecutive access probes. \n
			:param pincrement: Range: 0 dB to 7.5 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(pincrement)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:NETWork:APRobes:PINCrement {param}')

	def get_pp_sequence(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:APRobes:PPSequence \n
		Snippet: value: int = driver.configure.network.aprobes.get_pp_sequence() \n
		Defines the maximum number of access probes which ATs are to transmit in a single access probe sequence. \n
			:return: pp_sequence: Range: 1 to 15
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:NETWork:APRobes:PPSequence?')
		return Conversions.str_to_int(response)

	def set_pp_sequence(self, pp_sequence: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:APRobes:PPSequence \n
		Snippet: driver.configure.network.aprobes.set_pp_sequence(pp_sequence = 1) \n
		Defines the maximum number of access probes which ATs are to transmit in a single access probe sequence. \n
			:param pp_sequence: Range: 1 to 15
		"""
		param = Conversions.decimal_value_to_str(pp_sequence)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:NETWork:APRobes:PPSequence {param}')

	def get_plength(self) -> int:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:APRobes:PLENgth \n
		Snippet: value: int = driver.configure.network.aprobes.get_plength() \n
		Defines the length in frames of the access probe preamble. \n
			:return: plength: Range: 1 frame to 6 frames
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:NETWork:APRobes:PLENgth?')
		return Conversions.str_to_int(response)

	def set_plength(self, plength: int) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:APRobes:PLENgth \n
		Snippet: driver.configure.network.aprobes.set_plength(plength = 1) \n
		Defines the length in frames of the access probe preamble. \n
			:param plength: Range: 1 frame to 6 frames
		"""
		param = Conversions.decimal_value_to_str(plength)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:NETWork:APRobes:PLENgth {param}')

	# noinspection PyTypeChecker
	def get_ac_duration(self) -> enums.AccessDuration:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:APRobes:ACDuration \n
		Snippet: value: enums.AccessDuration = driver.configure.network.aprobes.get_ac_duration() \n
		Defines the length in slots of the access cycle. \n
			:return: ac_duration: S16 | S32 | S64 | S128 16/32/64/128 slot cycle
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:NETWork:APRobes:ACDuration?')
		return Conversions.str_to_scalar_enum(response, enums.AccessDuration)

	def set_ac_duration(self, ac_duration: enums.AccessDuration) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:APRobes:ACDuration \n
		Snippet: driver.configure.network.aprobes.set_ac_duration(ac_duration = enums.AccessDuration.S128) \n
		Defines the length in slots of the access cycle. \n
			:param ac_duration: S16 | S32 | S64 | S128 16/32/64/128 slot cycle
		"""
		param = Conversions.enum_scalar_to_str(ac_duration, enums.AccessDuration)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:NETWork:APRobes:ACDuration {param}')

	# noinspection PyTypeChecker
	def get_pl_slots(self) -> enums.PlSlots:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:APRobes:PLSLots \n
		Snippet: value: enums.PlSlots = driver.configure.network.aprobes.get_pl_slots() \n
		Defines the length in slots of the access probe preamble. \n
			:return: pl_slots: S4 | S16 4/16 slot preamble
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:NETWork:APRobes:PLSLots?')
		return Conversions.str_to_scalar_enum(response, enums.PlSlots)

	def set_pl_slots(self, pl_slots: enums.PlSlots) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:APRobes:PLSLots \n
		Snippet: driver.configure.network.aprobes.set_pl_slots(pl_slots = enums.PlSlots.S16) \n
		Defines the length in slots of the access probe preamble. \n
			:param pl_slots: S4 | S16 4/16 slot preamble
		"""
		param = Conversions.enum_scalar_to_str(pl_slots, enums.PlSlots)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:NETWork:APRobes:PLSLots {param}')

	# noinspection PyTypeChecker
	def get_sam_rate(self) -> enums.SamRate:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:APRobes:SAMRate \n
		Snippet: value: enums.SamRate = driver.configure.network.aprobes.get_sam_rate() \n
		Defines the sector access maximum rate at which the AT can transmit on the access channel. \n
			:return: sam_rate: R9K | R19K | R38K 9.6/19.2/38.4 kbit/s
		"""
		response = self._core.io.query_str('CONFigure:EVDO:SIGNaling<Instance>:NETWork:APRobes:SAMRate?')
		return Conversions.str_to_scalar_enum(response, enums.SamRate)

	def set_sam_rate(self, sam_rate: enums.SamRate) -> None:
		"""SCPI: CONFigure:EVDO:SIGNaling<instance>:NETWork:APRobes:SAMRate \n
		Snippet: driver.configure.network.aprobes.set_sam_rate(sam_rate = enums.SamRate.R19K) \n
		Defines the sector access maximum rate at which the AT can transmit on the access channel. \n
			:param sam_rate: R9K | R19K | R38K 9.6/19.2/38.4 kbit/s
		"""
		param = Conversions.enum_scalar_to_str(sam_rate, enums.SamRate)
		self._core.io.write(f'CONFigure:EVDO:SIGNaling<Instance>:NETWork:APRobes:SAMRate {param}')
