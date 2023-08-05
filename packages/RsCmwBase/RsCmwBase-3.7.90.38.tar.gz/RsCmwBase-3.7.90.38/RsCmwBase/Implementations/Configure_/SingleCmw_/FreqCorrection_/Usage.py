from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Usage:
	"""Usage commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("usage", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Correction_Table_Rx: str: String identifying the table assigned to the RX direction. If no table is active, an empty string is returned.
			- Correction_Table_Tx: str: String identifying the table assigned to the TX direction. If no table is active, an empty string is returned."""
		__meta_args_list = [
			ArgStruct.scalar_str('Correction_Table_Rx'),
			ArgStruct.scalar_str('Correction_Table_Tx')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Correction_Table_Rx: str = None
			self.Correction_Table_Tx: str = None

	def get(self, connector: str) -> GetStruct:
		"""SCPI: CONFigure:CMWS:FDCorrection:USAGe \n
		Snippet: value: GetStruct = driver.configure.singleCmw.freqCorrection.usage.get(connector = r1) \n
		Lists the correction tables assigned to a selected R&S CMWS RF connector. \n
			:param connector: Selects a single R&S CMWS connector For possible values, see 'Values for RF Path Selection'.
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.value_to_str(connector)
		return self._core.io.query_struct(f'CONFigure:CMWS:FDCorrection:USAGe? {param}', self.__class__.GetStruct())
