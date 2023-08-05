from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Time:
	"""Time commands group definition. 10 total commands, 2 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("time", core, parent)

	@property
	def daylightSavingTime(self):
		"""daylightSavingTime commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_daylightSavingTime'):
			from .Time_.DaylightSavingTime import DaylightSavingTime
			self._daylightSavingTime = DaylightSavingTime(self._core, self._base)
		return self._daylightSavingTime

	@property
	def hrTimer(self):
		"""hrTimer commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_hrTimer'):
			from .Time_.HrTimer import HrTimer
			self._hrTimer = HrTimer(self._core, self._base)
		return self._hrTimer

	# noinspection PyTypeChecker
	class LocalStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Hour: int: Range: 0 to 23
			- Minute: int: Range: 0 to 59
			- Second: int: Range: 0 to 59"""
		__meta_args_list = [
			ArgStruct.scalar_int('Hour'),
			ArgStruct.scalar_int('Minute'),
			ArgStruct.scalar_int('Second')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Hour: int = None
			self.Minute: int = None
			self.Second: int = None

	def get_local(self) -> LocalStruct:
		"""SCPI: SYSTem:TIME:LOCal \n
		Snippet: value: LocalStruct = driver.system.time.get_local() \n
		Sets the local time of the operating system clock. \n
			:return: structure: for return value, see the help for LocalStruct structure arguments.
		"""
		return self._core.io.query_struct('SYSTem:TIME:LOCal?', self.__class__.LocalStruct())

	def set_local(self, value: LocalStruct) -> None:
		"""SCPI: SYSTem:TIME:LOCal \n
		Snippet: driver.system.time.set_local(value = LocalStruct()) \n
		Sets the local time of the operating system clock. \n
			:param value: see the help for LocalStruct structure arguments.
		"""
		self._core.io.write_struct('SYSTem:TIME:LOCal', value)

	# noinspection PyTypeChecker
	class UtcStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Hour: int: Range: 0 to 23
			- Minute: int: Range: 0 to 59
			- Second: int: Range: 0 to 59"""
		__meta_args_list = [
			ArgStruct.scalar_int('Hour'),
			ArgStruct.scalar_int('Minute'),
			ArgStruct.scalar_int('Second')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Hour: int = None
			self.Minute: int = None
			self.Second: int = None

	def get_utc(self) -> UtcStruct:
		"""SCPI: SYSTem:TIME:UTC \n
		Snippet: value: UtcStruct = driver.system.time.get_utc() \n
		Sets the universal time coordinated (UTC) of the operating system clock. \n
			:return: structure: for return value, see the help for UtcStruct structure arguments.
		"""
		return self._core.io.query_struct('SYSTem:TIME:UTC?', self.__class__.UtcStruct())

	def set_utc(self, value: UtcStruct) -> None:
		"""SCPI: SYSTem:TIME:UTC \n
		Snippet: driver.system.time.set_utc(value = UtcStruct()) \n
		Sets the universal time coordinated (UTC) of the operating system clock. \n
			:param value: see the help for UtcStruct structure arguments.
		"""
		self._core.io.write_struct('SYSTem:TIME:UTC', value)

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Hour: int: Range: 0 to 23
			- Min: int: No parameter help available
			- Sec: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Hour'),
			ArgStruct.scalar_int('Min'),
			ArgStruct.scalar_int('Sec')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Hour: int = None
			self.Min: int = None
			self.Sec: int = None

	def get_value(self) -> ValueStruct:
		"""SCPI: SYSTem:TIME \n
		Snippet: value: ValueStruct = driver.system.time.get_value() \n
		Sets the universal time coordinated (UTC) of the operating system clock. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('SYSTem:TIME?', self.__class__.ValueStruct())

	def set_value(self, value: ValueStruct) -> None:
		"""SCPI: SYSTem:TIME \n
		Snippet: driver.system.time.set_value(value = ValueStruct()) \n
		Sets the universal time coordinated (UTC) of the operating system clock. \n
			:param value: see the help for ValueStruct structure arguments.
		"""
		self._core.io.write_struct('SYSTem:TIME', value)

	def clone(self) -> 'Time':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Time(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
