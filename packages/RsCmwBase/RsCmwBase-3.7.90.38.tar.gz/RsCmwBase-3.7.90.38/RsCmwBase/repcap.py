from enum import Enum
from .Internal.RepeatedCapability import VALUE_DEFAULT
from .Internal.RepeatedCapability import VALUE_EMPTY


# noinspection SpellCheckingInspection
class BitNr(Enum):
	"""Repeated capability BitNr"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Nr8 = 8
	Nr9 = 9
	Nr10 = 10
	Nr11 = 11
	Nr12 = 12


# noinspection SpellCheckingInspection
class CmwVariant(Enum):
	"""Repeated capability CmwVariant \n
	CMW Variant"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Cmw1 = 1
	Cmw100 = 100


# noinspection SpellCheckingInspection
class Eout(Enum):
	"""Repeated capability Eout \n
	Box number"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Eout1 = 1
	Eout2 = 2
	Eout3 = 3
	Eout4 = 4


# noinspection SpellCheckingInspection
class FileNr(Enum):
	"""Repeated capability FileNr \n
	instrument"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Nr1 = 1
	Nr2 = 2


# noinspection SpellCheckingInspection
class Frequency(Enum):
	"""Repeated capability Frequency \n
	Box number"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Freq1 = 1
	Freq2 = 2
	Freq3 = 3
	Freq4 = 4


# noinspection SpellCheckingInspection
class GpibInstance(Enum):
	"""Repeated capability GpibInstance \n
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
	Inst17 = 17
	Inst18 = 18
	Inst19 = 19
	Inst20 = 20
	Inst21 = 21
	Inst22 = 22
	Inst23 = 23
	Inst24 = 24
	Inst25 = 25
	Inst26 = 26
	Inst27 = 27
	Inst28 = 28
	Inst29 = 29
	Inst30 = 30
	Inst31 = 31
	Inst32 = 32


# noinspection SpellCheckingInspection
class HislipInstance(Enum):
	"""Repeated capability HislipInstance \n
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
	Inst17 = 17
	Inst18 = 18
	Inst19 = 19
	Inst20 = 20
	Inst21 = 21
	Inst22 = 22
	Inst23 = 23
	Inst24 = 24
	Inst25 = 25
	Inst26 = 26
	Inst27 = 27
	Inst28 = 28
	Inst29 = 29
	Inst30 = 30
	Inst31 = 31
	Inst32 = 32


# noinspection SpellCheckingInspection
class IpAddress(Enum):
	"""Repeated capability IpAddress \n
	Nr of IP Address"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Addr1 = 1
	Addr2 = 2
	Addr3 = 3


# noinspection SpellCheckingInspection
class NwAdapter(Enum):
	"""Repeated capability NwAdapter \n
	Number of NW Adapter"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Adapter1 = 1
	Adapter2 = 2
	Adapter3 = 3
	Adapter4 = 4
	Adapter5 = 5


# noinspection SpellCheckingInspection
class RsibInstance(Enum):
	"""Repeated capability RsibInstance \n
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
	Inst17 = 17
	Inst18 = 18
	Inst19 = 19
	Inst20 = 20
	Inst21 = 21
	Inst22 = 22
	Inst23 = 23
	Inst24 = 24
	Inst25 = 25
	Inst26 = 26
	Inst27 = 27
	Inst28 = 28
	Inst29 = 29
	Inst30 = 30
	Inst31 = 31
	Inst32 = 32


# noinspection SpellCheckingInspection
class RxFilter(Enum):
	"""Repeated capability RxFilter \n
	FilterNo"""
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


# noinspection SpellCheckingInspection
class Slot(Enum):
	"""Repeated capability Slot \n
	SlotNr"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Nr1 = 1
	Nr2 = 2
	Nr3 = 3
	Nr4 = 4


# noinspection SpellCheckingInspection
class SocketInstance(Enum):
	"""Repeated capability SocketInstance \n
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
	Inst17 = 17
	Inst18 = 18
	Inst19 = 19
	Inst20 = 20
	Inst21 = 21
	Inst22 = 22
	Inst23 = 23
	Inst24 = 24
	Inst25 = 25
	Inst26 = 26
	Inst27 = 27
	Inst28 = 28
	Inst29 = 29
	Inst30 = 30
	Inst31 = 31
	Inst32 = 32


# noinspection SpellCheckingInspection
class Trigger(Enum):
	"""Repeated capability Trigger \n
	Number of User Trigger"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Trg1 = 1
	Trg2 = 2
	Trg3 = 3
	Trg4 = 4


# noinspection SpellCheckingInspection
class TxFilter(Enum):
	"""Repeated capability TxFilter \n
	FilterNo"""
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


# noinspection SpellCheckingInspection
class VxiInstance(Enum):
	"""Repeated capability VxiInstance \n
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
	Inst17 = 17
	Inst18 = 18
	Inst19 = 19
	Inst20 = 20
	Inst21 = 21
	Inst22 = 22
	Inst23 = 23
	Inst24 = 24
	Inst25 = 25
	Inst26 = 26
	Inst27 = 27
	Inst28 = 28
	Inst29 = 29
	Inst30 = 30
	Inst31 = 31
	Inst32 = 32


# noinspection SpellCheckingInspection
class Window(Enum):
	"""Repeated capability Window \n
	1-n"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Win1 = 1
	Win2 = 2
	Win3 = 3
	Win4 = 4
	Win5 = 5
	Win6 = 6
	Win7 = 7
	Win8 = 8
	Win9 = 9
	Win10 = 10
	Win11 = 11
	Win12 = 12
	Win13 = 13
	Win14 = 14
	Win15 = 15
	Win16 = 16
	Win17 = 17
	Win18 = 18
	Win19 = 19
	Win20 = 20
	Win21 = 21
	Win22 = 22
	Win23 = 23
	Win24 = 24
	Win25 = 25
	Win26 = 26
	Win27 = 27
	Win28 = 28
	Win29 = 29
	Win30 = 30
	Win31 = 31
	Win32 = 32
