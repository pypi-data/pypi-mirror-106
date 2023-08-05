from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Device:
	"""Device commands group definition. 3 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("device", core, parent)

	@property
	def vi(self):
		"""vi commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_vi'):
			from .Device_.Vi import Vi
			self._vi = Vi(self._core, self._base)
		return self._vi

	@property
	def id(self):
		"""id commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_id'):
			from .Device_.Id import Id
			self._id = Id(self._core, self._base)
		return self._id

	def clone(self) -> 'Device':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Device(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
