from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Instrument:
	"""Instrument commands group definition. 3 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("instrument", core, parent)

	@property
	def consistency(self):
		"""consistency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_consistency'):
			from .Instrument_.Consistency import Consistency
			self._consistency = Consistency(self._core, self._base)
		return self._consistency

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

	def clone(self) -> 'Instrument':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Instrument(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
