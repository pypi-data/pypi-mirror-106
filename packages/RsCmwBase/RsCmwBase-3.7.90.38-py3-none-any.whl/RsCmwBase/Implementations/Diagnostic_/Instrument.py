from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Instrument:
	"""Instrument commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("instrument", core, parent)

	def load(self, appl_name_and_li_number: str) -> None:
		"""SCPI: DIAGnostic:INSTrument:LOAD \n
		Snippet: driver.diagnostic.instrument.load(appl_name_and_li_number = '1') \n
		No command help available \n
			:param appl_name_and_li_number: No help available
		"""
		param = Conversions.value_to_quoted_str(appl_name_and_li_number)
		self._core.io.write(f'DIAGnostic:INSTrument:LOAD {param}')

	def set_unload(self, appl_name_and_li_number: str) -> None:
		"""SCPI: DIAGnostic:INSTrument:UNLoad \n
		Snippet: driver.diagnostic.instrument.set_unload(appl_name_and_li_number = '1') \n
		No command help available \n
			:param appl_name_and_li_number: No help available
		"""
		param = Conversions.value_to_quoted_str(appl_name_and_li_number)
		self._core.io.write(f'DIAGnostic:INSTrument:UNLoad {param}')
