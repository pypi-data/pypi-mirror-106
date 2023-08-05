from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HardCopy:
	"""HardCopy commands group definition. 5 total commands, 2 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("hardCopy", core, parent)

	@property
	def device(self):
		"""device commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_device'):
			from .HardCopy_.Device import Device
			self._device = Device(self._core, self._base)
		return self._device

	@property
	def interior(self):
		"""interior commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_interior'):
			from .HardCopy_.Interior import Interior
			self._interior = Interior(self._core, self._base)
		return self._interior

	def get_data(self) -> bytes:
		"""SCPI: HCOPy:DATA \n
		Snippet: value: bytes = driver.hardCopy.get_data() \n
		Captures a screenshot and returns the result in block data format, see also 'Block Data Format'. method RsCmwBase.
		HardCopy.data captures the entire window, method RsCmwBase.HardCopy.Interior.data only the interior of the window. It is
		recommended to 'switch on' the display before sending this command, see method RsCmwBase.System.Display.update. \n
			:return: data: dblock Screenshot in 488.2 block data format
		"""
		response = self._core.io.query_bin_block('HCOPy:DATA?')
		return response

	def set_file(self, filename: str) -> None:
		"""SCPI: HCOPy:FILE \n
		Snippet: driver.hardCopy.set_file(filename = '1') \n
		Captures a screenshot and stores it to the specified file. method RsCmwBase.HardCopy.file captures the entire window,
		method RsCmwBase.HardCopy.Interior.file only the interior of the window. If a 'Remote' dialog is displayed instead of the
		normal display contents, this command switches on the display before taking a screenshot, and afterwards off again. \n
			:param filename: String parameter specifying the absolute path and name of the file. The file name extension is added automatically according to the configured format (see method RsCmwBase.HardCopy.Device.formatPy) . Aliases are allowed (see method RsCmwBase.MassMemory.aliases) . Wildcards are not allowed.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'HCOPy:FILE {param}')

	def clone(self) -> 'HardCopy':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = HardCopy(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
