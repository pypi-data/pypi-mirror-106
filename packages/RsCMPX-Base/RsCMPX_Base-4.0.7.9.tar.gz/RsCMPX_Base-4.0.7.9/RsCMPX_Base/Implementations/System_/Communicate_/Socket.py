from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Socket:
	"""Socket commands group definition. 3 total commands, 3 Sub-groups, 0 group commands
	Repeated Capability: SocketInstance, default value after init: SocketInstance.Inst1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("socket", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_socketInstance_get', 'repcap_socketInstance_set', repcap.SocketInstance.Inst1)

	def repcap_socketInstance_set(self, enum_value: repcap.SocketInstance) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to SocketInstance.Default
		Default value after init: SocketInstance.Inst1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_socketInstance_get(self) -> repcap.SocketInstance:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def vresource(self):
		"""vresource commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_vresource'):
			from .Socket_.Vresource import Vresource
			self._vresource = Vresource(self._core, self._base)
		return self._vresource

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Socket_.Mode import Mode
			self._mode = Mode(self._core, self._base)
		return self._mode

	@property
	def port(self):
		"""port commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_port'):
			from .Socket_.Port import Port
			self._port = Port(self._core, self._base)
		return self._port

	def clone(self) -> 'Socket':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Socket(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
