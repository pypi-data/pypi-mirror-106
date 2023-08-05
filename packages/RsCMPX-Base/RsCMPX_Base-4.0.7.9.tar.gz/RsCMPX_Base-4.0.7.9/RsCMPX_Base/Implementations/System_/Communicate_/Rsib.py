from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rsib:
	"""Rsib commands group definition. 1 total commands, 1 Sub-groups, 0 group commands
	Repeated Capability: RsibInstance, default value after init: RsibInstance.Inst1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rsib", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_rsibInstance_get', 'repcap_rsibInstance_set', repcap.RsibInstance.Inst1)

	def repcap_rsibInstance_set(self, enum_value: repcap.RsibInstance) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to RsibInstance.Default
		Default value after init: RsibInstance.Inst1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_rsibInstance_get(self) -> repcap.RsibInstance:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def vresource(self):
		"""vresource commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_vresource'):
			from .Rsib_.Vresource import Vresource
			self._vresource = Vresource(self._core, self._base)
		return self._vresource

	def clone(self) -> 'Rsib':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rsib(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
