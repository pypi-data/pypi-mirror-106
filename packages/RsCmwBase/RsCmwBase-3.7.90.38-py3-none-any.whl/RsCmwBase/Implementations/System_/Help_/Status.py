from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Status:
	"""Status commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("status", core, parent)

	def get_bits(self) -> List[str]:
		"""SCPI: SYSTem:HELP:STATus:BITS \n
		Snippet: value: List[str] = driver.system.help.status.get_bits() \n
		Returns a list of paths for the bits of the STATus:OPERation registers at the lowest level of the hierarchy. Each path is
		represented by a string containing all registers from highest to lowest level separated by colons.
		Example: 'STATus:OPERation:TASK:A:GPRF:MEASurement:POWer:OFF' \n
			:return: bits: No help available
		"""
		response = self._core.io.query_str('SYSTem:HELP:STATus:BITS?')
		return Conversions.str_to_str_list(response)

	def get_register(self) -> List[str]:
		"""SCPI: SYSTem:HELP:STATus[:REGister] \n
		Snippet: value: List[str] = driver.system.help.status.get_register() \n
		Returns a list of paths for the STATus:OPERation registers. Each path is represented by a string containing all registers
		from highest level down to the individual register, separated by colons. For the GPRF power measurement for example the
		following paths are listed: 'STATus:OPERation', 'STATus:OPERation:TASK', 'STATus:OPERation:TASK:A',
		'STATus:OPERation:TASK:A:GPRF', 'STATus:OPERation:TASK:A:GPRF:MEASurement',
		'STATus:OPERation:TASK:A:GPRF:MEASurement:POWer' \n
			:return: register: No help available
		"""
		response = self._core.io.query_str('SYSTem:HELP:STATus:REGister?')
		return Conversions.str_to_str_list(response)
