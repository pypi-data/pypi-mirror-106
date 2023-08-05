from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Llimit:
	"""Llimit commands group definition. 4 total commands, 4 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("llimit", core, parent)

	@property
	def rxDc(self):
		"""rxDc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rxDc'):
			from .Llimit_.RxDc import RxDc
			self._rxDc = RxDc(self._core, self._base)
		return self._rxDc

	@property
	def txDc(self):
		"""txDc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_txDc'):
			from .Llimit_.TxDc import TxDc
			self._txDc = TxDc(self._core, self._base)
		return self._txDc

	@property
	def rxImage(self):
		"""rxImage commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rxImage'):
			from .Llimit_.RxImage import RxImage
			self._rxImage = RxImage(self._core, self._base)
		return self._rxImage

	@property
	def txImage(self):
		"""txImage commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_txImage'):
			from .Llimit_.TxImage import TxImage
			self._txImage = TxImage(self._core, self._base)
		return self._txImage

	def clone(self) -> 'Llimit':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Llimit(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
