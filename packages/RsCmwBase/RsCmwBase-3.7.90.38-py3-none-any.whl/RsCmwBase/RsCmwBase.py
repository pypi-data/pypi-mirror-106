from typing import List

from .Internal.Core import Core
from .Internal.InstrumentErrors import RsInstrException
from .Internal.CommandsGroup import CommandsGroup
from .Internal.VisaSession import VisaSession
from .Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RsCmwBase:
	"""410 total commands, 32 Sub-groups, 3 group commands"""
	_driver_options = "SupportedInstrModels = CMW500/CMW100/CMW270/CMW280/CMP, SupportedIdnPatterns = CMW, SimulationIdnString = 'Rohde&Schwarz,CMW500,100001,3.7.90.0038'"

	def __init__(self, resource_name: str, id_query: bool = True, reset: bool = False, options: str = None, direct_session: object = None):
		"""Initializes new RsCmwBase session. \n
		Parameter options tokens examples:
			- 'Simulate=True' - starts the session in simulation mode. Default: False
			- 'SelectVisa=socket' - uses no VISA implementation for socket connections - you do not need any VISA-C installation
			- 'SelectVisa=rs' - forces usage of RohdeSchwarz Visa
			- 'SelectVisa=ni' - forces usage of National Instruments Visa
			- 'QueryInstrumentStatus = False' - same as driver.utilities.instrument_status_checking = False
			- 'DriverSetup=(WriteDelay = 20, ReadDelay = 5)' - Introduces delay of 20ms before each write and 5ms before each read
			- 'DriverSetup=(OpcWaitMode = OpcQuery)' - mode for all the opc-synchronised write/reads. Other modes: StbPolling, StbPollingSlow, StbPollingSuperSlow
			- 'DriverSetup=(AddTermCharToWriteBinBLock = True)' - Adds one additional LF to the end of the binary data (some instruments require that)
			- 'DriverSetup=(AssureWriteWithTermChar = True)' - Makes sure each command/query is terminated with termination character. Default: Interface dependent
			- 'DriverSetup=(TerminationCharacter = 'x')' - Sets the termination character for reading. Default: '<LF>' (LineFeed)
			- 'DriverSetup=(IoSegmentSize = 10E3)' - Maximum size of one write/read segment. If transferred data is bigger, it is split to more segments
			- 'DriverSetup=(OpcTimeout = 10000)' - same as driver.utilities.opc_timeout = 10000
			- 'DriverSetup=(VisaTimeout = 5000)' - same as driver.utilities.visa_timeout = 5000
			- 'DriverSetup=(ViClearExeMode = 255)' - Binary combination where 1 means performing viClear() on a certain interface as the very first command in init
			- 'DriverSetup=(OpcQueryAfterWrite = True)' - same as driver.utilities.opc_query_after_write = True
		:param resource_name: VISA resource name, e.g. 'TCPIP::192.168.2.1::INSTR'
		:param id_query: if True: the instrument's model name is verified against the models supported by the driver and eventually throws an exception.
		:param reset: Resets the instrument (sends *RST command) and clears its status sybsystem
		:param options: string tokens alternating the driver settings.
		:param direct_session: Another driver object or pyVisa object to reuse the session instead of opening a new session."""
		self._core = Core(resource_name, id_query, reset, RsCmwBase._driver_options, options, direct_session)
		self._core.driver_version = '3.7.90.0038'
		self._options = options
		self._add_all_global_repcaps()
		self._custom_properties_init()
		# noinspection PyTypeChecker
		self._base = CommandsGroup("ROOT", self._core, None)

	@classmethod
	def from_existing_session(cls, session: object, options: str = None) -> 'RsCmwBase':
		"""Creates a new RsCmwBase object with the entered 'session' reused. \n
		:param session: can be an another driver or a direct pyvisa session.
		:param options: string tokens alternating the driver settings."""
		# noinspection PyTypeChecker
		return cls(None, False, False, options, session)

	def __str__(self) -> str:
		if self._core.io:
			return f"RsCmwBase session '{self._core.io.resource_name}'"
		else:
			return f"RsCmwBase with session closed"

	@staticmethod
	def assert_minimum_version(min_version: str) -> None:
		"""Asserts that the driver version fulfills the minimum required version you have entered.
		This way you make sure your installed driver is of the entered version or newer."""
		min_version_list = min_version.split('.')
		curr_version_list = '3.7.90.0038'.split('.')
		count_min = len(min_version_list)
		count_curr = len(curr_version_list)
		count = count_min if count_min < count_curr else count_curr
		for i in range(count):
			minimum = int(min_version_list[i])
			curr = int(curr_version_list[i])
			if curr > minimum:
				break
			if curr < minimum:
				raise RsInstrException(f"Assertion for minimum RsCmwBase version failed. Current version: '3.7.90.0038', minimum required version: '{min_version}'")
				
	@staticmethod
	def list_resources(expression: str = '?*::INSTR', visa_select: str = None) -> List[str]:
		"""Finds all the resources defined by the expression
			- '?*' - matches all the available instruments
			- 'USB::?*' - matches all the USB instruments
			- "TCPIP::192?*' - matches all the LAN instruments with the IP address starting with 192
		:param expression: see the examples in the function
		:param visa_select: optional parameter selecting a specific VISA. Examples: '@ni', '@rs'
		"""
		rm = VisaSession.get_resource_manager(visa_select)
		resources = rm.list_resources(expression)
		rm.close()
		# noinspection PyTypeChecker
		return resources

	def close(self) -> None:
		"""Closes the active RsCmwBase session."""
		self._core.io.close()

	def get_session_handle(self) -> object:
		"""Returns the underlying session handle."""
		return self._core.get_session_handle()

	def _add_all_global_repcaps(self) -> None:
		"""Adds all the repcaps defined as global to the instrument's global repcaps dictionary."""

	def _custom_properties_init(self):
		"""Adds all the interfaces that are custom for the driver."""
		from .CustomFiles.utilities import Utilities
		self.utilities = Utilities(self._core)
		from .CustomFiles.events import Events
		self.events = Events(self._core)
		from .CustomFiles.reliability import Reliability
		self.reliability = Reliability(self._core)

	@property
	def configure(self):
		"""configure commands group. 12 Sub-classes, 1 commands."""
		if not hasattr(self, '_configure'):
			from .Implementations.Configure import Configure
			self._configure = Configure(self._core, self._base)
		return self._configure

	@property
	def multiCmw(self):
		"""multiCmw commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_multiCmw'):
			from .Implementations.MultiCmw import MultiCmw
			self._multiCmw = MultiCmw(self._core, self._base)
		return self._multiCmw

	@property
	def sense(self):
		"""sense commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_sense'):
			from .Implementations.Sense import Sense
			self._sense = Sense(self._core, self._base)
		return self._sense

	@property
	def system(self):
		"""system commands group. 24 Sub-classes, 11 commands."""
		if not hasattr(self, '_system'):
			from .Implementations.System import System
			self._system = System(self._core, self._base)
		return self._system

	@property
	def source(self):
		"""source commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_source'):
			from .Implementations.Source import Source
			self._source = Source(self._core, self._base)
		return self._source

	@property
	def calibration(self):
		"""calibration commands group. 3 Sub-classes, 2 commands."""
		if not hasattr(self, '_calibration'):
			from .Implementations.Calibration import Calibration
			self._calibration = Calibration(self._core, self._base)
		return self._calibration

	@property
	def ipc(self):
		"""ipc commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_ipc'):
			from .Implementations.Ipc import Ipc
			self._ipc = Ipc(self._core, self._base)
		return self._ipc

	@property
	def diagnostic(self):
		"""diagnostic commands group. 17 Sub-classes, 1 commands."""
		if not hasattr(self, '_diagnostic'):
			from .Implementations.Diagnostic import Diagnostic
			self._diagnostic = Diagnostic(self._core, self._base)
		return self._diagnostic

	@property
	def trigger(self):
		"""trigger commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_trigger'):
			from .Implementations.Trigger import Trigger
			self._trigger = Trigger(self._core, self._base)
		return self._trigger

	@property
	def cmwd(self):
		"""cmwd commands group. 1 Sub-classes, 4 commands."""
		if not hasattr(self, '_cmwd'):
			from .Implementations.Cmwd import Cmwd
			self._cmwd = Cmwd(self._core, self._base)
		return self._cmwd

	@property
	def procedure(self):
		"""procedure commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_procedure'):
			from .Implementations.Procedure import Procedure
			self._procedure = Procedure(self._core, self._base)
		return self._procedure

	@property
	def get(self):
		"""get commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_get'):
			from .Implementations.Get import Get
			self._get = Get(self._core, self._base)
		return self._get

	@property
	def correction(self):
		"""correction commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_correction'):
			from .Implementations.Correction import Correction
			self._correction = Correction(self._core, self._base)
		return self._correction

	@property
	def catalog(self):
		"""catalog commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_catalog'):
			from .Implementations.Catalog import Catalog
			self._catalog = Catalog(self._core, self._base)
		return self._catalog

	@property
	def write(self):
		"""write commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_write'):
			from .Implementations.Write import Write
			self._write = Write(self._core, self._base)
		return self._write

	@property
	def firmwareUpdate(self):
		"""firmwareUpdate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_firmwareUpdate'):
			from .Implementations.FirmwareUpdate import FirmwareUpdate
			self._firmwareUpdate = FirmwareUpdate(self._core, self._base)
		return self._firmwareUpdate

	@property
	def macroCreate(self):
		"""macroCreate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_macroCreate'):
			from .Implementations.MacroCreate import MacroCreate
			self._macroCreate = MacroCreate(self._core, self._base)
		return self._macroCreate

	@property
	def triggerInvoke(self):
		"""triggerInvoke commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_triggerInvoke'):
			from .Implementations.TriggerInvoke import TriggerInvoke
			self._triggerInvoke = TriggerInvoke(self._core, self._base)
		return self._triggerInvoke

	@property
	def globalWait(self):
		"""globalWait commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_globalWait'):
			from .Implementations.GlobalWait import GlobalWait
			self._globalWait = GlobalWait(self._core, self._base)
		return self._globalWait

	@property
	def globalClearStatus(self):
		"""globalClearStatus commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_globalClearStatus'):
			from .Implementations.GlobalClearStatus import GlobalClearStatus
			self._globalClearStatus = GlobalClearStatus(self._core, self._base)
		return self._globalClearStatus

	@property
	def status(self):
		"""status commands group. 7 Sub-classes, 1 commands."""
		if not hasattr(self, '_status'):
			from .Implementations.Status import Status
			self._status = Status(self._core, self._base)
		return self._status

	@property
	def instrument(self):
		"""instrument commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_instrument'):
			from .Implementations.Instrument import Instrument
			self._instrument = Instrument(self._core, self._base)
		return self._instrument

	@property
	def display(self):
		"""display commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_display'):
			from .Implementations.Display import Display
			self._display = Display(self._core, self._base)
		return self._display

	@property
	def formatPy(self):
		"""formatPy commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_formatPy'):
			from .Implementations.FormatPy import FormatPy
			self._formatPy = FormatPy(self._core, self._base)
		return self._formatPy

	@property
	def unit(self):
		"""unit commands group. 0 Sub-classes, 13 commands."""
		if not hasattr(self, '_unit'):
			from .Implementations.Unit import Unit
			self._unit = Unit(self._core, self._base)
		return self._unit

	@property
	def gotoLocal(self):
		"""gotoLocal commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gotoLocal'):
			from .Implementations.GotoLocal import GotoLocal
			self._gotoLocal = GotoLocal(self._core, self._base)
		return self._gotoLocal

	@property
	def buffer(self):
		"""buffer commands group. 1 Sub-classes, 6 commands."""
		if not hasattr(self, '_buffer'):
			from .Implementations.Buffer import Buffer
			self._buffer = Buffer(self._core, self._base)
		return self._buffer

	@property
	def trace(self):
		"""trace commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_trace'):
			from .Implementations.Trace import Trace
			self._trace = Trace(self._core, self._base)
		return self._trace

	@property
	def hardCopy(self):
		"""hardCopy commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_hardCopy'):
			from .Implementations.HardCopy import HardCopy
			self._hardCopy = HardCopy(self._core, self._base)
		return self._hardCopy

	@property
	def saveState(self):
		"""saveState commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_saveState'):
			from .Implementations.SaveState import SaveState
			self._saveState = SaveState(self._core, self._base)
		return self._saveState

	@property
	def recallState(self):
		"""recallState commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_recallState'):
			from .Implementations.RecallState import RecallState
			self._recallState = RecallState(self._core, self._base)
		return self._recallState

	@property
	def massMemory(self):
		"""massMemory commands group. 6 Sub-classes, 10 commands."""
		if not hasattr(self, '_massMemory'):
			from .Implementations.MassMemory import MassMemory
			self._massMemory = MassMemory(self._core, self._base)
		return self._massMemory

	def get_macro_enable(self) -> bool:
		"""SCPI: *EMC \n
		Snippet: value: bool = driver.get_macro_enable() \n
		Enables or disables the execution of all macros that are defined for the active remote connection. Note: In contrast to
		SCPI specifications, macro execution is disabled by default. \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('*EMC?')
		return Conversions.str_to_bool(response)

	def set_macro_enable(self, enable: bool) -> None:
		"""SCPI: *EMC \n
		Snippet: driver.set_macro_enable(enable = False) \n
		Enables or disables the execution of all macros that are defined for the active remote connection. Note: In contrast to
		SCPI specifications, macro execution is disabled by default. \n
			:param enable: ON | OFF | 0 | 1 Boolean value to enable or disable macro execution. In the disabled state (OFF / 0) , macros in a command sequence are not expanded. The R&S CMW issues an error message: 113, Undefined header;MacroLabel.
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'*EMC {param}')

	def get_device_number(self) -> int:
		"""SCPI: *DEV \n
		Snippet: value: int = driver.get_device_number() \n
		Queries the device number. It equals the 'Assigned Instrument' number minus 1. \n
			:return: instrument_no: Range: 0 to n
		"""
		response = self._core.io.query_str('*DEV?')
		return Conversions.str_to_int(response)

	def set_device_number(self, instrument_no: int) -> None:
		"""SCPI: *DEV \n
		Snippet: driver.set_device_number(instrument_no = 1) \n
		Queries the device number. It equals the 'Assigned Instrument' number minus 1. \n
			:param instrument_no: No help available
		"""
		param = Conversions.decimal_value_to_str(instrument_no)
		self._core.io.write(f'*DEV {param}')

	def get_global_opc(self) -> bool:
		"""SCPI: *GOPC \n
		Snippet: value: bool = driver.get_global_opc() \n
		No command help available \n
			:return: gopc: No help available
		"""
		response = self._core.io.query_str('*GOPC?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'RsCmwBase':
		"""Creates a deep copy of the RsCmwBase object. Also copies:
			- All the existing Global repeated capability values
			- All the default group repeated capabilities setting \n
		Does not check the *IDN? response, and does not perform Reset.
		After cloning, you can set all the repeated capabilities settings independentely from the original group.
		Calling close() on the new object does not close the original VISA session"""
		cloned = RsCmwBase.from_existing_session(self.get_session_handle(), self._options)
		self._base.synchronize_repcaps(cloned)
		
		return cloned

	def restore_all_repcaps_to_default(self) -> None:
		"""Sets all the Group and Global repcaps to their initial values"""
		self._base.restore_repcaps()
