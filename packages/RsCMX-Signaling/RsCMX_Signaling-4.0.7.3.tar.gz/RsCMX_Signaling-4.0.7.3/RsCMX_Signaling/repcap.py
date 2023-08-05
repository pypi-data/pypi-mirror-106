from enum import Enum
from .Internal.RepeatedCapability import VALUE_DEFAULT
from .Internal.RepeatedCapability import VALUE_EMPTY


# noinspection SpellCheckingInspection
class Cword(Enum):
	"""Repeated capability Cword"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Nr1 = 1
	Nr2 = 2


# noinspection SpellCheckingInspection
class Nnum(Enum):
	"""Repeated capability Nnum"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Nr310 = 310
	Nr311 = 311


# noinspection SpellCheckingInspection
class Pattern(Enum):
	"""Repeated capability Pattern \n
	TDD Pattern"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Nr1 = 1


# noinspection SpellCheckingInspection
class Tnum(Enum):
	"""Repeated capability Tnum"""
	Empty = VALUE_EMPTY
	Default = VALUE_DEFAULT
	Nr300 = 300
	Nr301 = 301
	Nr310 = 310
	Nr311 = 311
	Nr319 = 319
