from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rx:
	"""Rx commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rx", core, parent)

	# noinspection PyTypeChecker
	class SetStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Connector_Bench: str: No parameter help available
			- Table_1: str: No parameter help available
			- Table_2: str: No parameter help available
			- Table_3: str: No parameter help available
			- Table_4: str: No parameter help available
			- Table_5: str: No parameter help available
			- Table_6: str: No parameter help available
			- Table_7: str: No parameter help available
			- Table_8: str: No parameter help available"""
		__meta_args_list = [
			]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Connector_Bench: str = None
			self.Table_1: str = None
			self.Table_2: str = None
			self.Table_3: str = None
			self.Table_4: str = None
			self.Table_5: str = None
			self.Table_6: str = None
			self.Table_7: str = None
			self.Table_8: str = None

	def set(self, structure: SetStruct) -> None:
		"""SCPI: CONFigure:CMWS:FDCorrection:ACTivate:RX \n
		Snippet: driver.configure.singleCmw.freqCorrection.activate.rx.set(value = [PROPERTY_STRUCT_NAME]()) \n
		No command help available \n
			:param structure: for set value, see the help for SetStruct structure arguments.
		"""
		self._core.io.write_struct(f'CONFigure:CMWS:FDCorrection:ACTivate:RX', structure)
