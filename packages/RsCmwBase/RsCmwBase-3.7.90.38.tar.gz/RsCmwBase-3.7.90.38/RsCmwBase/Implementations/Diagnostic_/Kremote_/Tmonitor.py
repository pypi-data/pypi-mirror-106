from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tmonitor:
	"""Tmonitor commands group definition. 9 total commands, 4 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("tmonitor", core, parent)

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_enable'):
			from .Tmonitor_.Enable import Enable
			self._enable = Enable(self._core, self._base)
		return self._enable

	@property
	def dump(self):
		"""dump commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dump'):
			from .Tmonitor_.Dump import Dump
			self._dump = Dump(self._core, self._base)
		return self._dump

	@property
	def statistic(self):
		"""statistic commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_statistic'):
			from .Tmonitor_.Statistic import Statistic
			self._statistic = Statistic(self._core, self._base)
		return self._statistic

	@property
	def trace(self):
		"""trace commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_trace'):
			from .Tmonitor_.Trace import Trace
			self._trace = Trace(self._core, self._base)
		return self._trace

	def reset(self) -> None:
		"""SCPI: DIAGnostic:KREMote:TMONitor:RESet \n
		Snippet: driver.diagnostic.kremote.tmonitor.reset() \n
		No command help available \n
		"""
		self._core.io.write(f'DIAGnostic:KREMote:TMONitor:RESet')

	def reset_with_opc(self) -> None:
		"""SCPI: DIAGnostic:KREMote:TMONitor:RESet \n
		Snippet: driver.diagnostic.kremote.tmonitor.reset_with_opc() \n
		No command help available \n
		Same as reset, but waits for the operation to complete before continuing further. Use the RsCmwBase.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'DIAGnostic:KREMote:TMONitor:RESet')

	def clone(self) -> 'Tmonitor':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tmonitor(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
