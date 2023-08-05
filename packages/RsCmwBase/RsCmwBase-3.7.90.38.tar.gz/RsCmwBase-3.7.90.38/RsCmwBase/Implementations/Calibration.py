from typing import List

from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal.Types import DataType
from ..Internal.StructBase import StructBase
from ..Internal.ArgStruct import ArgStruct
from .. import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Calibration:
	"""Calibration commands group definition. 10 total commands, 3 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("calibration", core, parent)

	@property
	def latest(self):
		"""latest commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_latest'):
			from .Calibration_.Latest import Latest
			self._latest = Latest(self._core, self._base)
		return self._latest

	@property
	def ipcr(self):
		"""ipcr commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_ipcr'):
			from .Calibration_.Ipcr import Ipcr
			self._ipcr = Ipcr(self._core, self._base)
		return self._ipcr

	@property
	def ipc(self):
		"""ipc commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_ipc'):
			from .Calibration_.Ipc import Ipc
			self._ipc = Ipc(self._core, self._base)
		return self._ipc

	# noinspection PyTypeChecker
	class AllStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Date: List[str]: Date of the calibration as string
			- Time: List[str]: Time of the calibration as string
			- Type_Py: List[enums.Type]: FSCorrection | UCORrection | CALibration | OGCal Type of the calibration FSCorrection: Correction performed in factory or service UCORrection: Correction performed by a customer CALibration: Verification in the factory OGCal: Verification by the service (outgoing calibration)"""
		__meta_args_list = [
			ArgStruct('Date', DataType.StringList, None, False, True, 1),
			ArgStruct('Time', DataType.StringList, None, False, True, 1),
			ArgStruct('Type_Py', DataType.EnumList, enums.Type, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Date: List[str] = None
			self.Time: List[str] = None
			self.Type_Py: List[enums.Type] = None

	def get_all(self) -> AllStruct:
		"""SCPI: CALibration:BASE:ALL \n
		Snippet: value: AllStruct = driver.calibration.get_all() \n
		Query the stored calibration information. A comma-separated list is returned, containing three parameters per calibration,
		as described below. \n
			:return: structure: for return value, see the help for AllStruct structure arguments.
		"""
		return self._core.io.query_struct('CALibration:BASE:ALL?', self.__class__.AllStruct())

	# noinspection PyTypeChecker
	class AcFileStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Type_Py: str: Name of the file as string
			- Date: str: Creation date as string"""
		__meta_args_list = [
			ArgStruct.scalar_str('Type_Py'),
			ArgStruct.scalar_str('Date')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Type_Py: str = None
			self.Date: str = None

	def get_ac_file(self) -> AcFileStruct:
		"""SCPI: CALibration:BASE:ACFile \n
		Snippet: value: AcFileStruct = driver.calibration.get_ac_file() \n
		Query name and creation date of the currently active RF path correction file. \n
			:return: structure: for return value, see the help for AcFileStruct structure arguments.
		"""
		return self._core.io.query_struct('CALibration:BASE:ACFile?', self.__class__.AcFileStruct())

	def clone(self) -> 'Calibration':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Calibration(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
