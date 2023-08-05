from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Prepare:
	"""Prepare commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("prepare", core, parent)

	def get_fdefault(self) -> bool:
		"""SCPI: SYSTem:STARtup:PREPare:FDEFault \n
		Snippet: value: bool = driver.system.startup.prepare.get_fdefault() \n
		Enables startup with factory default state. \n
			:return: on_off: No help available
		"""
		response = self._core.io.query_str('SYSTem:STARtup:PREPare:FDEFault?')
		return Conversions.str_to_bool(response)

	def set_fdefault(self, on_off: bool) -> None:
		"""SCPI: SYSTem:STARtup:PREPare:FDEFault \n
		Snippet: driver.system.startup.prepare.set_fdefault(on_off = False) \n
		Enables startup with factory default state. \n
			:param on_off: 0 | 1 Behavior during the startup: 0: Restore previous settings. 1: Set instrument to its factory default state.
		"""
		param = Conversions.bool_to_str(on_off)
		self._core.io.write(f'SYSTem:STARtup:PREPare:FDEFault {param}')
