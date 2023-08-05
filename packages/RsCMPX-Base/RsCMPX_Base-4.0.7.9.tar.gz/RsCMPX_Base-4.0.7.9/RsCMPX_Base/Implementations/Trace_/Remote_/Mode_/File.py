from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class File:
	"""File commands group definition. 11 total commands, 11 Sub-groups, 0 group commands
	Repeated Capability: FileNr, default value after init: FileNr.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("file", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_fileNr_get', 'repcap_fileNr_set', repcap.FileNr.Nr1)

	def repcap_fileNr_set(self, enum_value: repcap.FileNr) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to FileNr.Default
		Default value after init: FileNr.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_fileNr_get(self) -> repcap.FileNr:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def dexecution(self):
		"""dexecution commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_dexecution'):
			from .File_.Dexecution import Dexecution
			self._dexecution = Dexecution(self._core, self._base)
		return self._dexecution

	@property
	def stopMode(self):
		"""stopMode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stopMode'):
			from .File_.StopMode import StopMode
			self._stopMode = StopMode(self._core, self._base)
		return self._stopMode

	@property
	def startMode(self):
		"""startMode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_startMode'):
			from .File_.StartMode import StartMode
			self._startMode = StartMode(self._core, self._base)
		return self._startMode

	@property
	def name(self):
		"""name commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_name'):
			from .File_.Name import Name
			self._name = Name(self._core, self._base)
		return self._name

	@property
	def formatPy(self):
		"""formatPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_formatPy'):
			from .File_.FormatPy import FormatPy
			self._formatPy = FormatPy(self._core, self._base)
		return self._formatPy

	@property
	def size(self):
		"""size commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_size'):
			from .File_.Size import Size
			self._size = Size(self._core, self._base)
		return self._size

	@property
	def rpc(self):
		"""rpc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rpc'):
			from .File_.Rpc import Rpc
			self._rpc = Rpc(self._core, self._base)
		return self._rpc

	@property
	def functions(self):
		"""functions commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_functions'):
			from .File_.Functions import Functions
			self._functions = Functions(self._core, self._base)
		return self._functions

	@property
	def parser(self):
		"""parser commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_parser'):
			from .File_.Parser import Parser
			self._parser = Parser(self._core, self._base)
		return self._parser

	@property
	def filterPy(self):
		"""filterPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_filterPy'):
			from .File_.FilterPy import FilterPy
			self._filterPy = FilterPy(self._core, self._base)
		return self._filterPy

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .File_.Enable import Enable
			self._enable = Enable(self._core, self._base)
		return self._enable

	def clone(self) -> 'File':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = File(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
