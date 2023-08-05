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
class Anb(Enum):
	"""Repeated capability Anb \n
	Number of Additional NB"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Nr1 = 1
	Nr2 = 2
	Nr3 = 3


# noinspection SpellCheckingInspection
class CellNo(Enum):
	"""Repeated capability CellNo \n
	Cell Number"""
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
class ClippingCounter(Enum):
	"""Repeated capability ClippingCounter \n
	number of Clipping Counter"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Nr1 = 1
	Nr2 = 2
	Nr3 = 3
	Nr4 = 4


# noinspection SpellCheckingInspection
class EutraBand(Enum):
	"""Repeated capability EutraBand \n
	SimultaneousBandNumber"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Band1 = 1
	Band2 = 2
	Band3 = 3
	Band4 = 4


# noinspection SpellCheckingInspection
class HMatrixColumn(Enum):
	"""Repeated capability HMatrixColumn \n
	column"""
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


# noinspection SpellCheckingInspection
class HMatrixRow(Enum):
	"""Repeated capability HMatrixRow \n
	row"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Row1 = 1
	Row2 = 2
	Row3 = 3
	Row4 = 4
	Row5 = 5
	Row6 = 6
	Row7 = 7
	Row8 = 8


# noinspection SpellCheckingInspection
class IPversion(Enum):
	"""Repeated capability IPversion \n
	IP Version"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	IPv4 = 4
	IPv6 = 6


# noinspection SpellCheckingInspection
class MatrixEightLine(Enum):
	"""Repeated capability MatrixEightLine \n
	matrix line 1 or 2"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Nr1 = 1
	Nr2 = 2


# noinspection SpellCheckingInspection
class MatrixFourLine(Enum):
	"""Repeated capability MatrixFourLine \n
	Matrix line 1 or 2"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Nr1 = 1
	Nr2 = 2


# noinspection SpellCheckingInspection
class MatrixLine(Enum):
	"""Repeated capability MatrixLine \n
	Matrix line 1 or 2"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Line1 = 1
	Line2 = 2
	Line3 = 3
	Line4 = 4


# noinspection SpellCheckingInspection
class MatrixTwoLine(Enum):
	"""Repeated capability MatrixTwoLine \n
	1st or 2nd line"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Nr1 = 1
	Nr2 = 2


# noinspection SpellCheckingInspection
class Mimo(Enum):
	"""Repeated capability Mimo \n
	MimoNxM"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	M42 = 42
	M44 = 44


# noinspection SpellCheckingInspection
class Output(Enum):
	"""Repeated capability Output \n
	Nr of Port"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Out1 = 1
	Out2 = 2
	Out3 = 3
	Out4 = 4


# noinspection SpellCheckingInspection
class Path(Enum):
	"""Repeated capability Path \n
	No of Path"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Path1 = 1
	Path2 = 2


# noinspection SpellCheckingInspection
class QAMmodulationOrder(Enum):
	"""Repeated capability QAMmodulationOrder \n
	Modulation Order"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	QAM64 = 64
	QAM256 = 256


# noinspection SpellCheckingInspection
class QAMmodulationOrderB(Enum):
	"""Repeated capability QAMmodulationOrderB \n
	QAM256"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	QAM256 = 256
	QAM1024 = 1024


# noinspection SpellCheckingInspection
class ReliabilityIndicatorNo(Enum):
	"""Repeated capability ReliabilityIndicatorNo \n
	RI Number"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	RIno1 = 1
	RIno2 = 2
	RIno3 = 3
	RIno4 = 4


# noinspection SpellCheckingInspection
class SecondaryCompCarrier(Enum):
	"""Repeated capability SecondaryCompCarrier \n
	SCC Number"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	CC1 = 1
	CC2 = 2
	CC3 = 3
	CC4 = 4
	CC5 = 5
	CC6 = 6
	CC7 = 7


# noinspection SpellCheckingInspection
class Stream(Enum):
	"""Repeated capability Stream \n
	Nr of MIMO Stream"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	S1 = 1
	S2 = 2


# noinspection SpellCheckingInspection
class SystemInfoBlock(Enum):
	"""Repeated capability SystemInfoBlock \n
	SIB-No."""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Sib8 = 8
	Sib16 = 16


# noinspection SpellCheckingInspection
class TbsIndexAlt(Enum):
	"""Repeated capability TbsIndexAlt \n
	Number"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Nr2 = 2
	Nr3 = 3


# noinspection SpellCheckingInspection
class Text(Enum):
	"""Repeated capability Text \n
	T 3412 Extended"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	T3324 = 3324
	T3402 = 3402
	T3412 = 3412


# noinspection SpellCheckingInspection
class UeReport(Enum):
	"""Repeated capability UeReport \n
	Number"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	V1020 = 1020
	V1090 = 1090


# noinspection SpellCheckingInspection
class ULqam(Enum):
	"""Repeated capability ULqam \n
	64-QAM"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	QAM64 = 64


# noinspection SpellCheckingInspection
class UTddFreq(Enum):
	"""Repeated capability UTddFreq \n
	frequency"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Freq128 = 128
	Freq384 = 384
	Freq768 = 768
