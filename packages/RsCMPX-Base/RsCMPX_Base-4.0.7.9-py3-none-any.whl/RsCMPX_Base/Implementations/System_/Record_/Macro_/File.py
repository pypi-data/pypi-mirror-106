from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class File:
	"""File commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("file", core, parent)

	def start(self, macro_id: str) -> None:
		"""SCPI: SYSTem:RECord:MACRo:FILE:STARt \n
		Snippet: driver.system.record.macro.file.start(macro_id = '1') \n
		Starts recording of submitted commands into a macro file. If the file exists, it is overwritten. If the file does not
		exist, it is created. \n
			:param macro_id: Path and filename of the destination file on the instrument
		"""
		param = Conversions.value_to_quoted_str(macro_id)
		self._core.io.write(f'SYSTem:RECord:MACRo:FILE:STARt {param}')

	def stop(self) -> None:
		"""SCPI: SYSTem:RECord:MACRo:FILE:STOP \n
		Snippet: driver.system.record.macro.file.stop() \n
		Stops recording of commands into a macro file. \n
		"""
		self._core.io.write(f'SYSTem:RECord:MACRo:FILE:STOP')

	def stop_with_opc(self) -> None:
		"""SCPI: SYSTem:RECord:MACRo:FILE:STOP \n
		Snippet: driver.system.record.macro.file.stop_with_opc() \n
		Stops recording of commands into a macro file. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCMPX_Base.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'SYSTem:RECord:MACRo:FILE:STOP')
