from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Date:
	"""Date commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("date", core, parent)

	# noinspection PyTypeChecker
	class LocalStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Year: int: Range: four-digit number
			- Month: int: Range: 1 to 12
			- Day: int: Range: 1 to n (depending on the Month)"""
		__meta_args_list = [
			ArgStruct.scalar_int('Year'),
			ArgStruct.scalar_int('Month'),
			ArgStruct.scalar_int('Day')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Year: int = None
			self.Month: int = None
			self.Day: int = None

	def get_local(self) -> LocalStruct:
		"""SCPI: SYSTem:DATE:LOCal \n
		Snippet: value: LocalStruct = driver.system.date.get_local() \n
		Sets the local date of the operating system calendar. \n
			:return: structure: for return value, see the help for LocalStruct structure arguments.
		"""
		return self._core.io.query_struct('SYSTem:DATE:LOCal?', self.__class__.LocalStruct())

	def set_local(self, value: LocalStruct) -> None:
		"""SCPI: SYSTem:DATE:LOCal \n
		Snippet: driver.system.date.set_local(value = LocalStruct()) \n
		Sets the local date of the operating system calendar. \n
			:param value: see the help for LocalStruct structure arguments.
		"""
		self._core.io.write_struct('SYSTem:DATE:LOCal', value)

	# noinspection PyTypeChecker
	class UtcStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Year: int: Range: four-digit number
			- Month: int: Range: 1 to 12
			- Day: int: Range: 1 to n (depending on the Month)"""
		__meta_args_list = [
			ArgStruct.scalar_int('Year'),
			ArgStruct.scalar_int('Month'),
			ArgStruct.scalar_int('Day')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Year: int = None
			self.Month: int = None
			self.Day: int = None

	def get_utc(self) -> UtcStruct:
		"""SCPI: SYSTem:DATE:UTC \n
		Snippet: value: UtcStruct = driver.system.date.get_utc() \n
		Sets the UTC date of the operating system calendar. \n
			:return: structure: for return value, see the help for UtcStruct structure arguments.
		"""
		return self._core.io.query_struct('SYSTem:DATE:UTC?', self.__class__.UtcStruct())

	def set_utc(self, value: UtcStruct) -> None:
		"""SCPI: SYSTem:DATE:UTC \n
		Snippet: driver.system.date.set_utc(value = UtcStruct()) \n
		Sets the UTC date of the operating system calendar. \n
			:param value: see the help for UtcStruct structure arguments.
		"""
		self._core.io.write_struct('SYSTem:DATE:UTC', value)

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Year: int: Range: four-digit number
			- Month: int: Range: 1 to 12
			- Day: int: Range: 1 to n (depending on the Month)"""
		__meta_args_list = [
			ArgStruct.scalar_int('Year'),
			ArgStruct.scalar_int('Month'),
			ArgStruct.scalar_int('Day')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Year: int = None
			self.Month: int = None
			self.Day: int = None

	def get_value(self) -> ValueStruct:
		"""SCPI: SYSTem:DATE \n
		Snippet: value: ValueStruct = driver.system.date.get_value() \n
		Sets the UTC date of the operating system calendar. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('SYSTem:DATE?', self.__class__.ValueStruct())

	def set_value(self, value: ValueStruct) -> None:
		"""SCPI: SYSTem:DATE \n
		Snippet: driver.system.date.set_value(value = ValueStruct()) \n
		Sets the UTC date of the operating system calendar. \n
			:param value: see the help for ValueStruct structure arguments.
		"""
		self._core.io.write_struct('SYSTem:DATE', value)
