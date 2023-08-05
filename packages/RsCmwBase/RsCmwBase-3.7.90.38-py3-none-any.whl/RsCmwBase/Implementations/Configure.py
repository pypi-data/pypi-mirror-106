from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal import Conversions
from .. import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Configure:
	"""Configure commands group definition. 54 total commands, 12 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("configure", core, parent)

	@property
	def spoint(self):
		"""spoint commands group. 3 Sub-classes, 2 commands."""
		if not hasattr(self, '_spoint'):
			from .Configure_.Spoint import Spoint
			self._spoint = Spoint(self._core, self._base)
		return self._spoint

	@property
	def semaphore(self):
		"""semaphore commands group. 4 Sub-classes, 2 commands."""
		if not hasattr(self, '_semaphore'):
			from .Configure_.Semaphore import Semaphore
			self._semaphore = Semaphore(self._core, self._base)
		return self._semaphore

	@property
	def mutex(self):
		"""mutex commands group. 3 Sub-classes, 3 commands."""
		if not hasattr(self, '_mutex'):
			from .Configure_.Mutex import Mutex
			self._mutex = Mutex(self._core, self._base)
		return self._mutex

	@property
	def multiCmw(self):
		"""multiCmw commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_multiCmw'):
			from .Configure_.MultiCmw import MultiCmw
			self._multiCmw = MultiCmw(self._core, self._base)
		return self._multiCmw

	@property
	def ipSet(self):
		"""ipSet commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ipSet'):
			from .Configure_.IpSet import IpSet
			self._ipSet = IpSet(self._core, self._base)
		return self._ipSet

	@property
	def adjustment(self):
		"""adjustment commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_adjustment'):
			from .Configure_.Adjustment import Adjustment
			self._adjustment = Adjustment(self._core, self._base)
		return self._adjustment

	@property
	def ipcr(self):
		"""ipcr commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ipcr'):
			from .Configure_.Ipcr import Ipcr
			self._ipcr = Ipcr(self._core, self._base)
		return self._ipcr

	@property
	def freqCorrection(self):
		"""freqCorrection commands group. 3 Sub-classes, 4 commands."""
		if not hasattr(self, '_freqCorrection'):
			from .Configure_.FreqCorrection import FreqCorrection
			self._freqCorrection = FreqCorrection(self._core, self._base)
		return self._freqCorrection

	@property
	def singleCmw(self):
		"""singleCmw commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_singleCmw'):
			from .Configure_.SingleCmw import SingleCmw
			self._singleCmw = SingleCmw(self._core, self._base)
		return self._singleCmw

	@property
	def cmwd(self):
		"""cmwd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cmwd'):
			from .Configure_.Cmwd import Cmwd
			self._cmwd = Cmwd(self._core, self._base)
		return self._cmwd

	@property
	def correction(self):
		"""correction commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_correction'):
			from .Configure_.Correction import Correction
			self._correction = Correction(self._core, self._base)
		return self._correction

	@property
	def mmonitor(self):
		"""mmonitor commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_mmonitor'):
			from .Configure_.Mmonitor import Mmonitor
			self._mmonitor = Mmonitor(self._core, self._base)
		return self._mmonitor

	# noinspection PyTypeChecker
	def get_fcontrol(self) -> enums.FanMode:
		"""SCPI: CONFigure:BASE:FCONtrol \n
		Snippet: value: enums.FanMode = driver.configure.get_fcontrol() \n
		Selects a fan control mode. \n
			:return: mode: LOW | NORMal | HIGH LOW: less cooling than in normal mode NORMal: default mode HIGH: more cooling than in normal mode
		"""
		response = self._core.io.query_str('CONFigure:BASE:FCONtrol?')
		return Conversions.str_to_scalar_enum(response, enums.FanMode)

	def set_fcontrol(self, mode: enums.FanMode) -> None:
		"""SCPI: CONFigure:BASE:FCONtrol \n
		Snippet: driver.configure.set_fcontrol(mode = enums.FanMode.HIGH) \n
		Selects a fan control mode. \n
			:param mode: LOW | NORMal | HIGH LOW: less cooling than in normal mode NORMal: default mode HIGH: more cooling than in normal mode
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.FanMode)
		self._core.io.write(f'CONFigure:BASE:FCONtrol {param}')

	def clone(self) -> 'Configure':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Configure(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
