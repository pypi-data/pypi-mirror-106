from enum import Enum
from .Internal.RepeatedCapability import VALUE_DEFAULT
from .Internal.RepeatedCapability import VALUE_EMPTY


# noinspection SpellCheckingInspection
class Carrier(Enum):
	"""Global Repeated capability Carrier \n
	Carrrier"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	C1 = 1
	C2 = 2
	C3 = 3
	C4 = 4
	C5 = 5
	C6 = 6
	C7 = 7
	C8 = 8
	C9 = 9
	C10 = 10
	C11 = 11
	C12 = 12
	C13 = 13
	C14 = 14
	C15 = 15
	C16 = 16
	C17 = 17
	C18 = 18
	C19 = 19
	C20 = 20
	C21 = 21
	C22 = 22
	C23 = 23
	C24 = 24
	C25 = 25
	C26 = 26
	C27 = 27
	C28 = 28
	C29 = 29
	C30 = 30
	C31 = 31
	C32 = 32


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
class Band(Enum):
	"""Repeated capability Band \n
	Band"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	B1 = 1
	B2 = 2
	B3 = 3
	B4 = 4
	B5 = 5
	B6 = 6
	B7 = 7
	B8 = 8
	B9 = 9
	B10 = 10
	B11 = 11
	B12 = 12
	B13 = 13
	B14 = 14
	B15 = 15
	B16 = 16
	B17 = 17
	B18 = 18
	B19 = 19
	B20 = 20
	B21 = 21
	B22 = 22
	B23 = 23
	B24 = 24
	B25 = 25
	B26 = 26
	B27 = 27
	B28 = 28
	B29 = 29
	B30 = 30
	B31 = 31
	B32 = 32


# noinspection SpellCheckingInspection
class BandCombination(Enum):
	"""Repeated capability BandCombination \n
	Selects the band combination"""
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
	Nr17 = 17
	Nr18 = 18
	Nr19 = 19
	Nr20 = 20
	Nr21 = 21
	Nr22 = 22
	Nr23 = 23
	Nr24 = 24
	Nr25 = 25
	Nr26 = 26
	Nr27 = 27
	Nr28 = 28
	Nr29 = 29
	Nr30 = 30
	Nr31 = 31
	Nr32 = 32


# noinspection SpellCheckingInspection
class Cell(Enum):
	"""Repeated capability Cell \n
	Selects the Neighbor Cell"""
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
class CounterNo(Enum):
	"""Repeated capability CounterNo \n
	Number"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Nr313 = 313


# noinspection SpellCheckingInspection
class Cycle(Enum):
	"""Repeated capability Cycle \n
	UE DTX cycle number"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Nr1 = 1
	Nr2 = 2


# noinspection SpellCheckingInspection
class DownCarrier(Enum):
	"""Repeated capability DownCarrier \n
	Selects neighbour carrier"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Dc1 = 1
	Dc2 = 2
	Dc3 = 3
	Dc4 = 4
	Dc5 = 5
	Dc6 = 6
	Dc7 = 7
	Dc8 = 8
	Dc9 = 9
	Dc10 = 10
	Dc11 = 11
	Dc12 = 12
	Dc13 = 13
	Dc14 = 14
	Dc15 = 15
	Dc16 = 16
	Dc17 = 17
	Dc18 = 18
	Dc19 = 19
	Dc20 = 20
	Dc21 = 21
	Dc22 = 22
	Dc23 = 23
	Dc24 = 24
	Dc25 = 25
	Dc26 = 26
	Dc27 = 27
	Dc28 = 28
	Dc29 = 29
	Dc30 = 30
	Dc31 = 31
	Dc32 = 32


# noinspection SpellCheckingInspection
class HSSCch(Enum):
	"""Repeated capability HSSCch \n
	Number of HS-SSCH"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	No1 = 1
	No2 = 2
	No3 = 3
	No4 = 4


# noinspection SpellCheckingInspection
class IPversion(Enum):
	"""Repeated capability IPversion \n
	IP Version"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	IPv4 = 4
	IPv6 = 6


# noinspection SpellCheckingInspection
class NonContigCell(Enum):
	"""Repeated capability NonContigCell \n
	Non-contiguous cells"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Nc2 = 2
	Nc3 = 3
	Nc4 = 4


# noinspection SpellCheckingInspection
class PacketData(Enum):
	"""Repeated capability PacketData \n
	Selects RMC data rate"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Pd8 = 8
	Pd16 = 16
	Pd32 = 32
	Pd64 = 64
	Pd128 = 128
	Pd384 = 384


# noinspection SpellCheckingInspection
class QuadratureAM(Enum):
	"""Repeated capability QuadratureAM \n
	QAM Modulation"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	QAM16 = 16
	QAM64 = 64


# noinspection SpellCheckingInspection
class RefMeasChannel(Enum):
	"""Repeated capability RefMeasChannel \n
	Selects RMC data rate"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Ch1 = 1
	Ch2 = 2
	Ch3 = 3
	Ch4 = 4
	Ch5 = 5


# noinspection SpellCheckingInspection
class SecondCode(Enum):
	"""Repeated capability SecondCode \n
	Index"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Sc1 = 1
	Sc2 = 2
	Sc3 = 3
	Sc4 = 4


# noinspection SpellCheckingInspection
class Timer(Enum):
	"""Repeated capability Timer \n
	Timeout"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	T313 = 313
	T323 = 323
	T3212 = 3212
	T3312 = 3312


# noinspection SpellCheckingInspection
class TransportBlock(Enum):
	"""Repeated capability TransportBlock \n
	Index"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	TBl1 = 1
	TBl2 = 2
	TBl3 = 3
	TBl4 = 4


# noinspection SpellCheckingInspection
class TransTimeInterval(Enum):
	"""Repeated capability TransTimeInterval \n
	TTI 2ms/10ms"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Tti2 = 2
	Tti10 = 10
