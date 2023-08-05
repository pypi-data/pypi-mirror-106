from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HardCopy:
	"""HardCopy commands group definition. 5 total commands, 2 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("hardCopy", core, parent)

	@property
	def device(self):
		"""device commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_device'):
			from .HardCopy_.Device import Device
			self._device = Device(self._core, self._base)
		return self._device

	@property
	def interior(self):
		"""interior commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_interior'):
			from .HardCopy_.Interior import Interior
			self._interior = Interior(self._core, self._base)
		return self._interior

	def get_data(self) -> bytes:
		"""SCPI: HCOPy:DATA \n
		Snippet: value: bytes = driver.hardCopy.get_data() \n
		No command help available \n
			:return: data: No help available
		"""
		response = self._core.io.query_bin_block('HCOPy:DATA?')
		return response

	def set_file(self, filename: str) -> None:
		"""SCPI: HCOPy:FILE \n
		Snippet: driver.hardCopy.set_file(filename = '1') \n
		No command help available \n
			:param filename: No help available
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'HCOPy:FILE {param}')

	def clone(self) -> 'HardCopy':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = HardCopy(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
