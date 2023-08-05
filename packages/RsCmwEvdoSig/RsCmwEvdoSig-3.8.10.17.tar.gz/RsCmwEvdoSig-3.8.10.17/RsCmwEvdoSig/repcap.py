from enum import Enum
from .Internal.RepeatedCapability import VALUE_DEFAULT
from .Internal.RepeatedCapability import VALUE_EMPTY


# noinspection SpellCheckingInspection
class Instance(Enum):
	"""Global Repeated capability Instance \n
	Selects the instrument"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Inst1 = 1
	Inst2 = 2
	Inst3 = 3
	Inst4 = 4
	Inst5 = 5
	Inst6 = 6
	Inst7 = 7
	Inst8 = 8
	Inst9 = 9
	Inst10 = 10
	Inst11 = 11
	Inst12 = 12
	Inst13 = 13
	Inst14 = 14
	Inst15 = 15
	Inst16 = 16


# noinspection SpellCheckingInspection
class CellNo(Enum):
	"""Repeated capability CellNo \n
	Number of Neighbor Cell"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Nr1 = 1
	Nr2 = 2
	Nr3 = 3
	Nr4 = 4
	Nr5 = 5
	Nr6 = 6
	Nr7 = 7
	Nr8 = 8
	Nr9 = 9
	Nr10 = 10
	Nr11 = 11
	Nr12 = 12
	Nr13 = 13
	Nr14 = 14
	Nr15 = 15
	Nr16 = 16


# noinspection SpellCheckingInspection
class IpAddress(Enum):
	"""Repeated capability IpAddress \n
	IP Version"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Version4 = 4
	Version6 = 6


# noinspection SpellCheckingInspection
class NeighborCell(Enum):
	"""Repeated capability NeighborCell \n
	Neighbor Cell Number LTE Entries"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Nr1 = 1
	Nr2 = 2
	Nr3 = 3
	Nr4 = 4
	Nr5 = 5
	Nr6 = 6
	Nr7 = 7
	Nr8 = 8
	Nr9 = 9
	Nr10 = 10
	Nr11 = 11
	Nr12 = 12
	Nr13 = 13
	Nr14 = 14
	Nr15 = 15
	Nr16 = 16


# noinspection SpellCheckingInspection
class Path(Enum):
	"""Repeated capability Path \n
	No of Path"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Nr1 = 1
	Nr2 = 2


# noinspection SpellCheckingInspection
class Segment(Enum):
	"""Repeated capability Segment \n
	Segment number"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	S1 = 1
	S2 = 2
	S3 = 3
	S4 = 4
