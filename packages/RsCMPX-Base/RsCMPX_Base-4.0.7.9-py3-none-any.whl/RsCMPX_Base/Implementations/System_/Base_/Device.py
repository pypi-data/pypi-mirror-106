from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Device:
	"""Device commands group definition. 7 total commands, 0 Sub-groups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("device", core, parent)

	# noinspection PyTypeChecker
	class SubinstStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Cur_Sub_Inst: int: Device number of the addressed subinstrument, as indicated in a VISA resource string for HiSLIP and as returned by *DEV?. Mapping: device number 0 = subinstrument 1 = assigned instrument 1
			- Sub_Inst_Count: int: Total number of subinstruments into which the instrument is split."""
		__meta_args_list = [
			ArgStruct.scalar_int('Cur_Sub_Inst'),
			ArgStruct.scalar_int('Sub_Inst_Count')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cur_Sub_Inst: int = None
			self.Sub_Inst_Count: int = None

	def get_subinst(self) -> SubinstStruct:
		"""SCPI: SYSTem:BASE:DEVice:SUBinst \n
		Snippet: value: SubinstStruct = driver.system.base.device.get_subinst() \n
		Queries the device number of the addressed subinstrument and the total number of existing subinstruments. \n
			:return: structure: for return value, see the help for SubinstStruct structure arguments.
		"""
		return self._core.io.query_struct('SYSTem:BASE:DEVice:SUBinst?', self.__class__.SubinstStruct())

	# noinspection PyTypeChecker
	class LicenseStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Sw_Option: List[str]: No parameter help available
			- License_Count: List[int]: No parameter help available
			- Instrument: List[int]: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Sw_Option', DataType.StringList, None, False, True, 1),
			ArgStruct('License_Count', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Instrument', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Sw_Option: List[str] = None
			self.License_Count: List[int] = None
			self.Instrument: List[int] = None

	def get_license(self) -> LicenseStruct:
		"""SCPI: SYSTem:BASE:DEVice:LICense \n
		Snippet: value: LicenseStruct = driver.system.base.device.get_license() \n
		No command help available \n
			:return: structure: for return value, see the help for LicenseStruct structure arguments.
		"""
		return self._core.io.query_struct('SYSTem:BASE:DEVice:LICense?', self.__class__.LicenseStruct())

	def set_license(self, value: LicenseStruct) -> None:
		"""SCPI: SYSTem:BASE:DEVice:LICense \n
		Snippet: driver.system.base.device.set_license(value = LicenseStruct()) \n
		No command help available \n
			:param value: see the help for LicenseStruct structure arguments.
		"""
		self._core.io.write_struct('SYSTem:BASE:DEVice:LICense', value)

	def get_count(self) -> int:
		"""SCPI: SYSTem:BASE:DEVice:COUNt \n
		Snippet: value: int = driver.system.base.device.get_count() \n
		Splits the instrument into subinstruments or assigns all hardware resources to a single subinstrument. Send this command
		to the subinstrument with the lowest number (device 0 / subinstrument 1 / assigned instrument 1) . To assign/distribute
		the available hardware resources to the subinstruments, a restart is performed automatically after you have changed the
		number of subinstruments. \n
			:return: count: Number of subinstruments The allowed subset of values depends on the number of connected RRHs.
		"""
		response = self._core.io.query_str('SYSTem:BASE:DEVice:COUNt?')
		return Conversions.str_to_int(response)

	def set_count(self, count: int) -> None:
		"""SCPI: SYSTem:BASE:DEVice:COUNt \n
		Snippet: driver.system.base.device.set_count(count = 1) \n
		Splits the instrument into subinstruments or assigns all hardware resources to a single subinstrument. Send this command
		to the subinstrument with the lowest number (device 0 / subinstrument 1 / assigned instrument 1) . To assign/distribute
		the available hardware resources to the subinstruments, a restart is performed automatically after you have changed the
		number of subinstruments. \n
			:param count: Number of subinstruments The allowed subset of values depends on the number of connected RRHs.
		"""
		param = Conversions.decimal_value_to_str(count)
		self._core.io.write(f'SYSTem:BASE:DEVice:COUNt {param}')

	def reset(self) -> None:
		"""SCPI: SYSTem:BASE:DEVice:RESet \n
		Snippet: driver.system.base.device.reset() \n
		No command help available \n
		"""
		self._core.io.write(f'SYSTem:BASE:DEVice:RESet')

	def reset_with_opc(self) -> None:
		"""SCPI: SYSTem:BASE:DEVice:RESet \n
		Snippet: driver.system.base.device.reset_with_opc() \n
		No command help available \n
		Same as reset, but waits for the operation to complete before continuing further. Use the RsCMPX_Base.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'SYSTem:BASE:DEVice:RESet')

	# noinspection PyTypeChecker
	class SetupStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Absolute_Item_Name: List[str]: No parameter help available
			- Instrument: List[int]: No parameter help available"""
		__meta_args_list = [
			ArgStruct('Absolute_Item_Name', DataType.StringList, None, False, True, 1),
			ArgStruct('Instrument', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Absolute_Item_Name: List[str] = None
			self.Instrument: List[int] = None

	def get_setup(self) -> SetupStruct:
		"""SCPI: SYSTem:BASE:DEVice:SETup \n
		Snippet: value: SetupStruct = driver.system.base.device.get_setup() \n
		No command help available \n
			:return: structure: for return value, see the help for SetupStruct structure arguments.
		"""
		return self._core.io.query_struct('SYSTem:BASE:DEVice:SETup?', self.__class__.SetupStruct())

	def set_setup(self, value: SetupStruct) -> None:
		"""SCPI: SYSTem:BASE:DEVice:SETup \n
		Snippet: driver.system.base.device.set_setup(value = SetupStruct()) \n
		No command help available \n
			:param value: see the help for SetupStruct structure arguments.
		"""
		self._core.io.write_struct('SYSTem:BASE:DEVice:SETup', value)

	def get_mscont(self) -> int:
		"""SCPI: SYSTem:BASE:DEVice:MSCont \n
		Snippet: value: int = driver.system.base.device.get_mscont() \n
		No command help available \n
			:return: max_si_count: No help available
		"""
		response = self._core.io.query_str('SYSTem:BASE:DEVice:MSCont?')
		return Conversions.str_to_int(response)

	def get_msc_count(self) -> int:
		"""SCPI: SYSTem:BASE:DEVice:MSCCount \n
		Snippet: value: int = driver.system.base.device.get_msc_count() \n
		Returns the maximum number of subinstruments into which the instrument can be split. \n
			:return: max_sc_count: The value 0 indicates that no split is possible.
		"""
		response = self._core.io.query_str('SYSTem:BASE:DEVice:MSCCount?')
		return Conversions.str_to_int(response)
