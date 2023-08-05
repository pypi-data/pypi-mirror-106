from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Off:
	"""Off commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("off", core, parent)

	def set(self) -> None:
		"""SCPI: SYSTem:SIGNaling:ALL:OFF \n
		Snippet: driver.system.signaling.all.off.set() \n
		Switch off all signaling applications, generators or measurements. \n
		"""
		self._core.io.write(f'SYSTem:SIGNaling:ALL:OFF')

	def set_with_opc(self) -> None:
		"""SCPI: SYSTem:SIGNaling:ALL:OFF \n
		Snippet: driver.system.signaling.all.off.set_with_opc() \n
		Switch off all signaling applications, generators or measurements. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCMPX_Base.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'SYSTem:SIGNaling:ALL:OFF')
