from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Headers:
	"""Headers commands group definition. 3 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("headers", core, parent)

	@property
	def access(self):
		"""access commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_access'):
			from .Headers_.Access import Access
			self._access = Access(self._core, self._base)
		return self._access

	def get_value(self) -> bytes:
		"""SCPI: DIAGnostic:HELP:HEADers \n
		Snippet: value: bytes = driver.diagnostic.help.headers.get_value() \n
		No command help available \n
			:return: header: No help available
		"""
		response = self._core.io.query_bin_block('DIAGnostic:HELP:HEADers?')
		return response

	def clone(self) -> 'Headers':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Headers(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
