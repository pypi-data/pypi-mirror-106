from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal import Conversions
from ..Internal.Utilities import trim_str_response
from ..Internal.StructBase import StructBase
from ..Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class System:
	"""System commands group definition. 99 total commands, 24 Sub-groups, 11 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("system", core, parent)

	@property
	def ipSet(self):
		"""ipSet commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ipSet'):
			from .System_.IpSet import IpSet
			self._ipSet = IpSet(self._core, self._base)
		return self._ipSet

	@property
	def device(self):
		"""device commands group. 0 Sub-classes, 8 commands."""
		if not hasattr(self, '_device'):
			from .System_.Device import Device
			self._device = Device(self._core, self._base)
		return self._device

	@property
	def connector(self):
		"""connector commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_connector'):
			from .System_.Connector import Connector
			self._connector = Connector(self._core, self._base)
		return self._connector

	@property
	def routing(self):
		"""routing commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_routing'):
			from .System_.Routing import Routing
			self._routing = Routing(self._core, self._base)
		return self._routing

	@property
	def reference(self):
		"""reference commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_reference'):
			from .System_.Reference import Reference
			self._reference = Reference(self._core, self._base)
		return self._reference

	@property
	def ssync(self):
		"""ssync commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ssync'):
			from .System_.Ssync import Ssync
			self._ssync = Ssync(self._core, self._base)
		return self._ssync

	@property
	def time(self):
		"""time commands group. 2 Sub-classes, 3 commands."""
		if not hasattr(self, '_time'):
			from .System_.Time import Time
			self._time = Time(self._core, self._base)
		return self._time

	@property
	def date(self):
		"""date commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_date'):
			from .System_.Date import Date
			self._date = Date(self._core, self._base)
		return self._date

	@property
	def display(self):
		"""display commands group. 1 Sub-classes, 6 commands."""
		if not hasattr(self, '_display'):
			from .System_.Display import Display
			self._display = Display(self._core, self._base)
		return self._display

	@property
	def error(self):
		"""error commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_error'):
			from .System_.Error import Error
			self._error = Error(self._core, self._base)
		return self._error

	@property
	def help(self):
		"""help commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_help'):
			from .System_.Help import Help
			self._help = Help(self._core, self._base)
		return self._help

	@property
	def record(self):
		"""record commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_record'):
			from .System_.Record import Record
			self._record = Record(self._core, self._base)
		return self._record

	@property
	def startup(self):
		"""startup commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_startup'):
			from .System_.Startup import Startup
			self._startup = Startup(self._core, self._base)
		return self._startup

	@property
	def update(self):
		"""update commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_update'):
			from .System_.Update import Update
			self._update = Update(self._core, self._base)
		return self._update

	@property
	def communicate(self):
		"""communicate commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_communicate'):
			from .System_.Communicate import Communicate
			self._communicate = Communicate(self._core, self._base)
		return self._communicate

	@property
	def cmw(self):
		"""cmw commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cmw'):
			from .System_.Cmw import Cmw
			self._cmw = Cmw(self._core, self._base)
		return self._cmw

	@property
	def singleCmw(self):
		"""singleCmw commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_singleCmw'):
			from .System_.SingleCmw import SingleCmw
			self._singleCmw = SingleCmw(self._core, self._base)
		return self._singleCmw

	@property
	def option(self):
		"""option commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_option'):
			from .System_.Option import Option
			self._option = Option(self._core, self._base)
		return self._option

	@property
	def password(self):
		"""password commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_password'):
			from .System_.Password import Password
			self._password = Password(self._core, self._base)
		return self._password

	@property
	def stIcon(self):
		"""stIcon commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_stIcon'):
			from .System_.StIcon import StIcon
			self._stIcon = StIcon(self._core, self._base)
		return self._stIcon

	@property
	def deviceFootprint(self):
		"""deviceFootprint commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_deviceFootprint'):
			from .System_.DeviceFootprint import DeviceFootprint
			self._deviceFootprint = DeviceFootprint(self._core, self._base)
		return self._deviceFootprint

	@property
	def generator(self):
		"""generator commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_generator'):
			from .System_.Generator import Generator
			self._generator = Generator(self._core, self._base)
		return self._generator

	@property
	def measurement(self):
		"""measurement commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_measurement'):
			from .System_.Measurement import Measurement
			self._measurement = Measurement(self._core, self._base)
		return self._measurement

	@property
	def signaling(self):
		"""signaling commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_signaling'):
			from .System_.Signaling import Signaling
			self._signaling = Signaling(self._core, self._base)
		return self._signaling

	def get_reliability(self) -> int:
		"""SCPI: SYSTem:BASE:RELiability \n
		Snippet: value: int = driver.system.get_reliability() \n
		Returns a reliability value indicating errors detected by the base software. \n
			:return: value: For reliability indicator values, see 'Reliability Indicator'
		"""
		response = self._core.io.query_str('SYSTem:BASE:RELiability?')
		return Conversions.str_to_int(response)

	def get_did(self) -> str:
		"""SCPI: SYSTem:DID \n
		Snippet: value: str = driver.system.get_did() \n
		No command help available \n
			:return: device_id: No help available
		"""
		response = self._core.io.query_str('SYSTem:DID?')
		return trim_str_response(response)

	def get_klock(self) -> bool:
		"""SCPI: SYSTem:KLOCk \n
		Snippet: value: bool = driver.system.get_klock() \n
		Locks or unlocks the local controls of the instrument, including the (soft-) front panel keys. \n
			:return: klock: No help available
		"""
		response = self._core.io.query_str('SYSTem:KLOCk?')
		return Conversions.str_to_bool(response)

	def set_klock(self, klock: bool) -> None:
		"""SCPI: SYSTem:KLOCk \n
		Snippet: driver.system.set_klock(klock = False) \n
		Locks or unlocks the local controls of the instrument, including the (soft-) front panel keys. \n
			:param klock: ON | OFF ON: Local key locked (key lock enabled) OFF: Local keys unlocked
		"""
		param = Conversions.bool_to_str(klock)
		self._core.io.write(f'SYSTem:KLOCk {param}')

	def preset(self, appl_name_and_li_number: str = None) -> None:
		"""SCPI: SYSTem:PRESet \n
		Snippet: driver.system.preset(appl_name_and_li_number = '1') \n
		A PRESet sets the parameters of the subinstrument to default values suitable for local/manual interaction. A RESet sets
		them to default values suitable for remote operation. Optionally, the preset/reset can be limited to a specific
		application instance. \n
			:param appl_name_and_li_number: String specifying an application and instance to be reset/preset. Example: 'LTE Meas1' for LTE UE measurements instance 1 Omitting the instance (e.g. 'LTE Meas') selects instance 1. The supported strings are listed in the table below.
		"""
		param = ''
		if appl_name_and_li_number:
			param = Conversions.value_to_quoted_str(appl_name_and_li_number)
		self._core.io.write(f'SYSTem:PRESet {param}'.strip())

	def preset_all(self) -> None:
		"""SCPI: SYSTem:PRESet:ALL \n
		Snippet: driver.system.preset_all() \n
		A PRESet sets the parameters of all subinstruments and the base settings to default values suitable for local/manual
		interaction. A RESet sets them to default values suitable for remote operation. \n
		"""
		self._core.io.write(f'SYSTem:PRESet:ALL')

	def preset_all_with_opc(self) -> None:
		"""SCPI: SYSTem:PRESet:ALL \n
		Snippet: driver.system.preset_all_with_opc() \n
		A PRESet sets the parameters of all subinstruments and the base settings to default values suitable for local/manual
		interaction. A RESet sets them to default values suitable for remote operation. \n
		Same as preset_all, but waits for the operation to complete before continuing further. Use the RsCmwBase.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'SYSTem:PRESet:ALL')

	def preset_base(self) -> None:
		"""SCPI: SYSTem:PRESet:BASE \n
		Snippet: driver.system.preset_base() \n
		A PRESet sets the base settings to default values suitable for local/manual interaction. A RESet sets them to default
		values suitable for remote operation. \n
		"""
		self._core.io.write(f'SYSTem:PRESet:BASE')

	def preset_base_with_opc(self) -> None:
		"""SCPI: SYSTem:PRESet:BASE \n
		Snippet: driver.system.preset_base_with_opc() \n
		A PRESet sets the base settings to default values suitable for local/manual interaction. A RESet sets them to default
		values suitable for remote operation. \n
		Same as preset_base, but waits for the operation to complete before continuing further. Use the RsCmwBase.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'SYSTem:PRESet:BASE')

	def reset(self, appl_name_and_li_number: str = None) -> None:
		"""SCPI: SYSTem:RESet \n
		Snippet: driver.system.reset(appl_name_and_li_number = '1') \n
		A PRESet sets the parameters of the subinstrument to default values suitable for local/manual interaction. A RESet sets
		them to default values suitable for remote operation. Optionally, the preset/reset can be limited to a specific
		application instance. \n
			:param appl_name_and_li_number: String specifying an application and instance to be reset/preset. Example: 'LTE Meas1' for LTE UE measurements instance 1 Omitting the instance (e.g. 'LTE Meas') selects instance 1. The supported strings are listed in the table below.
		"""
		param = ''
		if appl_name_and_li_number:
			param = Conversions.value_to_quoted_str(appl_name_and_li_number)
		self._core.io.write(f'SYSTem:RESet {param}'.strip())

	def reset_all(self) -> None:
		"""SCPI: SYSTem:RESet:ALL \n
		Snippet: driver.system.reset_all() \n
		A PRESet sets the parameters of all subinstruments and the base settings to default values suitable for local/manual
		interaction. A RESet sets them to default values suitable for remote operation. \n
		"""
		self._core.io.write(f'SYSTem:RESet:ALL')

	def reset_all_with_opc(self) -> None:
		"""SCPI: SYSTem:RESet:ALL \n
		Snippet: driver.system.reset_all_with_opc() \n
		A PRESet sets the parameters of all subinstruments and the base settings to default values suitable for local/manual
		interaction. A RESet sets them to default values suitable for remote operation. \n
		Same as reset_all, but waits for the operation to complete before continuing further. Use the RsCmwBase.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'SYSTem:RESet:ALL')

	def reset_base(self) -> None:
		"""SCPI: SYSTem:RESet:BASE \n
		Snippet: driver.system.reset_base() \n
		A PRESet sets the base settings to default values suitable for local/manual interaction. A RESet sets them to default
		values suitable for remote operation. \n
		"""
		self._core.io.write(f'SYSTem:RESet:BASE')

	def reset_base_with_opc(self) -> None:
		"""SCPI: SYSTem:RESet:BASE \n
		Snippet: driver.system.reset_base_with_opc() \n
		A PRESet sets the base settings to default values suitable for local/manual interaction. A RESet sets them to default
		values suitable for remote operation. \n
		Same as reset_base, but waits for the operation to complete before continuing further. Use the RsCmwBase.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'SYSTem:RESet:BASE')

	# noinspection PyTypeChecker
	class TzoneStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Hour: int: Range: -12 to 15
			- Minute: int: Range: -59 to 59"""
		__meta_args_list = [
			ArgStruct.scalar_int('Hour'),
			ArgStruct.scalar_int('Minute')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Hour: int = None
			self.Minute: int = None

	def get_tzone(self) -> TzoneStruct:
		"""SCPI: SYSTem:TZONe \n
		Snippet: value: TzoneStruct = driver.system.get_tzone() \n
		Specifies the offset of the local time to the universal time coordinated (UTC) due to the time zone. There can be an
		additional offset due to daylight saving time (DST) . Changing the time zone (offset) does not affect an eventual DST
		offset or the time zone configured via method RsCmwBase.System.Time.DaylightSavingTime.Rule.value. The local time is
		calculated as: local time = UTC + time zone offset + DST offset \n
			:return: structure: for return value, see the help for TzoneStruct structure arguments.
		"""
		return self._core.io.query_struct('SYSTem:TZONe?', self.__class__.TzoneStruct())

	def set_tzone(self, value: TzoneStruct) -> None:
		"""SCPI: SYSTem:TZONe \n
		Snippet: driver.system.set_tzone(value = TzoneStruct()) \n
		Specifies the offset of the local time to the universal time coordinated (UTC) due to the time zone. There can be an
		additional offset due to daylight saving time (DST) . Changing the time zone (offset) does not affect an eventual DST
		offset or the time zone configured via method RsCmwBase.System.Time.DaylightSavingTime.Rule.value. The local time is
		calculated as: local time = UTC + time zone offset + DST offset \n
			:param value: see the help for TzoneStruct structure arguments.
		"""
		self._core.io.write_struct('SYSTem:TZONe', value)

	def get_version(self) -> float:
		"""SCPI: SYSTem:VERSion \n
		Snippet: value: float = driver.system.get_version() \n
		Queries the SCPI version number to which the instrument complies. The instrument complies to the final SCPI version 1999.
		0. \n
			:return: version: No help available
		"""
		response = self._core.io.query_str('SYSTem:VERSion?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'System':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = System(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
