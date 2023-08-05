from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CorrectionTable:
	"""CorrectionTable commands group definition. 10 total commands, 5 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("correctionTable", core, parent)

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
			- Table_Name: str: No parameter help available
			- Frequency: List[float]: No parameter help available
			- Correction: List[float]: No parameter help available"""
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
		Snippet: driver.configure.base.freqCorrection.correctionTable.set_create(value = CreateStruct()) \n
		No command help available \n
			:param value: see the help for CreateStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:BASE:FDCorrection:CTABle:CREate', value)

	# noinspection PyTypeChecker
	class EraseStruct(StructBase):
		"""Structure for setting input parameters. Contains optional set arguments. Fields: \n
			- Table_Name: str: No parameter help available
			- Frequency: List[float]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_str('Table_Name'),
			ArgStruct('Frequency', DataType.FloatList, None, True, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Table_Name: str = None
			self.Frequency: List[float] = None

	def set_erase(self, value: EraseStruct) -> None:
		"""SCPI: CONFigure:BASE:FDCorrection:CTABle:ERASe \n
		Snippet: driver.configure.base.freqCorrection.correctionTable.set_erase(value = EraseStruct()) \n
		No command help available \n
			:param value: see the help for EraseStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:BASE:FDCorrection:CTABle:ERASe', value)

	# noinspection PyTypeChecker
	class AddStruct(StructBase):
		"""Structure for setting input parameters. Contains optional set arguments. Fields: \n
			- Table_Name: str: No parameter help available
			- Frequency: List[float]: No parameter help available
			- Correction: List[float]: No parameter help available"""
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
		Snippet: driver.configure.base.freqCorrection.correctionTable.set_add(value = AddStruct()) \n
		No command help available \n
			:param value: see the help for AddStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:BASE:FDCorrection:CTABle:ADD', value)

	def delete(self, table_name: str) -> None:
		"""SCPI: CONFigure:BASE:FDCorrection:CTABle:DELete \n
		Snippet: driver.configure.base.freqCorrection.correctionTable.delete(table_name = '1') \n
		No command help available \n
			:param table_name: No help available
		"""
		param = Conversions.value_to_quoted_str(table_name)
		self._core.io.write(f'CONFigure:BASE:FDCorrection:CTABle:DELete {param}')

	def delete_all(self, table_path: str = None) -> None:
		"""SCPI: CONFigure:BASE:FDCorrection:CTABle:DELete:ALL \n
		Snippet: driver.configure.base.freqCorrection.correctionTable.delete_all(table_path = '1') \n
		No command help available \n
			:param table_path: No help available
		"""
		param = ''
		if table_path:
			param = Conversions.value_to_quoted_str(table_path)
		self._core.io.write(f'CONFigure:BASE:FDCorrection:CTABle:DELete:ALL {param}'.strip())

	def clone(self) -> 'CorrectionTable':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CorrectionTable(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
