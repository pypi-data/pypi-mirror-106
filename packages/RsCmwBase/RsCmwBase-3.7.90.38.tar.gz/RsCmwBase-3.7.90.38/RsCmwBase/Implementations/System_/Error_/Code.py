from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Code:
	"""Code commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("code", core, parent)

	def get_all(self) -> int:
		"""SCPI: SYSTem:ERRor:CODE:ALL \n
		Snippet: value: int = driver.system.error.code.get_all() \n
		Queries and deletes all entries in the error queue. The command returns only the error numbers, not the error
		descriptions. Positive error numbers are instrument-specific. Negative error numbers are reserved by the SCPI standard. \n
			:return: error_code: No help available
		"""
		response = self._core.io.query_str('SYSTem:ERRor:CODE:ALL?')
		return Conversions.str_to_int(response)

	def get_next(self) -> int:
		"""SCPI: SYSTem:ERRor:CODE[:NEXT] \n
		Snippet: value: int = driver.system.error.code.get_next() \n
		Queries and deletes the oldest entry in the error queue. The command returns only the error number, not the error
		description. Positive error numbers are instrument-specific. Negative error numbers are reserved by the SCPI standard. \n
			:return: error: No help available
		"""
		response = self._core.io.query_str('SYSTem:ERRor:CODE:NEXT?')
		return Conversions.str_to_int(response)
