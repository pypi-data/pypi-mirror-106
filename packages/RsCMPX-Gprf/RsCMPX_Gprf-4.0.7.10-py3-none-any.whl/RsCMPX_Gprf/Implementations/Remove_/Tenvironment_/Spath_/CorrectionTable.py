from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CorrectionTable:
	"""CorrectionTable commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("correctionTable", core, parent)

	# noinspection PyTypeChecker
	class RxStruct(StructBase):
		"""Structure for setting input parameters. Contains optional set arguments. Fields: \n
			- Name_Signal_Path: str: No parameter help available
			- Correction_Table: List[str]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_str('Name_Signal_Path'),
			ArgStruct('Correction_Table', DataType.StringList, None, True, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Name_Signal_Path: str = None
			self.Correction_Table: List[str] = None

	def set_rx(self, value: RxStruct) -> None:
		"""SCPI: REMove:TENVironment:SPATh:CTABle:RX \n
		Snippet: driver.remove.tenvironment.spath.correctionTable.set_rx(value = RxStruct()) \n
		No command help available \n
			:param value: see the help for RxStruct structure arguments.
		"""
		self._core.io.write_struct('REMove:TENVironment:SPATh:CTABle:RX', value)

	# noinspection PyTypeChecker
	class TxStruct(StructBase):
		"""Structure for setting input parameters. Contains optional set arguments. Fields: \n
			- Name_Signal_Path: str: No parameter help available
			- Correction_Table: List[str]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_str('Name_Signal_Path'),
			ArgStruct('Correction_Table', DataType.StringList, None, True, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Name_Signal_Path: str = None
			self.Correction_Table: List[str] = None

	def set_tx(self, value: TxStruct) -> None:
		"""SCPI: REMove:TENVironment:SPATh:CTABle:TX \n
		Snippet: driver.remove.tenvironment.spath.correctionTable.set_tx(value = TxStruct()) \n
		No command help available \n
			:param value: see the help for TxStruct structure arguments.
		"""
		self._core.io.write_struct('REMove:TENVironment:SPATh:CTABle:TX', value)
