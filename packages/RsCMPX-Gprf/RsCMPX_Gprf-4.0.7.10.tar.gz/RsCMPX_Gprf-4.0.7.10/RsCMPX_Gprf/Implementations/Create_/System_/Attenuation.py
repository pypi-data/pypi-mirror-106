from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Attenuation:
	"""Attenuation commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("attenuation", core, parent)

	# noinspection PyTypeChecker
	class CorrectionTableStruct(StructBase):
		"""Structure for setting input parameters. Contains optional set arguments. Fields: \n
			- Name: str: No parameter help available
			- Frequency: List[float]: No parameter help available
			- Attenuation: List[float]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_str('Name'),
			ArgStruct('Frequency', DataType.FloatList, None, True, True, 1),
			ArgStruct('Attenuation', DataType.FloatList, None, True, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Name: str = None
			self.Frequency: List[float] = None
			self.Attenuation: List[float] = None

	def set_correction_table(self, value: CorrectionTableStruct) -> None:
		"""SCPI: CREate:SYSTem:ATTenuation:CTABle \n
		Snippet: driver.create.system.attenuation.set_correction_table(value = CorrectionTableStruct()) \n
		No command help available \n
			:param value: see the help for CorrectionTableStruct structure arguments.
		"""
		self._core.io.write_struct('CREate:SYSTem:ATTenuation:CTABle', value)
