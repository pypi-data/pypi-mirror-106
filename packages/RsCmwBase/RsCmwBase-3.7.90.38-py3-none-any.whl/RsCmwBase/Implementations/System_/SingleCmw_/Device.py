from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Device:
	"""Device commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("device", core, parent)

	def get_id(self) -> str:
		"""SCPI: SYSTem:CMWS:DEVice:ID \n
		Snippet: value: str = driver.system.singleCmw.device.get_id() \n
		Queries the device identification of an R&S CMWS connected to the R&S CMW. \n
			:return: idn: Device ID string
		"""
		response = self._core.io.query_str('SYSTem:CMWS:DEVice:ID?')
		return trim_str_response(response)
