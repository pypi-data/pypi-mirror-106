from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sense:
	"""Sense commands group definition. 13 total commands, 4 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sense", core, parent)

	@property
	def ipSet(self):
		"""ipSet commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ipSet'):
			from .Sense_.IpSet import IpSet
			self._ipSet = IpSet(self._core, self._base)
		return self._ipSet

	@property
	def temperature(self):
		"""temperature commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_temperature'):
			from .Sense_.Temperature import Temperature
			self._temperature = Temperature(self._core, self._base)
		return self._temperature

	@property
	def reference(self):
		"""reference commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_reference'):
			from .Sense_.Reference import Reference
			self._reference = Reference(self._core, self._base)
		return self._reference

	@property
	def firmwareUpdate(self):
		"""firmwareUpdate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_firmwareUpdate'):
			from .Sense_.FirmwareUpdate import FirmwareUpdate
			self._firmwareUpdate = FirmwareUpdate(self._core, self._base)
		return self._firmwareUpdate

	def clone(self) -> 'Sense':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sense(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
