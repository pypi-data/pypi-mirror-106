from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dump:
	"""Dump commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dump", core, parent)

	def set(self) -> None:
		"""SCPI: DIAGnostic:LOG:DUMP \n
		Snippet: driver.diagnostic.log.dump.set() \n
		No command help available \n
		"""
		self._core.io.write(f'DIAGnostic:LOG:DUMP')

	def set_with_opc(self) -> None:
		"""SCPI: DIAGnostic:LOG:DUMP \n
		Snippet: driver.diagnostic.log.dump.set_with_opc() \n
		No command help available \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwBase.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'DIAGnostic:LOG:DUMP')
