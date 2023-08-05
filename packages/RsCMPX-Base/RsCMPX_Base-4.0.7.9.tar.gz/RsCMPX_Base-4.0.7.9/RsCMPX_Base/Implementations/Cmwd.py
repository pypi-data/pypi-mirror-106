from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ..Internal.Types import DataType
from ..Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cmwd:
	"""Cmwd commands group definition. 5 total commands, 1 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cmwd", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .Cmwd_.State import State
			self._state = State(self._core, self._base)
		return self._state

	def initiate(self) -> None:
		"""SCPI: INITiate:CMWD \n
		Snippet: driver.cmwd.initiate() \n
		No command help available \n
		"""
		self._core.io.write(f'INITiate:CMWD')

	def initiate_with_opc(self) -> None:
		"""SCPI: INITiate:CMWD \n
		Snippet: driver.cmwd.initiate_with_opc() \n
		No command help available \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCMPX_Base.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'INITiate:CMWD')

	def stop(self) -> None:
		"""SCPI: STOP:CMWD \n
		Snippet: driver.cmwd.stop() \n
		No command help available \n
		"""
		self._core.io.write(f'STOP:CMWD')

	def stop_with_opc(self) -> None:
		"""SCPI: STOP:CMWD \n
		Snippet: driver.cmwd.stop_with_opc() \n
		No command help available \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCMPX_Base.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'STOP:CMWD')

	def abort(self) -> None:
		"""SCPI: ABORt:CMWD \n
		Snippet: driver.cmwd.abort() \n
		No command help available \n
		"""
		self._core.io.write(f'ABORt:CMWD')

	def abort_with_opc(self) -> None:
		"""SCPI: ABORt:CMWD \n
		Snippet: driver.cmwd.abort_with_opc() \n
		No command help available \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCMPX_Base.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'ABORt:CMWD')

	def fetch(self) -> str:
		"""SCPI: FETCh:CMWD \n
		Snippet: value: str = driver.cmwd.fetch() \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:return: result_string: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:CMWD?', suppressed)
		return trim_str_response(response)

	def clone(self) -> 'Cmwd':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cmwd(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
