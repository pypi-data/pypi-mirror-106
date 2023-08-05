from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Types import DataType
from ...Internal.ArgSingleList import ArgSingleList
from ...Internal.ArgSingle import ArgSingle
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FreqCorrection:
	"""FreqCorrection commands group definition. 16 total commands, 3 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("freqCorrection", core, parent)

	@property
	def correctionTable(self):
		"""correctionTable commands group. 6 Sub-classes, 4 commands."""
		if not hasattr(self, '_correctionTable'):
			from .FreqCorrection_.CorrectionTable import CorrectionTable
			self._correctionTable = CorrectionTable(self._core, self._base)
		return self._correctionTable

	@property
	def activate(self):
		"""activate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_activate'):
			from .FreqCorrection_.Activate import Activate
			self._activate = Activate(self._core, self._base)
		return self._activate

	@property
	def usage(self):
		"""usage commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_usage'):
			from .FreqCorrection_.Usage import Usage
			self._usage = Usage(self._core, self._base)
		return self._usage

	def save(self, table_path: str = None) -> None:
		"""SCPI: CONFigure:BASE:FDCorrection:SAV \n
		Snippet: driver.configure.freqCorrection.save(table_path = '1') \n
		Saves the correction tables for a selected subinstrument from the RAM to the system drive. This action is performed
		automatically when the R&S CMW application software is closed, for example, by pressing the standby key. However, you can
		use the command to save your work manually after creating or configuring correction tables. \n
			:param table_path: String selecting the subinstrument If omitted: subinstrument addressed by the remote channel. 'instn': subinstrument n+1
		"""
		param = ''
		if table_path:
			param = Conversions.value_to_quoted_str(table_path)
		self._core.io.write(f'CONFigure:BASE:FDCorrection:SAV {param}'.strip())

	def recall(self, table_path: str = None) -> None:
		"""SCPI: CONFigure:BASE:FDCorrection:RCL \n
		Snippet: driver.configure.freqCorrection.recall(table_path = '1') \n
		Loads all correction tables for a selected subinstrument from the system drive into the RAM. This action is performed
		automatically when the R&S CMW application software is started. However, you can use the command to retrieve the
		correction tables after the disk contents have been modified. Or you can use it to undo changes and fall back to the
		tables stored on the system drive. \n
			:param table_path: String selecting the subinstrument If omitted: subinstrument addressed by the remote channel. 'instn': subinstrument n+1
		"""
		param = ''
		if table_path:
			param = Conversions.value_to_quoted_str(table_path)
		self._core.io.write(f'CONFigure:BASE:FDCorrection:RCL {param}'.strip())

	def deactivate(self, connector: str, direction: enums.RxTxDirection = None, rf_converter: enums.RfConverterInPath = None) -> None:
		"""SCPI: CONFigure:FDCorrection:DEACtivate \n
		Snippet: driver.configure.freqCorrection.deactivate(connector = r1, direction = enums.RxTxDirection.RX, rf_converter = enums.RfConverterInPath.RF1) \n
		Deactivates any correction tables for a specific RF connector or a specific connector / converter combination.
		For bidirectional connectors, the tables can be deactivated for both directions or for one direction. \n
			:param connector: Selects a single RF connector For possible connector values, see 'Signal Path Settings'.
			:param direction: RXTX | RX | TX Specifies the direction for which the tables are deactivated. RX means input and TX means output. For a pure output connector, RX is ignored. RXTX: both directions (for output connector same effect as TX) RX: input (not allowed for output connector) TX: output Default: RXTX
			:param rf_converter: RF1 | RF2 | RF3 | RF4 RX and TX module in the path (RFn = RXn, TXn)
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('connector', connector, DataType.RawString), ArgSingle('direction', direction, DataType.Enum, True), ArgSingle('rf_converter', rf_converter, DataType.Enum, True))
		self._core.io.write(f'CONFigure:FDCorrection:DEACtivate {param}'.rstrip())

	def deactivate_all(self, direction: enums.RxTxDirection = None, table_path: str = None) -> None:
		"""SCPI: CONFigure:FDCorrection:DEACtivate:ALL \n
		Snippet: driver.configure.freqCorrection.deactivate_all(direction = enums.RxTxDirection.RX, table_path = '1') \n
		Deactivates all correction tables for all RF connectors of a selected subinstrument. For bidirectional connectors, the
		tables can be deactivated for both directions or for one direction. \n
			:param direction: RXTX | RX | TX Specifies the direction for which the tables are deactivated. RX means input and TX means output. For a pure output connector, RX is ignored. RXTX: both directions (for output connector same effect as TX) RX: input (not allowed for output connector) TX: output Default: RXTX
			:param table_path: String selecting the subinstrument If omitted: subinstrument addressed by the remote channel. 'instn': subinstrument n+1
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('direction', direction, DataType.Enum, True), ArgSingle('table_path', table_path, DataType.String, True))
		self._core.io.write(f'CONFigure:FDCorrection:DEACtivate:ALL {param}'.rstrip())

	def clone(self) -> 'FreqCorrection':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FreqCorrection(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
