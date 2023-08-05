from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CorrectionTable:
	"""CorrectionTable commands group definition. 10 total commands, 6 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("correctionTable", core, parent)

	@property
	def deleteAll(self):
		"""deleteAll commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_deleteAll'):
			from .CorrectionTable_.DeleteAll import DeleteAll
			self._deleteAll = DeleteAll(self._core, self._base)
		return self._deleteAll

	@property
	def length(self):
		"""length commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_length'):
			from .CorrectionTable_.Length import Length
			self._length = Length(self._core, self._base)
		return self._length

	@property
	def details(self):
		"""details commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_details'):
			from .CorrectionTable_.Details import Details
			self._details = Details(self._core, self._base)
		return self._details

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .CorrectionTable_.Catalog import Catalog
			self._catalog = Catalog(self._core, self._base)
		return self._catalog

	@property
	def count(self):
		"""count commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_count'):
			from .CorrectionTable_.Count import Count
			self._count = Count(self._core, self._base)
		return self._count

	@property
	def exist(self):
		"""exist commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_exist'):
			from .CorrectionTable_.Exist import Exist
			self._exist = Exist(self._core, self._base)
		return self._exist

	# noinspection PyTypeChecker
	class CreateStruct(StructBase):
		"""Structure for setting input parameters. Contains optional set arguments. Fields: \n
			- Table_Name: str: String parameter used to identify the table by other commands and to store the table on the system drive. The string must comply to Windows™ file name conventions, see 'Mass Memory Commands'. You can add the prefix 'instn/' to address subinstrument number n+1. Example: 'inst2/mytable' means 'mytable' for subinstrument number 3
			- Frequency: List[float]: Optional setting parameter. Range: 70 MHz to 6 GHz, Unit: Hz
			- Correction: List[float]: Optional setting parameter. Range: -50 dB to 90 dB, Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_str('Table_Name'),
			ArgStruct('Frequency', DataType.FloatList, None, True, True, 1),
			ArgStruct('Correction', DataType.FloatList, None, True, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Table_Name: str = None
			self.Frequency: List[float] = None
			self.Correction: List[float] = None

	def set_create(self, value: CreateStruct) -> None:
		"""SCPI: CONFigure:BASE:FDCorrection:CTABle:CREate \n
		Snippet: driver.configure.freqCorrection.correctionTable.set_create(value = CreateStruct()) \n
		Creates a correction table for frequency-dependent attenuation and stores it in the RAM. If a table with the given name
		exists for the addressed subinstrument, it is overwritten. The parameter pairs <Frequency>, <Correction> are used to fill
		the table. A command with an incomplete pair (e.g. <Frequency> without <Correction>) is ignored completely.
		To add entries to an existing table, see method RsCmwBase.Configure.FreqCorrection.CorrectionTable.add. You can enter
		parameter pairs in any order. The table entries (pairs) are automatically sorted from lowest to highest frequency.
		The supported frequency range depends on the instrument model and the available options. The supported range can be
		smaller than stated here. See 'R&S CMW Models'. \n
			:param value: see the help for CreateStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:BASE:FDCorrection:CTABle:CREate', value)

	# noinspection PyTypeChecker
	class EraseStruct(StructBase):
		"""Structure for setting input parameters. Contains optional set arguments. Fields: \n
			- Table_Name: str: String parameter identifying the table. To display a list of existing tables, use the command CONFigure:BASE:FDCorrection:CTABle:CATalog?. You can add the prefix 'instn/' to address subinstrument number n+1.
			- Frequency: List[float]: Optional setting parameter. Selects the table entry to be removed. The value must match the frequency of an existing table entry. To remove several entries, specify a comma-separated list of frequencies. Range: 70 MHz to 6 GHz, Unit: Hz"""
		__meta_args_list = [
			ArgStruct.scalar_str('Table_Name'),
			ArgStruct('Frequency', DataType.FloatList, None, True, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Table_Name: str = None
			self.Frequency: List[float] = None

	def set_erase(self, value: EraseStruct) -> None:
		"""SCPI: CONFigure:BASE:FDCorrection:CTABle:ERASe \n
		Snippet: driver.configure.freqCorrection.correctionTable.set_erase(value = EraseStruct()) \n
		Removes one or more selected entries from a correction table. Each table entry consists of a frequency value and a
		correction value. Entries to be removed are selected via their frequency values. The supported frequency range depends on
		the instrument model and the available options. The supported range can be smaller than stated here. See 'R&S CMW Models'. \n
			:param value: see the help for EraseStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:BASE:FDCorrection:CTABle:ERASe', value)

	# noinspection PyTypeChecker
	class AddStruct(StructBase):
		"""Structure for setting input parameters. Contains optional set arguments. Fields: \n
			- Table_Name: str: String parameter identifying the table. To display a list of existing tables, use the command CONFigure:BASE:FDCorrection:CTABle:CATalog?. You can add the prefix 'instn/' to address subinstrument number n+1.
			- Frequency: List[float]: Optional setting parameter. Range: 70 MHz to 6 GHz, Unit: Hz
			- Correction: List[float]: Optional setting parameter. Range: -50 dB to 90 dB, Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_str('Table_Name'),
			ArgStruct('Frequency', DataType.FloatList, None, True, True, 1),
			ArgStruct('Correction', DataType.FloatList, None, True, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Table_Name: str = None
			self.Frequency: List[float] = None
			self.Correction: List[float] = None

	def set_add(self, value: AddStruct) -> None:
		"""SCPI: CONFigure:BASE:FDCorrection:CTABle:ADD \n
		Snippet: driver.configure.freqCorrection.correctionTable.set_add(value = AddStruct()) \n
		Adds entries to an existing correction table. At least one parameter pair has to be specified. A command with an
		incomplete pair (e.g. <Frequency> without <Correction>) is ignored completely. You can add parameter pairs in any order.
		The table entries (pairs) are automatically sorted from lowest to highest frequency. The supported frequency range
		depends on the instrument model and the available options. The supported range can be smaller than stated here. See 'R&S
		CMW Models'. \n
			:param value: see the help for AddStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:BASE:FDCorrection:CTABle:ADD', value)

	def delete(self, table_name: str) -> None:
		"""SCPI: CONFigure:BASE:FDCorrection:CTABle:DELete \n
		Snippet: driver.configure.freqCorrection.correctionTable.delete(table_name = '1') \n
		Deletes a correction table from the RAM and the system drive. \n
			:param table_name: String parameter identifying the table. To display a list of existing tables, use the command CONFigure:BASE:FDCorrection:CTABle:CATalog?. You can add the prefix 'instn/' to address subinstrument number n+1.
		"""
		param = Conversions.value_to_quoted_str(table_name)
		self._core.io.write(f'CONFigure:BASE:FDCorrection:CTABle:DELete {param}')

	def clone(self) -> 'CorrectionTable':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CorrectionTable(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
