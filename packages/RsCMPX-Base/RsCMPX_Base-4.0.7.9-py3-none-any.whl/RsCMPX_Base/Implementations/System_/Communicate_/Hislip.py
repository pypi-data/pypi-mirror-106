from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hislip:
	"""Hislip commands group definition. 1 total commands, 1 Sub-groups, 0 group commands
	Repeated Capability: HislipInstance, default value after init: HislipInstance.Inst1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("hislip", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_hislipInstance_get', 'repcap_hislipInstance_set', repcap.HislipInstance.Inst1)

	def repcap_hislipInstance_set(self, enum_value: repcap.HislipInstance) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to HislipInstance.Default
		Default value after init: HislipInstance.Inst1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_hislipInstance_get(self) -> repcap.HislipInstance:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def vresource(self):
		"""vresource commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_vresource'):
			from .Hislip_.Vresource import Vresource
			self._vresource = Vresource(self._core, self._base)
		return self._vresource

	def clone(self) -> 'Hislip':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Hislip(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
