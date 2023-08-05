from enum import Enum
from .Internal.RepeatedCapability import VALUE_DEFAULT
from .Internal.RepeatedCapability import VALUE_EMPTY


# noinspection SpellCheckingInspection
class MeasInstance(Enum):
	"""Global Repeated capability MeasInstance \n
	Selects the instrument"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Inst1 = 1
	Inst2 = 2
	Inst3 = 3
	Inst4 = 4


# noinspection SpellCheckingInspection
class AccPointName(Enum):
	"""Repeated capability AccPointName \n
	APNSUFFIX"""
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


# noinspection SpellCheckingInspection
class Client(Enum):
	"""Repeated capability Client \n
	Index of server instance"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Ix1 = 1
	Ix2 = 2
	Ix3 = 3
	Ix4 = 4
	Ix5 = 5
	Ix6 = 6
	Ix7 = 7
	Ix8 = 8


# noinspection SpellCheckingInspection
class Codec(Enum):
	"""Repeated capability Codec \n
	VirtualSubscriber"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Ix1 = 1
	Ix2 = 2
	Ix3 = 3
	Ix4 = 4
	Ix5 = 5
	Ix6 = 6
	Ix7 = 7
	Ix8 = 8
	Ix9 = 9
	Ix10 = 10


# noinspection SpellCheckingInspection
class Dlink(Enum):
	"""Repeated capability Dlink \n
	Index"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Ix1 = 1
	Ix2 = 2
	Ix3 = 3
	Ix4 = 4


# noinspection SpellCheckingInspection
class Fltr(Enum):
	"""Repeated capability Fltr \n
	Index of impairement entry"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Ix1 = 1
	Ix2 = 2
	Ix3 = 3
	Ix4 = 4
	Ix5 = 5
	Ix6 = 6
	Ix7 = 7
	Ix8 = 8
	Ix9 = 9
	Ix10 = 10
	Ix11 = 11
	Ix12 = 12
	Ix13 = 13
	Ix14 = 14
	Ix15 = 15


# noinspection SpellCheckingInspection
class Impairments(Enum):
	"""Repeated capability Impairments \n
	Index of impairement entry"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Ix1 = 1
	Ix2 = 2
	Ix3 = 3
	Ix4 = 4
	Ix5 = 5
	Ix6 = 6
	Ix7 = 7
	Ix8 = 8
	Ix9 = 9
	Ix10 = 10
	Ix11 = 11
	Ix12 = 12
	Ix13 = 13
	Ix14 = 14
	Ix15 = 15


# noinspection SpellCheckingInspection
class Ims(Enum):
	"""Repeated capability Ims \n
	IMS Server Number"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Ix1 = 1
	Ix2 = 2


# noinspection SpellCheckingInspection
class Imsi(Enum):
	"""Repeated capability Imsi \n
	IMSI Suffix"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Ix1 = 1
	Ix2 = 2
	Ix3 = 3
	Ix4 = 4
	Ix5 = 5
	Ix6 = 6
	Ix7 = 7
	Ix8 = 8
	Ix9 = 9
	Ix10 = 10


# noinspection SpellCheckingInspection
class Nat(Enum):
	"""Repeated capability Nat \n
	Index of server instance"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Ix1 = 1
	Ix2 = 2
	Ix3 = 3
	Ix4 = 4
	Ix5 = 5
	Ix6 = 6
	Ix7 = 7
	Ix8 = 8


# noinspection SpellCheckingInspection
class PcscFnc(Enum):
	"""Repeated capability PcscFnc \n
	Pcscf"""
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
class Profile(Enum):
	"""Repeated capability Profile \n
	Subscriber"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Nr1 = 1
	Nr2 = 2
	Nr3 = 3
	Nr4 = 4
	Nr5 = 5


# noinspection SpellCheckingInspection
class Server(Enum):
	"""Repeated capability Server \n
	Index of server instance"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Ix1 = 1
	Ix2 = 2
	Ix3 = 3
	Ix4 = 4
	Ix5 = 5
	Ix6 = 6
	Ix7 = 7
	Ix8 = 8


# noinspection SpellCheckingInspection
class Slot(Enum):
	"""Repeated capability Slot \n
	Index"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Nr1 = 1
	Nr2 = 2
	Nr3 = 3
	Nr4 = 4


# noinspection SpellCheckingInspection
class Subscriber(Enum):
	"""Repeated capability Subscriber \n
	Subscriber"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Nr1 = 1
	Nr2 = 2
	Nr3 = 3
	Nr4 = 4
	Nr5 = 5


# noinspection SpellCheckingInspection
class Trace(Enum):
	"""Repeated capability Trace \n
	TraceIndex"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Ix1 = 1
	Ix2 = 2
	Ix3 = 3
	Ix4 = 4
	Ix5 = 5
	Ix6 = 6
	Ix7 = 7
	Ix8 = 8
	Ix9 = 9
	Ix10 = 10


# noinspection SpellCheckingInspection
class UserId(Enum):
	"""Repeated capability UserId \n
	2 Dimension"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Ix1 = 1
	Ix2 = 2
	Ix3 = 3
	Ix4 = 4
	Ix5 = 5
	Ix6 = 6
	Ix7 = 7
	Ix8 = 8
	Ix9 = 9
	Ix10 = 10


# noinspection SpellCheckingInspection
class VirtualSubscriber(Enum):
	"""Repeated capability VirtualSubscriber \n
	Index of impairement entry"""
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
