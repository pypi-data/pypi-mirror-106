from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.Utilities import trim_str_response
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pending:
	"""Pending commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pending", core, parent)

	def get(self, filter_py: str = None, mode: enums.ExpressionMode = None) -> str:
		"""SCPI: STATus:GENerator:CONDition:PENDing \n
		Snippet: value: str = driver.status.generator.condition.pending.get(filter_py = '1', mode = enums.ExpressionMode.REGex) \n
		Lists all generator tasks or measurement tasks whose current state equals the state indicated by the last mnemonic. The
		results are collected from the CONDition parts of the lowest level registers of the STATus:OPERation register hierarchy.
		They are returned as a comma-separated list of strings. Each string is composed of the complete path of the status
		register plus the current state. \n
			:param filter_py: No help available
			:param mode: No help available
			:return: bitname: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('filter_py', filter_py, DataType.String, True), ArgSingle('mode', mode, DataType.Enum, True))
		response = self._core.io.query_str(f'STATus:GENerator:CONDition:PENDing? {param}'.rstrip())
		return trim_str_response(response)
