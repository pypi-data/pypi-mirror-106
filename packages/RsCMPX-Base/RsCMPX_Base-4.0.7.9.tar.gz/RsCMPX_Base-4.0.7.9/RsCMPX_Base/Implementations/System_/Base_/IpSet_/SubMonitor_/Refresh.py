from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Refresh:
	"""Refresh commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("refresh", core, parent)

	def set(self) -> None:
		"""SCPI: SYSTem:BASE:IPSet:SMONitor:REFResh \n
		Snippet: driver.system.base.ipSet.subMonitor.refresh.set() \n
		No command help available \n
		"""
		self._core.io.write(f'SYSTem:BASE:IPSet:SMONitor:REFResh')

	def set_with_opc(self) -> None:
		"""SCPI: SYSTem:BASE:IPSet:SMONitor:REFResh \n
		Snippet: driver.system.base.ipSet.subMonitor.refresh.set_with_opc() \n
		No command help available \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCMPX_Base.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'SYSTem:BASE:IPSet:SMONitor:REFResh')
